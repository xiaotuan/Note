在 shell 脚本中使用 Lynx 时，大多数情况下你只是要提取 Web 页面中的某条（或某几条）特定信息。完成这个任务的方法称作**屏幕抓取**。

用 lynx 进行屏幕抓取的最简单方法是用 `-dump` 选项。这个选项不会在终端屏幕上显示 Web 页面。相反，它会将 Web 页面文本数据直接显示在 STDOUT 上。

```shell
$ lynx -dump http://fota.redstone.net.cn/Home/Index/login
   [1][ota_en.png] [2]中文 [3]English
   ____________________
   ____________________
   ____________________ 验证码
   [ ] 保存用户名
   登录

References

   1. http://fota.redstone.net.cn/Home/Index/login
   2. http://fota.redstone.net.cn/Home/Index/login?language=zh-cn
   3. http://fota.redstone.net.cn/Home/Index/login?language=en-us
```

每个链接都由一个标号标定，Lynx 在 Web 页面数据后显示了所有标号所指向的地址。

下面的例子演示了从天气网站获取当地天气数据的脚本：

```shell
#!/bin/bash
# extract the current weather for Chicago, IL

URL="http://weather.yahoo.com/united-states/illinois/chicago-2379574/"
LYNX=$(which lynx)
TMPFILE=$(mktemp tmpXXXXXX)
$LYNX -dump $URL > $TMPFILE
conditions=$(cat $TMPFILE | sed -n '/IL, United States/{n;p}')
temp=$(cat $TMPFILE | sed -n '/Feels Like/p' | awk '{print $4}')
rm -f $TMPFILE
echo "Current conditions: $conditions"
echo The current temp outside is: $temp
```



