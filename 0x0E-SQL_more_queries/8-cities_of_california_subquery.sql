-- lists all the cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;
SELECT name
FROM cities
WHERE name = "California"
ORDER BY cities ASC;
