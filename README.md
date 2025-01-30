# Azure Car Sales ETL

This project implements an ETL (Extract, Transform, Load) pipeline for car sales data using Azure services. The purpose is to process raw datasets, perform data preprocessing and transformation, load the data into a database, and create Power BI reports. 

## Project Structure

📂 azure-car-sales-etl │── 📂 data # Raw and cleaned datasets (CSV, Excel) │── 📂 scripts # Python preprocessing and ETL scripts │── 📂 sql # SQL scripts for database creation │── 📂 pipeline # Azure Data Factory templates (JSON) │── 📂 reports # Power BI dashboard files (.pbix) │── 📂 docs # Documentation and setup guide 


## Project Components

### 1. **Data**
   - Contains raw and cleaned datasets used for ETL processing.
   - Files are typically in CSV or Excel format.
 

### 2. **Scripts**
   - Python scripts for data preprocessing, transformation, and loading to the database.
   - Implements the logic for cleaning and transforming raw data into a usable format.


### 3. **SQL**
   - SQL scripts used to create the database schema and tables for storing processed data.


### 4. **Pipeline**
   - Azure Data Factory templates for orchestrating the ETL pipeline.
   - These templates define the activities for data movement and transformation within Azure.


### 5. **Reports**
   - Power BI dashboard files that visualize the processed data.


### 6. **Docs**
   - Documentation and setup guide for the project.
   - Contains instructions for setting up the ETL pipeline, Power BI reports, and database.



