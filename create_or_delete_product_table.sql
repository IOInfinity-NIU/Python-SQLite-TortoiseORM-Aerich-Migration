-- SQLite
-- Create Time: 2022/12/02
-- Title      : Create or delete product table
-- File Name  : create_or_delete_product_table.sql
-- Author     : IOInfinity x 源碼無限 <ioinfinity.studio@gmail.com>


-- Create product table
CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(64) NOT NULL,
    product_type VARCHAR(16) NOT NULL,
    base64_image TEXT NULL 
);


-- Delete product table
DROP TABLE product;
