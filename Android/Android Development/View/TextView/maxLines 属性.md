可以通过 `maxLines` 属性设置 `TextView` 的最大显示行数。

```xml
<TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:maxLines="3"
        android:text="sklfkjsksdflasjdfalksweofiaslfkj \
        assfdasdkfalsdjflskdklsdkfasdlfjkljldsklfewifjals \
        kfjlewfjasdfjasldfjiwaeofjasid \
        slfkasdflkasflaskfdalskdfaslfjas \
        sadkflasjdlfkjasdlfkasdflasdfk"/>
```

也就是说，即使 `TextView` 的高度能够显示超过 3 行的字符，也不会显示超过 3 行的字符。