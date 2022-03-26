if else 语句的通用形式如下所示：

```c
if (expression) {
    statement1
} else {
    statement2
}
```

如果 expression 为真（非 0），则执行 statement1；如果 expression 为假或 0，则执行 else 后面的 statement2。statement1 和 statement2 可以是一条简单语句或复合语句。例如：

```c
if (all_days != 0) {
    printf("%d days total: %.1f%% were below freezing.\n", all_days, 100.0 * (float) cold_days / all_days);
} else {	
	printf("No data entered!\n");
}
```

