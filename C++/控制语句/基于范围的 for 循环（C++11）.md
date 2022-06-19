`C++ 11` 新增了一种循环：基于范围的 `for` 循环。这简化了一种常见的循环任务：对数组（或容器类，如 `vector` 和 `array`）的每个元素执行相同的操作，例如：

```cpp
double prices[5] = { 4.99, 10.99, 6.87, 7.99, 8.49 };
for (double x : prices)
    cout << x << std::endl;
```

要修改数组的元素，需要使用不同的循环变量语法：

```cpp
for (double &x : prices)
    x = x * 0.80;	// 20% off sale
```

还可结合使用基于范围的 `for` 循环和初始化列表：

```cpp
for (int x : { 3, 5, 2, 8, 6 })
    cout << x << " ";
cout << '\n';
```

