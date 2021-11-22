一般可以通过如下代码创建新的 `ArrayAdapter`：

```
ArrayAdapter<String> aa = new ArrayAdapter<>(this,
                android.R.layout.simple_dropdown_item_1line,
                new String[]{"English", "Hebrew", "Hindi", "Spanish", "German", "Greek"});
```

或者：

```
ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                R.array.planets, android.R.layout.simple_spinner_item);
```

