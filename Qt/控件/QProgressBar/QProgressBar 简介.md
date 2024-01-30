`QProgressBar` 的父类是 `QWidget`，一般用于进度显示，常用属性如下：

+ `minimum`、`maximum`：最小值和最大值。
+ `value`：当前值，可以设定或读取当前值。
+ `textVisible`：是否显示文字，文字一般是百分比表示的进度。
+ `orientation`：可以设置为水平或垂直方向。
+ `format`：显示文字的格式，`%p%` 显示百分比，`%v` 显示当前值，`%m` 显示总步数。缺省为 `%p%`。