### 1.6.1 无操作系统时的LED驱动

在嵌入式系统的设计中，LED一般直接由CPU的GPIO（通用可编程I/O口）控制。GPIO一般由两组寄存器控制，即一组控制寄存器和一组数据寄存器。控制寄存器可设置GPIO口的工作方式为输入或是输出。当引脚被设置为输出时，向数据寄存器的对应位写入1和0会分别在引脚上产生高电平和低电平；当引脚设置为输入时，读取数据寄存器的对应位可获得引脚上的电平为高或低。

在本例子中，我们屏蔽具体CPU的差异，假设在GPIO_REG_CTRL物理地址处的控制寄存器处的第n位写入1可设置GPIO为输出，在地址GPIO_REG_DATA物理地址处的数据寄存器的第n位写入1或0可在引脚上产生高或低电平，则无操作系统的情况下，设备驱动为代码清单1.3。

代码清单1.3 无操作系统时的LED驱动

1 #define reg_gpio_ctrl *(volatile int *)(ToVirtual(GPIO_REG_CTRL)) 
 
 2 #define reg_gpio_data *(volatile int *)(ToVirtual(GPIO_REG_DATA)) 
 
 3 /*初始化LED*/ 
 
 4 void LightInit(void) 
 
 5 { 
 
 6 reg_gpio_ctrl |= (1 << n); /*设置GPIO为输出*/ 
 
 7 } 
 
 8 
 
 9 /*点亮LED*/ 
 
 10 void LightOn(void) 
 
 11 { 
 
 12 reg_gpio_data |= (1 << n); /*在GPIO上输出高电平*/ 
 
 13 } 
 
 14 
 
 15 /*熄灭LED*/ 
 
 16 void LightOff(void) 
 
 17 { 
 
 18 reg_gpio_data &= ～(1 << n); /*在GPIO上输出低电平*/ 
 
 19 }

上述程序中的LightInit()、LightOn()、LightOff()都直接作为驱动提供给应用程序的外部接口函数。程序中ToVirtual()的作用是当系统启动了硬件MMU之后，根据物理地址和虚拟地址的映射关系，将寄存器的物理地址转化为虚拟地址。

