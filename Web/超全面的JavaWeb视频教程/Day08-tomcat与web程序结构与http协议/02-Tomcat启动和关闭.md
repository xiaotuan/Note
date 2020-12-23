### 1. 安装、启动、配置 Tomcat

下载 Tomcat 可以到 <http://tomcat.apache.org> 下载。

Tomcat 分为安装版和解压版：

+ 安装版：一台电脑上只能安装一个 Tomcat；
+ 解压版：无需安装，解压即可用，解压多少份都可以，所以我们选择解压版。

### 2. 启动和关闭 Tomcat

在启动 Tomcat 之前，我们必须要配置环境变量：

+ JAVA_HOME：必须先配置 JAVA_HOME，因为 Tomcat 启动需要使用 JDK；
+ CATALANA_HOME：如果是安装版，那么还需要配置这个变量，这个变量用来指定 Tomcat 的安装路径。例如：F:\apache-tomcat-7.0.42 。
+ 启动：进入 %CATALANA_HOME%\bin 目录，找到 startup.bat，双击即可；
+ 关闭：进入 %CATALANA_HOME%\bin 目录，找到 shutdown.bat，双击即可；

> 注意：点击 startup.bat 后窗口一闪即消失，请检查 JAVA_HOME 环境变量配置是否正确。

