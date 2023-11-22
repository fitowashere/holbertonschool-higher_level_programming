-- Script that list all records with a score less than 10 in table
SELECT score, name FROM second_table HAVING score>=10 ORDER BY score DESC;