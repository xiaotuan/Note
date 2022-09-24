[toc]

### 1. 学习 curl

`curl` 工具允许你从特定的 Web 服务中接收数据。与 `wget` 不同之处在于，你还可以用它向 Web 服务器发送数据。

> 提示：安装 `curl` 的命令如下：
>
> ```shell
> sudo apt-get install curl
> ```

除了 `curl` 工具，你还需要一个能够提供免费 SMS 消息发送服务的网站。在本脚本中用到的是 <http://testbelt.com/text>。这个网站允许你每天免费发送最多 75 条短信。

要使用 `curl` 和 <http://textbelt.com/text/> 向自己发送短信，需使用下列语法：

```shell
$ curl http://textbelt.com/text \
-d number=YourPhoneNumber \
-d "message=Your Test Message"
```

### 2. 使用电子邮件发送短信

通过电子邮件发送短信的基本语法如下：

```shell
$ mail -s "Your test message" your_phone_number@your_sms_gateway
```

不幸的是，当你按照语法输入完命令之后，必须输入要发送的短信并按下<kbd>Ctrl</kbd> + <kbd>D</kbd> 才能够发送。

```shell
$ echo "This is a test" > message.txt
$ mail -s "Test from email" \
3123482348@vtext.com < message.txt
```

### 3. 创建脚本

```shell
#!/bin/bash
#
# Send a Test Message
#####################################
#
# Script Variables ####
#
phone="233942094"
SMSrelay_url=http://textbelt.com/text
text_message="System Code Red"
#
# Send text #####################
#
curl -s $SMSrelay_url -d \
number=$phone \
-d "message=$text_message" > /dev/null
#
exit
```

