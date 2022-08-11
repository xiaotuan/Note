[toc]

> 提示：Django 模板文档网址为：<https://docs.djangoproject.com/en/4.1/ref/templates/>

目录结构：

```
learning_log
|_ 11_env
|_ learning_log
|	|_ __init__.py
|	|_ settings.py
|	|_ urls.py
|	|_ wsgi.py
|_ learning_logs
|	|_ migrations
|	|_ templates
|	|_ learning_logs
|	|	|_index.html
|	|	|_ base.html
|	|_ admin.py
|	|_ apps.py
|	|_ __init__.py
|	|_ models.py
|	|_ tests.py
|	|_ urls.py
|	|_ views.py
|_ db.sqlite3
|_ manage.py
```

### 1. 父模板

我们首先来创建一个名为 base.html  的模板，并将其存储在 index.html 所在的目录中。这个文件包含所有页面都有的元素；其他模板都继承 base.html。

**base.html**

```html
<p>
    <a href="{% url 'learning_logs:index' %}">Learning Log</a>
</p>

{% block content %}{% endblock content %}
```

为创建链接，我们使用了一个模板标签，它是用大括号和百分号（`{% %}`）表示的。模板标签是一小段代码，生成要在网页中显示的信息。在这个实例中，模板标签 `{% url 'learning_logs:index' %}` 生成一个 URL，该 URL 与 learning_logs/urls.py 中定义的名为 index 的 URL  模式。

### 2. 子模板

现在需要重新编写 index.html，使其继承 base.html，如下所示：

```html
{% extends "learning_logs/base.html" %}

{% block content %}
<p>
    Learning Log helps you keep track of your learning, for any topic you're learning about.
</p>
{% endblock content %}
```

子模板的第一行必须包含标签 `{% entends %}`，让 Django 指定它继承了哪个父模板。