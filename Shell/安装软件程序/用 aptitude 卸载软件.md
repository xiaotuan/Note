要想只删除软件包而不删除数据和配置文件，可以使用 `aptitude` 的 `remove` 选项。要删除软件包和相关的数据和配置文件，可用 `purge` 选项：

```shell
$ sudo aptitude purge wine
[sudo] password for user:
The following packages will be REMOVED:
    cabextract{ u} esound- clients{ u} esound- common{ u} gnome- exe- thumbnailer {u} icoutils{ u} imagemagick{ u} libaudio2{ u} libaudiofile0{ u} libcdt4{ u} libesd0{ u} libgraph4{ u} libgvc5{ u} libilmbase6{ u} libmagickcore3- extra {u} libmpg123- 0{ u} libnetpbm10{ u} libopenal1{ u} libopenexr6{ u} libpathplan4{ u} libxdot4{ u} netpbm{ u} ttf- mscorefonts- installer{ u} ttf- symbol- replacement{ u} winbind{ u} wine{ p} wine1. 2{ u} wine1. 2- gecko {u}

0 packages upgraded, 0 newly installed, 27 to remove and 6 not upgraded. 
Need to get 0B of archives. After unpacking 121MB will be freed. 
Do you want to continue? [Y/n/?] Y
```

> 提示：要看软件包是否已删除，可以再用 `aptitude` 的 `search` 选项。如果在软件包名称的前面看到一个 c，意味着软件已删除，但配置文件尚未从系统中清除；如果前面是个 p 的话，说明配置文件也已删除。