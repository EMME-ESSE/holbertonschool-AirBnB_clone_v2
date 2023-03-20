-- script that prepares the MySQL server for the project
--creation of the database 
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creation of the user 
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost"
-- password for the user
SET PASSWORD FOR "hbnb_dev"@"localhost" = hbnb_dev_pwd;
-- give all privileges to the user on the database
GRANT ALL PRIVILEGES ON hbnb_dev_db TO "hbnb_dev"@"localhost";
-- gives the select privileges to the user
GRANT SELECT PRIVILEGES ON performance_schema TO "hbnb_dev"@"localhost";