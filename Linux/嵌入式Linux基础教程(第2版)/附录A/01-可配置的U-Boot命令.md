### 附录A　可配置的U-Boot命令

U-Boot包含70多个可配置的命令，表A-1中总结了这些命令。除此以外，还有很多非标准命令，其中一些与具体的硬件有关或仍处于实验阶段。如果你想获取最新的完整命令列表，请直接参考源码。这里列出的命令都是在头文件.../include/config_cmd_all.h中定义的，路径中的...代表U-Boot顶层源码目录。

<center class="my_markdown"><b class="my_markdown">表A-1　可配置的U-Boot命令</b></center>

| **命令集** | 命令的含义 |
| :-----  | :-----  | :-----  | :-----  |
| `CONFIG_CMD_AMBAPP` | 打印AMBA总线的即插即用信息 |
| `CONFIG_CMD_ASKENV` | 询问环境变量 |
| `CONFIG_CMD_AT91_SPIMUX` | 最新的U-Boot源码中没有实现这个命令 |
| `CONFIG_CMD_AUTOSCRIPT` | 支持Autoscript |
| `CONFIG_CMD_BDI` | 显示板卡信息（bdinfo） |
| `CONFIG_CMD_BEDBUG` | 包含BedBug调试器 |
| `CONFIG_CMD_BMP` | 支持BMP |
| `CONFIG_CMD_BOOTD` | 默认引导命令（bootd） |
| `CONFIG_CMD_BSP` | 与具体板卡相关的功能 |
| `CONFIG_CMD_CACHE` | `icache` 和 `dcache` 命令 |
| `CONFIG_CMD_CDP` | 思科发现协议（Cisco Discovery Protocol） |
| `CONFIG_CMD_CONSOLE` | 显示控制台信息（coninfo） |
| `CONFIG_CMD_DATE` | 支持RTC、日期/时间等 |
| `CONFIG_CMD_DHCP` | 支持DHCP |
| `CONFIG_CMD_DIAG` | 诊断命令 |
| `CONFIG_CMD_DISPLAY` | 支持显示 |
| `CONFIG_CMD_DOC` | 支持Disk-on-chip |
| `CONFIG_CMD_DTT` | 数码温度计和调温器 |
| `CONFIG_CMD_ECHO` | 回显参数 |
| `CONFIG_CMD_EDITENV` | 互动式编辑环境变量 |
| `CONFIG_CMD_EEPROM` | 支持读/写EEPROM |
| `CONFIG_CMD_ELF` | ELF（VxWorks）加载/引导命令 |
| `CONFIG_CMD_EXT2` | 支持EXT2 |
| `CONFIG_CMD_FAT` | 支持FAT |
| `CONFIG_CMD_FDC` | 支持软盘 |
| `CONFIG_CMD_FDOS` | 支持软盘DOS |
| `CONFIG_CMD_FLASH` | 闪存相关命令（比如 `erase` 、 `protect` ） |
| `CONFIG_CMD_FPGA` | 支持FPGA配置 |
| `CONFIG_CMD_HWFLOW` | RTS/CTS硬件流控 |
| `CONFIG_CMD_I2C` | 支持I<sup class="my_markdown">2</sup>C串行总线 |
| `CONFIG_CMD_IDE` | 支持IDE硬盘驱动器 |
| `CONFIG_CMD_IMI` | IMI相关信息 |
| `CONFIG_CMD_IMLS` | 列出所有找到的镜像 |
| `CONFIG_CMD_IMMAP` | 支持IMMR dump |
| `CONFIG_CMD_IRQ` | 中断相关信息 |
| `CONFIG_CMD_ITEST` | 整数（和字符串）测试 |
| `CONFIG_CMD_JFFS2` | 支持JFFS2 |
| `CONFIG_CMD_KGDB` | `kgdb` |
| `CONFIG_CMD_LICENSE` | 打印GPL许可证文本 |
| `CONFIG_CMD_LOADB` | `loadb` |
| `CONFIG_CMD_LOADS` | `loads` |
| `CONFIG_CMD_MEMORY` | `md` 、  `mm` 、  `nm` 、  `mw` 、  `cp` 、  `cmp` 、  `crc` 、 `base` 、  `loop` 、 `mtest` |
| `CONFIG_CMD_MFSL` | 支持Microblaze FSL |
| `CONFIG_CMD_MG_DISK` | 支持Mflash |
| `CONFIG_CMD_MII` | 支持MII |
| `CONFIG_CMD_MISC` | 其他功能，比如sleep |
| `CONFIG_CMD_MMC` | 支持MMC |
| `CONFIG_CMD_MTDPARTS` | 支持管理MTD分区 |
| `CONFIG_CMD_NAND` | 支持NAND |
| `CONFIG_CMD_NET` | `bootp` 、 `tftpboot` 、 `rarpboot` |
| `CONFIG_CMD_NFS` | 支持NFS |
| `CONFIG_CMD_ONENAND` | 支持OneNAND子系统 |
| `CONFIG_CMD_PCI` | PCI相关信息 |
| `CONFIG_CMD_PCMCIA` | 支持PCMCIA |
| `CONFIG_CMD_PING` | 支持ping |
| `CONFIG_CMD_PORTIO` | 端口I/O |
| `CONFIG_CMD_REGINFO` | 寄存器转储 |
| `CONFIG_CMD_REISER` | 支持Reiserfs |
| `CONFIG_CMD_RUN` | 在环境变量中运行命令 |
| `CONFIG_CMD_SAVEENV` | 保存环境命令 |
| `CONFIG_CMD_SAVES` | 保存S record dump |
| `CONFIG_CMD_SCSI` | 支持SCSI |
| `CONFIG_CMD_SDRAM` | 打印SDRAM DIMM SPD信息 |
| `CONFIG_CMD_SETEXPR` | 通过eval表达式设置环境变量 |
| `CONFIG_CMD_SETGETDCR` | 在4xx上支持DCR |
| `CONFIG_CMD_SNTP` | 支持SNTP |
| `CONFIG_CMD_SOURCE` | 从内存中运行脚本（源码） |
| `CONFIG_CMD_SPI` | SPI工具 |
| `CONFIG_CMD_TERMINAL` | 在某个端口上启动终端仿真器 |
| `CONFIG_CMD_UNIVERSE` | 支持Tundra Universe |
| `CONFIG_CMD_UNZIP` | 解压一块内存区域 |
| `CONFIG_CMD_USB` | 支持USB |
| `CONFIG_CMD_VFD` | 支持VFD（TRAB） |
| `CONFIG_CMD_XIMG` | 加载多镜像的一部分 |



