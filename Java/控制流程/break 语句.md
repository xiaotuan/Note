[toc]

### 1. 不带标签的 break 语句

不带标签的 `break` 语句用于退出 `switch` 语句和循环语句，例如：

```java
while (years <= 100) {
    balance += payment;
    double interest = balance * interestRate / 100;
    balance += interest;
    if (balance >= goal) break;
    years++;
}
```

### 2. 带标签的 break 语句

带标签的 `break` 语句用于跳出多重嵌套的循环语句。请注意，标签必须放在希望跳出的最外层循环之前，并且必须紧跟一个冒号。例如：

```java
Scanner in = new Scanner(System.in);
int n;
read_data:
while (...)	{	// this loop statement is tagged with the label
	...
    for (...) {	// this inner loop is not labeled
        System.out.print("Enter a number >= 0: ");
        n = in.nextInt();
        if (n < 0) {	// should never happen-can't go on
        	break read_data;
        }
        // break out of read_data loop
        ...
}

// this statement is executed immediately after the labeled break
if (n < 0) {	// check for bad situation
	// deal with bad situation
} else {
    // carry out normal processing
}
```

> 提示
>
> 可以将标签应用到任何语句中，甚至可以应用到 if 语句或者块语句中。

