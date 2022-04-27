[toc]

### 1. 问题现象

执行 `git push` 命名将代码上传至 Github 报如下错误信息：

```shell
$ git push Github
ssh: connect to host github.com port 22: Connection timed out
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

### 2. 问题分析

经确认网络可以连接到 Github 网站，SSH key 也是正常的。查看报错信息，发现错误提示无法通过 22 端口连接 github.com 网站。怀疑 22 端口被其他程序占用了，更换端口号后恢复正常。

### 3. 解决办法

在 `.ssh` 文件夹下添加一个名为 `config` 文件，文件内容如下所示：

```
Host github.com
User git
Hostname ssh.github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa
Port 443
```

