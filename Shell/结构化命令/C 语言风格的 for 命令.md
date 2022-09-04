以下是 bash 中 C  语言风格的 `for` 循环的基本格式：

```shell
for (( variable assignment; condition; iteration process ))
```

例如：

```shell
#!/bin/bash
# testing the C-style for loop

for (( i=1; i <= 10; i++ ))
do 
	echo "The next number is $i"
done
```

C 语言风格的 `for` 命令也允许为迭代使用多个变量。循环会单独处理每个变量，你可以为每个变量定义不同的迭代过程。尽管可以使用多个变量，但你只能在 `for` 循环中定义一种条件：

```shell
#!/bin/bash
# multiple variables

for (( a=1, b=10; a <= 10; a++, b-- ))
do
	echo "$a - $b"
done
```

