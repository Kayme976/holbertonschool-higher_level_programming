-- Creates  the table id_not_null on your MySQL server
CREATE TABLE IF NOT EXISTS $1.id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);