-- creates the table force_name on your MySQL server
-- force_name attributes: id INT, name VARCHAR(256) can’t be null
-- The database name will be passed as an argument of the mysql command
-- Even if the table force_name already exists, the script will not fail

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
