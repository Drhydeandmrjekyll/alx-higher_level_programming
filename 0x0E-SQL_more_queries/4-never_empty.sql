-- Creates a table 'id_not_null' if not already existing, with columns 'id' (INT with default 1) and 'name' (VARCHAR(256)).
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
