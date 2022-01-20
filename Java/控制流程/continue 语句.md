[toc]

### 1. 不带标签的 continue 语句

`continue` 语句将控制转移到最内层循环的首部，例如：

```java
Scanner in = new Scanner(System.in);
while (sum < goal) {
    System.out.print("Enter a number: ");
    n = in.nextInt();
    if (n < 0) continue;
    sum += n;	// not executed if n < 0
}
```

### 2. 带标签的 continue 语句

带标签的 `continue` 语句，将跳到与标签匹配的循环首部。