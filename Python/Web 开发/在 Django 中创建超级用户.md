[toc]

### 1. 创建超级用户

可以通过执行下面命令并按提示操作为 Django 创建超级用户：

```shell
(11_env) learning_log$ python3 manage.py createsuperuser
Username (leave blank to use 'xiaotuan'): ll_admin
Email address: 
Password: 
Password (again): 
Superuser created successfully.
(11_env) learning_log$
```

### 2. 向管理网站注册模型

Django 自动在管理网站中添加了一些模型，如 User 和 Group，但对于我们创建的模型，必须手工进行注册：

**admin.py**

```python
from django.contrib import admin

from learning_logs.models import Topic

admin.site.register(Topic)
```

可以通过 http://localhost:8000/admin/ 访问管理网站。