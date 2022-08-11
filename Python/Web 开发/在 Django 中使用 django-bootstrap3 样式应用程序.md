[toc]

> 提示：django-bootstrap3 官方文档地址：<http://getbootstrap.com/>。

### 1. 安装 django-bootstrap3

在活动的虚拟环境中执行如下命令：

```shell
(11_env) learning_log$ pip install django-bootstrap3
```

### 2. 激活 django-bootstrap3

需要在 settings.py 的 INSTANLLED_APPS 中添加如下代码：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 第三方应用程序
    'bootstrap3',
    
    # 我的应用程序
    'learning_logs',
]
```

我们需要让  django-bootstrap3 包含 jQuery，让你能够使用 Bootstrap 模板提供的一些交互式元素，请在 settings.py 的末尾添加如下代码：

```python
BOOTSTRAP3 = {
	'include_query': True,
}
```

### 3. 使用 Bootstrap 来设置样式

#### 3.1 定义 HTML 头部

需要在模板顶部加载 django-bootstrap3 中的模块标签集：

```html
{% load bootstrap3 %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Learning Log</title>

    {% bootstrap_css %}
    {% bootstrap_javascript %}

  </head>
  
  <body>

    <!-- Static navbar -->
    <nav class="navbar navbar-default navbar-static-top">
      <div class="container">
          
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed"
              data-toggle="collapse" data-target="#navbar"
              aria-expanded="false" aria-controls="navbar">
          </button>
          <a class="navbar-brand" href="{% url 'learning_logs:index' %}">
              Learning Log</a>
        </div>
        
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a href="{% url 'learning_logs:topics' %}">Topics</a></li>
          </ul>
          
          <ul class="nav navbar-nav navbar-right">
            {% if user.is_authenticated %}
              <li><a>Hello, {{ user.username }}.</a></li>
              <li><a href="{% url 'users:logout' %}">log out</a></li>
            {% else %}
              <li><a href="{% url 'users:register' %}">register</a></li>
              <li><a href="{% url 'users:login' %}">log in</a></li>
            {% endif %}
          </ul>
        </div><!--/.nav-collapse -->
        
      </div>
    </nav>
    
    <div class="container">

      <div class="page-header">
        {% block header %}{% endblock %}
      </div>
      <div>
        {% block content %}{% endblock %}
      </div>

    </div> <!-- /container -->

  </body>
</html>
```

**index.html**

```html
{% extends "learning_logs/base.html" %}

{% block header %}
  <div class='jumbotron'>
      <h1>Track your learning.</h1>        
  </div>
{% endblock %}

{% block content %}
  <h2>
    <a href="{% url 'users:register' %}">Register an account</a> to make
     your own Learning Log, and list the topics you're learning about.
  </h2>
  <h2>
    Whenever you learn something new about a topic, make an entry 
    summarizing what you've learned.
  </h2>
{% endblock %}
```

