在 `Windows` 以及 `Linux` 下分别启动和关闭 `Tomcat` 服务器的批处理文件。只要运行这些批处理文件，即可启动或关闭 `Tomcat` 服务器。

<center><b>启动和关闭 Tomcat 服务器的批处理文件</b></center>

| 操作系统 | 启动脚本                        | 关闭脚本                         |
| -------- | ------------------------------- | -------------------------------- |
| Windows  | <CATALINE_HOME>/bin/startup.bat | <CATALINA_HOME>/bin/shutdown.bat |
| Linux    | <CATALINA_HOME>/bin/startup.sh  | <CATALINA_HOME>/bin/shutdown.sh  |

`Tomcat` 服务器启动后，就可以在浏览器中访问以下 URL：

```
http://localhost:8080/
```

