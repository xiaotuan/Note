`QLCDNumber` 是模拟 `LCD` 显示数字的组件，可以显示整数或小数，但就如实际的 `LCD` 一样，要设定显示数字的个数。显示整数时，还可以选择以不同进制来显示，如十进制、二进制、十六进制。其主要属性如下：

+ `digitCount`：显示的数的位数，如果是小数，小数点也算一个数位。
+ `smallDecimalPoint`：是否有小数点，如果有小数点，就可以显示小数。
+ `mode`：数的显示进制，通过调用函数 `setDecMode()`、`setBinMode()`，`setOctMode()`、`setHexMode()` 可以设置为常用的十进制、二进制、八进制、十六进制格式。
+ `value`：返回显示值，浮点数。若设置为显示整数，会自动四舍五入后得到整数，设置为 `intValue` 的值。如果 `smallDecimalPoint=true`，设置 `value` 时可以显示小数，但是数的位数不能超过 `digitCount`。
+ `intValue`：返回显示的整数值。

例如，若 `smallDecimalPoint=true`，`digitCount=3`，设置 `value=2.36`，则界面上 `LCDNumber` 组件会显示为 2.4；若设置 `value=1456.25`，则界面上 `LCDNumber` 组件只会显示 145。所以，用 `QLCDNumber` 作为显示组件时，应注意这些属性的配合。