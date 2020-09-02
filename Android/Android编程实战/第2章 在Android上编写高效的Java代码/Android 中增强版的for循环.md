Java SE 5.0 还引入了增强版的 for 循环，提供了一个通用的缩写表达式来遍历集合和数组。首先，比较以下五种方法：

```java
void loopOne(String[] names) {
    int size = names.length;
    for (int i = 0; i < size; i++) {
        printName(names[i]);
    }
}

void loopTwo(String[] names) {
    for (String name : names) {
        printName(name);
    }
}

void loopThree(Collection<String> names) {
    for (String name : names) {
        printName(name);
    }
}

void loopFour(Collection<String> names) {
    Iterator<String> iterator = names.iterator();
    while (iterator.hasNext()) {
        printName(iterator.next());
    }
}

// 不要在 ArrayList 上使用增强版的 for 循环
void loopFive(ArrayList<String> names) {
    int size = name.size();
    for (int i = 0; i < size; i++) {
        printName(names.get(i));
    }
}
```

对 `Collection` 对象来说，增强版 for 循环和使用迭代器遍历元素有着相同的性能。ArrayList 对象应避免使用增强版 for 循环。

如果不仅需要遍历元素，而且需要元素的位置，就一定要使用数组或者 ArrayList，因为所有其他 Collection 类在这些情况下会更慢。