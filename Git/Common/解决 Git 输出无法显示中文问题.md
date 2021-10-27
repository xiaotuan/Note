[toc]

### 方法一：

在终端输入如下命令：

```shell
$ git config --global core.quotepath false
$ git config --global i18n.commitencoding utf-8 # 设置提交命令的时候使用utf-8编码集提交
$ git config --global i18n.logoutputencoding utf-8 # 日志输出时使用utf-8编码集显示
$ export LESSCHARSET=utf-8 # 设置LESS字符集为utf-8
```

### 方法二：

在终端中输入如下命令：

```shell
$ git config --global core.quotepath false
```

同时修改终端字符设置，将其设置成 `UTF-8` 编码格式。在终端标题栏上右击鼠标，在弹出的菜单中选择 `Options...`，在 `Options` 对话框中的左边选择 `Text` 项，在右边 `Character set` 下拉列表中选择 `UTF-8`，然后点击 `Save` 按钮保存修改并关闭对话框。

