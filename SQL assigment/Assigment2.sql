SELECT LastName,FirstName,Total
FROM Invoice i join Customer c on i.CustomerId = c.CustomerId 
WHERE Country = "Germany"
ORDER BY Total DESC 

SELECT TrackId, Bytes, Name
FROM Track t 
ORDER BY Bytes DESC 

SELECT InvoiceId, TrackId
FROM InvoiceLine
WHERE InvoiceId = 410

SELECT Name, GenreId, COUNT(*) as Or_something
FROM Track
WHERE GenreId = 2 

SELECT BillingCountry, Total, COUNT(*) as counter 
FROM Invoice
WHERE BillingCountry = "USA" and Total > 10	 or BillingCountry <> "USA" and Total > 5

SELECT Total, CustomerId, SUM(TOTAL)
FROM Invoice
WHERE BillingCountry = "Germany" 
ORDER BY Total DESC	

SELECT SUM(Total), CustomerId
FROM Invoice i
GROUP BY CustomerId 
ORDER BY SUM(Total) DESC
LIMIT 5 OFFSET 20 

SELECT BillingCountry, Count(*) as counter
FROM Invoice i 
WHERE BillingCountry = "Germany"

SELECT BillingCountry, Total, ROUND(AVG(Total),2) as german_average
FROM Invoice i 
WHERE BillingCountry = "Germany"

SELECT TrackId, Quantity, InvoiceId, COUNT(TrackId)
FROM InvoiceLine i 
GROUP BY InvoiceId
ORDER BY COUNT(TrackId) DESC


SELECT AlbumId, COUNT(AlbumId) as counter, TrackId as long_track
FROM Track
WHERE Milliseconds >= 300000
GROUP BY AlbumId 
HAVING counter >= 10

SELECT UnitPrice, t.GenreId, ROUND(AVG(Milliseconds)) as Average, g.Name 
FROM Track t join Genre g on t.GenreId = g.GenreId
WHERE UnitPrice = "1.99"
GROUP BY t.GenreId
ORDER BY Average DESC 


SELECT (MAX(Total)-MIN(Total)) as Spending_range, CustomerId
FROM Invoice i 
GROUP BY CustomerId 
ORDER BY Spending_range DESC


#EXAM 

SELECT GenreId, UnitPrice, COUNT(TrackId) as counting
FROM Track t 
WHERE UnitPrice == '0.99' 
GROUP BY GenreId 
order by counting DESC 

SELECT Name
FROM Genre g 
WHERE GenreId = 3

SELECT i.CustomerId, InvoiceDate, FirstName, LastName
FROM Invoice i join Customer c on i.CustomerId = c.CustomerId 
WHERE InvoiceDate > 2012-01-31 & InvoiceDate < 2012-03-01 

SELECT i.CustomerId, InvoiceDate, FirstName, LastName
FROM Invoice i join Customer c on i.CustomerId = c.CustomerId 
WHERE LastName = 'Ramos'

SELECT GenreId, COUNT(Quantity) as counting, count(InvoiceLineId), COUNT(t.TrackId) 
FROM Track t join InvoiceLine il on t.TrackId = il.TrackId 
GROUP BY GenreId 
order by counting DESC

SELECT Name
FROM Genre g 
WHERE GenreId = 7

SELECT CustomerId, Total, AVG(Total), (SUM(Total)/COUNT(CustomerId)) as average
FROM Invoice i 
GROUP by CustomerId
having AVG(Total) > average

WITH customer_totals AS (
    SELECT CustomerId, SUM(Total) AS total_expenditure
    FROM Invoice
    GROUP BY CustomerId
)
SELECT CustomerId, total_expenditure
FROM customer_totals
WHERE total_expenditure > (
    SELECT AVG(total_expenditure) FROM customer_totals
);

SELECT BillingCountry, Total, CustomerId, InvoiceId
FROM Invoice
WHERE BillingCountry == 'USA'
order by Total DESC 

SELECT Country, COUNT(DISTINCT CustomerId) AS UniqueCustomers,
       RANK() OVER (ORDER BY COUNT(DISTINCT CustomerId) DESC) AS Rank
FROM Customer
GROUP BY Country
ORDER BY Rank;

SELECT FirstName, LastName
from Customer
WHERE Country = 'Germany'

SELECT t.TrackId, Quantity 
FROM Track t join InvoiceLine il on t.TrackId = il.TrackId 
group by t.TrackId 
order by Quantity DESC

SELECT InvoiceID, COUNT(InvoiceId), Total 
FROM Track t join Invoice i on t.TrackId = il.TrackId 
FROM Invoice
ORDER BY Total DESC



SELECT InvoiceDate, SUM(Total) AS TotalExpenditure
FROM Invoice
WHERE BillingCountry = 'Austria' AND InvoiceDate IN (2010-01-01, 2012-12-31)
GROUP BY InvoiceDate
ORDER BY TotalExpenditure 
