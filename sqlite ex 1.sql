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
