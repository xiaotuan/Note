[toc]

### 1. Makefile 规则格式

`Makefile` 里面是由一系列的规则组成的，这些规则格式如下：

```
目标......：依赖文件集合......
	命令1
	命令2
	......
```

例如：

```makefile
main: main.o input.o calcu.o
	gcc -o main main.o input.o, calcu.o
```

我们以下面的示例为例来分析 `Makefile` 的用法：

```makefile
main: main.o input.o calcu.o
	gcc -o main main.o input.o calcu.o
main.o: main.c
	gcc -c main.c
input.o: input.c
	gcc -c input.c
calcu.o: calcu.c
	gcc -c calcu.c

clean:
	rm *.o
	rm main
```

`make` 命令在执行这个 `Makefile` 的时候其执行步骤如下：

首先更新第一条规则中的 `main`，第一条规则的目标成为默认目标，只要默认目标更新了那么就认为 `Makefile` 的工作。在第一次编译的时候由于 `main` 还不存在，因此第一条规则会执行，第一条规则依赖于文件 `main.o`、`input.o` 和 `calcu.o` 这三个 `.o` 文件，这三个 `.o` 文件目前还都没有，因此必须先更新这三个文件。`make` 会查找以这三个 `.o` 文件为目标的规则并执行。以 `main.o` 为例，发现更新 `main.o` 的是第二条规则，因此会执行第二条规则，第二条规则里面的命令为 `gcc -c main.c`。最后一个规则目标是 `clean`，它没有依赖文件，因此会默认为依赖文件都是最新的，所以其对应的命令不会执行，当我们想要执行 `clean` 的话可以直接使用命令 `make clean`。

我们再来总结一下 `Make` 的执行过程：

1. `make` 命令会在当前目录下查找以 `Makefile`（`makefile` 其实也可以）命名的文件。
2. 当找到 `Makefile` 文件以后就会按照 `Makefile` 中定义的规则去编译生成最终的目标文件。
3. 当发现目标文件不存在，或者目标所依赖的文件比目标文件新（也就是最后修改时间比目标文件晚）的话就会执行后面的命令来更新目标。

除了 `Makefile` 的 “终结目标” 所在的规则以外，其他规则的顺序在 `Makefile` 中是没有意义的，“终极目标” 就是指在使用 `make` 命令的时候没有指定具体的目标时，`make` 默认的那个目标，它是 `Makefile` 文件中第一个规则的目标，如果 `Makefile` 中的第一个规则有多个目标，那么这些目标中的第一个目标就是 `make` 的 “终极目标”。

### 2. Makefile 变量

跟 C 语言一样 `Makefile` 也支持变量的，先看一下前面的例子：

```makefile
main: main.o input.o calcu.o
	gcc -o main main.o input.o calcu.o
```

不像 C 语言中的变量有 `int`、`char` 等各种类型，`Makefile` 中的变量都是字符串！类似 C 语言中的宏。使用变量将上面的代码修改以后如下所示：

```makefile
# Makefile 变量的使用
objects = main.o input.o calcu.o
make: $(objects)
	gcc -o main $(objects)
```

第一行是注释，`Makefile` 中可以写注释，注释开头要用符号 `#`。第二行我们定义了一个变量 `objects`，并且给这个变量进行了赋值，其值为字符串 `main.o input.o calcu.o`，第三行和第四行使用到了变量 `objects`，`Makefile` 中变量的引用方法是 `$(变量名)`，比如本例中的 `$(objects)`。

在上面示例代码中定义变量 `objects` 的时候使用 `=` 对其进行了赋值，`Makefile` 变量的赋值符还有其他两个 `:=` 和 `?=`，我们来看一下这三种赋值符的区别：

**1. 赋值符 "="**

使用 `=` 在给变量的赋值的时候，不一定使用已经定义好的值，也可以使用后面定义的值，比如如下代码：

```makefile
name = zzk
curname = $(name)
name = zouzhongkai

print:
	@echo curname: $(curname)
```

运行结果如下：

```shell
$ make
curname: zouzhongkai
```

在 `Makefile` 要输出一串字符的话使用 `echo`，第 6 行中的 `echo` 前面加了个 `@` 符号，因为 `Make` 在执行的过程中会自动输出命令执行过程，在命令前面加上 `@` 的会就不会输出命令执行过程。

可以看到 `curname` 的值不是 `zzk`，竟然是 `zuozhongkai`，也就是变量 `name` 最后一次赋值的结果，这就是赋值符 `=` 的神奇之处！借助另外一个变量，可以将变量的真实值推到后面去定义。也就是变量的真实值取决于它所引用的变量的最后一次有效值。

**2. 赋值符 ":="**

将上面示例代码中的 `=` 改为 `:=`，修改完成以后的代码如下：

```makefile
name = zzk
curname := $(name)
name = zouzhongkai

print:
	@echo curname: $(curname)
```

运行效果如下：

```shell
$ make
curname: zzk
```

可以看到此时的 `curname` 是 `zzk`，不是 `zuozhongkai` 了。这是因为赋值符 `:=` 不会使用后面定义的变量，只能使用前面已经定义好的。

**3. 赋值符 "?="**

`?=` 是一个很有用的赋值符，比如下面这行代码：

```makefile
curname ?= zouzhongkai
```

上述代码的意思就是，如果变量 `curname` 前面没有被赋值，那么次变量就是 `zouzhongkai`，如果前面已经赋过值了，那么就使用前面的值。

**4. 变量追加 "+="**

`Makefile` 中的变量是字符串，有时候我们需要给前面已经定义好的变量添加一些字符串进去，此时就要使用到符号 `+=`，比如如下代码：

```makefile
objects = main.o input.o
objects += calcu.o
```

### 3. Makefile 模式规则

我们以下面例子为例：

```makefile
main: main.o input.o calcu.o
	gcc -o main main.o input.o calcu.o
main.o: main.c
	gcc -c main.c
input.o: input.c
	gcc -c input.c
calcu.o: calcu.c
	gcc -c calcu.c

clean:
	rm *.o
	rm main
```

上述 `Makefile` 中第 3 ~ 8 行是将对应的 `.c` 源文件编译为 `.o` 文件，每一个 `C` 文件都要写一个对应的规则，如果工程中 `C` 文件很多的话显然不能这么做。为此，我们可以使用 `Makefile` 中的模式规则，通过模式规则我们就可以使用一条规则来将所有的 `.c` 文件编译为对应的 `.o` 文件。

模式规则中，至少在规则的目标定义中药包含 `%`，否则就是一般规则，目标中的 `%` 表示对文件名的匹配，`%` 表示长度任意的非空字符串，比如 `%.c` 就是所有以 `.c` 结尾的文件。

当 `%` 出现在目标中的时候，目标中 `%` 所代表的值决定了依赖中的 `%` 值，使用方法如下：

```makefile
%.o: %.c
	命令
```

因此，上面的示例可以修改为如下形式：

```makefile
objects = main.o input.o calcu.o
main: $(objects)
	gcc -o main $(objects)
%.o: %.c
	# 命令

clean:
	rm *.o
	rm main
```

上面的 `Makefile` 还不能运行，因为第 6 行的命令我们还没写，第 6 行的命令我们需要借助另外一种强大的变量——自动变量。

### 4. Makefile 自动变量

所谓自动化变量就是把模式中所定义的一系列的文件自动的挨个取出，直至所有的复合模式的文件都取完，自动化变量只应该出现在规则的命令中，常用的自动化变量如下：

| 自动化变量 | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| `$@`       | 规则中的目标集合，在模式规则中，如果有多个目标的话，`$@` 表示匹配模式中定义的目标集合 |
| `$%`       | 当目标是函数库的时候表示规则中的目标成员名，如果目标不是函数库文件，那么其值为空。 |
| `$<`       | 依赖文件集合中的第一个文件，如果依赖文件是以模式（即 `%`）定义的，那么 `$<` 就是复合模式的一系列的文件集合。 |
| `$?`       | 所有比目标新的依赖目标集合，以空格分开。                     |
| `$^`       | 所有依赖文件的集合，使用空格分开，如果在依赖文件中有多个重复的文件，`$^` 会去除重复的依赖文件，值保留一份。 |
| `$+`       | 和 `$^` 类似，但是当依赖文件存在重复的话不会去除重复的依赖文件。 |
| `$*`       | 这个变量表示目标模式中 `%` 及其之前的部分，如果目标是 `test/a.test.c`，目标模式为 `a.%.c`，那么 `$*` 就是 `test/a.test`。 |

自动化变量中，常用的三种：`$@`、`$<` 和 `$^`，我们使用自动化变量来完成上面示例中的 `Makefile`，最终的代码如下：

```makefile
objects = main.o input.o calcu.o
main: $(objects)
	gcc -o main $(objects)
%.o: %.c
	gcc -c $<

clean:
	rm *.o
	rm main
```

### 5. Makefile 伪目标

`Makefile` 有一种特殊的目标——伪目标，一般的目标名都是要生成的文件，而伪目标不代表真正的目标名，在执行 `make` 命令的时候通过指定这个伪目标来执行其所在规则的定义的命令。

使用伪目标主要是为了避免 `Makefile` 中定义的执行命令的目标和工作目录下的实际文件出现名字冲突，有时候我们需要编写一个规则用来执行一些命令，但是这个规则不是用来创建文件的，例如：

```makefile
clean:
	rm *.o
	rm main
```

上述规则中并没有创建文件 `clean` 的命令，因此工作目录下永远都不会存在文件 `clean`，当我们输入 `make clean` 以后，后面的 `rm *.o` 和 `rm main` 总是会执行。可是如果我们在工作目录下创建一个名为 `clean` 的文件，那就不一样了，当执行 `make clean` 的时候，规则因为没有依赖文件，所以目标被认为是最新的，因此后面的 `rm` 命令也不会执行。为了避免这个问题，我们可以将 `clean` 声明为伪目标，声明方式如下：

```makefile
.PHONY: clean
```

例如：

```makefile
objects = main.o input.o calcu.o
main: $(objects)
	gcc -o main $(objects)
	
.PHONY : clean

%.o: %.c
	gcc -c $<

clean:
	rm *.o
	rm main
```

声明 `clean` 为伪目标以后不管当前目录下是否存在名为 `clean` 的文件，输入 `make clean` 的话规则后面的 `rm` 命令都会执行。

### 6. Makefile 条件判断

`Makefile` 条件判断语法有两种：

```makefile
<条件关键字>
	<条件为真时执行的语句>
endif
```

以及：

```makefile
<条件关键字>
	<条件为真时执行的语句>
else
	<条件为假时执行的语句>
endif
```

其中条件关键字有 4 个：`ifeq`、`ifneq`、`ifdef` 和 `ifndef`，这四个关键字起始分为两对：`ifeq` 与 `ifneq`、`ifdef` 与 `ifndef`。`ifeq` 用来判断是否相等，`ifneq` 就是判断是否不相等，`ifeq` 用法如下：

```makefile
ifeq (<参数 1>, <参数 2>)
ifeq '<参数 1>', '<参数 2>'
ifeq "<参数 1>", "<参数 2>"
ifeq '<参数 1>', "<参数 2>"
ifeq "<参数 1>", '<参数 2>'
```

`ifdef` 和 `ifndef` 的用法如下：

```makefile
ifdef <变量名>
```

如果 "变量名" 的值非空，那么表示表达式为真，否则表达式为假。

### 7. Makefile 函数使用

`Makefile` 中的函数是已经定义好的，我们直接使用，不支持我们自定义函数，函数的用法如下：

```makefile
$(函数名 参数集合)
```

或者

```makefile
${函数名 参数集合}
```

参数集合是函数的多个参数，参数之间以逗号 `,` 隔开，函数名和参数之间以 "空格" 分隔开，函数的调用以  `$` 开头。

#### 7.1 subst 函数

`subst` 函数用来完成字符串替换，调用形式如下：

```makefile
$(subst <from>,<to>,<text>)
```

此函数的功能是将字符串 `<text>` 中的 `<from>` 内容替换为 `<to>`，函数返回被替换以后的字符串，比如：

```makefile
$(subst zzk,ZZK,my name is zzk)
```

把字符串 "my name is zzk" 中的 "zzk" 替换为 "ZZK"。

##### 7.2 patsubst 函数

`patsubst` 函数用来完成模式字符串替换，使用方法如下：

```makefile
$(patsubst <pattern>,<replacement>,<text>)
```

此函数查找字符串 `<text>` 中的单词是否符合模式 `<pattern>`，如果匹配就用 `<replacement>` 来替换掉，`<pattern>` 可以使用通配符 `%`，表示任意长度的字符串，函数返回值就是替换后的字符串。比如：

```makefile
$(patsubst %.c,%.o,a.c b.c c.c)
```

将字符串 "a.c b.c c.c" 中的所有符合 `%.c` 的字符串，替换为 `%.o`，替换完成以后的字符串为 `a.o b.o c.o`。

#### 7.3 dir 函数

`dir` 函数用来获取目录，使用方法如下：

```makefile
$(dir <names...>)
```

此函数用来从文件名序列 `<names>` 中提取出目录部分，返回值是文件名序列 `<names>` 的目录部分，比如：

```makefile
$(dir /src/a.c)
```

提取文件 `/src/a.c` 的目录部分，也就是 `/src/`。

#### 7.4 notdir 函数

`notdir` 函数的功能是去掉文件中的目录部分，也即使提取文件名，用法如下：

```makefile
$(notdir <names...>)
```

例如：

```makefile
$(notdir /src/a.c)
```

提取文件 `/src/a.c` 中的非目录部分，也就是文件名 `a.c`。

#### 7.5 foreach 函数

`foreach` 函数用来完成循环，用法如下：

```makefile
$(foreach <var>,<list>,<text>)
```

此函数的意思就是把参数 `<list>` 中的单词逐一取出来放到参数 `<var>` 中，然后再执行 `<text>` 所包含的表达式。每次 `<text>` 都会返回一个字符串，循环的过程中，`<text>` 中所包含的每个字符串会以空格隔开，最后当整个循环结束时，`<text>` 所返回的每个字符串所组成的整个字符串将会是函数 `foreach` 函数的返回值。

#### 7.6 wildcard 函数

通配符 `%` 只能在规则中，只有在规则中它才会展开，如果在变量定义和函数使用时，通配符不会自动展开，这个时候就要用到函数 `wildcard`，使用方法如下：

```makefile
$(wildcard PATTERN...)
```

比如：

```makefile
$(wildcard *.c)
```

上面的代码是用来获取当前目录下所有的 `.c` 文件。
