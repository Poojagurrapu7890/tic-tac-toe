
USE orders;
show tables;
Select * from address;
 describe product;
 describe carton;
 Select * from online_customer;
 Select * from product_class;
 Select * from shipper;
 Select * from order_items;
 Select * from  order_items where order_id = 10013;
 Select * from order_header where order_id = 10013;
-- Q1: Display product details with adjusted prices and sort by category (descending): --

-- If the category is 2050, increase the price by ₹2000.
-- If the category is 2051, increase the price by ₹500.
-- If the category is 2052, increase the price by ₹600.

SELECT 
    product_class_code,
    product_id,
    product_desc,
    CASE
        WHEN product_class_code = 2050 THEN product_price + 2000
        WHEN product_class_code = 2051 THEN product_price + 500
        WHEN product_class_code = 2052 THEN product_price + 600
        ELSE product_price
    END AS adjusted_product_price
FROM
    PRODUCT
ORDER BY product_class_code DESC;

-- Q2:
-- Display inventory status based on product quantity:
-- For Electronics & Computer:
-- ≤ 10: Low stock, 11–30: In stock, ≥ 31: Enough stock.
-- For Stationery & Clothes:
-- ≤ 20: Low stock, 21–80: In stock, ≥ 81: Enough stock.
-- For other categories:
-- ≤ 15: Low stock, 16–50: In stock, ≥ 51: Enough stock.
-- If quantity is 0, show "Out of stock."

SELECT 
    product_class.product_class_desc, 
    product.product_id, 
    product.product_desc, 
    product.product_quantity_avail,
    CASE 
        WHEN product.product_quantity_avail = 0 THEN 'Out of stock'
        WHEN product_class.product_class_desc IN ('Electronics', 'Computer') THEN 
            CASE 
                WHEN product.product_quantity_avail <= 10 THEN 'Low stock'
                WHEN product.product_quantity_avail BETWEEN 11 AND 30 THEN 'In stock'
                WHEN product.product_quantity_avail >= 31 THEN 'Enough stock'
            END
        WHEN product_class.product_class_desc IN ('Stationery', 'Clothes') THEN 
            CASE 
                WHEN product.product_quantity_avail <= 20 THEN 'Low stock'
                WHEN product.product_quantity_avail BETWEEN 21 AND 80 THEN 'In stock'
                WHEN product.product_quantity_avail >= 81 THEN 'Enough stock'
            END
        ELSE 
            CASE 
                WHEN product.product_quantity_avail <= 15 THEN 'Low stock'
                WHEN product.product_quantity_avail BETWEEN 16 AND 50 THEN 'In stock'
                WHEN product.product_quantity_avail >= 51 THEN 'Enough stock'
            END
    END AS inventory_status
FROM 
    product
JOIN 
    product_class ON product.product_class_code = product_class.product_class_code;
-- Q3:
-- Count cities in countries (excluding USA & Malaysia) with more than 1 city, sorted by descending city count:

SELECT 
    country, 
    COUNT(city) AS city_count
FROM 
    ADDRESS
WHERE 
    country NOT IN ('USA', 'MALAYSIA')
GROUP BY 
    country
HAVING 
    city_count > 1
ORDER BY 
    city_count DESC;


-- Q4:
-- Display customer details and order information for cities with pin codes that do not contain '0':

SELECT 
    online_customer.customer_id, 
    CONCAT(online_customer.CUSTOMER_FNAME, ' ', online_customer.CUSTOMER_LNAME) AS customer_full_name,
    address.city, 
    address.pincode, 
    order_header.order_id, 
    product_class.product_class_desc, 
    product.product_desc, 
    order_items.product_quantity * product.product_price AS subtotal
FROM 
    online_customer
JOIN 
    address ON online_customer.address_id = address.address_id
JOIN 
    order_header ON online_customer.customer_id = order_header.customer_id
JOIN 
    order_items ON order_header.order_id = order_items.order_id
JOIN 
    product ON order_items.product_id = product.product_id
JOIN 
    product_class ON product.product_class_code = product_class.product_class_code
WHERE 
    address.pincode NOT LIKE '%0%' 
ORDER BY 
    customer_full_name, subtotal;
-- Q5:
-- Find the product with the maximum quantity bought (quantity-wise) along with product ID 201:
SELECT 
    product.product_id, 
    product.product_desc, 
    SUM(order_items.product_quantity) AS totalquantity
FROM order_items
JOIN product ON order_items.product_id = product.product_id
WHERE order_items.product_id = 201 OR order_items.product_id = (
        SELECT order_items.product_id
        FROM order_items
        GROUP BY order_items.product_id
        ORDER BY SUM(order_items.product_quantity) DESC
        LIMIT 1
	)
GROUP BY product.product_id, product.product_desc;

-- Q6:
-- Display all customers (with or without orders) along with order details:

SELECT 
    online_customer.customer_id,
    CONCAT(online_customer.CUSTOMER_FNAME, ' ', online_customer.CUSTOMER_LNAME) AS customer_name,
    online_customer.CUSTOMER_EMAIL,
    order_header.order_id,
    product.product_desc,
    order_items.product_quantity,
    (order_items.product_quantity * product.product_price) AS subtotal
FROM 
    online_customer
LEFT JOIN 
    order_header ON online_customer.customer_id = order_header.customer_id
LEFT JOIN 
    order_items ON order_header.order_id = order_items.order_id
LEFT JOIN 
    product ON order_items.product_id = product.product_id;
-- Q7:
-- Find the optimum carton with the least volume greater than the total item volume for order ID 10006:

SELECT 
    CARTON.CARTON_ID, 
    CARTON.LEN * CARTON.WIDTH * CARTON.HEIGHT AS carton_volume
FROM 
    CARTON
WHERE 
    CARTON.LEN * CARTON.WIDTH * CARTON.HEIGHT > (
        SELECT 
            SUM(PRODUCT.LEN * PRODUCT.WIDTH * PRODUCT.HEIGHT * ORDER_ITEMS.PRODUCT_QUANTITY)
        FROM 
            ORDER_ITEMS
        JOIN 
            PRODUCT ON ORDER_ITEMS.PRODUCT_ID = PRODUCT.PRODUCT_ID
        WHERE 
            ORDER_ITEMS.ORDER_ID = 10006
    )
ORDER BY 
    carton_volume
LIMIT 1;

-- Q8:
-- Display customers who bought more than 10 products per shipped order:

SELECT 
    order_header.customer_id,
    CONCAT(online_customer.CUSTOMER_FNAME, ' ', online_customer.CUSTOMER_LNAME) AS customer_full_name,
    order_header.order_id,
    SUM(order_items.product_quantity) AS total_order_quantity
FROM 
    order_header
JOIN 
    online_customer ON order_header.customer_id = online_customer.customer_id
JOIN 
    order_items ON order_header.order_id = order_items.order_id
WHERE order_header.order_status = 'Shipped'     
GROUP BY 
    order_header.customer_id, online_customer.CUSTOMER_FNAME, online_customer.CUSTOMER_LNAME, order_header.order_id
HAVING 
    SUM(order_items.product_quantity) > 10;
-- Q9:
-- Display total product quantity shipped for orders with ID > 10060:
 
SELECT 
    order_header.order_id,
    order_header.customer_id,
    CONCAT(online_customer.CUSTOMER_FNAME, ' ', online_customer.CUSTOMER_LNAME) AS customer_full_name,
    SUM(order_items.product_quantity) AS total_quantity
FROM 
    order_header
JOIN 
    online_customer ON order_header.customer_id = online_customer.customer_id
JOIN 
    order_items ON order_header.order_id = order_items.order_id
WHERE 
    order_header.order_id > 10060
GROUP BY 
    order_header.order_id, order_header.customer_id, customer_full_name;
-- Q10:
-- Find the product class with the highest quantity shipped to countries other than India and USA, along with the total value:
SELECT 
    product_class.product_class_desc, 
    SUM(order_items.product_quantity) AS total_quantity,
    SUM(order_items.product_quantity * product.product_price) AS total_value
FROM 
    order_items
JOIN 
    product USING(product_id)
JOIN 
    product_class USING(product_class_code)
JOIN 
    order_header USING(order_id)
JOIN 
    online_customer USING(customer_id)
JOIN 
    address USING(address_id)
WHERE 
    address.country NOT IN ('India', 'USA')
GROUP BY 
    product_class.product_class_desc
ORDER BY 
    total_quantity DESC
LIMIT 1;

