# Azure Car Sales ETL

This project implements an ETL (Extract, Transform, Load) pipeline for car sales data using Azure services. The purpose is to process raw datasets, perform data preprocessing and transformation, load the data into a database, and create Power BI reports. 

## Project Structure

📂 azure-car-sales-etl │── 📂 data # Raw and cleaned datasets (CSV, Excel) │── 📂 scripts # Python preprocessing and ETL scripts │── 📂 sql # SQL scripts for database creation │── 📂 pipeline # Azure Data Factory templates (JSON) │── 📂 reports # Power BI dashboard files (.pbix) │── 📂 docs # Documentation and setup guide │── .gitignore # Ignore unnecessary files (e.g., large datasets) │── README.md # Project overview and setup instructions │── requirements.txt # Python dependencies 


## Project Components

### 1. **Data**
   - Contains raw and cleaned datasets used for ETL processing.
   - Files are typically in CSV or Excel format.
   - **Example**: `sales_data_raw.csv`

### 2. **Scripts**
   - Python scripts for data preprocessing, transformation, and loading to the database.
   - Implements the logic for cleaning and transforming raw data into a usable format.
   - **Example**: `data_cleaning.py`, `etl_pipeline.py`

### 3. **SQL**
   - SQL scripts used to create the database schema and tables for storing processed data.
   - **Example**: `create_sales_table.sql`

### 4. **Pipeline**
   - Azure Data Factory templates for orchestrating the ETL pipeline.
   - These templates define the activities for data movement and transformation within Azure.
   - **Example**: `sales_etl_pipeline.json`

### 5. **Reports**
   - Power BI dashboard files that visualize the processed data.
   - **Example**: `car_sales_dashboard.pbix`

### 6. **Docs**
   - Documentation and setup guide for the project.
   - Contains instructions for setting up the ETL pipeline, Power BI reports, and database.
   - **Example**: `setup_guide.md`

### 7. **.gitignore**
   - A file that specifies which files should be ignored by Git (e.g., large datasets, temporary files).

### 8. **requirements.txt**
   - Lists the Python dependencies required to run the ETL scripts.
   - **Example**: 
     ```
     pandas==1.3.2
     numpy==1.21.0
     azure-storage-blob==12.8.0
     ```
     

## Setup Instructions

### Prerequisites
- Python 3.x
- Azure account with access to Azure Data Factory
- Power BI Desktop

### 1. Clone the repository
```bash
git clone https://github.com/your-username/azure-car-sales-etl.git
cd azure-car-sales-etl
