-- creates a table called first_table in the current database
-- the database name will be passed as an argument
-- the script will not fail even if the table first_table already exists

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
