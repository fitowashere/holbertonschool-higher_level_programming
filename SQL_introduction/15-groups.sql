-- Script to list the number of records with the same score in 'second_table'
-- and sort the results by the count of records in descending order

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;