Java sE 8 增加了默认方法 `Collection.removeIf` 和 `List.replaceAll`，这两个方法稍有些复杂。要提供一个 `lambda` 表达式来测试或转换元素。例如，下面的代码将删除所有短词，并把其余单词改为小写：

```java
words.removeIf(w -> w.length() <= 3);
words.replaceAll(String::toLowerCase); 
```

>   提示：`Collections` 接口中还有许多有用的算法实现方法，具体请参照 API 文档。