[toc]

`QSlider`、`QScrollBar` 和 `Qdial` 3 个组件都从 `QAbstractSlider` 继承而来，有一些共有的属性。`QSlider` 是滑动的标尺型组件，滑动标尺上的一个滑块可以改变值。

基类 `QAbstractSlider` 的主要属性包括以下几种：

+ `minimum`、`maximum`：设置输入范围的最小值和最大值。
+ `singleStep`：单步长，拖动标尺上的滑块，或按下左/右光标键时的最小变化数值。
+ `pageStep`：在 `Slider` 上输入焦点，按 `PgUp` 或 `PgDn` 键时变化的数值。
+ `value`：组件的当前值，拖动滑块时自动改变此值，并限定在 `minimum` 和 `maximum` 定义的范围之内。
+ `sliderPosition`：滑块的位置，若 `tracking` 属性设置为 `true`，`sliderPosition` 就等于 `value`。
+ `tracking`：`sliderPosition` 是否等同于 `value`，如果 `tracking=true`，改变 `value` 时也同时改变 `sliderPosition`。
+ `orientation`：`Slider` 的方向，可以设置为水平或垂直。方向参数是 `Qt` 的枚举类型 `enum Qt::Orientation`，取值包括以下两种：
  + `Qt::Horizontal` 水平方向
  + `Qt::Vertical` 垂直方向
+ `invertedAppearance`：显示方式是否反向，`invertedAppearance=false` 时， 水平的 `Slider` 由左向右数值增大，否则返过来。
+ `invertedControls`：反向按键控制，若 `invertedControls=true`，则按下 `PgUp` 或   `PgDn` 按键时调整数值的方向相反。

属于 `QSlider` 的专有属性有两个，如下：

+ `tickPosition`：标尺刻度的显示位置，使用枚举类型 `QSlider::TickPosition`，取值包括以下 6 种：
  + `QSlider::NoTicks`：不显示刻度
  + `QSlider::TicksBothSides`：标尺两侧都显示刻度
  + `QSlider::TicksAbove`：标尺上方显示刻度
  + `QSlider::TicksBelow`：标尺下方显示刻度
  + `QSlider::TicksLeft`：标尺左侧显示刻度
  + `QSlider::TicksRight`：标尺右侧显示刻度
+ `tickInterval`：标尺刻度的间隔值，若设置为 0，会在 `singleStep` 和 `pageStep` 之间自动选择。