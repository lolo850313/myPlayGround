-- concatenate 加号 + 或 双竖杠 || 表示(依据软件不同而不同)。将两列拼接起来。
SELECT vend_name + ' (' + vend_country + ') '
FROM Vendors
ORDER BY vend_name;
