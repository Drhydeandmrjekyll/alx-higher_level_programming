-- Defines a table 'unique_id' if it doesn't exist, having columns 'id' (INT with default 1) and 'name' (VARCHAR(256)).
-- The 'id' column values are unique due to the defined uniqueness constraint.
CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
