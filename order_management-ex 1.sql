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
