-- Create a new user 'user_0d_1' if it doesn't already exist, with a password 'user_0d_1_pwd',
-- allowing them to connect from 'localhost
-- Grant all privileges to the user 'user_0d_1' when accessing any database and table
-- using the 'user_0d_1'@'localhost' login
-- Update the privilege table to reflect the changes made
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
