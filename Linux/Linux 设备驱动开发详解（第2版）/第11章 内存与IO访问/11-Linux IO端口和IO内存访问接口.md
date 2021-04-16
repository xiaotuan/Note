### 11.4.1 Linux I/O端口和I/O内存访问接口

#### 1．I/O端口

在Linux设备驱动中，应使用Linux内核提供的函数来访问定位于I/O空间的端口，这些函数包括如下几种。

（1）读写字节端口（8位宽）。

unsigned inb(unsigned port); 
 
 void outb(unsigned char byte, unsigned port);

（2）读写字端口（16位宽）。

unsigned inw(unsigned port); 
 
 void outw(unsigned short word, unsigned port);

（3）读写长字端口（32位宽）。

unsigned inl(unsigned port); 
 
 void outl(unsigned longword, unsigned port);

（4）读写一串字节。

void insb(unsigned port, void *addr, unsigned long count); 
 
 void outsb(unsigned port, void *addr, unsigned long count);

（5）insb()从端口port开始读count个字节端口，并将读取结果写入addr指向的内存；outsb() 将addr指向的内存的count个字节连续地写入port开始的端口。

（6）读写一串字。

void insw(unsigned port, void *addr, unsigned long count); 
 
 void outsw(unsigned port, void *addr, unsigned long count);

（7）读写一串长字。

void insl(unsigned port, void *addr, unsigned long count); 
 
 void outsl(unsigned port, void *addr, unsigned long count);

上述各函数中I/O端口号port的类型高度依赖于具体的硬件平台，因此，只是写出了unsigned。

#### 2．I/O内存

在内核中访问I/O内存之前，需首先使用ioremap()函数将设备所处的物理地址映射到虚拟地址。ioremap()的原型如下：

void *ioremap(unsigned long offset, unsigned long size);

ioremap()与vmalloc()类似，也需要建立新的页表，但是它并不进行vmalloc()中所执行的内存分配行为。ioremap()返回一个特殊的虚拟地址，该地址可用来存取特定的物理地址范围。通过ioremap()获得的虚拟地址应该被iounmap()函数释放，其原型如下：

void iounmap(void * addr);

在设备的物理地址被映射到虚拟地址之后，尽管可以直接通过指针访问这些地址，但是可以使用Linux内核的如下一组函数来完成设备内存映射的虚拟地址的读写，这些函数如下所示。

（1）读I/O内存。

unsigned int ioread8(void *addr); 
 
 unsigned int ioread16(void *addr); 
 
 unsigned int ioread32(void *addr);

与上述函数对应的较早版本的函数为（这些函数在Linux 2.6中仍然被支持）：

unsigned readb(address); 
 
 unsigned readw(address); 
 
 unsigned readl(address);

（2）写I/O内存。

void iowrite8(u8 value, void *addr); 
 
 void iowrite16(u16 value, void *addr); 
 
 void iowrite32(u32 value, void *addr);

与上述函数对应的较早版本的函数为（这些函数在Linux 2.6中仍然被支持）：

void writeb(unsigned value, address); 
 
 void writew(unsigned value, address); 
 
 void writel(unsigned value, address);

（3）读一串I/O内存。

void ioread8_rep(void *addr, void *buf, unsigned long count); 
 
 void ioread16_rep(void *addr, void *buf, unsigned long count); 
 
 void ioread32_rep(void *addr, void *buf, unsigned long count);

（4）写一串I/O内存。

void iowrite8_rep(void *addr, const void *buf, unsigned long count); 
 
 void iowrite16_rep(void *addr, const void *buf, unsigned long count); 
 
 void iowrite32_rep(void *addr, const void *buf, unsigned long count);

（5）复制I/O内存。

void memcpy_fromio(void *dest, void *source, unsigned int count); 
 
 void memcpy_toio(void *dest, void *source, unsigned int count);

（6）设置I/O内存。

void memset_io(void *addr, u8 value, unsigned int count);

#### 3．把I/O端口映射到内存空间

void *ioport_map(unsigned long port, unsigned int count);

通过这个函数，可以把port开始的count个连续的I/O端口重映射为一段“内存空间”。然后就可以在其返回的地址上像访问I/O内存一样访问这些I/O端口。当不再需要这种映射时，需要调用下面的函数来撤销。

void ioport_unmap(void *addr);

实际上，分析ioport_map()的源代码可发现，映射到内存空间行为实际上是给开发人员制造的一个“假象”，并没有映射到内核虚拟地址，仅仅是为了让工程师可使用统一的I/O内存访问接口访问I/O端口。

