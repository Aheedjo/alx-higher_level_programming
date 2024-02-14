-- a script that lists all records of the table second_table
-- Records should be listed by descending score
-- Results should display the score and the name (in this order)
-- Don’t list rows without a name value

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;

