import pandas as pd
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler
from scipy.stats import zscore

# Initialize tqdm for pandas
tqdm.pandas()

# Load the raw dataset
raw_data = pd.read_csv("carSaleRG.csv")

# Create an empty report string
report = []

# Add dataset initial information to the report
report.append("=== Initial Dataset Information ===")
report.append(f"Total Rows: {raw_data.shape[0]}")
report.append(f"Total Columns: {raw_data.shape[1]}")
report.append("\nMissing Values:\n")
report.append(raw_data.isnull().sum().to_string())

# Step 1: Handle missing values
with tqdm(total=3, desc="Handling Missing Values", unit="step") as pbar:
    raw_data['Annual Income'] = raw_data['Annual Income'].fillna(raw_data['Annual Income'].median())
    pbar.update(1)
    raw_data['Gender'] = raw_data['Gender'].fillna("Unknown")
    pbar.update(1)
    raw_data['Phone'] = raw_data['Phone'].fillna("Not Provided")
    pbar.update(1)

# Step 2: Clean and validate data
with tqdm(total=4, desc="Cleaning and Validating Data", unit="step") as pbar:
    raw_data['Price'] = pd.to_numeric(raw_data['Price'], errors='coerce')
    pbar.update(1)
    raw_data['Date'] = pd.to_datetime(raw_data['Date'], errors='coerce')
    pbar.update(1)
    raw_data = raw_data.dropna(subset=['Price', 'Date'])
    pbar.update(1)
    raw_data = raw_data[raw_data['Price'] >= 0]
    pbar.update(1)

# Step 3: Remove outliers
with tqdm(total=1, desc="Removing Outliers", unit="step") as pbar:
    raw_data['Price_zscore'] = zscore(raw_data['Price'])
    raw_data = raw_data[raw_data['Price_zscore'].abs() <= 3]
    raw_data = raw_data.drop(columns=['Price_zscore'])
    pbar.update(1)

# Step 4: Clean text columns
with tqdm(total=2, desc="Cleaning Text Columns", unit="column") as pbar:
    raw_data['Customer Name'] = raw_data['Customer Name'].str.strip().str.title()
    pbar.update(1)
    raw_data['Dealer_Name'] = raw_data['Dealer_Name'].str.strip().str.title()
    pbar.update(1)

# Step 5: Add derived columns
with tqdm(total=1, desc="Adding Derived Columns", unit="column") as pbar:
    raw_data['Year'] = raw_data['Date'].dt.year
    raw_data['Month'] = raw_data['Date'].dt.month  # Add Month feature
    raw_data['DayOfWeek'] = raw_data['Date'].dt.dayofweek  # Add DayOfWeek feature
    raw_data['Quarter'] = raw_data['Date'].dt.quarter  # Add Quarter feature
    raw_data['IncomeSegment'] = pd.cut(
        raw_data['Annual Income'], 
        bins=[0, 50000, 100000, 200000], 
        labels=['Low', 'Medium', 'High']
    )  # Customer segmentation
    pbar.update(1)

# Step 6: Partition the data
with tqdm(total=4, desc="Partitioning Data", unit="table") as pbar:
    customers = raw_data[['Customer Name', 'Gender', 'Annual Income', 'Phone']].drop_duplicates()
    pbar.update(1)
    
    # Adding DealerID column based on Dealer_No
    dealers = raw_data[['Dealer_No', 'Dealer_Name', 'Dealer_Region']].drop_duplicates()
    dealers['DealerID'] = dealers['Dealer_No']  # Creating DealerID in Dealers table
    pbar.update(1)
    
    # Creating DealerID in Sales table
    sales = raw_data[['Car_id', 'Date', 'Price', 'Dealer_No']]
    sales['DealerID'] = sales['Dealer_No']  # Creating DealerID in Sales table
    pbar.update(1)

    cars = raw_data[['Car_id', 'Company', 'Model', 'Engine', 'Transmission', 'Color', 'Body Style']].drop_duplicates()
    pbar.update(1)

# Update the report with partition details
report.append("\n\n=== Partition Summary ===")
report.append(f"Customers Table: {customers.shape[0]} rows")
report.append(f"Dealers Table: {dealers.shape[0]} rows")
report.append(f"Cars Table: {cars.shape[0]} rows")
report.append(f"Sales Table: {sales.shape[0]} rows")

# Step 7: Save cleaned data to Excel
output_file = "processed_car_sales.xlsx"
with tqdm(total=1, desc="Saving Data to Excel", unit="file") as pbar:
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        customers.to_excel(writer, sheet_name="Customers", index=False)
        dealers.to_excel(writer, sheet_name="Dealers", index=False)
        cars.to_excel(writer, sheet_name="Cars", index=False)
        sales.to_excel(writer, sheet_name="Sales", index=False)
    pbar.update(1)

# Update report with export details
report.append("\n\n=== Export Details ===")
report.append(f"Data successfully exported to '{output_file}'.")

# Step 8: Save the report to a text file
report_file = "preprocessing_report.txt"
with tqdm(total=1, desc="Saving Report", unit="file") as pbar:
    with open(report_file, "w") as file:
        file.write("\n".join(report))
    pbar.update(1)

print(f"Data preprocessing complete. Report saved to '{report_file}'.")
