CREATE TABLE customer7 (
    cust_id INT PRIMARY KEY,
    cust_name VARCHAR(50),
    city VARCHAR(50),
    email VARCHAR(100),
    join_date DATE
);

CREATE TABLE products (
    prod_id INT PRIMARY KEY,
    prod_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock INT
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    cust_id INT,
    order_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (cust_id) REFERENCES customer7(cust_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    prod_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (prod_id) REFERENCES products(prod_id)
);
INSERT INTO customer7 VALUES
(1, 'Amit Sharma', 'Delhi', 'amit@gmail.com', '2022-01-15'),
(2,'hani', 'Ahemadabad','hani@gmail.com','2023-02-16'),
(3,'pooja','mumbai','pooja@gmail.com','2022-01-4'),
(4,'maya','goa','maya@gmail.com','2024-03-22'),
(5,'payal','surat','payal@gmail.com','24-07-21');

select *from customer7;

INSERT INTO products VALUES
(101, 'Laptop', 'Electronics', 65000, 50),
(102, 'Smartphone', 'Electronics', 20000.00, 25),
(103, 'Chair', 'Furniture', 1500.00, 50),
(104, 'Book', 'Stationery', 300.00, 100),
(105, 'Headphones', 'Electronics', 2500.00, 30);

select* from products;

INSERT INTO orders (order_id, cust_id, order_date, status) VALUES
(1001, 1, '2026-04-01', 'Pending'),
(1002, 2, '2026-04-05', 'Shipped'),
(1003, 3, '2026-04-10', 'Delivered'),
(1004, 1, '2026-04-15', 'Cancelled'),
(1005, 2, '2026-04-20', 'Processing');

select*from orders;


INSERT INTO order_items VALUES
(1, 1001, 101, 1),
(2, 1002, 102, 2),
(3, 1003, 103, 3),
(4, 1004, 104, 4),
(5, 1005, 105, 5);

select* from order_items;

select* from customer7 where city = 'mumbai';
select* from products where category = 'Electronics';
select* from orders where status = 'delivered';
select* from orders where order_date > '2023-01-31';
select* from products where price>10000;
select count(*) as total_customers from customers;
select prod_name, stock from products;
select *from orders where order_date between '2024-08-01' and '2024-08-31';
select * from customer7 where cust_name LIKE 'A%';
select *from products order by price ASC LIMIT 1;
select cust_id,count(*) from orders group by cust_id;