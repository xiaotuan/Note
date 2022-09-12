[toc]

### 1. 安装 zipfile37

```shell
$ pip3 install zipfile37
Collecting zipfile37
  Downloading zipfile37-0.1.3.tar.gz (20 kB)
Building wheels for collected packages: zipfile37
  Building wheel for zipfile37 (setup.py) ... done
  Created wheel for zipfile37: filename=zipfile37-0.1.3-py3-none-any.whl size=21029 sha256=ff7152d727313cd93e236bc3afaffa5ed856ef35e22bb9068428dcc220e4d95f
  Stored in directory: /home/xiaotuan/.cache/pip/wheels/55/d6/4d/2e95d4ca45f2a4b7d6ac3cf3210106ed456035aec731037496
Successfully built zipfile37
Installing collected packages: zipfile37
Successfully installed zipfile37-0.1.3
```

### 2. 压缩文件

```shell
import zipfile37

z = zipfile37.ZipFile("code.zip", "w", zipfile37.ZIP_STORED)
z.write("cplus.cpp")
z.write("test16.sh")
# "test.sh"：要压缩的文件，"test/test.sh"：将其压缩到压缩包文件路径
z.write("test.sh", "test/test.sh")
z.close()
```

