如果 `input` 函数需要用户输入的使用一个字符串，则在输入时需要使用双引号或单引号将内容包含起来输入：

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

终端效果如下：
```console
$ Tell me something, and I will repeat it back to you: "I love you."
$ I love you
```