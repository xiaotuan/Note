[toc]

假如有如下一个模块：

**pizza.py**

```python
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
```

### 1. 导入模块

可以使用 `import pizza` 导入 `pizza` 模块，例如：

```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 2. 导入模块中指定的函数

可以使用如下语法导入模块中的特定函数：

```python
from module_name import function_name
```

通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：

```python
from module_name import function_0, function_1, function_2
```

例如：

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 3. 使用 as 给函数指定别名

指定别名的通用语法如下：

```python
from module_name import function_name as fn
```

例如：

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 4. 使用 as 给模块指定别名

给模块指定别名的通用语法如下：

```python 
import module_name as mn
```

例如：

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 5. 导入模块中的所有函数

导入模块中的所有函数通用语法如下：

```python
from module_name import *
```

例如：

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

