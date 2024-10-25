# Delopgave 2 

### del 2
SELECT * 
FROM PRODUCTS
ORDER BY UnitPrice;


### del 3
SELECT CustomerID
FROM customers
WHERE country IN ('Spain', 'UK');

### del 4 - found 2 only
SELECT *
FROM PRODUCTS 
WHERE UnitsInStock >100 and UnitPrice >=25;

### del 5
SELECT DISTINCT ShipCountry 
FROM Orders;

### del 6
SELECT OrderID
FROM Orders
WHERE MONTH(OrderDate) = 10 and YEAR(ORderDate) = 1996;

### del 7
SELECT OrderID
FROM Orders
WHERE ShipRegion is NULL 
and 
ShipCountry = 'Germany'
and
Freight >= 100
and
EmployeeID = 1
and
YEAR(OrderDate) = 1996;


### del 8
SELECT *
FROM Orders
WHERE ShippedDate > RequiredDate;


### del 9
SELECT OrderID
From Orders
WHERE YEAR(OrderDate) = 1997 
and MONTH(OrderDate) IN (01,02,03,04)  # selecting months 
and ShipCountry = 'Canada';


### del 10
SELECT OrderID
FROM Orders
WHERE 
EmployeeID IN (2,5,8)
and 
not ShipRegion is NULL
and ShipVia IN (1,3)
order by EmployeeID, ShipVia ASC;


### del 11 (har en fejl - ReportsTo doesnt exist)
SELECT EmployeeID
FROM Employees
WHERE not Region IS NULL
# OR ReportsTo IS NULL
and YEAR(BirthDate) < 1961;

### del 11 (
SELECT EmployeeID
FROM Employees
WHERE not Region IS NULL
# OR ReportsTo IS NULL
and YEAR(BirthDate) < 1961;