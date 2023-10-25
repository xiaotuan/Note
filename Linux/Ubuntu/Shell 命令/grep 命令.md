`grep` 命令用于查找文件内容：

```shell
xiaotuan@xiaotuan:~$ grep -rn "Ubuntu" /
/home/xiaotuan/examples.desktop:122:Comment=Example content for Ubuntu
/home/xiaotuan/examples.desktop:123:Comment[aa]=Ubuntuh addattinoh ceelallo
/home/xiaotuan/examples.desktop:124:Comment[ace]=Contoh aso ke Ubuntu
......
```

+ `-r` ：递归查找
+ `-n`：显示行号
+ `-i`：忽略大小写