`Matrix` 类的一些重要方法如下：

+ `matrix.reset()`：将矩阵重置为单位矩阵，应用该操作时不会对视图进行任何更改。
+ `matrix.setScale()`：更改大小。
+ `matrix.setTranslate()`：更改位置以模拟移动效果。
+ `matrix.setRotate()`：更改方向。
+ matrix.setSkew()`：扭曲视图。

可以连续指定多个矩阵或者将它们相乘，以将各种变换效果组合在一起。考虑一下示例，其中 m1、m2 和 m3 是单位矩阵：

`m1.setScale();`

`m2.setTranlate();`

`m3.concat(m1,m2);`

使用 m1 变换视图，然后使用 m2 来变换结果视图，这相当于使用 m3 变换相同的视图。请注意，set 方法替换了原来的变化，而且 `m3.concat(m1, m2)` 不同于 `m3.concat(m2, m1)`。

你已经看到了 `preTranslate` 和 `postTranslate` 方法用于影响矩阵变换的模式。实际上，pre 和 post 方法并不是 translate 所独有的，每个 set 变换方法都有自己的 pre 和 post 版本。最后，`preTranslate` 方法，比如 `m1.preTranslate(m2)` 等价于
`m1.concat(m2, m1)`

同样，`m1.postTranslate(m2)` 方法等价于

`m1.concat(m1, m2)`

此外，代码：

```java
matrix.setScale(interpolatedTime, interpolatedTime);
matrix.preTranslate(-centerX, -centerY);
matrix.postTranslate(centerX, centerY);
```

等价于：

```java
Matrix matrixPreTranslate = new Matrix();
matrixPreTranslate.setTranslate(-centerX, -centerY);

Matrix matrixPostTranslate = new Matrix();
matrixPostTranslate.setTranslate(centerX, centerY);

matrix.concat(matrixPreTranslate, matrix);
matrix.postTranslate(matrix, matrixpostTranslate);
```

