[toc]

### 1. break

```python
i = 1
while i <= 5:
    # 条件：如果吃到 4 或 > 3 打印吃饱了不吃了
    if i == 4:
        print('吃饱了，不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1
```

### 2. continue

```python
i = 1
while i <= 5:
    # 条件：如果吃到 4 或 > 3 打印吃饱了不吃了
    if i == 3:
        print('吃出一个大虫了，这个苹果不吃了')
        # 如果使用 continue，在 continue 之前一定要修改计数器，否则进入死循环
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1
```

