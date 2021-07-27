-- lists the number of records with the same score in second_table(hbtn_0c_0)
-- the list will be sorted by the number of records(descending)
-- the database name will be passed as an argument to the mysql command

SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
