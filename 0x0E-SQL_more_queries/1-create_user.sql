-- Create a new user 'user_0d_1' if it doesn't already exist, with a password 'user_0d_1_pwd',
-- allowing them to connect from 'localhost
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to the user 'user_0d_1' when accessing any database and table
-- using the 'user_0d_1'@'localhost' login
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
-- Update the privilege table to reflect the changes made
FLUSH PRIVILEGES;
