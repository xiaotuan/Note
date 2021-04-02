### 11.1.2　SQLite数据库

本书假设读者对数据库的基本概念和SQL语句已经有基础的知识，为了用实例研究Qt SQL的数据库编程功能，本章采用SQLite数据库作为数据库实例。

SQLite是一种无需服务器、无需进行任何配置的数据库，所有的数据表、索引等数据库元素全都存储在一个文件里，在应用程序里使用SQLite数据库就完全可以当作一个文件来使用。SQLite是可以跨平台使用的数据库，在不同平台之间可以随意复制数据库。SQLite的驱动库文件很小，包含完整功能的驱动可以小到只有500 KB。

SQLite是一种开源免费使用的数据库，可以从其官网下载最新版本的数据库驱动安装文件。

SQLite Expert是SQLite数据库可视化管理工具，可以从其官网下载最新的安装文件，SQLite Expert安装文件带有SQLite数据库驱动，所以安装SQLite Expert后无需再下载安装SQLite数据库驱动。

在SQLite Expert软件里建立一个数据库demodb.db3，在此数据库里建立4个表，本章的Qt SQL编程实例都采用这个数据库文件作为数据库实例。

SQLite Expert软件进行数据库字段设计的界面如图11-1所示。

![204.png](../images/204.png)
<center class="my_markdown"><b class="my_markdown">图11-1　在SQLite软件里设计数据库</b></center>

（1）employee数据表是一个员工信息表，用于在实例samp11_1里演示通过QSqlTableModel获取、显示和编辑数据表的内容，employee的字段定义见表11-2。

<center class="my_markdown"><b class="my_markdown">表11-2　employee数据表的字段定义</b></center>

| 序号 | 字段名 | 类型 | 描述 | 说明 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 1 | EmpNo | INT | 员工编号 | 主键，非空 |
| 2 | Name | VARCHAR(20) | 姓名 | 非空 |
| 3 | Gender | VARCHAR(4) | 性别 | 缺省值=“男” |
| 4 | Height | FLOAT | 身高 | 缺省值=1.71 |
| 5 | Birthday | DATE | 出生日期 |
| 6 | Mobile | VARCHAR(18) | 手机号 |
| 7 | Province | VARCHAR(20) | 省份 |
| 8 | City | VARCHAR(20) | 城市 |
| 9 | Department | VARCHAR(30) | 工作部门 |
| 10 | Education | VARCHAR(16) | 教育程度 |
| 11 | Salary | CURRENCY | 工资 | 缺省值=3500 |
| 12 | Photo | BLOB | 照片 | BLOB字段可存储任何二进制内容 |
| 13 | Memo | MEMO | 备注 | MEMO字段可存储任意长度普通文本 |

（2）departments数据表是一个学院信息表，记录学院编号和学院名称。其字段定义见表11-3。

<center class="my_markdown"><b class="my_markdown">表11-3　departments数据表的字段定义</b></center>

| 序号 | 字段名 | 类型 | 描述 | 说明 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 1 | departID | INT | 学院编号 | 主键，非空 |
| 2 | departments | VARCHAR(40) | 学院名称 | 非空 |

（3）majors数据表是专业信息表，记录各专业的信息。其字段定义见表11-4。

<center class="my_markdown"><b class="my_markdown">表11-4　majors数据表的字段定义</b></center>

| 序号 | 字段名 | 类型 | 描述 | 说明 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 1 | majorID | INT | 专业编号 | 主键，非空 |
| 2 | major | VARCHAR(40) | 专业名称 | 非空 |
| 3 | departID | INT | 所属学院编号 | 非空，等于departments表中某个学院的departID |

departments和majors构成一个Master/Detail关系数据表，majors表里的departID字段记录了这个专业属于哪个学院，departments表里的一条记录关联majors表中的多条记录。

（4）studInfo是一个记录学生信息的数据表。其字段定义见表11-5。

<center class="my_markdown"><b class="my_markdown">表11-5　studInfo数据表的字段定义</b></center>

| 序号 | 字段名 | 类型 | 描述 | 说明 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 1 | studID | INT | 学号 | 主键，非空 |
| 2 | name | VARCHAR(10) | 姓名 | 非空 |
| 3 | gender | VARCHAR(4) | 性别 |
| 4 | departID | INT | 学院编号 | 关联departments表中的记录 |
| 5 | majorID | INT | 专业编号 | 关联majors表中的记录 |

studInfo表中记录学生的所在学院采用了代码字段departID，具体的学院名称需要通过查询departments表中相同的departID的记录获得；majorID记录了专业代码，具体的专业名称需要查找majors表中的记录获取。这两个字段都是代码字段，只存储代码，具体的意义需要查询关联数据表的相应记录获得，在实际的数据库设计中经常用到这种设计方式。

Qt SQL中使用QSqlRelationalTableModel可以很方便地实现这种代码型数据表的显示与编辑，实例samp11_4显示了QSqlRelationalTableModel的使用方法。

