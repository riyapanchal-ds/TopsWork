
CREATE TABLE customer5 (
    cust_id INT PRIMARY KEY,
    cust_name VARCHAR(50),
    city VARCHAR(50),
    email VARCHAR(100),
    join_date DATE
);

CREATE TABLE products5 (
    prod_id INT PRIMARY KEY,
    prod_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock INT
);

CREATE TABLE orders5 (
    order_id INT PRIMARY KEY,
    cust_id INT,
    order_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (cust_id) REFERENCES customer5(cust_id)
);

CREATE TABLE order_items5 (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    prod_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders5(order_id),
    FOREIGN KEY (prod_id) REFERENCES products5(prod_id)
);

INSERT INTO customer5 VALUES
(1, 'Amit Sharma', 'Delhi', 'amit@gmail.com', '2022-01-15'),
(2,'hani', 'Ahemadabad','hani@gmail.com','2023-02-16'),
(3,'pooja','mumbai','pooja@gmail.com','2022-01-4'),
(4,'maya','goa','maya@gmail.com','2024-03-22'),
(5,'payal','surat','payal@gmail.com','2024-07-21');
select *from customer5;

INSERT INTO products5 VALUES
(101, 'Laptop', 'Electronics', 65000, 50),
(102, 'Smartphone', 'Electronics', 20000.00, 25),
(103, 'Chair', 'Furniture', 1500.00, 50),
(104, 'Book', 'Stationery', 300.00, 100),
(105, 'Headphones', 'Electronics', 2500.00, 30
);

select* from products5;

INSERT INTO orders5 (order_id, cust_id, order_date, status) VALUES
(1001, 1, '2026-04-01', 'Pending'),
(1002, 2, '2026-04-05', 'Shipped'),
(1003, 3, '2026-04-10', 'Delivered'),
(1004, 1, '2026-04-15', 'Cancelled'),
(1005, 2, '2026-04-20', 'Processing');

select*from orders5;


INSERT INTO order_items5 VALUES
(1, 1001, 101, 1),
(2, 1002, 102, 2),
(3, 1003, 103, 3),
(4, 1004, 104, 4),
(5, 1005, 105, 5);

select* from order_items5;

-- 1..Count how many orders each customer has placed.
select count(*), cust_name
from customer5,orders5
where customer5.cust_id=orders5.cust_id group by cust_name;

-- 2..Find the total quantity of products ordered in each order.
SELECT SUM(quantity) AS total_quantity, orders5.order_id FROM orders5, order_items5
WHERE orders5.order_id = order_items5.order_id GROUP BY orders5.order_id;

-- 3..Display the most expensive product in each category.
select category,prod_name,price from products5 where
price = (select max(price) from products5 where category = products5.category);
 
 -- 4..Find customers who have never placed an order.
select customer5.cust_id,customer5.cust_name  from customer5 left join
orders5 on customer5.cust_id=orders5.cust_id where orders5.order_id is null;

-- 5.. Show total sales (price × quantity) of each product.
select products5.prod_name,sum(products5.price*order_items5.quantity)as
total_sales from products5 join order_items5 on products5.prod_id=order_items5.prod_id
group by products5.prod_name;

-- 6.. List all products that have been ordered more than 2 times.
select products5.prod_name,order_items5.quantity from products5 join
order_items5 on products5.prod_id = order_items5.prod_id where order_items5.quantity>2;

-- 7.. Find the total revenue generated in 2024.
SELECT SUM(products5.price * order_items5.quantity) AS total_revenue FROM orders5 
JOIN order_items5 ON order_items5.order_id = order_items5.order_id
JOIN products5 ON order_items5.prod_id = products5.prod_id WHERE YEAR(orders5.order_date) = 2024;

-- 8..Display all orders along with customer names and order status.
SELECT orders5.order_id,customer5.cust_name,orders5.status FROM orders5 
JOIN customer5 ON orders5.cust_id = customer5.cust_id;

-- 9.. Show the number of “Delivered” vs “Cancelled” orders.
SELECT status,COUNT(*) as total_orders from orders5 WHERE status in ('Delivered', 'Cancelled')
GROUP BY status;