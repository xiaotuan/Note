可以执行 `runserver` 命令来运行 Django 项目：

```shell
$ python manage.py runserver
```

> 注意：如果出现错误信息 "That port is already in use"（指定端口已被占用），请执行命令 `python manage.py runserver 8001`，让 Django 使用另一个端口。