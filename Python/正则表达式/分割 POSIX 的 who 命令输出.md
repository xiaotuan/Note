> 提示：在 `Windows` 系统中可以使用 `tasklist` 命令替代 `who` 来得到类似的结果。

### 1. Python 2.x 版本

**rewho.py**

```python
#!/usr/bin/env python

import os
import re

f = os.popen('who', 'r')
for eachLine in f:
	print re.split(r'\s\s+|\t', eachLine.rstrip())
f.close()
```

运行结果如下：

```shell
$ python rewho.py 
['xiaotuan tty7', '2023-06-19 10:20 (:0)']
```

### 2. Python 3.x 版本

**rewho.py**

```python
#!/usr/bin/env python

import os
import re

with os.popen('who', 'r') as f:
	for eachLine in f:
		print(re.split(r'\s\s+|\t', eachLine.rstrip()))
```

运行结果如下：

```shell
$ python3 rewho.py 
['xiaotuan tty7', '2023-06-19 10:20 (:0)']
```

### 3. 通用版本

**rewho.py**

```python
#!/usr/bin/env python

import os
import re
from distutils.log import warn as printf

with os.popen('who', 'r') as f:
	for eachLine in f:
		printf(re.split(r'\s\s+|\t', eachLine.rstrip()))
```

> 注意：`with` 语句是从 `Python 2.5` 开始引入的。

### 4. 处理 DOS 环境下 tasklist 命令的输出

**retasklist.py**

```python
#!/usr/bin/env python

import os
import re

with os.popen('tasklist /nh', 'r') as f:
    for eachLine in f:
        print(re.findall(r'([\w.]+(?:[\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)', eachLine.rstrip()))
```

运行结果如下：

```shell
[]
[('Process', '0', '8 K')]
[('System', '4', '2,952 K')]
[('Registry', '148', '63,560 K')]
[('smss.exe', '552', '328 K')]
[('csrss.exe', '728', '2,364 K')]
[('wininit.exe', '820', '944 K')]
[('csrss.exe', '828', '5,492 K')]
[('winlogon.exe', '916', '4,940 K')]
[('services.exe', '500', '7,528 K')]
.....
```

