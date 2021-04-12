### 9.2.2　安装Docker Compose

Docker Compose可用于多种平台。本节将介绍在Windows、Mac以及Linux上的几种安装方法。当然还有其他的安装方法，不过以下几种足够帮助读者入门。

##### 1．在Windows 10上安装Docker Compose

在Windows 10上运行Docker的推荐工具是Windows版Docker（Docker for Windows, DfW)。Docker Compose会包含在标准DfW安装包中。所以，安装DfW之后就已经有Docker Compose工具了。

在PowerShell或CMD终端中使用如下命令可以检查Docker Compose是否安装成功。

```rust
> docker-compose --version
docker-compose version 1.18.0, build 8dd22a96
```

关于在Windows 10上安装Windows版Docker的更多内容请见第3章。

##### 2．在Mac上安装Docker Compose

与Windows 10一样，Docker Compose也作为Mac版Docker（Docker for Mac, DfM）的一部分进行安装，所以一旦安装了DfM，也就安装了Docker Compose。

在终端中运行如下命令检查Docker Compose是否安装。

```rust
$ docker-compose --version
docker-compose version 1.18.0, build 8dd22a96
```

关于安装Mac版Docker的更多内容请见第3章。

##### 3．在Windows Server上安装Docker Compose

Docker Compose在Windows Server上是作为一个单独的二进制文件安装的。因此，使用它的前提是确保在Windows Server上已经正确安装了Docker。

在PowerShell终端中输入如下命令来安装Docker Compose。为了便于阅读，下面的命令使用反引号（`）来对换行进行转义，从而将多行命令合并。

下面的命令安装的是 `1.18.0` 版本的Docker Compose，读者请自行选择版本号：https://github. com/docker/compose/releases。只需要将URL中的 `1.18.0` 替换为你希望安装的版本即可。

```rust
> Invoke-WebRequest ` "https://github.com/docker/compose/releases/download/1\
.18.0/docker-compose-Windows-x86_64.exe" `
-UseBasicParsing `
-OutFile $Env:ProgramFiles\docker\docker-compose.exe
Writing web request
Writing request stream... (Number of bytes written: 5260755)
```

使用 `docker-compose --version` 命令查看安装情况。

```rust
> docker-compose --version
docker-compose version 1.18.0, build 8dd22a96
```

Docker Compose安装好了，只要Windows Server上安装有Docker引擎即可使用。

##### 4．在Linux上安装Docker Compose

在Linux上安装Docker Compose分为两步。首先使用 `curl` 命令下载二进制文件，然后使用 `chmod` 命令将其置为可运行。

Docker Compose在Linux上的使用，同样需要先安装有Docker引擎。

如下命令会下载 `1.18.0` 版本的Docker Compose到 `/usr/bin/local` 。请在GitHub上查找想安装的版本，并替换URL中的 `1.18.0` 。

下面的示例是一条写成多行的命令，如果要将其合并为一行，请删掉反斜杠（ `\` ）。

```rust
$ curl -L \
 https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`\
uname -s`-`uname -m` \
 -o /usr/local/bin/docker-compose
% Total % Received Time Time Time Current
                        Total   Spent   Left    Speed
100   617    0   617    0 --:--:-- --:--:-- --:--:-- 1047
100 8280k  100 8280k    0  0:00:03  0:00:03 --:--:-- 4069k
```

下载docker-compose二进制文件后，使用如下命令使其可执行。

```rust
$ chmod +x /usr/local/bin/docker-compose
```

检查安装情况以及版本。

```rust
$ docker-compose --version
docker-compose version 1.18.0, build 8dd22a9
```

现在就可以在Linux上使用Docker Compose了。

此外，也可以使用 `pip` 来安装Docker Compose的Python包。不过，本书无意在各种各样的安装方法中花费过多篇幅，点到为止，继续后续的内容。

