-- Creates  the table force_name on your MySQL server
CREATE TABLE IF NOT EXISTS $1.force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);