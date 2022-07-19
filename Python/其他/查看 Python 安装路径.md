1. 不管 Windows 还是 Linux，在终端里输入 python，打开 python 后输入如下：

   ```shell
   > python
   Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>> import sys
   >>> sys.executable
   'C:\\Users\\xiaotuan\\AppData\\Local\\Programs\\Python\\Python310\\python.exe'
   >>>
   ```

2. 或者直接在终端中输入如下命令：

   ```shell
   > python -c "import sys; print(sys.executable);"
   C:\Users\xiaotuan\AppData\Local\Programs\Python\Python310\python.exe
   ```

   

