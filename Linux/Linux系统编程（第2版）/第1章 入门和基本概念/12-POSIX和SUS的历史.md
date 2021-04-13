### 1.3.1　POSIX和SUS的历史

在20世纪80年代中期，电气电子工程师协会（IEEE）开启了UNIX系统上的系统级接口的标准化工作。自由软件运动（Free Software Movement）的创始人Richard Stallman建议把该标准命名成POSIX（发音[pahz-icks]），其全称是Portable Operating System Interface（可移植操作系统接口）。

该工作的第一成果是在1988年获得通过的IEEE std 1003.1-1988（简称POSIX 1988）。1990年，IEEE对 POSIX标准进行了修订，通过了IEEE std 1003.1-1990（POSIX 1990）。后续的修订IEEE Std 1003.1b-1993（POSIX 1993或称POSIX.1b）和IEEE Std 1003.1c-1995（POSIX 1995或称POSIX.1c）分别描述了非强制性的实时和线程支持。2001年，这些非强制性标准在POSIX 1990的基础上进行整合，形成单一标准IEEE Std 1003.1-2001（POSIX 2001）。最新的标准IEEE Std 1003.1-2008 （POSIX 2008）在2008年12月发布。所有的核心POSIX标准都简称为POSIX.1，其中2008年的版本为最新版。

从20世纪80年代后期到20世纪90年代初期，UNIX系统厂商卷入了一场“UNIX之战”中，每家厂商都处心积虑地想将自己的UNIX变体定义成真正的“UNIX”操作系统。几大主要的UNIX厂商聚集在了工业联盟The Open Group周围，The Open Group是由开放软件基金会（Open Software Foundation，OSF）和X/Open合并组成。The Open Group提供证书、白皮书和兼容测试。在20世纪90年代初，正值UNIX之战如火如荼，The Open Group发布了单一UNIX规范（SUS）。SUS广受欢迎，很大原因归于SUS是免费的，而POSIX标准成本很高。今天，SUS合并了最新的POSIX标准。

第一个版本的SUS发布于1994年，然后在1997年和2002年分别发布了两个修订版SUSv2和SUSv3。最新的SUSv4在2008年发布。SUSv4修订结合了IEEE Std 1003.1-2008标准以及一些其他标准。本书将以POSIX标准介绍系统调用和其他接口，原因是SUS是对POSIX的扩展。

