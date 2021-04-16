### 23.1.3 Little Endian与Big Endian

采用Little Endian模式的CPU对操作数的存放方式是从低字节到高字节，而Big Endian模式对操作数的存放方式是从高字节到低字节。例如，16bit宽的数0x1234在Little Endian模式CPU内存中的存放方式（假设从地址0x4000开始存放）为：

| 内存地址 | 0x4000 | 0x4001 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| 存放内容 | 0x34 | 0x12 |

而在Big Endian模式，CPU内存中的存放方式则为：

| 内存地址 | 0x4000 | 0x4001 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| 存放内容 | 0x12 | 0x34 |

32bit宽的数0x12345678在Little Endian模式CPU内存中的存放方式（假设从地址0x4000开始存放）为：

| 内存地址 | 0x4000 | 0x4001 | 0x4002 | 0x4003 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 存放内容 | 0x78 | 0x56 | 0x34 | 0x12 |

而在Big Endian 模式CPU 内存中的存放方式则为：

| 内存地址 | 0x4000 | 0x4001 | 0x4002 | 0x4003 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| 存放内容 | 0x12 | 0x34 | 0x56 | 0x78 |

内核中定义如下多个宏来进行Big Endian模式与Little Endian模式的互换，包括cpu_to_le64、le64_to_cpu、cpu_to_le32、le32_to_cpu、cpu_to_le16、le16_to_cpu。

内核中定义如下多个宏来进行Big Endian模式与Big Endian模式的互换：

cpu_to_be64、be64_to_cpu、cpu_to_be32、be32_to_cpu、cpu_to_be16、be16_to_cpu。

在Linux/drivers目录的ATM、IEEE1394、SCSI、NET、USB等源码中，都大量存在对上述这些宏的使用。

