### 
  1.5 卸载MySQL


<img class="my_markdown" class="h-pic" src="../images/Figure-0047-55.jpg" style="width:103px;  height: 98px; "/> 本节视频教学录像：2分钟

卸载MySQL需要保证能完全卸载，这样才不影响下次安装使用，下面以Windows 7为例介绍具体的卸载过程。

⑴在Windows服务中停止MySQL的服务。

⑵打开“控制面板”，单击“程序和功能”，找到“MySQL”，右键单击从下拉菜单中选择卸载（或者使用其他软件卸载）。

⑶卸载完成后，删除安装目录下的MySQL文件夹及程序数据文件夹，如C:\Program Files (x86)\MySQL 和 C:\ProgramData\MySQL。

⑷在运行中输入“regedit”，进入注册表，将所有的MySQL注册表内容完全清除，具体删除内容如下：

①HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Application\MySQL 目录删除；

②HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\Services\Eventlog\Application\MySQL 目录删除；

③HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog\Application\MySQL目录删除。

⑸操作完成重新启动计算机。

注意 
 在删除C:\ProgramData文件下的MySQL文件时，需要在“工具→文件夹选项→查看”中选中“显示隐藏的文件、文件夹和驱动器”选项。

