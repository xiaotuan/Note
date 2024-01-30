可以调用 `QColor::setRgb()` 函数生成颜色。`QColor` 的静态函数 `setRgb()` 定义为：

```cpp
void setRgb(int r, int g, int b, int a = 255);
```

其中 `r`、`g`、`b` 是红、绿、蓝颜色值，均在 0 到 255 之间，a 是颜色的 `alpha` 值，缺省是 255，取值范围也是 0 ~ 255。

例如：

```cpp
QColor color;
color.setRgb(255, 128, 66, 255);
```



