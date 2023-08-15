-- This query removes low-scoring records from 'second_table'
DELETE FROM second_table WHERE score <= 5;
