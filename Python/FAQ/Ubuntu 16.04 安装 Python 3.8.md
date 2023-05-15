1. 下载 Python 3.8 源代码

   ```shell
   $ wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tar.xz
   ```

2. 解压源代码

   ```shell
   $ tar -xvJf  Python-3.8.1.tar.xz
   ```

3. 进入源代码目录

   ```shell
   $ cd Python-3.8.1
   ```

4. 安装依赖

   ```shell
   $ sudo apt-get install python-dev
   $ sudo apt-get install libffi-dev
   $ sudo apt-get install libssl-dev
   $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev
   ```

5. 配置编译环境

   ```shell
   $ ./configure prefix=/usr/local/python3
   ```

6. 开始编译

   ```shell
   $ make
   ```

7. 安装 Python

   ```shell
   $ make install
   ```

8. 修改软连接

   ```shell
   $ sudo mv /usr/bin/python /usr/bin/python.bak
   $ sudo ln -s /usr/local/python3/bin/python3 /usr/bin/python
   ```

9. 安装/升级 pip

   ```shell
   $ sudo apt-get install python3-pip
   $ pip3 install --upgrade pip
   ```

   如果升级失败，可以使用如下命令升级：

   ```shell
   $ python -m pip install --upgrade pip
   ```

   

