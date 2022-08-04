**killApp.sh**

```shell
#!/bin/bash

# 使用方法：
#    $ ./killApp.sh 应用包名

# 获取应用进程信息
value=`adb shell ps | grep $1`
echo $value
if [[ -n $value ]];then
	# 获取进程ID
    pid=`echo $value | awk '{ print $2 }'`
    echo $pid
    # 杀死进程
    adb shell kill $pid
else
	echo "应用未运行"
fi
```

