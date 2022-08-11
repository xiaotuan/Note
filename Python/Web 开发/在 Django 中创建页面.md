[toc]

### 1. 映射 URL

打开项目主文件夹 learning_log 中的 urls.py 文件，你将看到如下代码：

```python
"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

我们需要包含 learning_logs 的URL:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls', namespace='learning_logs'))
]
```

默认的 urls.py 包含在文件夹 learning_log 中，现在我们需要在文件夹 learning_logs 中创建另一个 urls.py 文件：

**urls.py**

```python
"""定义 learning_logs 的 URL 模式"""
from django.urls import path

from . import views

urlpatterns = [
	# 主页
    path(r'^$', views.index, name='index),
]
```

### 2. 编写视图

learning_logs 中的文件 views.py 是你执行命令 `python manage.py startapp` 时自动生成的，当前其内容如下：

**views.py**

```python
from django.shortcuts import render

# Create your views here.
```

下面的代码演示了该如何为主页编写视图：

```python
from django.shortcuts import render

def index(request):
	"""学习笔记的主页"""
	return render(request, 'learning_logs/index.html')
```

### 3. 编写模板

在文件夹 learning_logs 中新建一个文件夹，并将其命名为 templates。在文件夹 templates 中，再新建一个文件夹，并将其命名为 learning_logs。在最里面的文件夹 learning_logs 中，新建一个文件，并将其命名为 index.html。

**index.html**

```html
<p>
    Learning Log
</p>
<p>
    Learning Log helps you keep track of your learning, for any topic you're learning about.
</p>
```

