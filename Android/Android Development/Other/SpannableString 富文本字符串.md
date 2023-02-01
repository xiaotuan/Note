[toc]

### 1. SpannableString 的 setSpan() 方法参数说明

```java
public void setSpan(Object what, int start, int end, int flags) {
    super.setSpan(what, start, end, flags);
}
```

+ what：要应用的样式
+ start：应用样式开始字符下标
+ end：应用样式结束字符下标（不包含）
+ flags：应用模式
  + SPAN_INCLUSIVE_EXCLUSIVE：SPAN_INCLUSIVE_EXCLUSIVE 类型的非 0 长度跨度扩展为包括在其起点但不在其终点插入的文本。 当长度为 0 时，它们的行为类似于标记。
  + SPAN_INCLUSIVE_INCLUSIVE：SPAN_INCLUSIVE_INCLUSIVE 类型的 Span 扩展为包括在其起点或终点插入的文本。
  + SPAN_EXCLUSIVE_EXCLUSIVE：SPAN_EXCLUSIVE_EXCLUSIVE 类型的 Span 不会扩展以包括在其起点或终点插入的文本。 它们的长度永远不能为 0，如果它们覆盖的所有文本都被删除，它们会自动从缓冲区中删除。
  + SPAN_EXCLUSIVE_INCLUSIVE：SPAN_EXCLUSIVE_INCLUSIVE 类型的非 0 长度跨度扩展为包括在其结束点插入但不在其起点插入的文本。 当长度为 0 时，它们的行为类似于点。

### 2. 设置字体

```java
SpannableString sStr = new SpannableString("最是那一低头的温柔，像一朵水莲花不胜凉风的娇羞，道一声珍重，道一声珍重，那一声珍重里有蜜甜的忧愁");
//设置字体(default,default-bold,monospace,serif,sans-serif)
sStr.setSpan(new TypefaceSpan("default"), 0, 2, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
```

### 3. 设置字体大小

```java
SpannableString sStr = new SpannableString("最是那一低头的温柔，像一朵水莲花不胜凉风的娇羞，道一声珍重，道一声珍重，那一声珍重里有蜜甜的忧愁");
//设置字体大小（绝对值,单位：像素）,第二个参数boolean dip，如果为true，表示前面的字体大小单位为dip，否则为像素
sStr.setSpan(new AbsoluteSizeSpan(20), 10, 12, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
sStr.setSpan(new AbsoluteSizeSpan(20, true), 12, 14, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);	
//设置字体大小（相对值,单位：像素） 参数表示为默认字体大小的多少倍, 0.5表示一半
sStr.setSpan(new RelativeSizeSpan(0.5f), 14, 16, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);  
//设置字体大小（相对值,单位：像素） 参数表示为默认字体宽度的多少倍 ,2.0f表示默认字体宽度的两倍，即X轴方向放大为默认字体的两倍，而高度不变
sStr.setSpan(new ScaleXSpan(2.0f), 32, 34, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE); 
```

### 4. 设置字体前景色

```java
SpannableString sStr = new SpannableString("最是那一低头的温柔，像一朵水莲花不胜凉风的娇羞，道一声珍重，道一声珍重，那一声珍重里有蜜甜的忧愁");
sStr.setSpan(new ForegroundColorSpan(Color.RED), 16, 18, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);  
```

### 5. 设置字体背景色

```java
SpannableString sStr = new SpannableString("最是那一低头的温柔，像一朵水莲花不胜凉风的娇羞，道一声珍重，道一声珍重，那一声珍重里有蜜甜的忧愁");
//设置字体背景色   
sStr.setSpan(new BackgroundColorSpan(Color.CYAN), 18, 20, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
```

### 6. 设置字体样式

```java
SpannableString sStr = new SpannableString("最是那一低头的温柔，像一朵水莲花不胜凉风的娇羞，道一声珍重，道一声珍重，那一声珍重里有蜜甜的忧愁");
//设置字体样式: NORMAL正常，BOLD粗体，ITALIC斜体，BOLD_ITALIC粗斜体   
sStr.setSpan(new StyleSpan(android.graphics.Typeface.NORMAL), 20, 21, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE); 
sStr.setSpan(new StyleSpan(android.graphics.Typeface.BOLD), 21, 22, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);   
sStr.setSpan(new StyleSpan(android.graphics.Typeface.ITALIC), 22, 23, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);   
sStr.setSpan(new StyleSpan(android.graphics.Typeface.BOLD_ITALIC), 23, 24, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
```

### 7. 设置下划线

```java
SpannableString sStr = new SpannableString("最是那一低头的温柔，像一朵水莲花不胜凉风的娇羞，道一声珍重，道一声珍重，那一声珍重里有蜜甜的忧愁");
//设置下划线   
sStr.setSpan(new UnderlineSpan(), 24, 26, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE); 
```

### 8. 设置删除线

```java
SpannableString sStr = new SpannableString("最是那一低头的温柔，像一朵水莲花不胜凉风的娇羞，道一声珍重，道一声珍重，那一声珍重里有蜜甜的忧愁");
//设置删除线   
sStr.setSpan(new StrikethroughSpan(), 26, 28, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
```

### 9. 设置上下标

```java
SpannableString sStr = new SpannableString("最是那一低头的温柔，像一朵水莲花不胜凉风的娇羞，道一声珍重，道一声珍重，那一声珍重里有蜜甜的忧愁");
//设置上下标
sStr.setSpan(new SubscriptSpan(), 28, 30, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);     
sStr.setSpan(new SuperscriptSpan(), 30, 32, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE); 
```

### 10. 设置项目符号

```java
SpannableString sStr = new SpannableString("最是那一低头的温柔，像一朵水莲花不胜凉风的娇羞，道一声珍重，道一声珍重，那一声珍重里有蜜甜的忧愁");
//设置项目符号   
sStr.setSpan(new BulletSpan(android.text.style.BulletSpan.STANDARD_GAP_WIDTH,Color.GREEN), 0 ,sStr.length(), Spanned.SPAN_EXCLUSIVE_EXCLUSIVE); //第一个参数表示项目符号占用的宽度，第二个参数为项目符号的颜色
```

### 11. 设置图片

```java
SpannableString sStr = new SpannableString("最是那一低头的温柔，像一朵水莲花不胜凉风的娇羞，道一声珍重，道一声珍重，那一声珍重里有蜜甜的忧愁");
//设置图片   
Drawable drawable = getResources().getDrawable(R.drawable.ic_launcher);    
drawable.setBounds(0, 0, drawable.getIntrinsicWidth(), drawable.getIntrinsicHeight());
sStr.setSpan(new ImageSpan(drawable), 24, 26, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);

// 设置图片时缩放图片
String text = "\t\t\t\t ";
SpannableString ss = new SpannableString(text);
Bitmap bitmap = getBitmap(resId);
int index = text.indexOf(" ");
ss.setSpan(new ImageSpan(this, bitmap), index, index + 1, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);

private Bitmap getBitmap(int resId) {
    Drawable d = getResources().getDrawable(resId);
    d.setBounds(0, 0, d.getIntrinsicWidth(), d.getIntrinsicHeight());
    Bitmap b = scaleBitmap(d, 0.4f);
    return b;
}

private Bitmap scaleBitmap(Drawable drawable, float scale) {
    int width = drawable.getIntrinsicWidth();
    int height = drawable.getIntrinsicHeight();
    Log.d(TAG, "scaleDrawable=>width: " + width + ", height: " + height);
    Bitmap b = drawableToBitmap(drawable);
    Matrix matrix = new Matrix();
    matrix.postScale(scale, scale);
    Bitmap bitmap = Bitmap.createBitmap(b, 0, 0, width, height, matrix, true);
    return bitmap;
}

private Bitmap drawableToBitmap(Drawable drawable) { // drawable 转换成 bitmap
    int width = drawable.getIntrinsicWidth();   // 取 drawable 的长宽
    int height = drawable.getIntrinsicHeight();
    Bitmap.Config config = drawable.getOpacity() != PixelFormat.OPAQUE ? Bitmap.Config.ARGB_8888:Bitmap.Config.RGB_565;         // 取 drawable 的颜色格式
    Bitmap bitmap = Bitmap.createBitmap(width, height, config);     // 建立对应 bitmap
    Canvas canvas = new Canvas(bitmap);         // 建立对应 bitmap 的画布
    drawable.setBounds(0, 0, width, height);
    drawable.draw(canvas);      // 把 drawable 内容画到画布中
    return bitmap;
}
```

### 12. 设置超链接

```java
SpannableString sStr2 = new SpannableString("电话邮件百度一下短信彩信进入地图");
//超级链接（需要添加setMovementMethod方法附加响应）   
sStr2.setSpan(new URLSpan("tel:8008820"), 0, 2, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);     //电话      
sStr2.setSpan(new URLSpan("mailto:kejunlu@qq.com"), 2, 4, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);     //邮件      
sStr2.setSpan(new URLSpan("http://www.baidu.com"), 4, 8, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);     //网络      
sStr2.setSpan(new URLSpan("sms:10086"), 8, 10, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);     //短信   使用sms:或者smsto:   
sStr2.setSpan(new URLSpan("mms:10086"), 10, 12, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);     //彩信   使用mms:或者mmsto:   
sStr2.setSpan(new URLSpan("geo:32.123456,-17.123456"), 12, 16, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);     //地图 
```

### 13. 设置缩进

`LeadingMarginSpan` 是接口，内部的 `Standard` 是它的标准实现方式。有两个构造方法，`Standard(int every)` 和 `Standard(int first, int rest)`。`Standard(int every)` 是给每一行都设置同样的缩进距离，而`Standard(int first, int rest)` 是给第一行和其他行分别设置缩进距离。

```java
SpannableString spannableString = new SpannableString(text);
LeadingMarginSpan.Standard what = new LeadingMarginSpan.Standard(width, 0)
spannableString.setSpan(what, 0, spannableString.length, SpannableString.SPAN_INCLUSIVE_INCLUSIVE)
```

