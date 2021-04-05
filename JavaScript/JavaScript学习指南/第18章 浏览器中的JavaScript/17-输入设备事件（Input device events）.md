#### 输入设备事件（Input device events）

前面已经学习过click了，但其实还有很多别的鼠标事件（ `mousedown` 、 `move` 、 `mouseup` 、 `mouseenter` 、 `mouseleave` 、 `mouseover` 、 `mousewheel` ）和键盘事件（ `keydown` 、 `keypress` 、 `keyup` ）。注意“触摸”事件（对于可触摸设备而言）是优先于鼠标事件执行的，但如果触摸事件没有对应的处理器，那么他们将会触发鼠标事件。比如，如果用户触摸一个按钮，但是触摸事件并没有显式的处理器，那么此时就会触发一个 `click` 事件。

