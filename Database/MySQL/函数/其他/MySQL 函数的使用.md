**案例目的：**

使用各种函数操作数据，掌握各种函数的作用和使用方法。

**案例操作过程：**

**步骤 01：** 使用数学函数 `RAND()` 生成 3 个 10 以内的随机整数。

```sql
mysql> SELECT ROUND(RAND() * 10), ROUND(RAND() * 10), ROUND(RAND() * 10);
+--------------------+--------------------+--------------------+
| ROUND(RAND() * 10) | ROUND(RAND() * 10) | ROUND(RAND() * 10) |
+--------------------+--------------------+--------------------+
|                  6 |                  5 |                  9 |
+--------------------+--------------------+--------------------+
1 row in set (0.00 sec)
```

**步骤 02：**使用 `SIN()`、`COS()`、`TAN()`、`COT()` 函数计算三角函数值，并将计算结果转换成整数值。

```sql
mysql> SELECT PI(), SIN(PI() / 2), COS(PI()), ROUND(TAN(PI()/4)), FLOOR(COT(PI() / 4));
+----------+---------------+-----------+--------------------+----------------------+
| PI()     | SIN(PI() / 2) | COS(PI()) | ROUND(TAN(PI()/4)) | FLOOR(COT(PI() / 4)) |
+----------+---------------+-----------+--------------------+----------------------+
| 3.141593 |             1 |        -1 |                  1 |                    1 |
+----------+---------------+-----------+--------------------+----------------------+
1 row in set (0.00 sec)
```

**步骤 03：**创建表，并使用字符串和日期函数对字段值进行操作。

```sql
mysql> CREATE TABLE member (m_id INT AUTO_INCREMENT PRIMARY KEY, m_FN VARCHAR(100), m_LN VARCHAR(100), m_birth DATETIME, m_info VARCHAR(255) NULL);
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO member VALUES (NULL, 'Halen ', 'Park', '1970-06-29', 'GoodMan ');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM member;
+------+--------+------+---------------------+----------+
| m_id | m_FN   | m_LN | m_birth             | m_info   |
+------+--------+------+---------------------+----------+
|    1 | Halen  | Park | 1970-06-29 00:00:00 | GoodMan  |
+------+--------+------+---------------------+----------+
1 row in set (0.00 sec)

mysql> SELECT LENGTH(m_FN), CONCAT(m_FN, m_LN), LOWER(m_info), REVERSE(m_info) FROM member;
+--------------+--------------------+---------------+-----------------+
| LENGTH(m_FN) | CONCAT(m_FN, m_LN) | LOWER(m_info) | REVERSE(m_info) |
+--------------+--------------------+---------------+-----------------+
|            6 | Halen Park         | goodman       |  naMdooG        |
+--------------+--------------------+---------------+-----------------+
1 row in set (0.01 sec)

mysql> SELECT YEAR(CURDATE())-YEAR(m_birth) AS age, DAYOFYEAR(m_birth) AS days, DATE_FORMAT(m_birth, '%W %D %M %Y') AS birthDate FROM member;
+------+------+-----------------------+
| age  | days | birthDate             |
+------+------+-----------------------+
|   53 |  180 | Monday 29th June 1970 |
+------+------+-----------------------+
1 row in set (0.00 sec)

mysql> INSERT INTO member VALUES (NULL, 'Samuel', 'Green', NOW(), NULL);
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM member;
+------+--------+-------+---------------------+----------+
| m_id | m_FN   | m_LN  | m_birth             | m_info   |
+------+--------+-------+---------------------+----------+
|    1 | Halen  | Park  | 1970-06-29 00:00:00 | GoodMan  |
|    2 | Samuel | Green | 2023-10-24 14:33:02 | NULL     |
+------+--------+-------+---------------------+----------+
2 rows in set (0.00 sec)

mysql> SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                2 |
+------------------+
1 row in set (0.00 sec)

mysql> SELECT m_birth, CASE WHEN YEAR(m_birth) < 2000 THEN 'old' WHEN YEAR(m_birth) > 2000 THEN 'young' ELSE 'not born' END AS status FROM member;
+---------------------+--------+
| m_birth             | status |
+---------------------+--------+
| 1970-06-29 00:00:00 | old    |
| 2023-10-24 14:33:02 | young  |
+---------------------+--------+
2 rows in set (0.00 sec)
```

