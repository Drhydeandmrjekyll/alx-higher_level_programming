-- Creates a database 'hbtn_0d_usa' if it doesn't already exist.
-- Within the database, a table 'states' is defined with columns:
--   - 'id' (INT) as a unique, non-null, auto-incremented primary key.
--   - 'name' (VARCHAR(256)) as a non-null column to store state names.
-- This table structure could be used to store and manage information about states in the USA.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL);
