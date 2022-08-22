`ls` 命令的 `-F` 选项能够在具有执行权限的文件名后加一个星号：

```shell
$ ls -lF
总用量 80
-rw-rw-r-- 1 xiaotuan xiaotuan     1 4月   2 11:31  _1.txt
-rwxrwxr-x 1 xiaotuan xiaotuan 17264 7月  19 19:36  a.out*
-rw-rw-r-- 1 xiaotuan xiaotuan    46 3月  11 16:33  a_text_file
-rw-rw-r-- 1 xiaotuan xiaotuan   237 4月  12 08:56  file.in
-rw------- 1 xiaotuan xiaotuan   206 4月  11 15:28  file.out
drwxrwxr-x 6 xiaotuan xiaotuan  4096 8月  10 09:04  learning_log/
-rw-r----- 1 xiaotuan xiaotuan    26 4月  11 15:10  myfile
-rwxrwxrwx 1 xiaotuan xiaotuan     0 8月  15 11:59  newfile*
-rw-r----- 1 xiaotuan xiaotuan     0 8月  16 10:25  newfile2
-rw-rw-r-- 1 xiaotuan xiaotuan   311 4月  22 16:04  node.js
drwx------ 3 xiaotuan xiaotuan  4096 8月   9 10:03 'Old Firefox Data'/
-r--r--r-- 1 root     root        73 5月  10 10:22  printf.txt
-rw-rw-r-- 1 xiaotuan xiaotuan    23 7月  26 11:14  result.txt
-rw-rw-r-- 1 xiaotuan xiaotuan  1279 7月  19 17:06  test.c
drwxrwxr-x 2 xiaotuan xiaotuan  4096 4月  11 18:38  testDir/
-rw-rw-r-- 1 xiaotuan xiaotuan   318 8月   4 19:26  test.py
-rwxrwxr-x 1 xiaotuan xiaotuan   174 4月   2 11:31  testSh.sh*
-rw------- 1 xiaotuan xiaotuan    11 7月  14 14:47  Xiaotuan-odUNuV
```

