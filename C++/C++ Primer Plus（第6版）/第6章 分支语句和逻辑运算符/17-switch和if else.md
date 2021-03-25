### 6.5.2　switch和if else

switch语句和if else语句都允许程序从选项中进行选择。相比之下，if else更通用。例如，它可以处理取值范围，如下所示：

```css
if (age > 17 && age < 35)
    index = 0;
else if (age >= 35 && age < 50)
    index = 1;
else if (age >= 50 && age < 65)
    index = 2;
else
    index = 3;
```

然而，switch并不是为处理取值范围而设计的。switch语句中的每一个case标签都必须是一个单独的值。另外，这个值必须是整数（包括char），因此switch无法处理浮点测试。另外，case标签值还必须是常量。如果选项涉及取值范围、浮点测试或两个变量的比较，则应使用if else语句。

然而，如果所有的选项都可以使用整数常量来标识，则可以使用switch语句或if else语句。由于switch语句是专门为这种情况设计的，因此，如果选项超过两个，则就代码长度和执行速度而言，switch语句的效率更高。

> **提示：**
> 如果既可以使用if else语句，也可以使用switch语句，则当选项不少于3个时，应使用switch语句。

