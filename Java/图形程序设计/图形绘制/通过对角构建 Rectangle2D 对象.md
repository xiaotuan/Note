通过对角坐标创建 `Rectangle2D` 对象。在这种情况下，首先创建一个空矩形，然后调用 `setFrameFromDiagonal` 方法，如下所示：

```java
Rectangle2D rect = new Rectangle2D.Double();
rect.setFrameFromDiagonal(px, py, qx, qy);
```

或者，如果已知的顶点分别用 `Point2D` 类型的两个对象 p 和 q 表示，就应该这样调用：

```java
rect.setFrameFromDiagonal(p, q);
```

