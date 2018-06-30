-- 百分号% 通配符，匹配任意字符任意次数（包括0次）,但不会匹配NULL的行
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE 'Fish%';

SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE '%Fish%';

SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE 'F%y';

-- 下划线_ 通配符，匹配任意字符1次数
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE '__ inch teddy bear';

-- 方括号[] 通配符，指定一个字符集，匹配指定位置的一个字符
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE '[JM]%' 
ORDER BY cust_contact;

-- 前缀字符^（脱字号）来否定
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE '[^JM]%' 
ORDER BY cust_contact;