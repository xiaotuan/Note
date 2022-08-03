<center><b>Linux 文件压缩工具</b></center>

| 工具     | 文件扩展名 | 描述                                                |
| -------- | ---------- | --------------------------------------------------- |
| bzip2    | .bz2       | 采用 Burrows-Wheeler 块排序文本压缩算法和霍夫曼编码 |
| compress | .Z         | 最初的 Unix 文件压缩状态，已经快没人用了            |
| gzip     | .gz        | GNU 压缩工具，用 Lempel-Ziv 编码                    |
| zip      | .zip       | Windows 上 PKZIP 工具的 Unix 实现                   |

`compress` 文件压缩工具已经很少在 Linux 系统上看到了。如果下载了带 `.Z` 扩展名的文件，通常可以通过安装 `compress` 包（在很多 Linux 发行版上叫作 ncompress），然后再用 `uncompress` 命令来解压文件。