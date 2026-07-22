-- ==========================================
-- DataForge ETL Database Schema
-- ==========================================

CREATE DATABASE IF NOT EXISTS dataforge_etl;

USE dataforge_etl;

-- ==========================================
-- Customers Table
-- ==========================================

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL
);

-- ==========================================
-- Products Table
-- ==========================================

CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL UNIQUE
);

-- ==========================================
-- Transactions Table
-- ==========================================

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    transaction_date DATE NOT NULL,

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);



-- Example
-- Format of creating database

CREATE DATABASE dataforge_etl;

USE dataforge_etl;

-- customer table--
CREATE TABLE customers(
	customer_id INT PRIMARY KEY,
    customer_name varchar(100)
);

show tables;

describe customers;

-- product table
create table products (
		product_id int primary key,
        product_name varchar(100) NOT NULL
);
describe products;

-- transactions table
create table transactions (
	transaction_id INT primary key,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price decimal(10, 2) NOT NULL,
    transaction_date date not null
); 

describe transactions;


alter table transactions
add constraint fk_customer
foreign key (customer_id)
references customers(customer_id);


alter table transactions
add constraint fk_product
foreign key (product_id)
references products (product_id);

drop table if exists transactions;

drop table if exists products;





-- Designinig new schema for dataforge-etl

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    transaction_date DATE NOT NULL
    );

alter table transactions
add constraint fk_customer
foreign key (customer_id)
references customers(customer_id);

alter table transactions
add constraint fk_product
foreign key (product_id)
references products(product_id);

describe customers;
describe transactions;
describe products;
show tables;

select * from customers;
select * from products
order by product_id;

select * from transactions;


