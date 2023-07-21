`getResource()` 方法是 `Class` 类的方法，通过该方法可以获取该类路径下的资源文件的 `URL` 对象。例如，`com.qty.table.ColorTableCellEditor` 类的类路径是 `工程路径/src/com/qty/table`，假设该路径下有 `Earth.gif` 文件，这时可以在 `ColorTableCellEditor` 类中调用如下方法获取 `Earth.gif` 文件的 `URL`：

```java
getClass().getResource("Earth.gif");
```

