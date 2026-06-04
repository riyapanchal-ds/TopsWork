CREATE TABLE customer6 (
    cust_id INT PRIMARY KEY,
    cust_name VARCHAR(50),
    city VARCHAR(50),
    email VARCHAR(100),
    join_date DATE
);

CREATE TABLE products6 (
    prod_id INT PRIMARY KEY,
    prod_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock INT
);

CREATE TABLE orders6 (
    order_id INT PRIMARY KEY,
    cust_id INT,
    order_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (cust_id) REFERENCES customer6(cust_id)
);

CREATE TABLE order_items6 (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    prod_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders6(order_id),
    FOREIGN KEY (prod_id) REFERENCES products6(prod_id)
);

INSERT INTO customer6 VALUES
(1, 'Amit Sharma', 'Delhi', 'amit@gmail.com', '2022-01-15'),
(2,'hani', 'Ahemadabad','hani@gmail.com','2023-02-16'),
(3,'pooja','mumbai','pooja@gmail.com','2022-01-4'),
(4,'maya','goa','maya@gmail.com','2024-03-22'),
(5,'payal','surat','payal@gmail.com','2024-07-21');
select *from customer6;

INSERT INTO products6 VALUES
(101, 'Laptop', 'Electronics', 65000, 50),
(102, 'Smartphone', 'Electronics', 20000.00, 25),
(103, 'Chair', 'Furniture', 1500.00, 50),
(104, 'Book', 'Stationery', 300.00, 100),
(105, 'Headphones', 'Electronics', 2500.00, 30
);

select* from products6;

INSERT INTO orders6 (order_id, cust_id, order_date, status) VALUES
(1001, 1, '2026-04-01', 'Pending'),
(1002, 2, '2026-04-05', 'Shipped'),
(1003, 3, '2026-04-10', 'Delivered'),
(1004, 1, '2026-04-15', 'Cancelled'),
(1005, 2, '2026-04-20', 'Processing');

select*from orders6;


INSERT INTO order_items6 VALUES
(1, 1001, 101, 1),
(2, 1002, 102, 2),
(3, 1003, 103, 3),
(4, 1004, 104, 4),
(5, 1005, 105, 5);

-- Advance level

-- Display the product categories ranked by total sales.
select products6.category,SUM(products6.price * order_items6.quantity) as total_sales
from products6 join order_items6 on products6.prod_id = order_items6.prod_id group by products6.category
order by total_sales desc;

-- Find customers who have purchased both “Laptop” and “Headphones”.
SELECT customer6.cust_name FROM customer6 JOIN orders6  ON customer6.cust_id = orders6.cust_id
JOIN order_items6  ON orders6.order_id = order_items6.order_id JOIN products6  ON order_items6.prod_id = products6.prod_id
WHERE products6.prod_name IN ('Laptop', 'Headphones') GROUP BY customer6.cust_id, customer6.cust_name
HAVING COUNT(DISTINCT products6.prod_name) = 2;


-- Show products that were never ordered.
SELECT products6.prod_name FROM products6 LEFT JOIN order_items6 
ON products6.prod_id = order_items6.prod_id WHERE order_items6.prod_id IS NULL;

-- Find orders with multiple products from different categories.
SELECT order_id FROM order_items6 JOIN products6 ON order_items6.prod_id = products6.prod_id
GROUP BY order_id HAVING COUNT(DISTINCT category) >1 ;


-- Calculate each month’s total revenue and show a running total.
SELECT MONTH(orders6.order_date) AS month,SUM(products6.price * order_items6.quantity) AS total_revenue
FROM orders6 JOIN order_items6 ON orders6.order_id = order_items6.order_id  JOIN products6 
ON order_items6.prod_id = products6.prod_id GROUP BY MONTH(orders6.order_date);


-- Display the average order value per customer.
SELECT customer6.cust_name,AVG(products6.price * order_items6.quantity) AS average_value
FROM customer6 JOIN orders6  ON customer6.cust_id = orders6.cust_id
JOIN order_items6  ON orders6.order_id = order_items6.order_id
JOIN products6 ON order_items6.prod_id = products6.prod_id
GROUP BY customer6.cust_name;

-- Show the most frequently ordered product.
SELECT products6.prod_name ,COUNT(*) AS times_ordered FROM products6 
JOIN order_items6 ON products6.prod_id = order_items6.prod_id
GROUP BY products6.prod_name ORDER BY times_ordered DESC LIMIT 1;


-- List customers who placed orders in at least 3 different months.
SELECT customer6.cust_name FROM customer6 
JOIN orders6 ON customer6.cust_id = orders6.cust_id
GROUP BY customer6.cust_name HAVING COUNT(DISTINCT MONTH(orders6.order_date)) >= 3;

-- Find products that are out of stock or nearly out of stock (less than 10 units).
SELECT prod_name, stock FROM products6 WHERE stock < 10;
