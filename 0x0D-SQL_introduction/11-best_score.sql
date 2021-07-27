-- lists all records with a score >= 10 in second_table(hbtn_0c_0)
-- display both the score and the name (in this order)
-- display records ordered by score(top first)
-- the database name will be passed as an argument of the mysql command

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
