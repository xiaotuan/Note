### 3.5.2 GNU C与ANSI C

Linux上可用的C编译器是GNU C编译器，它建立在自由软件基金会的编程许可证的基础上，因此可以自由发布。GNU C对标准C进行一系列扩展，以增强标准C的功能。

#### 1．零长度和变量长度数组

GNU C允许使用零长度数组，在定义变长对象的头结构时，这个特性非常有用。例如：

struct var_data { 
 
 int len; 
 
 char data[0]; 
 
 };

char data[0]仅仅意味着程序中通过var_data结构体实例的data[index]成员可以访问len之后的第index个地址，它并没有为data[]数组分配内存，因此sizeof(struct var_data)=sizeof(int)。

假设struct var_data的数据域就保存在struct var_data紧接着的内存区域，则通过如下代码可以遍历这些数据：

struct var_data s; 
 
 ... 
 
 for (i = 0; i < s.len; i++) 
 
 printf("%02x", s.data[i]);

GNU C中也可以使用1个变量定义数组，例如如下代码中定义的“double x[n]”：

int main (int argc, char *argv[]) 
 
 { 
 
 int i, n = argc; 
 
 double x[n];

for (i = 0; i < n; i++) 
 
 x[i] = i;

return 0; 
 
 }

#### 2．case范围

GNU C支持case x…y这样的语法，区间[x,y]的数都会满足这个case的条件，请看下面的代码：

switch (ch) { 
 
 case '0'... '9': c -= '0'; 
 
 break; 
 
 case 'a'... 'f': c -= 'a' - 10; 
 
 break; 
 
 case 'A'... 'F': c -= 'A' - 10; 
 
 break; 
 
 }

代码中的case '0'... '9'等价于标准C中的：

case '0': case '1': case '2': case '3': case '4': 
 
 case '5': case '6': case '7': case '8': case '9':



#### 3．语句表达式

GNU C把包含在括号中的复合语句看做是一个表达式，称为语句表达式，它可以出现在任何允许表达式的地方。我们可以在语句表达式中使用原本只能在复合语句中使用的循环、局部变量等，例如：

#define min_t(type,x,y) \ 
 
 ({ type __x = (x); type __y = (y); __x < __y ? __x: __y; }) 
 
 int ia, ib, mini; 
 
 float fa, fb, minf; 
 
 mini = min_t(int, ia, ib); 
 
 minf = min_t(float, fa, fb);

因为重新定义了_ _xx和_ _y这两个局部变量，所以以上述方式定义的宏将不会有副作用。在标准C中，对应的如下宏则会产生副作用：

#define min(x,y) ((x) < (y) ? (x) : (y))

代码min(++ia,++ib)会被展开为((++ia) < (++ib) ? (++ia): (++ib))，传入宏的“参数”被增加2次。

#### 4．typeof关键字

typeof(x)语句可以获得x的类型，因此，我们可以借助typeof重新定义min这个宏：

#define min(x,y) ({ \ 
 
 const typeof(x) _x = (x); \ 
 
 const typeof(y) _y = (y); \ 
 
 (void) (&_x == &_y); \ 
 
 _x < _y ? _x : _y; })

我们不需要像min_t(type,x,y)这个宏那样把type传入，因为通过typeof(x)、typeof(y)可以获得type。代码行(void) (&_x == &_y)的作用是检查_x和_y的类型是否一致。

#### 5．可变参数宏

标准C就支持可变参数函数，意味着函数的参数是不固定的，例如printf()函数的原型为：

int printf( const char *format [, argument]... );

而在 GNU C中，宏也可以接受可变数目的参数，例如：

#define pr_debug(fmt,arg...) \ 
 
 printk(fmt,##arg)

这里arg表示其余的参数，可以是零个或多个，这些参数以及参数之间的逗号构成arg的值，在宏扩展时替换arg，例如下列代码：

pr_debug("%s:%d",filename,line)

会被扩展为：

printk("%s:%d", filename, line)

使用“##”的原因是处理arg不代表任何参数的情况，这时候，前面的逗号就变得多余了。使用“##”之后，GNU C预处理器会丢弃前面的逗号，这样，代码：

pr_debug("success!\n")

会被正确地扩展为：

printk("success!\n")

而不是：

printk("success!\n",)

这正是我们希望看到的。



#### 6．标号元素

标准C要求数组或结构体的初始化值必须以固定的顺序出现，在GNU C中，通过指定索引或结构体成员名，允许初始化值以任意顺序出现。

指定数组索引的方法是在初始化值前添加“[INDEX] =”，当然也可以用“[FIRST ... LAST] =”的形式指定一个范围。例如，下面的代码定义一个数组，并把其中的所有元素赋值为0：

unsigned char data[MAX] = { [0 ... MAX-1] = 0 };

下面的代码借助结构体成员名初始化结构体：

struct file_operations ext2_file_operations = { 
 
 llseek: generic_file_llseek, 
 
 read: generic_file_read, 
 
 write: generic_file_write, 
 
 ioctl: ext2_ioctl, 
 
 mmap: generic_file_mmap, 
 
 open: generic_file_open, 
 
 release: ext2_release_file, 
 
 fsync: ext2_sync_file, 
 
 };

但是，Linux 2.6推荐类似的代码应该尽量采用标准C的方式：

struct file_operations ext2_file_operations = { 
 
 .llseek = generic_file_llseek, 
 
 .read = generic_file_read, 
 
 .write = generic_file_write, 
 
 .aio_read = generic_file_aio_read, 
 
 .aio_write = generic_file_aio_write, 
 
 .ioctl = ext2_ioctl, 
 
 .mmap = generic_file_mmap, 
 
 .open = generic_file_open, 
 
 .release = ext2_release_file, 
 
 .fsync = ext2_sync_file, 
 
 .readv = generic_file_readv, 
 
 .writev = generic_file_writev, 
 
 .sendfile = generic_file_sendfile, 
 
 };

#### 7．当前函数名

GNU C预定义了两个标志符保存当前函数的名字，_ _FUNCTION_ _保存函数在源码中的名字，_ _PRETTY_FUNCTION_ _保存带语言特色的名字。在C函数中，这两个名字是相同的。

void example() 
 
 { 
 
 printf("This is function:%s", _ _FUNCTION_ _); 
 
 }

代码中的_ _FUNCTION_ _意味着字符串“example”。C99已经支持_ _func_ _宏，因此建议在Linux编程中不再使用_ _FUNCTION_ _，而转而使用_ _func_ _：

void example() 
 
 { 
 
 printf("This is function:%s", _ _func_ _); 
 
 }

#### 8．特殊属性声明

GNU C允许声明函数、变量和类型的特殊属性，以便进行手工的代码优化和定制代码检查的方法。要指定一个声明的属性，只需要在声明后添加_ _attribute_ _ (( ATTRIBUTE ))。其中ATTRIBUTE为属性说明，如果存在多个属性，则以逗号分隔。GNU C支持noreturn、format、section、aligned、packed等十多个属性。

noreturn属性作用于函数，表示该函数从不返回。这会让编译器优化代码，并消除不必要的警告信息。例如：

# define ATTRIB_NORET _ _attribute_ _((noreturn)) .... 
 
 asmlinkage NORET_TYPE void do_exit(long error_code) ATTRIB_NORET;

format属性也用于函数，表示该函数使用printf、scanf或strftime风格的参数，指定format属性可以让编译器根据格式串检查参数类型。例如：

asmlinkage int printk(const char * fmt, ...) _ _attribute_ _ ((format (printf, 1, 2)));

上述代码中的第1个参数是格式串，从第2个参数开始都会根据printf()函数的格式串规则检查参数。

unused属性作用于函数和变量，表示该函数或变量可能不会被用到，这个属性可以避免编译器产生警告信息。

aligned属性用于变量、结构体或联合体，指定变量、结构体或联合体的对界方式，以字节为单位，例如：

struct example_struct { 
 
 char a; 
 
 int b; 
 
 long c; 
 
 } _ _attribute_ _((aligned(4)));

表示该结构类型的变量以4字节对界。

packed属性作用于变量和类型，用于变量或结构体成员时表示使用最小可能的对界，用于枚举、结构体或联合体类型时表示该类型使用最小的内存。例如：

struct example_struct { 
 
 char a; 
 
 int b; 
 
 long c _ _attribute_ _((packed)); 
 
 };

![BZ___95_134_1002_211_1079.png](../images/BZ___95_134_1002_211_1079.png)
编译器对结构体成员及变量对界的目的是为了更快地访问结构体成员及变量占据的内存。例如，对于一个32位的整型变量，若以4字节方式存放（即低两位地址为00），则CPU在一个总线周期内就可以读取32位；若不然，CPU需要两次总线周期才能组合为一个32位整型。

#### 9．内建函数

GNU C提供了大量的内建函数，其中大部分是标准C库函数的GNU C编译器内建版本，例如memcpy()等，它们与对应的标准C库函数功能相同。

不属于库函数的其他内建函数的命名通常以_ _builtin开始，如下所示。

● 内建函数_ _builtin_return_address (LEVEL)返回当前函数或其调用者的返回地址，参数LEVEL 指定调用栈的级数，如0表示当前函数的返回地址，1表示当前函数的调用者的返回地址。

● 内建函数_ _builtin_constant_p(EXP)用于判断一个值是否为编译时常数，如果参数EXP的值是常数，函数返回1，否则返回0。

● 内建函数_ _builtin_expect(EXP, C)用于为编译器提供分支预测信息，其返回值是整数表达式EXP的值，C的值必须是编译时常数。

例如，下面的代码检测第1个参数是否为编译时常数以确定采用参数版本还是非参数版本的代码：

#define test_bit(nr,addr) \ 
 
 (_ _builtin_constant_p(nr) ? \ 
 
 constant_test_bit((nr),(addr)) : \ 
 
 variable_test_bit((nr),(addr)))

在使用gcc编译C程序的时候，如果使用“-ansi –pedantic”编译选项，则会告诉编译器不使用GNU扩展语法。例如对于如下C程序test.c：

struct var_data { 
 
 int len; 
 
 char data[0]; 
 
 };

struct var_data a;

直接编译可以通过：

gcc -c test.c

如果使用“-ansi –pedantic”编译选项，编译会报警：

gcc -ansi -pedantic -c test.c 
 
 test.c:3: warning: ISO C forbids zero-size array ‘data’

