### 1. 命令概述

`basename -` 从文件名中剥离目录和后缀

`basename` 命令用于打印目录或者文件的基本名称。`basename` 和 `dirname` 命令通常用于 `shell` 脚本中的命令替换来指定和指定的输入文件名称有所差异的输出文件名称。

### 2. 命令格式

basename 名称 [后缀]

basename 选项

### 3. 常用选项

```shell
Mandatory arguments to long options are mandatory for short options too.
  -a, --multiple       support multiple arguments and treat each as a NAME
  -s, --suffix=SUFFIX  remove a trailing SUFFIX
  -z, --zero           separate output with NUL rather than newline
      --help     display this help and exit
      --version  output version information and exit
```

### 4. 参考示例

```shell
$ basename /usr/bin/sort          -> "sort"
$ basename include/stdio.h .h     -> "stdio"
$ basename -s .h include/stdio.h  -> "stdio"
$ basename -a any/str1 any/str2   -> "str1" followed by "str2"
```

> `basename $0` 常用于获取脚本文件名