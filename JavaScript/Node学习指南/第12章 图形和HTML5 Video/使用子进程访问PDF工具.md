为了在 Ubuntu 上使用 wkhtmltopdf，需要安装支持这一功能的库：

```console
$ apt-get install openssl build-essential xorg libssl-dev
```

然后需要安装 xvfb 工具，允许 wkhtmltopdf 运行在虚拟的 X server 上（绕过对 X Windows 依赖）：

```console
apt-get install xvfb
```

下一步，创建一个 shell 脚本—— wkhtmltopdf.sh，将 wkhtmltopdf 包裹在 xvfb 中。代码行为：

```shell
xvfb -run -a -s "-screen 0 640x480x16 wkhtmltopdf $*"
```

将这个 shell 脚本放在 `/usr/bin` 目录下，并用 `chmod a+x` 改变文件权限。

在下面命令行中，下面这行代码接收一个连接到远程网页的 URL 然后使用所有默认设置生成 PDF:

```shell
wkhtmltopdf.sh http://remoteweb.com/page1.html page1.pdf
```

示例12-1 简单的包含 wkhtmltopdf 的 Node 程序

```js
var spawn = require('child-process').spawn

// 命令行参数
var url = process.argv[2]
var output = process.argv[3]
if (url && output) {
  var wkhtmltopdf = spawn('wkhtmltopdf.sh', [url, output])
  wkhtmltopdf.stdout.setEncoding('utf8')
  wkhtmltopdf.stdout.on('data', function (data) {
    console.log(data)
  })
  wkhtmltopdf.stderr.on('data', function (code) {
    console.log('child process exited with code ' + code)
  })
} else {
  console.log('You need to provide a URL and output file name')
}