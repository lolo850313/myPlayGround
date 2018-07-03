-- GROUP BY。num_prods为计算字段（用COUNT（*）函数建立）
SELECT vend_id , COUNT(*) AS num_prods
FROM Products
GROUP BY vend_id;

