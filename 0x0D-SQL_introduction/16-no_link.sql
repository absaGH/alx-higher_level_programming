-- lists all records of the table second_table of the database hbtn_0c_0
-- it doesn't display rows without a name value
-- display the score and the name (in this order)
-- display the record by descending score
-- the database name will be passed as an argument to the mysql command

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
