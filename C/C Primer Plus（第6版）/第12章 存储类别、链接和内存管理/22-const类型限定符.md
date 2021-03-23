#### 12.5.1　 `const` 类型限定符

第4章和第10章中介绍过 `const` 。以 `const` 关键字声明的对象，其值不能通过赋值或递增、递减来修改。在ANSI兼容的编译器中，以下代码：

```c
const int nochange;   /* 限定nochange的值不能被修改 */
nochange = 12;        /* 不允许 */
```

编译器会报错。但是，可以初始化 `const` 变量。因此，下面的代码没问题：

```c
const int nochange = 12; /* 没问题 */
```

该声明让 `nochange` 成为只读变量。初始化后，就不能再改变它的值。

可以用 `const` 关键字创建不允许修改的数组：

```c
const int days1[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
```

#### 1．在指针和形参声明中使用 `const` 

声明普通变量和数组时使用 `const` 关键字很简单。指针则复杂一些，因为要区分是限定指针本身为 `const` 还是限定指针指向的值为 `const` 。下面的声明：

```c
const float * pf; /* pf 指向一个float类型的const值 */
```

创建的 `pf` 指向不能被改变的值，而 `pf` 本身的值可以改变。例如，可以设置该指针指向其他 `const` 值。相比之下，下面的声明：

```c
float * const pt; /* pt 是一个const指针 */
```

创建的指针 `pt` 本身的值不能更改。 `pt` 必须指向同一个地址，但是它所指向的值可以改变。下面的声明：

```c
const float * const ptr;
```

表明 `ptr` 既不能指向别处，它所指向的值也不能改变。

还可以把 `const` 放在第3个位置：

```c
float const * pfc; // 与const float * pfc;相同
```

如注释所示，把 `const` 放在类型名之后、*之前，说明该指针不能用于改变它所指向的值。简而言之， `const` 放在*左侧任意位置，限定了指针指向的数据不能改变； `const` 放在*的右侧，限定了指针本身不能改变。

`const` 关键字的常见用法是声明为函数形参的指针。例如，假设有一个函数要调用 `display()` 显示一个数组的内容。要把数组名作为实际参数传递给该函数，但是数组名是一个地址。该函数可能会更改主调函数中的数据，但是下面的原型保证了数据不会被更改：

```c
void display(const int array[], int limit);
```

在函数原型和函数头，形参声明 `const int array[]` 与 `const int`  *  `array` 相同，所以该声明表明不能更改 `array` 指向的数据。

ANSI C库遵循这种做法。如果一个指针仅用于给函数访问值，应将其声明为一个指向 `const` 限定类型的指针。如果要用指针更改主调函数中的数据，就不使用 `const` 关键字。例如，ANSI C中的 `strcat()` 原型如下：

```c
char *strcat(char * restrict s1, const char * restrict s2);
```

回忆一下， `strcat()` 函数在第1个字符串的末尾添加第2个字符串的副本。这更改了第1个字符串，但是未更改第2个字符串。上面的声明体现了这一点。

#### 2．对全局数据使用 `const` 

前面讲过，使用全局变量是一种冒险的方法，因为这样做暴露了数据，程序的任何部分都能更改数据。如果把数据设置为 `const` ，就可避免这样的危险，因此用 `const` 限定符声明全局数据很合理。可以创建 `const` 变量、 `const` 数组和 `const` 结构（结构是一种复合数据类型，将在下一章介绍）。

然而，在文件间共享 `const` 数据要小心。可以采用两个策略。第一，遵循外部变量的常用规则，即在一个文件中使用定义式声明，在其他文件中使用引用式声明（用 `extern` 关键字）：

```c
/* file1.c -- 定义了一些外部const变量 */
const double PI = 3.14159;
const char * MONTHS[12] = { "January", "February", "March", "April", "May", 
                            "June", "July","August", "September", "October",   
                            "November", "December" };
/* file2.c -- 使用定义在别处的外部const变量 */
extern const double PI;
extern const * MONTHS [];
```

另一种方案是，把 `const` 变量放在一个头文件中，然后在其他文件中包含该头文件：

```c
/* constant.h --定义了一些外部const变量*/
static const double PI = 3.14159;
static const char * MONTHS[12] ={"January", "February", "March", "April", "May",
                                 "June", "July","August", "September", "October",
                                 "November", "December"};
/* file1.c --使用定义在别处的外部const变量*/
#include "constant.h"
/* file2.c --使用定义在别处的外部const变量*/
#include "constant.h"
```

这种方案必须在头文件中用关键字 `static` 声明全局 `const` 变量。如果去掉 `static` ，那么在 `file1.c` 和 `file2.c` 中包含 `constant.h` 将导致每个文件中都有一个相同标识符的定义式声明，C标准不允许这样做（然而，有些编译器允许）。实际上，这种方案相当于给每个文件提供了一个单独的数据副本<sup class="my_markdown">[1]</sup>。由于每个副本只对该文件可见，所以无法用这些数据和其他文件通信。不过没关系，它们都是完全相同（每个文件都包含相同的头文件）的 `const` 数据（声明时使用了 `const` 关键字），这不是问题。

头文件方案的好处是，方便你偷懒，不用惦记着在一个文件中使用定义式声明，在其他文件中使用引用式声明。所有的文件都只需包含同一个头文件即可。但它的缺点是，数据是重复的。对于前面的例子而言，这不算什么问题，但是如果 `const` 数据包含庞大的数组，就不能视而不见了。

