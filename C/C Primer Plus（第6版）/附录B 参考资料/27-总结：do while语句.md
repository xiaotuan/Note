#### B.4.4　总结： `do` 　 `while` 语句

**关键字**

`do`  **　**  `while` 语句的关键字是 `do` 和 `while` 。

**一般注解：**

`do`

`while`
语句创建一个循环，在
`expression`
为假或0之前重复执行循环体中的内容。
`do`

`while`
语句是一种出口条件循环，即在执行完循环体后才根据测试条件决定是否再次执行循环。因此，该循环至少必须执行一次。
`statement`
部分可是一条简单语句或复合语句。

**形式：**

```c
do
statement
while ( expression );

```

在`test`为假或0之前，重复执行`statement`部分。

**示例：**

```c
do
     scanf("%d", &number);
while (number != 20);
```

