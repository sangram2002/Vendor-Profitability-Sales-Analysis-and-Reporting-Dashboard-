import numpy as np
import pandas as pd
import os
import logging
import psutil
from sqlalchemy import create_engine
import time
import sqlite3
from sqlalchemy.pool import NullPool


# 200MB threshold based on typical CSV file sizes:
# - Current files are ~18MB (from log File Size: 18984007)
# - Set higher threshold to only chunk genuinely large files
FILE_THRESHOLD = 2e8  # 200MB

# Setup logging
os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def calculate_chunk_size(df_shape):
    """
    Calculate optimal chunk size based on DataFrame shape and SQLite variable limit
    Args:
        df_shape: Tuple of (rows, columns) from DataFrame.shape
    Returns:
        int: Optimal chunk size that stays under SQLite's 999 variable limit
    """
    SQLITE_VARIABLE_LIMIT = 999
    num_columns = df_shape[1]
    
    # Calculate max rows per chunk
    max_rows = SQLITE_VARIABLE_LIMIT // num_columns
    
    # Use 90% of max for safety margin
    safe_chunk_size = int(max_rows * 0.9)
    
    logger.info(f"Calculated chunk size: {safe_chunk_size} rows for {num_columns} columns")
    return safe_chunk_size

def log_memory_usage():
    """Log current memory usage"""
    mem = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
    logger.info(f"Memory usage: {mem:.2f} MB")

def ingest_db(df, table_name, engine):
    """Ingest dataframe into database table"""
    CHUNK_SIZE = calculate_chunk_size(df.shape)
    start = time.time()
    
    try:

        # Then perform the ingestion
        df.to_sql(
            table_name, 
            engine, 
            if_exists='replace', 
            index=False,
            chunksize=CHUNK_SIZE
        )
        logger.info(f"Data ingested into table {table_name} successfully")
    
    except sqlite3.OperationalError as e:
        error_msg = f"SQLite operational error: {str(e)}"
        logger.error(error_msg)
        print(error_msg)
        raise
    except Exception as e:
        logger.error(f"Error ingesting {table_name}: {str(e)}")
        raise
    finally:
        logger.info(f"Time taken: {(time.time() - start)/60:.2f} minutes")


def process_file(file_path):
    """Process a single CSV file"""
    file_size = os.path.getsize(file_path)
    CHUNK_SIZE = 1000
    
    try:
        if file_size > FILE_THRESHOLD:
            chunks = pd.read_csv(file_path, chunksize=CHUNK_SIZE)
            df = pd.concat(chunks, ignore_index=True)
        else:
            df = pd.read_csv(file_path)
        print(f"Read file: {os.path.basename(file_path)}, File Size: {file_size}, Shape: {df.shape}")
        logger.info(f"Read file: {os.path.basename(file_path)}, File Size: {file_size}, Shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error reading file: {str(e)}")
        raise

def main():
    """Main execution function"""
    try:
        data_path = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data directory not found: {data_path}")

        # Create engine with timeout and connection pooling disabled
        engine = create_engine(
            'sqlite:///inventory.db', 
            connect_args={'timeout': 30},  # 30 second timeout
            poolclass=NullPool  # Disable connection pooling
        )
        
        for file in os.listdir(data_path):
            if file.endswith('sales.csv'):
                print('hi')
                file_path = os.path.join(data_path, file)
                df = process_file(file_path)
                table_name = file.split('.')[0]
                print(f"Processing {file_path} into table {table_name}")
                ingest_db(df, table_name, engine)
                print('done')
                
        return 0
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        return 1

if __name__ == '__main__':
    exit(main())