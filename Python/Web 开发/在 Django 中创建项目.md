可以执行如下命令来新建一个项目：

```shell
django-admin startproject learning_log .
```

> 注意：千万别忘了命令后面的句点，否则部署应用程序时将遭遇一些配置问题。如果忘记了这个句点，就将创建的文件和文件夹删除，再重新运行这个命令。

执行命令后创建的 learning_log 目录包含 4 个文件，其中最重要的是 `settings.py`、`urls.py` 和 `wsgi.py`。文件 `settings.py` 指定 Django 如何与你的系统交互以及如何管理项目。在开发项目过程中我们将修改其中一些设置，并添加一些设置。文件 `urls.py` 告诉 Django 应创建那些网页来响应浏览器请求。文件 `wsgi.py` 帮助 Django 提供它创建的文件，这个文件名是 web server gateway interface（Web 服务器网关接口）的首字母。

