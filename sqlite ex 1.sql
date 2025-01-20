SELECT Title
FROM Albums
WHERE AlbumId = '67';

SELECT Name, Milliseconds / 1000 AS LengthInSeconds
FROM tracks
WHERE Milliseconds BETWEEN 50000 AND 70000;

SELECT Title, Name
FROM albums
JOIN artists ON albums.ArtistId = artists.ArtistId
WHERE Name LIKE '%black%';

SELECT DISTINCT BillingCountry
FROM invoices

SELECT BillingCity, SUM(Total) AS TotalAmount
FROM invoices
GROUP BY BillingCity
ORDER BY TotalAmount DESC
LIMIT 1;

SELECT BillingCountry, COUNT(DISTINCT CustomerId) AS CustomerCount
FROM Invoices
WHERE BillingCountry IS NOT NULL
GROUP BY BillingCountry
ORDER BY CustomerCount DESC;

SELECT COUNT(*) 
FROM Invoices
WHERE InvoiceDate LIKE '2009%' OR InvoiceDate LIKE '2011%';

SELECT *
FROM Employees
WHERE Title LIKE '%Sales support Agent%';

-- SQLITE EX 2 --

SELECT MediaTypeId, COUNT(*) AS UsageCount
FROM Tracks
GROUP BY MediaTypeId
ORDER BY UsageCount DESC;

SELECT 
    Customers.FirstName || ' ' || Customers.LastName AS FullName,
    Invoices.InvoiceId,
    Invoices.InvoiceDate,
    Invoices.BillingCountry
FROM 
    Customers
JOIN 
    Invoices
ON 
    Customers.CustomerId = Invoices.CustomerId
WHERE 
    Invoices.BillingCountry = 'Brazil';

SELECT 
    Artists.Name AS ArtistName,
    COUNT(Tracks.TrackId) AS TotalTracks
FROM 
    Artists
JOIN 
    Albums
ON 
    Artists.ArtistId = Albums.ArtistId
JOIN 
    Tracks
ON 
    Albums.AlbumId = Tracks.AlbumId
WHERE 
    Tracks.GenreId = (SELECT GenreId FROM Genres WHERE Name = 'Rock')
GROUP BY 
    Artists.Name
ORDER BY 
    TotalTracks DESC
LIMIT 10;

SELECT 
    Customers.FirstName, 
    Customers.LastName, 
    Customers.CustomerId, 
    Customers.Country
FROM 
    Customers
WHERE 
    Customers.Country != 'USA';
