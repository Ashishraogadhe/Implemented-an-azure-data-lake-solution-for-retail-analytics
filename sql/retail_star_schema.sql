CREATE TABLE dbo.DimCustomer (
    CustomerKey INT IDENTITY(1,1) PRIMARY KEY,
    CustomerId NVARCHAR(50),
    FirstName NVARCHAR(100),
    LastName NVARCHAR(100),
    Email NVARCHAR(255),
    Country NVARCHAR(50)
);

CREATE TABLE dbo.DimProduct (
    ProductKey INT IDENTITY(1,1) PRIMARY KEY,
    ProductId NVARCHAR(50),
    ProductName NVARCHAR(255),
    Category NVARCHAR(100),
    Brand NVARCHAR(100)
);

CREATE TABLE dbo.DimDate (
    DateKey INT PRIMARY KEY,
    [Date] DATE,
    Year INT,
    Month INT,
    Day INT
);

CREATE TABLE dbo.FactSales (
    SalesId NVARCHAR(50),
    CustomerKey INT,
    ProductKey INT,
    DateKey INT,
    StoreId NVARCHAR(50),
    Quantity INT,
    SalesAmount DECIMAL(18,2),
    Currency NVARCHAR(10)
);
