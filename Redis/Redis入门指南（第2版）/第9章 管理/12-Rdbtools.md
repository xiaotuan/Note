### 9.3.3 Rdbtools

Rdbtools 是一个Redis的快照文件解析器，它可以根据快照文件导出JSON数据文件、分析 Redis 中每个键的占用空间情况等。Rdbtools 是使用 Python 开发的，项目地址是 https:/ /github.com/sripathikrishnan/redis-rdb-tools。

#### 1．安装Rdbtools

使用如下命令安装Rdbtools：

```shell
git clone https://github.com/sripathikrishnan/redis-rdb-tools
cd redis-rdb-tools
sudo python setup.py install

```

#### 2．生成快照文件

如果没有启用RDB持久化，可以使用 `SAVE` 命令手动使Redis生成快照文件。

#### 3．将快照导出为JSON格式

快照文件是二进制格式，不利于查看，可以使用Rdbtools来将其导出为JSON格式，命令如下：

```shell
rdb --command json /path/to/dump.rdb > outputfilename.json 
```

其中 `/path/to/dump.rdb` 是快照文件的路径，`output`` ``filename.json` 为要导出的文件路径。

#### 4．生成空间使用情况报告

Rdbtools能够将快照文件中记录的每个键的存储情况导出为CSV文件，可以将该CSV文件导入到Excel等数据分析工具中分析来了解Redis的使用情况。命令如下：

```shell
rdb -c memory /path/to/dump.rdb > output_filename.csv

```

导出的CSV文件的字段及说明如表9-1所示。

<center class="my_markdown"><b class="my_markdown">表9-1 Rdbtools导出的CSV文件字段说明</b></center>

| 字　　段 | 说　　明 |
| :-----  | :-----  | :-----  | :-----  |
| `database` | 存储该键的数据库索引 |
| `type` | 键类型（使用 `TYPE` 命令获得） |
| `key` | 键名 |
| `size_in_bytes` | 键大小（字节） |
| `encoding` | 内部编码（使用 `OBJECTENCODING` 命令获得） |
| `num_elements` | 键的元素数 |
| `len_largest_element` | 最大元素的长度 |



