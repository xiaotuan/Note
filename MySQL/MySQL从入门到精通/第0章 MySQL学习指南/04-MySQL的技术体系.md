### 
  0.3 MySQL的技术体系


<img class="my_markdown" class="h-pic" src="../images/Figure-0026-17.jpg" style="width:87px;  height: 86px; "/> 本节视频教学录像：3分钟

要学好MySQL，就必须先要对MySQL数据库的技术体系做一个系统的了解和认识，这对于学者以后进行数据库的开发和应用有重要的意义。

⒈ C/S架构

C/S（Client/Server）结构，即大家熟知的客户机和服务器结构。通过C/S可以充分利用两端硬件环境的优势，将任务合理分配到Client端和Server端来实现，降低了系统的通讯开销。目前大多数应用软件系统都是C/S形式的两层结构。

在C/S模式中服务器通常采用高性能的PC、工作站或小型机，并采用大型数据库系统，如Oracle、MySQL 等。客户端需要安装专用的客户端软件。用户使用应用程序时，首先启动客户端通过有关命令告知服务器完成各种操作，而服务器则按照命令提供相应的服务。每一个客户端软件都可以向一个服务器或应用程序服务器发出请求。

⒉ MySQL命令行实用程序

MySQL数据库管理系统提供了许多命令行工具程序，这些工具用来管理MySQL服务器、对数据库进行访问控制、管理MySQL用户以及数据库备份和恢复工具等。这些工具程序分为MySQL服务器端工具程序和客户端工具程序。

⒊ MySQL Workbench

MySQL Workbench是一款专为MySQL设计的ER/数据库建模工具。它是著名的数据库设计工具DBDesigner4的继任者。你可以用MySQLWorkbench设计和创建新的数据库图示，建立数据库文档，以及进行复杂的MySQL迁移。主要功能如下。

●数据库设计和模型建立。

●SQL 开发。

●数据库管理。

MySQL Workbench同时有开源和商业化两个版本。

⑴ MySQL Workbench Community Edition（社区版本），用户可免费使用。

⑵ MySQL Workbench Standard Edition（商业版本），需要收取费用，官方提供技术支持。

两个版本的软件均支持Windows和Linux系统。

