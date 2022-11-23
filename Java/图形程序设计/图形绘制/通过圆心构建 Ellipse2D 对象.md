在构造椭圆时，通常可以知道椭圆的中心、宽和高，而不是外界矩形的顶点。通常采用下列方式构造椭圆：

```java
Ellipse2D circle = new Ellipse2D.Double();
circle.setFrameFromCenter(centerX,  centerY, centerX + radius, centerY + radius);
```

