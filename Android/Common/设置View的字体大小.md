可以使用下面的方法设置 `TextView` 、`EditText` 等视图的字体大小：

```java
int fontSize =  mSharedPreferences.getInt(ComAssisentSharedPreferences.PREF_LOG_VIEW_TEXT_SIZE, getResources().getInteger(R.integer.default_log_text_size));
EditText mLogEt.setTextSize(TypedValue.COMPLEX_UNIT_SP, fontSize);
```

