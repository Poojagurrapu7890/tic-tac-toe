SELECT Title
FROM Albums
WHERE AlbumId = '67';

SELECT Name, Milliseconds / 1000 AS LengthInSeconds
FROM tracks
WHERE Milliseconds BETWEEN 50000 AND 70000;
