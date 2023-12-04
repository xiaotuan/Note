Ubuntu 提供了一个命令来帮助用户完成这个功能，那就是 `man` 命令，通过 `man` 命令可以查看其他命令的语法格式、主要功能、主要参数说明等，`man` 命令格式如下：

```shell
man [命令名]
```

例如：

```shell
$ man ifconfig
```

执行上面命令后将显示如下信息：

```shell
IFCONFIG(8)                Linux Programmer's Manual               IFCONFIG(8)

NAME
       ifconfig - configure a network interface

SYNOPSIS
       ifconfig [-v] [-a] [-s] [interface]
       ifconfig [-v] interface [aftype] options | address ...

DESCRIPTION
       Ifconfig  is  used to configure the kernel-resident network interfaces.
       It is used at boot time to set up interfaces as necessary.  After that,
       it  is  usually  only  needed  when  debugging or when system tuning is
       needed.

       If no arguments are given, ifconfig displays the  status  of  the  cur‐
       rently  active interfaces.  If a single interface argument is given, it
       displays the status of the given interface only; if a single  -a  argu‐
       ment  is  given,  it  displays the status of all interfaces, even those
       that are down.  Otherwise, it configures an interface.

Address Families
       If the first argument after the interface name  is  recognized  as  the
 Manual page ifconfig(8) line 1 (press h for help or q to quit)
```

