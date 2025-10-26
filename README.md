![Power BI Dashboard Link]https://app.powerbi.com/groups/me/reports/8805de3d-2336-4cf4-8e2c-eac1ee608662/f53ad9b0b1654b4e03b5?experience=power-bi

This is the link to view Power BI Dashboard.

# 🧾 Vendor Performance Data Analytics Project

## 📊 Overview
This project presents an **end-to-end Vendor Performance Analysis pipeline** that integrates **SQL, Python (Pandas, SQLite3, Statsmodels)**, and **Power BI** to evaluate vendor profitability, sales efficiency, and pricing behavior.  
The objective was to **analyze vendor performance**, identify **profitability drivers**, and perform **statistical testing** to determine if there are significant differences in profit margins among vendors.

---

## ⚙️ Tools & Technologies Used
| Category | Tools / Libraries |
|-----------|-------------------|
| **Database** | SQLite3 |
| **Data Manipulation & Analysis** | Python, Pandas, NumPy |
| **Statistical Analysis** | SciPy (`ttest_ind`), Statsmodels (`confidence intervals`, hypothesis testing) |
| **Data Visualization** | Matplotlib, Seaborn, Power BI |
| **SQL Queries** | Joins, CTEs, Aggregations, Subqueries |
| **Logging & Debugging** | Python `logging` module |
| **Environment** | Jupyter Notebook, Power BI Desktop |

---

## 🏗️ Project Workflow
1. **Data Integration**
   - Imported **5 CSV files** (Purchase, Sales, Freight, Vendor, and Inventory data).
   - Created an **SQLite database** using SQLAlchemy with **logging and error handling**.
   - Merged datasets into a unified table for vendor-level analytics.

2. **Data Transformation & Cleaning**
   - Standardized vendor and brand mappings.
   - Handled missing values, inconsistent data entries, and verified data integrity.
   - Used SQL joins and aggregations to prepare the `Vendor_Sales_Summary` table.

3. **Exploratory Data Analysis (EDA)**
   - Visualized purchase contribution by top 10 vendors using **donut and bar charts**.
   - Analyzed bulk purchase impact on unit price through **boxplots**.
   - Evaluated capital locked in unsold inventory per vendor.

4. **Statistical Analysis**
   - Calculated **95% Confidence Intervals (CI)** for profit margins using `statsmodels`.
   - Conducted **two-sample t-test** (`scipy.stats.ttest_ind`) to test:
     > *Is there a significant difference in profit margins between top-performing and low-performing vendors?*
   - Derived actionable insights for pricing optimization and vendor selection.

5. **Visualization & Reporting**
   - Designed **interactive Power BI dashboards** visualizing:
     - Total Purchase Cost  
     - Sales Revenue  
     - Freight Contribution  
     - Profit Margin by Vendor  
   - Delivered summarized insights for strategic decision-making.

---

## 📈 Key Insights
| Observation | Insight |
|--------------|----------|
| **Large orders have the lowest unit price (~$10.78/unit)** | Bulk purchasing yields significant cost benefits. |
| **Price difference between small and large orders ≈ −72%** | Indicates strong incentives for vendors to buy in bulk. |
| **Low-performing vendors have higher profit margins (40.48%–42.62%)** | Suggests premium pricing or lower operational costs. |
| **Top-performing vendors have narrower margins (30.74%–31.61%)** | Reflects volume-based pricing strategies with thinner margins. |

---

## 🧮 Statistical Results
- **Top Vendors 95% CI:** (30.74%, 31.61%)  
- **Low Vendors 95% CI:** (40.48%, 42.62%)  
- **Two-Sample T-Test:** p-value < 0.05 → *Significant difference in mean profit margins.*

---

## 📊 Power BI Dashboard Highlights
- Vendor-wise profitability breakdown  
- Purchase and freight cost contribution  
- Sales efficiency by vendor and category  
- Interactive filters for category, vendor, and date range  

---

## 🧠 Business Impact
- Helped identify **cost inefficiencies and pricing gaps**.  
- Improved **vendor selection and procurement strategy**.  
- Enabled **data-driven decision-making** via automated reporting and visualization.

---

## 🚀 Future Enhancements
- Automate Power BI refresh using a Python scheduler.
- Integrate predictive analytics for vendor performance forecasting.
- Deploy dashboards to Power BI Service for real-time monitoring.

---

## 👨‍💻 Author
**Sangram Patro**  
_Data Analyst | Business Analyst | Data Science Enthusiast_  
📧 [sangramkeshari2002@gmail.com ]  
🌐 [https://github.com/sangram2002]  

## Snapshots
Show what the dashboard looks like
![Dashboard Preview](https://github.com/sangram2002/Vendor-Profitability-Sales-Analysis-and-Reporting-Dashboard-/blob/main/Snapshot%20of%20the%20Dashboard.png)

