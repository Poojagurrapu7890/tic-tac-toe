USE orders;
show tables;

 drop table address;
 describe product;
 describe carton;

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
ORDER BY 
   product_class_code DESC
LIMIT 60;


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
    city_count DESC
LIMIT 2;

SELECT 
    online_customer.customer_id, 
    online_customer.CUSTOMER_FNAME || ' ' || online_customer.CUSTOMER_LNAME,
    address.city, 
    address.pincode, 
    order_header.order_id, 
    product_class.product_class_desc, 
    product.product_desc, 
    order_items.product_quantity * product.product_price 
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
    online_customer.CUSTOMER_FNAME || ' ' || online_customer.CUSTOMER_LNAME, 
    order_items.product_quantity * product.product_price;

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
    order_header.order_id, order_header.customer_id, online_customer.CUSTOMER_FNAME, online_customer.CUSTOMER_LNAME;
    
SELECT 
    order_header.customer_id,
    CONCAT(online_customer.first_name, ' ', online_customer.last_name) AS customer_full_name,
    order_header.order_id,
    SUM(order_items.product_quantity) AS total_order_quantity
FROM 
    order_header
JOIN 
    online_customer ON order_header.customer_id = online_customer.customer_id
JOIN 
    order_items ON order_header.order_id = order_items.order_id
GROUP BY 
    order_header.customer_id, online_customer.first_name, online_customer.last_name, order_header.order_id
HAVING 
    SUM(order_items.product_quantity) > 10;

