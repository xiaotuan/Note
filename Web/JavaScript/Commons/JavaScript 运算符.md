<center><b>JavaScript 运算符</b></center>

| 运算符                                                       | 操作                                     | A    | N    | 类型                  |
| ------------------------------------------------------------ | ---------------------------------------- | ---- | ---- | --------------------- |
| ++                                                           | 前/后增量                                | R    | 1    | lval -> num           |
| --                                                           | 前/后减量                                | R    | 1    | lval -> num           |
| -                                                            | 求反                                     | R    | 1    | num -> num            |
| +                                                            | 转换为数字                               | R    | 1    | num -> num            |
| ~                                                            | 按位求反                                 | R    | 1    | int -> int            |
| ！                                                           | 逻辑非                                   | R    | 1    | bool -> bool          |
| delete                                                       | 删除属性                                 | R    | 1    | lval -> lval          |
| typeof                                                       | 检测操作数类型                           | R    | 1    | any -> str            |
| void                                                         | 返回 undefined 值                        | R    | 1    | any -> undef          |
| *、/、%                                                      | 乘、除、求余                             | L    | 2    | num, num -> num       |
| +、-                                                         | 加、减                                   | L    | 2    | num, num -> num       |
| +                                                            | 字符串连接                               | L    | 2    | str, str -> str       |
| <<                                                           | 左移位                                   | L    | 2    | int, int -> int       |
| >>                                                           | 右移位                                   | L    | 2    | int, int -> int       |
| >>>                                                          | 无符号右移位                             | L    | 2    | int, int -> int       |
| <、<=、>、>=                                                 | 比较数字顺序                             | L    | 2    | num, num -> bool      |
| <、<=、>、>=                                                 | 比较在字母表中的顺序                     | L    | 2    | str, stri -> bool     |
| instanceof                                                   | 测试对象类                               | L    | 2    | obj, func -> bool     |
| in                                                           | 测试属性是否存在                         | L    | 2    | str, obj -> bool      |
| ==                                                           | 判断相等                                 | L    | 2    | any, any -> bool      |
| !=                                                           | 判断不等                                 | L    | 2    | any, any -> bool      |
| ===                                                          | 判断恒等                                 | L    | 2    | any, any -> bool      |
| !==                                                          | 判断非恒等                               | L    | 2    | any, any -> bool      |
| &                                                            | 按位与                                   | L    | 2    | int, int ->int        |
| ^                                                            | 按位异或                                 | L    | 2    | int, int -> int       |
| \|                                                           | 按位或                                   | L    | 2    | int, int -> int       |
| &&                                                           | 逻辑与                                   | L    | 2    | any, any -> any       |
| \|\|                                                         | 逻辑或                                   | L    | 2    | any, any -> any       |
| ?:                                                           | 条件运算符                               | R    | 3    | bool, any, any -> any |
| =<br />*=、/=、%=、<br />+=、-=、&=、<br />^=、\|=、<<=、<br />>>=、>>>= | 变量赋值或对象属性赋值运算符             | R    | 2    | lval, any -> any      |
| ,                                                            | 忽略第一个操作数，<br />返回第二个操作数 | L    | 2    | any, any -> any       |

