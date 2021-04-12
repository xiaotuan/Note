### 6.2.1 Lua语法

> 前面提到过在Lua中只有 `nil` 和 `false` 才是假，其余值，包括空字符串和 `0` ，都被认为是真值。这是一个容易出问题的地方，比如Redis的 `EXISTS` 命令返回值 `1` 和 `0` 分别表示存在或不存在，但下面的代码无论  `EXISTS` 命令的结果是 `1` 还是 `0` ， `exists`  变量的值都是  `true` ：
> 所以需要将 `redis.call('exists', 'key')` 改写成  `redis.call('exists', 'key') == 1`  才正确。

Redis使用Lua 5.1版本，所以本书介绍的Lua语法基于此版本。本节不会完整地介绍Lua语言中的所有要素，而是只着重介绍编写Redis脚本会用到的部分，对Lua语言感兴趣的读者推荐阅读Lua作者Roberto Ierusalimschy写的*Programming in Lua*这本书。

```shell
 if redis.call('exists', 'key') then
   exists = true
 else
   exists = false
 end

```

#### 1．数据类型

Lua是一个动态类型语言，一个变量可以存储任何类型的值。编写Redis脚本时会用到的类型如表6-1所示。

<center class="my_markdown"><b class="my_markdown">表6-1 Lua常用数据类型</b></center>

| 类 型 名 | 取　　值 |
| :-----  | :-----  | :-----  | :-----  |
| 空（nil） | 空类型只包含一个值，即 `nil` 。 `nil` 表示空，所有没有赋值的变量或表的字段都是 `nil` |
| 布尔（boolean） | 布尔类型包含 `true` 和 `false` 两个值 |
| 数字（number） | 整数和浮点数都是使用数字类型存储，如 `1、0.2、3.5e20` 等 |
| 字符串（string） | 字符串类型可以存储字符串，且与Redis的键值一样都是二进制安全的。字符串可以使用单引号或双引号表示，两个符号是相同的。比如 `'a'` ， `"b"` 都是可以的。字符串中可以包含转义字符，如 `\n` 、 `\r` 等 |
| 表（table） | 表类型是Lua语言中唯一的数据结构，既可以当数组又可以当字典，十分灵活 |
| 函数（function） | 函数在Lua中是一等值（first-class value），可以存储在变量中、作为函数的参数或返回结果 |

#### 2．变量

Lua的变量分为全局变量和局部变量。全局变量无须声明就可以直接使用，默认值是 `nil` 。如：

```shell
a = 1　　   -- 为全局变量a赋值
print(b)    -- 无需声明即可使用，默认值是nil
a = nil　　   -- 删除全局变量a的方法是将其赋值为nil。全局变量没有声明和未声明之分，只有非nil和nil的区别

```

在Redis脚本中不能使用全局变量，只允许使用局部变量以防止脚本之间相互影响。声明局部变量的方法为 `local` 变量名，就像这样：

```shell
local c　　   -- 声明一个局部变量c，默认值是nil
local d = 1 -- 声明一个局部变量d并赋值为1
local e, f  -- 可以同时声明多个局部变量

```

同样声明一个存储函数的局部变量的方法为：

```shell
local say_hi = function ()
　　print 'hi'
end

```

变量名必须是非数字开头，只能包含字母、数字和下划线，区分大小写。变量名不能与Lua的保留关键字相同，保留关键字如下：

```shell
and　　   break    do　　   else　　   elseif
end　　   false    for　　  function   if
in　　    local    nil　　  not　　    or
repeat   return   then　　 true　　   until　　 while

```

局部变量的作用域为从声明开始到所在层的语句块末尾，比如：

```shell
local x = 10
if true then
　　local x = x + 1
　　print(x)
　　do
　　　　local x = x + 1
　　　　print(x)
　　end
　　print(x)
end
print(x)

```

打印结果为：

```shell
11
12
11
10

```

#### 3．注释

Lua的注释有单行和多行两种。

单行注释以 `--` 开始，到行尾结束，在上面的代码已经使用过了，一般习惯在 `--` 后面跟上一个空格。

多行注释以 `--[[` 开始，到 `]]` 结束，如：

```shell
--[[

```

```shell
这是一个多行注释

```

```shell
]]

```

#### 4．赋值

Lua支持多重赋值，比如：

```shell
local a, b = 1, 2　　 -- a的值是1，b的值是2
local c, d = 1, 2, 3  -- c的值是1，d的值是2，3被舍弃了
local e, f = 1　　　　 -- e的值是1，f的值是nil

```

在执行多重赋值时，Lua会先计算所有表达式的值，比如

```shell
local a = {1, 2, 3}
local i = 1
i, a[i] = i + 1, 5

```

Lua计算所有表达式的值后，上面最后一个赋值语句变为 `i, a[1] = 2, 5` ，所以赋值后 `i` 的值为 `2` ， `a` 则为 `{5, 2, 3}` 3。

3 Lua的表类型索引是从1开始的，后文会介绍。

Lua中函数也可以返回多个值，后面会讲到。

#### 5．操作符

Lua有以下5类操作符。

（1）数学操作符。数学操作符包括常见的 `+` 、 `-` 、 `*` 、 `/` 、 `%` （取模）、 `-` （一元操作符，取负）和幂运算符号 `^` 。

数学操作符的操作数如果是字符串会自动转换成数字，比如：

```shell
print('1' + 1)　　    -- 2
print('10' * 2)　　   -- 20

```

（2）比较操作符。Lua的比较操作符如表6-2所示。

<center class="my_markdown"><b class="my_markdown">表6-2 Lua的比较操作符</b></center>

| 操 作 符 | 说　　明 |
| :-----  | :-----  | :-----  | :-----  |
| `==` | 比较两个操作数的类型和值是否都相等 |
| `~=` | 与 `==` 的结果相反 |
| `< ， > ， <= ， >=` | 小于、大于、小于等于、大于等于 |

比较操作符的结果一定是布尔类型。比较操作符不同于数学操作符，不会对两边的操作数进行自动类型转换，也就是说：

```shell
print(1 == '1')　　　　  -- false, 二者类型不同，不会进行自动类型转换
print({'a'} == {'a'})    -- false, 对于表类型值比较的是二者的引用

```

如果需要比较字符串和数字，可以手动进行类型转换。比如下面两个结果都是 `true` ：

```shell
print(1 == tonumber('1'))
print('1' == tostring(1))

```

其中 `tonumber` 函数还可以进行进制转换，比如：

```shell
print(tonumber('F', 16))  -- 将字符串'F'从16进制转成10进制结果是15

```

（3）逻辑操作符。Lua的逻辑操作符如表6-3所示。

<center class="my_markdown"><b class="my_markdown">表6-3 Lua的逻辑操作符</b></center>

| 操 作 符 | 说　　明 |
| :-----  | :-----  | :-----  | :-----  |
| `not` | 根据操作数的真和假相应地返回 `false` 和 `true` |
| `and` | `a and b` 中如果 `a` 是真则返回 `b` ，否则返回 `a` |
| `or` | `a or b` 中如果 `a` 是假则返回 `a` ，否则返回 `b` |

只要操作数不是 `nil` 或 `false` ，逻辑操作符就认为操作数是真，否则是假。特别需要注意的是即使是 `0` 或空字符串也被当作真（Ruby开发者肯定会比较适应这一点）。下面是几个逻辑操作符的例子：

```shell
print(1 and 5)　　　　 -- 5
print(1 or 5)　　　　 -- 1
print(not 0)　　　　   -- false
print('' or 1)　　　　 -- ''

```

Lua的逻辑操作符支持短路，也就是说对于 `false and foo()` ，Lua不会调用 `foo` 函数，因为第一个操作数已经决定了无论 `foo` 函数返回的结果是什么，该表达式的值都是 `false` 。 `or` 操作符与之类似。

（4）连接操作符。连接操作符只有一个： `..` ，用来连接两个字符串，比如：

```shell
print('hello' .. ' ' .. 'world!')    -- 'hello world!'

```

连接操作符会自动把数字类型的值转换成字符串类型：

```shell
print('The price is ' .. 25)　　　　  -- 'The price is 25'

```

（5）取长度操作符。取长度操作符是Lua 5.1中新增加的操作符，同样只有一个，即 `#` ，用来获取字符串或表的长度：

```shell
print(#'hello')　　　　　　 -- 5

```

各个运算符的优先级顺序如表6-4所示。

<center class="my_markdown"><b class="my_markdown">表6-4 运算符的优先级（优先级依次降低）</b></center>

| `^` |
| :-----  | :-----  | :-----  |
| `not # -` （一元） |
| `* / %` |
| `+ -` |
| `..` |
| `< > <= >= ~= ==` |
| `and` |
| `or` |

#### 6． **if** 语句

Lua的 `if` 语句格式如下：

```shell
if 条件表达式 then
  语句块
elseif 条件表达式 then
  语句块
else
  语句块
end

```

注意

Lua与JavaScript一样每个语句都可以 `;` 结尾，但一般来说编写Lua时都会省略 `;` （Lua的作者也是这样做的）。Lua也并不强制要求缩进，所有语句也可以写在一行中，比如：

```shell
a = 1
b = 2
if a then
  b = 3
else
  b = 4
end

```

可以写成

```shell
a = 1 b = 2 if a then b = 3 else b = 4 end

```

甚至如下代码也是正确的：

```shell
a = 
1 b = 2 if a
then b = 3 else b
= 4 end

```

但为了增强可读性，在编写的时候一定要注意缩进。

#### 7．循环语句

Lua支持 `while、repeat` 和 `for` 循环语句。

`while` 语句的形式为：

```shell
while 条件表达式 do
　　语句块
end

```

`repeat` 语句的形式为：

```shell
repeat
　　语句块
until 条件表达式

```

`for` 语句有两种形式，一种是数字形式：

```shell
for 变量 = 初值, 终值, 步长 do
　　语句块
end

```

其中步长可以省略，默认步长为1。例如，使用 `for` 循环计算1～100的和：

```shell
local sum = 0
for i = 1, 100 do
　　sum = sum + i
end

```

提示

> for语句中的循环变量（即本例中的 `i` ）是局部变量，作用域为 `for` 循环体内。虽然没有使用 `local` 声明，但它不是全局变量。

`for` 语句的通用形式为：

```shell
for 变量1, 变量2, ..., 变量N in 迭代器 do
　　语句块
end

```

在编写Redis脚本时我们常用通用形式的 `for` 语句遍历表的值，下面还会再介绍。

#### 8．表类型

表是Lua中唯一的数据结构，可以理解为关联数组，任何类型的值（除了空类型）都可以作为表的索引。

表的定义方式为：

```shell
a = {}　　　　　　　　 -- 将变量a赋值为一个空表
a['field'] = 'value' -- 将field字段赋值value
print(a.field)　　　　 -- 打印内容为'value'，a.field是a['field']的语法糖
people = {　　　　　　 -- 也可以这样定义
  name = 'Bob',
  age = 29
}
print(people.name)    -- 打印的内容为'Bob'

```

当索引为整数的时候表和传统的数组一样，例如：

```shell
a = {}
a[1] = 'Bob'
a[2] = 'Jeff'

```

可以写成下面这样：

```shell
a = {'Bob', 'Jeff'}
print(a[1])　　　　　　　　 -- 打印的内容为'Bob'

```

注意

> Lua约定数组4的索引是从1开始的，而不是0。

4此处的数组指的是数组形式的表类型，即索引为从1开始的递增整数。

可以使用通用形式的 `for` 语句遍历数组，例如：

```shell
for index, value in ipairs(a) do
　　 print(index)　　　　　　-- index迭代数组a的索引
　　 print(value)　　　　　　-- value迭代数组a的值
end

```

打印的结果是：

```shell
1
Bob
2
Jeff

```

`ipairs` 是Lua内置的函数，实现类似迭代器的功能。当然还可以使用数字形式的 `for` 语句遍历数组，例如：

```shell
for i = 1, #a do
　　 print(i)
　　 print(a[i])
end

```

输出的结果和上例相同。 `#a` 的作用是获取表 `a` 的长度。

Lua还提供了一个迭代器 `pairs` ，用来遍历非数组的表值，例如：

```shell
people = {
  name = 'Bob',
  age = 29
}
for index, value in pairs(people) do
　　print(index)
　　print(value)
end

```

打印结果为：

```shell
name
Bob
age
29

```

`pairs` 与 `ipairs` 的区别在于前者会遍历所有值不为 `nil` 的索引，而后者只会从索引1开始递增遍历到最后一个值不为 `nil` 的整数索引。

#### 9．函数

函数的定义为：

```shell
function (参数列表)
　　函数体
end

```

可以将其赋值给一个局部变量，比如：

```shell
local square = function (num)
　　return num * num
end

```

如果没有参数，括号也不能省略。Lua还提供了一个语法糖来简化函数的定义，比如：

```shell
local function square (num)
　　return num * num
end

```

这段代码会被转换为：

```shell
local square
square = function (num)
　　return num * num
end

```

因为在赋值前声明了局部变量 `square` ，所以可以在函数内部引用自身（实现递归）。

如果实参的个数小于形参的个数，则没有匹配到的形参的值为 `nil` 。相对应的，如果实参的个数大于形参的个数，则多出的实参会被忽略。如果希望捕获多出的实参（即实现可变参数个数），可以让最后一个形参为 `...` 。比如，希望传入若干个参数计算这些数的平方：

```shell
local function square (...)
　　local argv = {...}
　　for i = 1, #argv do
　　　　argv[i] = argv[i] * argv[i]
　　end
　　return unpack(argv)
end
a, b, c = square(1, 2, 3)
print(a)
print(b)
print(c)

```

输出结果为：

```shell
1
4
9

```

在第二个 `square` 函数中，我们首先将 `...` 转换为表 `argv` ，然后对表的每个元素计算其平方值。 `unpack` 函数用来返回表中的元素，在上例中 `argv` 表中有 3 个元素，所以 `return unpack(argv)` 相当于 `return argv[1], argv[2], argv[3]` 。

在Lua中 `return` 和 `break` （用于跳出循环）语句必须是语句块中的最后一条语句，简单地说在这两条语句后面只能是 `end``，``else` 或 `until` 三者之一。如果希望在语句块的中间使用这两条语句的话可以人为地使用 `do` 和 `end` 将其包围。

