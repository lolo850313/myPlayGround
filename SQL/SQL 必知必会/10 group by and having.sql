-- concatenate 加号 + 或 双竖杠 || 表示(依据软件不同而不同)。将两列拼接起来。
SELECT vend_name + ' (' + vend_country + ') '
FROM Vendors
ORDER BY vend_name;

SELECT vend_name ||' (' + vend_country || ') '
FROM Vendors
ORDER BY vend_name;

-- 使用RTRIM（），LTRIM（），TRIM（）去掉左右空格
SELECT vend_name + ' (' + RTRIM(vend_country) + ') '
FROM Vendors
ORDER BY vend_name;

SELECT vend_name +|| '(' + RTRIM(vend_country) || ') '
FROM Vendors
ORDER BY vend_name;

-- 使用AS（alias）是一个字段或值的替换名，以供客户端引用
SELECT vend_name + ' (' + RTRIM(vend_country) + ') '
AS vend_title
FROM Vendors
ORDER BY vend_name;

SELECT vend_name +|| '(' + RTRIM(vend_country) || ') '
AS vend_title
FROM Vendors
ORDER BY vend_name;