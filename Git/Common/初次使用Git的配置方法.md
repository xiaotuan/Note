1. 配置 Git 信息

```shell
$ git config --global user.name "your name"
$ git config --global user.email "your_email@youremail.com"
```

2. 生成 SSHKEY

```shell
$ ssh-keygen -o
Generating public/private rsa key pair.
Enter file in which to save the key (/home/schacon/.ssh/id_rsa):
Created directory '/home/schacon/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/schacon/.ssh/id_rsa.
Your public key has been saved in /home/schacon/.ssh/id_rsa.pub.
The key fingerprint is:
d0:82:24:8e:d7:f1:bb:9b:33:53:96:93:49:da:9b:e3 schacon@mylaptop.local
```

成功的话会在~/下生成.ssh文件夹，进去，打开id_rsa.pub，复制里面的key。回到github上，进入 Account Settings（账户配置），左边选择SSH Keys，Add SSH Key,title随便填，粘贴在你电脑上生成的key。

3. 验证连接

```shell
$ ssh -T git@github.com
Hi xiaotuan! You've successfully authenticated, but GitHub does not provide shell access.
```

