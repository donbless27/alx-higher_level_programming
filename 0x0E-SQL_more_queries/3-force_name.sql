-- creates the table force_name on your MySQL server
-- The database name will be passed as an argument of the mysql command
-- The script should not fail If the table force_name already exists
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
