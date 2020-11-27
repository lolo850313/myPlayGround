-- 聚积函数，对某些行运行的函数，计算并返回一个值。
-- AVG（）函数，平均数函数。
SELECT AVG(prod_price) AS avg_price
FROM Products;

-- AVG也可以确定特定行列的平均值
SELECT AVG(prod_price) AS avg_price
FROM Products
WHERE vend_id = "DLL01";

-- COUNT()确定表中行的数目或符合特定条件的行数目
-- COUNT(*)对表中行数目进行计算，不管列中包含是NULL还是非NULL值。
SELECT COUNT(*) AS num_cust
FROM Customers;

-- COUNT（）对特定列中具有值的行进行计算，忽略NULL
SELECT COUNT(cust_email) AS num_cust
FROM Customers;

-- MAX()返回指定列中的最大值，忽略NULL
SELECT MAX(prod_price) AS max_price
FROM Products;

-- MIN()返回指定列中的最大值，忽略NULL
SELECT MIN(prod_price) AS max_price
FROM Products;

-- SUM()返回指定列中的和，忽略NULL
SELECT SUM(quantity) AS item_ordered
FROM OrderItems
WHERE order_num = 20005;

-- SUM()用来合计计算值。
SELECT SUM(item_price*quantity) AS total_price
FROM OrderItems
WHERE order_num = 20005;

-- 对以上5个聚集函数都可以使用ALL参数或DISTINCT。ALL为默认，不指定DISTINCT即为ALL。
SELECT AVG(DISTINCT prod_price) AS avg_price
FROM Products
WHERE vend_id = "DLL01";

-- 组合聚集函数
SELECT COUNT(*) AS num_items,
        MIN(prod_price) AS price_min,
        MAX(prod_price) AS price_max,
        AVG(prod_price) AS price_avg, 
FROM Products;