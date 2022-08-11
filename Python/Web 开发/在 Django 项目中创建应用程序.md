[toc]

### 1. 创建应用程序

激活虚拟环境后再执行命令 `startapp` 就可以创建应用程序了：

```shell
$ source 11_env/bin/activate
(11_env) learning_log$ python3 manage.py startapp learning_logs
(11_env) learning_log$ ls
11_env  db.sqlite3  learning_log  learning_logs  manage.py
(11_env) learning_log$ ls learning_logs/
admin.py  apps.py  __init__.py  migrations  models.py  tests.py  views.py
```

命令 `startapp appname` 让 Django 建立创建应用程序所需的基础设施。如果查看项目目录，将看到其中新增了一个文件夹 learning_logs.

### 2. 定义模型

打开文件 `models.py`，其内容如下：

```python
from django.db import models

# Create your models here.
```

下面时表示用户将要存储的主题模型：

```python
from django.db import models

class Topic(models.Model):
	"""用户学习的主题"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	
	def __str__(self):
		""" 返回模型的字符串表示"""
		return self.text
```

属性 text 是一个 `CharField` —— 由字符或文本组成的数据。定义 `CharField` 属性时，必须告诉 Django 该在数据库中预留多少控件。

属性 date_added 是一个 DateTimeField —— 记录日期和时间的数据。我们传递了实参 auto_now_add=True，每当用户创建新主题时，这都让 Djano 将资格属性自动设置成当前日期和时间。

> 注意：要获悉可在模型中使用的各种字段，请参阅 [Djano Model Field Reference（Django 模型字段参考）](https://docs.djangoproject.com/en/4.1/ref/models/fields/)。

Django 调用方法 `__str__()` 来显示模型的简单表示。

> 注意：如果你使用的是 Python 2.7，应调用方法 `__unicode__()`，而不是 `__str__()`，但其中的代码相同。

### 3. 激活模块

要使用模块，必须让 Django 将应用程序包含到项目中。为此，打开 `settings.py`（它位于目录 `learning_log/learning_log` 中。

```python
--snip--
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'learning_logs',
]
--snip
```

需要让 Django 修改数据库，使其能够存储与模型 Topic 相关的信息。为此，在终端窗口中执行下面的命令：

```shell
(11_env) learning_log$ python3 manage.py makemigrations learning_logs
Migrations for 'learning_logs':
  learning_logs/migrations/0001_initial.py
    - Create model Topic
(11_env) learning_log$ 
```

命令 `makemigrations` 让 Django 确定该如何修改数据库，使其能够存储与我们定义的新模型相关联的数据。输出表明 Django 创建了一个名为 0001_initial.py 的迁移文件，这个文件将在数据库中为模型 Topic 创建一个表。

下面来应用这种迁移，让 Django 替我们修改数据库：

```shell
(11_env) learning_log$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0001_initial... OK
(11_env) learning_log$ 
```

### 4. 定义模型 Entry

下面是模型 Entry 的代码：

**models.py**

```python
from django.db import models

class Topic(models.Model):
	"""用户学习的主题"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	
	def __str__(self):
		""" 返回模型的字符串表示"""
		return self.text
		

class Entry(models.Model):
	"""学到的有关某个主题的具体知识"""
	topic = models.ForeignKey(
		Topic,
		on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'
	

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text[:50] + "..."
```

像 Topic 一样，Entry 也继承了 Django 基类 Model。第一个属性 topic 是一个 ForeignKey 实例。外键是一个数据库术语，它引用了数据库中的另一条记录；这些代码将每个条目关联到特定的主题。每个主题创建时，都给它分配了一个键（或 ID）。需要在两项数据之间建立联系时，Django 使用与每项信息相关联的键。

我们在 Entry 类中嵌套了 Meta 类。Meta 存储用于管理模型的额外信息，在这里，它让我们能够设置一个特殊属性，让 Dijango 在需要时使用 Entries 来表示多个条目。如果没有这个类， Django 将使用 Entrys 来表示多个条目。

### 5. 迁移模型 Entry

由于我们添加了一个新模型，因此需要再次迁移数据库。

```shell
(11_env) learning_log$ python3 manage.py makemigrations learning_logs
Migrations for 'learning_logs':
  learning_logs/migrations/0002_entry.py
    - Create model Entry
(11_env) $ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0002_entry... OK
(11_env) learning_log$ 
```

### 6. 向管理网站注册 Entry

我们还需要注册模型 Entry:

**admin.py**

```python
from django.contrib import admin

from learning_logs.models import Topic
from learning_logs.models import Entry

admin.site.register(Topic)
admin.site.register(Entry)
```

