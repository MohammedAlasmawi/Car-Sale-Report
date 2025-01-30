CREATE TABLE Customers (
    CustomerID INT IDENTITY PRIMARY KEY,
    Name NVARCHAR(100),
    Gender NVARCHAR(10),
    AnnualIncome DECIMAL(10, 2),
    Phone NVARCHAR(15)
);

CREATE TABLE Dealers (
    DealerID INT IDENTITY PRIMARY KEY,
    Dealer_No NVARCHAR(50),
    Dealer_Name NVARCHAR(100),
    Dealer_Reg NVARCHAR(50)
);

CREATE TABLE Cars (
    CarID INT PRIMARY KEY,
    Company NVARCHAR(50),
    Model NVARCHAR(50),
    Engine NVARCHAR(50),
    Transmission NVARCHAR(50),
    Color NVARCHAR(50),
    Body_Style NVARCHAR(50)
);

CREATE TABLE Sales (
    SaleID INT IDENTITY PRIMARY KEY,
    CarID INT FOREIGN KEY REFERENCES Cars(CarID),
    DealerID INT FOREIGN KEY REFERENCES Dealers(DealerID),
    CustomerID INT FOREIGN KEY REFERENCES Customers(CustomerID),
    SaleDate DATE,
    Price DECIMAL(10, 2)
);
