`Tkinter` 在系统中不是默认必须安装的，可以通过在 Python 解释器中尝试导入 `Tkinter` 模块（Python 1 和 2 版本，在 Python 3 中重命名为 `tkinter`）来检查 `Tkinter` 是否可用。如果 `Tkinter` 可用，则不会有错误发生，如下所示：

```shell
qintuanye@WB-SVR-27:~/work01/mtk/12/8766/C/mt8766_s$ python
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import Tkinter
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 42, in <module>
    raise ImportError, str(msg) + ', please install the python-tk package'
ImportError: No module named _tkinter, please install the python-tk package
>>> 
```

或：

```shell
PS C:\Users\Xiaotuan\Desktop> python
Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import tkinter
>>>
```

