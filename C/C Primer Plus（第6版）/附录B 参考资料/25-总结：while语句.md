#### B.4.2　总结： `while` 语句

**关键字**

`while` 语句的关键字是 `while` 。

**一般注释**

`while` 语句创建了一个循环，在 `expression` 为假之前重复执行。 `while` 语句是一个入口条件循环，在下一轮迭代之前先确定是否要再次循环。因此可能一次循环也不执行。 `statement` 可以是一个简单语句或复合语句。

**形式**

`while ( expression )`

`statement`

当 `expression` 为假（或 `0` ）之前，重复执行 `statement` 部分。

**示例**

```c
while (n++ < 100)
     printf(" %d %d\n",n, 2*n+1);
while (fargo < 1000)
{
     fargo = fargo + step;
     step = 2 * step;
}
```

