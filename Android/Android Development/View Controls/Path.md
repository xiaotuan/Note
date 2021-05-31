[toc]

### 1. 设置抗锯齿

```java
mPaint.setAntiAlias(true);
```

也可以在其创建实例时设置：

```java
Path mPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
```

### 2. 设置线宽

```java
mPath.setStrokeeWidth(2f);
```

### 3. 设置颜色

```java
mPath.setColor(Color.GRAY);
```

### 4. 设置样式

```java
mPath.setStyle(Paint.Style.FILL);
```

可设置的样式有：FILL（填充）、STROKE（描边）、FILL_AND_STROKE（填充加描边）。
