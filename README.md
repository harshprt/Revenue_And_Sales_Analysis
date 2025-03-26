
# 📊 Sales Analysis Project

A comprehensive sales analysis project using **PostgreSQL** and **Python** to derive actionable insights, visualize trends, and optimize sales strategies.

---

## 🚀 Project Overview
This project demonstrates the application of data analysis and visualization techniques on a sales dataset. Key objectives include:
- Understanding revenue trends.
- Identifying top-performing products, regions, and customers.
- Providing actionable insights for business decision-making.

---

## 📂 Project Structure

```
Sales_Analysis_Project/
│
├── data/                           # Raw and processed data files
│   ├── sales_data.csv          # Raw sales data file 1
│   ├── large_sales_data.csv          # Raw sales data file 2
│   ├── sales_project_export.csv           # Combined data after SQL processing
│
├── notebooks/                      # Jupyter Notebook
│   ├── Sales_Analysis.ipynb
│
├── scripts/                        # SQL and Python scripts
│   ├── Sales_Analysis.py           # Python analysis script
│   ├── sales_analysis_queries.sql  # SQL ETL and analysis queries
│
├── visualizations/                 # Visualizations used in the project
│   ├── monthly_revenue_trends.png
│   ├── revenue_by_region.png
│   ├── top_customers.png
│   ├── revenue_by_product.png
│
├── docs/                           # Documentation
│   ├── Sales_Analysis_Project_Report.docx
│
├── README.md                       # Project description and overview
├── requirements.txt                # Python dependencies
```

---

## 🔍 Key Insights

### 1️⃣ Monthly Revenue Trends
- Observed steady growth with a **13% monthly increase in revenue**.
- **Visualization**: Line chart showing revenue trends month by month.

### 2️⃣ Revenue by Region
- The **North region** contributed the highest revenue of **$1.2M annually**.
- The **South region** had the lowest performance, indicating potential for improvement.

### 3️⃣ Top Customers
- The top 10 customers contributed **30% of the total revenue**, highlighting the importance of key accounts.

### 4️⃣ Revenue by Product
- **Smartphones** were the highest-performing product, contributing **45% of the total revenue**.

---

## 🛠 Tools and Technologies
- **PostgreSQL**: Data storage and ETL (Extraction, Transformation, Loading).
- **Python**: Data analysis and visualization.
- **Matplotlib**: Visualization of trends and metrics.
- **Jupyter Notebook**: Interactive coding environment.

---

## 📋 How to Use This Repository

### Prerequisites
Ensure the following are installed on your system:
- Python 3.7+
- PostgreSQL
- Jupyter Notebook

### Steps to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/danielsklar/Sales_Analysis_Project.git
   cd Sales_Analysis_Project
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the PostgreSQL database**:
   - Import the raw data files (`raw_data_file1.csv` and `raw_data_file2.csv`) into PostgreSQL.
   - Execute the SQL queries in `sales_analysis_queries.sql` to process the data.

4. **Run the analysis**:
   - Open `Sales_Analysis.ipynb` in Jupyter Notebook or execute `Sales_Analysis.py`:
     ```bash
     python scripts/Sales_Analysis.py
     ```

5. **View Visualizations**:
   - Visualizations are saved in the `visualizations/` folder.

---

## 📊 Key Files
| File/Folder                       | Description                                     |
|-----------------------------------|-------------------------------------------------|
| `data/`                           | Contains raw and processed data files.          |
| `notebooks/Sales_Analysis.ipynb`  | Jupyter Notebook for the analysis.              |
| `scripts/Sales_Analysis.py`       | Python script for analysis.                     |
| `scripts/sales_analysis_queries.sql` | SQL queries for data processing and analysis.  |
| `visualizations/`                 | Visualizations generated from the analysis.     |
| `docs/Sales_Analysis_Project_Report.docx` | Detailed project report.                     |

---

## 📬 Contact
Feel free to reach out for any questions or collaboration opportunities:
- **Email**: daniel.sklar1@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/daniel-sklar1
