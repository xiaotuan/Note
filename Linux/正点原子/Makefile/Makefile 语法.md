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

