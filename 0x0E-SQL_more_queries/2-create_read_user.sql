-- Create database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create a user if they do not already exist, and set their authentication credentials
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant the SELECT privilege on all tables in the hbtn_0d_2 database to the user
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
-- Flush privileges to ensure that the changes take effect
FLUSH PRIVILEGES;
