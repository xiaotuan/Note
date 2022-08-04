可以使用 `echo $BASH_SUBSHELL` 命令查看是否生成了子 shell。如果该命令返回 0，就表明没有子 shell。如果返回 1 或者其他更大的数字，就表明存在子 shell。

```shell
$ pwd ; ls ; cd /etc ; pwd ; cd ; pwd ; ls ; echo $BASH_SUBSHELL
/home/qintuanye/AndroidProjectConfig
build.log  codes  main.py  README.md  resources  Temp  test
/etc
/home/qintuanye
AndroidProjectConfig  ssh_bak  Tools  work01  work02
0
$ (pwd ; ls ; cd /etc ; pwd ; cd ; pwd ; ls ; echo $BASH_SUBSHELL)
/home/qintuanye/AndroidProjectConfig
build.log  codes  main.py  README.md  resources  Temp  test
/etc
/home/qintuanye
AndroidProjectConfig  ssh_bak  Tools  work01  work02
1
```

