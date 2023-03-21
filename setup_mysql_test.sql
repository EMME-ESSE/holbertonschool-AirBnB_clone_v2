--creation of the database 
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creation of the user 
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" IDENTIFIED BY 'hbnb_test_pwd';

-- give all privileges to the user on the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";

-- gives the select privileges to the user
GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost";