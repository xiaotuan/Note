下面示例说明了break语句的工作状态。请注意，标签必须放在希望跳出的最外层循环之前，并且必须紧跟一个冒号。

```java
Scanner in = new Scanner(System.in);
int n;
read_data:
while (...) {	// this loop statement is tagged with the label
	...
    for (...) {	// this inner loop is not labeled
    	System.out.print("Enter a number >= 0: ");
        n = in.nextInt();
        if (n < 0) {	// should never happen-can't go on
        	break read_data;
            // break out of read_data loop
        }
        ...
    }
}
// this statement is executed immediately after the labeled break
if (n < 0) {	// check for bad situation
	// deal with bad situation
} ele {
    // carry out normal processing
}
```

> 注释：事实上，可以将标签应用到任何语句中，甚至可以应用到 if 语句或者块语句中，如下所示：
>
> ```java
> label:
> {
>     ...
>     if (condition) break label;	// exits block
>     ...
> }
> // jumps here when the break statement executes
> ```

还有一种带标签的 `continue` 语句，将跳到与标签匹配的循环首部。
