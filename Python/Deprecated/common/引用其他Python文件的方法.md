有如下目录：



```css
-python
----file1
---------file1_1
------------------pfile1_1.py
---------pfile1.py
----file2
---------pfile2.py
----pfile.py
----data.py
```

即python文件夹下有file1, file2, pfile.py, data.py，文件夹file1下又有file1_1, pfile1.py，  文件夹file2下有pfile2.py，文件夹file1_1下又有pfile1_1.py。

## 1.导入下一级/多级目录

在文件pfile.py中导入pfile1.py, pfile2.py或 pfile1_1.py，并使用其中的函数（假设函数名分别文fun1(), fun2(), fun1_1()）：



```python
# 当前路径：/home/puxitong/python/

# 导入同级目录下的data.py
import data

# 导入下一级目录file1下的pfile1.py
from file1 import pfile1
pfile1.fun1()

# 导入下一级目录file2下的pfile2.py
from file2 import pfile2
pfile2.fun2()

# 导入下一级目录file2下的pfile1.py中的函数fun1()
from file1.pfile1 import fun1
fun1()

# 导入下两级目录file1/file1_1/下的pfile1_1.py
from file1.file1_1 import pfile1_1
pfile1_1.fun1_1()
```

##### 可以看出，导入同级目录下的文件时，格式为：

> import 文件名

##### 导入下一级目录下的文件时，格式为：

> from 文件夹名 import 文件名

##### 导入下二级目录下的文件时，格式为：

> from 下一级文件夹名.下二级文件夹名 import 文件名

##### 导入下多级目录下的文件时以此类推，即：

> from 文件夹1.文件夹2.文件夹3. .. .文件夹n import 文件名

**需要注意的是，这种导入方式下，如果要用导入的文件中的函数或者类，需要在其前面加上文件名，即 "文件名.函数名" 的形式**。

##### 我们也可以只导入需要的函数或类，格式为：

> from 文件夹名.文件名 import 函数1，函数2，类1，…

有些教程里面说，需要在下一级目录下新建一个空的python文件命名为 __init__.py，但我在运行时发现不建一个文件也会导入成功。

## 2.导入上一级/任一级目录



```css
-python
----file1
---------file1_1
------------------pfile1_1.py
---------pfile1.py
----file2
---------pfile2.py
----pfile.py
----data.py
```

如果要在pfile1.py中调用pfile.py 和 pfile2.py，因为当前路径是 '/home/puxitong/python/file1/' ，而 pfile.py和pfile1.py在路径'/home/puxitong/python/'  及其子路径下，这里的思路是将上一级目录 '/home/puxitong/python/' 添加在系统路径中，可以直接访问pfile.py，然后将pfile2.py 按照下一级路径导入方式进行导入：

```python
# 当前路径：/home/puxitong/python/file1/

# 导入pfile.py前先将其路径添加到系统路径中
import sys
sys.path.append('/home/puxitong/python/')

# 导入pfile.py
import pfile

# 导入pfile2.py
from file1 import pfile2
```

如果要在pfile1_1.py中导入pfile.py, pfile1.py, pfile2.py呢? 原理是一样的,即将文件pfile.py所在路径添加到系统路径中,可直接导入pfile.py, 再按照下级文件导入方式导入pfile1.py和pfile2.py:



```python
# 当前路径：/home/puxitong/python/file1/file1_1/

# 导入pfile.py前先将其路径添加到系统路径中
import sys
sys.path.append('/home/puxitong/python/')

# 导入pfile.py
import pfile

# 导入pfile1.py
from file2 import pfile1

# 导入pfile2.py
from file2 import pfile2
```

##### 自然地,导入任意.py文件时,只需要在导入该文件前用

> sys.path.append('该文件所在的绝对路径')

##### 将该文件所在的绝对路径添加到系统路径中,再进行同级目录或下级目录导入方式导入即可.