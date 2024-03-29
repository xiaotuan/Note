可以像如下编写代码，在终端中就可以看到彩色的文本输出：

```java
System.out.println("\033[7;31;46m" + mDateFormat.format(new Date()) + "    " + msg + "\033[0m");
```

格式说明：

````
"\033[样式;前景色;背景色m" + 要输出的文本 + "\033[0m"
````

+ 必须以 `\033[` 作为设置颜色的前缀，以 `m` 作为后缀。
+ `\033[0m` 表示恢复默认颜色。
+ 样式、前景色、背景色的顺序可以随意调换，例如：`前景色;样式;背景色`。
+ 样式的可用值有：
  + 0：空样式
  + 1：粗体
  + 4：下划线
  + 7：反色
+ 前景色：
  + 30：白色
  + 31：红色
  + 32：绿色
  + 33：黄色
  + 34：蓝色
  + 35：紫色
  + 36：浅蓝
  + 37：灰色
+ 背景色：
  + 40：白色
  + 41：红色
  + 42：绿色
  + 43：黄色
  + 44：蓝色
  + 45：紫色
  + 46：浅蓝
  + 47：灰色

> 注意：
>
> 1. 当样式作为最后一个参数时，例如：`前景色;背景色;样式`，这时不能设置样式为 0，否则设置前面设置的样式将会被重置，也就是说恢复到系统默认输出样式
>
> 2. 可以不必设置所有的颜色和样式，可以设置其中的一个或两个值，比如：`\033[1m` : 只设置样式，`\033[31m`：只设置前景色，`\033[1;31m` 只设置样式和前景色。
>
> 3. 如果想使以后的所有打印都同一设置的，可以使用如下代码：
>
>    ```java
>    System.out.print("\033[31;42;1m");
>    System.out.println("这个是测试文本");
>    System.out.println("这是第二段文本。");
>    ......
>    System.out.print("\033[0m");
>    ```
>
>    