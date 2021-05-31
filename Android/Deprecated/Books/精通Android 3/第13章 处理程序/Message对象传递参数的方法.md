```java
obtainMessage();
obtainMessage(int what);
obtainMessage(int what, Object object);
obtainMessage(int what, int arg1, int arg2);
obtainMessage(int what, int arg1, int arg2, Object obj);
```

`Object object` 参数存在一些限制，在这类情况下，它需要为 `parcellable`。在这类情况下，在 `Message` 对象上现实使用 `setData()` 方法将更加安全、更可兼容，该方法接受一个 bundle。