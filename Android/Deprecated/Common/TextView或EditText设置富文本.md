可以通过下面的方法给 TextView 或 EditText 设置富文本字符串：

```java
TextView tv3 = findViewById(R.id.tv3);
        tv3.setText("Styling the content of a TextView dynamically", TextView.BufferType.SPANNABLE);
        Spannable spn = (Spannable) tv3.getText();
        spn.setSpan(new BackgroundColorSpan(Color.RED), 0, 7, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE);
        spn.setSpan(new StyleSpan(Typeface.BOLD_ITALIC), 0, 7, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE);

        EditText et = findViewById(R.id.et);
        et.setText("Styling the content of an EditText dynamically");
        Spannable spn2 = (Spannable) et.getText();
        spn2.setSpan(new BackgroundColorSpan(Color.RED), 0, 7, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE);
        spn2.setSpan(new StyleSpan(Typeface.BOLD_ITALIC), 0, 7, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE);
```

