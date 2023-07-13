-- Active: 1689074010025@@127.0.0.1@3306@database_1
-- We can use database_name.table_name in order to make a table for the specific database
CREATE TABLE if NOT EXISTS database_1.table_name(c1 INT,c2 VARCHAR(50),c3 FLOAT,c4 INT,c5 VARCHAR(60));
-- Using command to create a table in database_2 from database_1 itself
CREATE TABLE if NOT EXISTS database_2.table_name(c1 INT,c2 VARCHAR(50),c3 FLOAT,c4 INT,c5 VARCHAR(60));
