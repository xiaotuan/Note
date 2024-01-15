[toc]

# 1 前言
`.NET5.0` 最近正式发布了，这个版本实现了对多个平台的统一支持，所以就尝鲜了一下，在自己的 `Ubuntu` 服务器上安装部署了一下 `.NET5.0` 的 `SDK`。本文就介绍安装和运行的具体过程。

# 2 安装
安装分为三步：

## 第1步 下载并更新包
由于微软的安装网址不在 `apt` 中，所以使用以下命令进行更新：

```shell
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
```

> 提示：可以在 <https://packages.microsoft.com/config/ubuntu/> 网站上查看支持的 `Ubuntu` 版本以及 `.NET` 的版本。

## 第2步 安装传输工具
为保证传输正常，需要使用 `apt-transport-https` 进行传输，安装方法如下：

```shell
sudo apt-get install apt-transport-https
sudo apt-get update
```

## 第3步 安装.NET5.0的SDK
`SDK` 的体积约为 `363 MB`，安装命令如下：

```shell
sudo apt-get install dotnet-sdk-5.0
```

# 3 建立程序
我们首先建立一个简单的控制台程序，毕竟在 `Linux` 上主要都是以命令的方式执行任务的。建立的命令只有1条：

```shell
$ dotnet new console --output sample1
```

然后就会输出以下内容

```
Welcome to .NET 5.0!
---------------------
SDK Version: 5.0.100

Telemetry
---------
The .NET tools collect usage data in order to help us improve your experience. It is collected by Microsoft and shared with the community. You can opt-out of telemetry by setting the DOTNET_CLI_TELEMETRY_OPTOUT environment variable to '1' or 'true' using your favorite shell.

Read more about .NET CLI Tools telemetry: https://aka.ms/dotnet-cli-telemetry

----------------
Installed an ASP.NET Core HTTPS development certificate.
To trust the certificate run 'dotnet dev-certs https --trust' (Windows and macOS only).
Learn about HTTPS: https://aka.ms/dotnet-https
----------------
Write your first app: https://aka.ms/dotnet-hello-world
Find out what's new: https://aka.ms/dotnet-whats-new
Explore documentation: https://aka.ms/dotnet-docs
Report issues and find source on GitHub: https://github.com/dotnet/core
Use 'dotnet --help' to see available commands or visit: https://aka.ms/dotnet-cli
--------------------------------------------------------------------------------------
Getting ready...
The template "Console Application" was created successfully.

Processing post-creation actions...
Running 'dotnet restore' on sample1/sample1.csproj...
  Determining projects to restore...
  Restored /root/.net5/sample1/sample1.csproj (in 70 ms).
Restore succeeded.
```

## 查看项目结构
使用 `tree sample1` 查看目录结构，内容如下所示：

```shell
root@server00:~/.net5# tree sample1/
sample1/
├── obj
│   ├── project.assets.json
│   ├── project.nuget.cache
│   ├── sample1.csproj.nuget.dgspec.json
│   ├── sample1.csproj.nuget.g.props
│   └── sample1.csproj.nuget.g.targets
├── Program.cs
└── sample1.csproj

1 directory, 7 files
```

查看一下主程序 `Progrom.cs` 的内容如下所示：

```shell
root@server00:~/.net5# cat sample1/Program.cs
using System;

namespace sample1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
```

另外，还有一个特别重要的项目配置文件 `sample1.csproj`，其内容为：

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net5.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>
```

## 编译并运行
现在使用命令 `dotnet run --project sample1` 进行编译并运行，可以看到以下内容：

```shell
root@server00:~/.net5# dotnet run --project sample1
Hello World!
```


运行成功。

然后我们再看一下项目的结构，可以看到出很多新的内容：

```shell
root@server00:~/.net5# tree sample1/
sample1/
├── bin
│   └── Debug
│       └── net5.0
│           ├── ref
│           │   └── sample1.dll
│           ├── sample1
│           ├── sample1.deps.json
│           ├── sample1.dll
│           ├── sample1.pdb
│           ├── sample1.runtimeconfig.dev.json
│           └── sample1.runtimeconfig.json
├── obj
│   ├── Debug
│   │   └── net5.0
│   │       ├── apphost
│   │       ├── ref
│   │       │   └── sample1.dll
│   │       ├── sample1.AssemblyInfo.cs
│   │       ├── sample1.AssemblyInfoInputs.cache
│   │       ├── sample1.assets.cache
│   │       ├── sample1.csprojAssemblyReference.cache
│   │       ├── sample1.csproj.CoreCompileInputs.cache
│   │       ├── sample1.csproj.FileListAbsolute.txt
│   │       ├── sample1.dll
│   │       ├── sample1.GeneratedMSBuildEditorConfig.editorconfig
│   │       ├── sample1.genruntimeconfig.cache
│   │       └── sample1.pdb
│   ├── project.assets.json
│   ├── project.nuget.cache
│   ├── sample1.csproj.nuget.dgspec.json
│   ├── sample1.csproj.nuget.g.props
│   └── sample1.csproj.nuget.g.targets
├── Program.cs
└── sample1.csproj

8 directories, 26 files
```

## 关于运行
其中，目录 `/sample1/bin/Debug/net5.0/sample1` 就是可执行程序，可以直接运行。比如：

```shell
root@server00:~/.net5# ./sample1/bin/Debug/net5.0/sample1
Hello World!
```

不过他还依赖于 `/sample1/bin/Debug/net5.0/ref/sample1.dll` 才可以运行。需要将其放置在指定的路径中，然后配置环境变量即可。
经测试，发现程序一共需要以下三个程序（放在同一目录中）才可运行：`sample1`、`sample1.dll` 和 `sample1.runtimeconfig.json`。其中最后一个为配置文件，内容如下：

```shell
root@server00:~/test1# cat sample1.runtimeconfig.json
{
  "runtimeOptions": {
    "tfm": "net5.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "5.0.0"
    }
  }
}
```


由此可见，此文件主要用于指定程序的类型和运行环境。

# 4 小结
通过本示例，可以看到安装和运行 `.NET5.0` 的程序还是很方便的，只需要几条命令即可。测试过程中也很顺利，几条命令运行完成，都得到了预期的效果。这样我们就可以使用 `.NET5.0` 来建立程序，可以看到

