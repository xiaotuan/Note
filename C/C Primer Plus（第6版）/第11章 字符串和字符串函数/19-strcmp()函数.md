#### 11.5.4　 `strcmp()` 函数

假设要把用户的响应与已存储的字符串作比较，如程序清单11.20所示。

程序清单11.20　 `nogo.c` 程序

```c
/* nogo.c -- 该程序是否能正常运行？ */
#include <stdio.h>
#define ANSWER "Grant"
#define SIZE 40
char * s_gets(char * st, int n);
int main(void)
{
     char try[SIZE];
     puts("Who is buried in Grant's tomb?");
     s_gets(try, SIZE);
     while (try != ANSWER)
     {
          puts("No, that's wrong. Try again.");
          s_gets(try, SIZE);
     }
     puts("That's right!");
     return 0;
}
char * s_gets(char * st, int n)
{
     char * ret_val;
     int i = 0;
     ret_val = fgets(st, n, stdin);
     if (ret_val)
     {
          while (st[i] != '\n' && st[i] != '\0')
               i++;
          if (st[i] == '\n')
               st[i] = '\0';
          else 
               while (getchar() != '\n')
                     continue;
     }
     return ret_val;
}
```

这个程序看上去没问题，但是运行后却不对劲。 `ANSWER` 和 `try` 都是指针，所以 `try != ANSWER` 检查的不是两个字符串是否相等，而是这两个字符串的地址是否相同。因为 `ANSWE` 和 `try` 存储在不同的位置，所以这两个地址不可能相同，因此，无论用户输入什么，程序都提示输入不正确。这真让人沮丧。

该函数要比较的是字符串的内容，不是字符串的地址。读者可以自己设计一个函数，也可以使用C标准库中的 `strcmp()` 函数（用于字符串比较）。该函数通过比较运算符来比较字符串，就像比较数字一样。如果两个字符串参数相同，该函数就返回 `0` ，否则返回非零值。修改后的版本如程序清单11.21所示。

程序清单11.21　 `compare.c` 程序

```c
/* compare.c -- 该程序可以正常运行 */
#include <stdio.h>
#include <string.h>   // strcmp()函数的原型在该头文件中
#define ANSWER "Grant"
#define SIZE 40
char * s_gets(char * st, int n);
int main(void)
{
     char try[SIZE];
     puts("Who is buried in Grant's tomb?");
     s_gets(try, SIZE);
     while (strcmp(try, ANSWER) != 0)
     {
          puts("No, that's wrong. Try again.");
          s_gets(try, SIZE);
     }
     puts("That's right!");
     return 0;
}
char * s_gets(char * st, int n)
{
     char * ret_val;
     int i = 0;
     ret_val = fgets(st, n, stdin);
     if (ret_val)
     {
          while (st[i] != '\n' && st[i] != '\0')
               i++;
          if (st[i] == '\n')
               st[i] = '\0';
          else 
               while (getchar() != '\n')
                     continue;
     }
     return ret_val;
}
```

> **注意**
> 由于非零值都为“真”，所以许多经验丰富的C程序员会把该例 `main()` 中的 `while` 循环头写成： `while (strcmp(try, ANSWER))`

`strcmp()` 函数比较的是字符串，不是整个数组，这是非常好的功能。虽然数组 `try` 占用了40字节，而存储在其中的 `"Grant"` 只占用了6字节（还有一个用来放空字符）， `strcmp()` 函数只会比较 `try` 中第1个空字符前面的部分。所以，可以用 `strcmp()` 比较存储在不同大小数组中的字符串。

如果用户输入 `GRANT` 、 `grant` 或 `Ulysses S. Grant` 会怎样？程序会告知用户输入错误。希望程序更友好，必须把所有正确答案的可能性包含其中。这里可以使用一些小技巧。例如，可以使用 `#define` 定义类似 `GRANT` 这样的答案，并编写一个函数把输入的内容都转换成大写，就解决了大小写的问题。但是，还要考虑一些其他错误的形式，这些留给读者完成。

#### 1． `strcmp()` 的返回值

如果 `strcmp()` 比较的字符串不同，它会返回什么值？请看程序清单11.22的程序示例。

程序清单11.22　 `compback.c` 程序

```c
/* compback.c -- strcmp()的返回值 */
#include <stdio.h>
#include <string.h>
int main(void)
{
     printf("strcmp(\"A\", \"A\") is ");
     printf("%d\n", strcmp("A", "A"));
     printf("strcmp(\"A\", \"B\") is ");
     printf("%d\n", strcmp("A", "B"));
     printf("strcmp(\"B\", \"A\") is ");
     printf("%d\n", strcmp("B", "A"));
     printf("strcmp(\"C\", \"A\") is ");
     printf("%d\n", strcmp("C", "A"));
     printf("strcmp(\"Z\", \"a\") is ");
     printf("%d\n", strcmp("Z", "a"));
     printf("strcmp(\"apples\", \"apple\") is ");
     printf("%d\n", strcmp("apples", "apple"));
     return 0;
}
```

在我们的系统中运行该程序，输出如下：

```c
strcmp("A", "A") is 0
strcmp("A", "B") is -1
strcmp("B", "A") is 1
strcmp("C", "A") is 1
strcmp("Z", "a") is -1
strcmp("apples", "apple") is 1
```

`strcmp()` 比较 `"A"` 和本身，返回 `0` ；比较 `"A"` 和 `"B"` ，返回 `-1` ；比较 `"B"` 和 `"A"` ，返回 `1` 。这说明，如果在字母表中第1个字符串位于第2个字符串前面， `strcmp()` 中就返回负数；反之， `strcmp()` 则返回正数。所以， `strcmp()` 比较 `"C"` 和 `"A"` ，返回 `1` 。其他系统可能返回 `2` ，即两者的ASCII码之差。ASCII标准规定，在字母表中，如果第1个字符串在第2个字符串前面， `strcmp()` 返回一个负数；如果两个字符串相同， `strcmp()` 返回 `0` ；如果第1个字符串在第2个字符串后面， `strcmp()` 返回正数。然而，返回的具体值取决于实现。例如，下面给出在不同实现中的输出，该实现返回两个字符的差值：

```c
strcmp("A", "A") is 0
strcmp("A", "B") is -1
strcmp("B", "A") is 1
strcmp("C", "A") is 2
strcmp("Z", "a") is -7
strcmp("apples", "apple") is 115
```

如果两个字符串开始的几个字符都相同会怎样？一般而言， `strcmp()` 会依次比较每个字符，直到发现第1对不同的字符为止。然后，返回相应的值。例如，在上面的最后一个例子中， `"apples"` 和 `"apple"` 只有最后一对字符不同（ `"apples"` 的 `s` 和 `"apple"` 的空字符）。由于空字符在ASCII中排第1。字符 `s` 一定在它后面，所以 `strcmp()` 返回一个正数。

最后一个例子表明， `strcmp()` 比较所有的字符，不只是字母。所以，与其说该函数按字母顺序进行比较，不如说是按机器排序序列（machine collating sequence）进行比较，即根据字符的数值进行比较（通常都使用ASCII值）。在ASCII中，大写字母在小写字母前面，所以 `strcmp("Z", "a")` 返回的是负值。

大多数情况下， `strcmp()` 返回的具体值并不重要，我们只在意该值是 `0` 还是非 `0` （即，比较的两个字符串是否相等）。或者按字母排序字符串，在这种情况下，需要知道比较的结果是为正、为负还是为 `0` 。

> **注意**
> `strcmp()` 函数比较的是字符串，不是字符，所以其参数应该是字符串（如 `"apples"` 和 `"A"` ），而不是字符（如 `'A'` ）。但是， `char` 类型实际上是整数类型，所以可以使用关系运算符来比较字符。假设 `word` 是存储在 `char` 类型数组中的字符串， `ch` 是 `char` 类型的变量，下面的语句都有效：

```c
if (strcmp(word, "quit") == 0) // 使用strcmp()比较字符串
     puts("Bye!");
if (ch == 'q') // 使用 == 比较字符
     puts("Bye!");
```

> 尽管如此，不要使用 `ch` 或 `'q'` 作为 `strcmp()` 的参数。

程序清单11.23用 `strcmp()` 函数检查程序是否要停止读取输入。

程序清单11.23　 `quit_chk.c` 程序

```c
/* quit_chk.c -- 某程序的开始部分 */
#include <stdio.h>
#include <string.h>
#define SIZE 80
#define LIM 10
#define STOP "quit"
char * s_gets(char * st, int n);
int main(void)
{
     char input[LIM][SIZE];
     int ct = 0;
     printf("Enter up to %d lines (type quit to quit):\n", LIM);
     while (ct < LIM && s_gets(input[ct], SIZE) != NULL &&
                     strcmp(input[ct], STOP) != 0)
     {
          ct++;
     }
     printf("%d strings entered\n", ct);
     return 0;
}
char * s_gets(char * st, int n)
{
     char * ret_val;
     int i = 0;
     ret_val = fgets(st, n, stdin);
     if (ret_val)
     {
          while (st[i] != '\n' && st[i] != '\0')
               i++;
          if (st[i] == '\n')
               st[i] = '\0';
          else 
               while (getchar() != '\n')
                     continue;
     }
     return ret_val;
}
```

该程序在读到 `EOF` 字符（这种情况下 `s_gets()` 返回 `NULL` ）、用户输入 `quit` 或输入项达到 `LIM` 时退出。

顺带一提，有时输入空行（即，只按下Enter键或Return键）表示结束输入更方便。为实现这一功能，只需修改一下 `while` 循环的条件即可：

```c
while (ct < LIM && s_gets(input[ct], SIZE) != NULL&& input[ct][0] != '\0')
```

这里， `input[ct]` 是刚输入的字符串， `input[ct][0]` 是该字符串的第1个字符。如果用户输入空行， `s_gets()` 便会把该行第1个字符（换行符）替换成空字符。所以，下面的表达式用于检测空行：

```c
input[ct][0] != '\0'
```

#### 2． `strncmp()` 函数

`strcmp()` 函数比较字符串中的字符，直到发现不同的字符为止，这一过程可能会持续到字符串的末尾。而 `strncmp()` 函数在比较两个字符串时，可以比较到字符不同的地方，也可以只比较第3个参数指定的字符数。例如，要查找以 `"astro"` 开头的字符串，可以限定函数只查找这5个字符。程序清单11.24演示了该函数的用法。

程序清单11.24　 `starsrch.c` 程序

```c
/* starsrch.c -- 使用 strncmp() */
#include <stdio.h>
#include <string.h>
#define LISTSIZE 6
int main()
{
     const char * list[LISTSIZE] =
     {
          "astronomy", "astounding",
          "astrophysics", "ostracize",
          "asterism", "astrophobia"
     };
     int count = 0;
     int i;
     for (i = 0; i < LISTSIZE; i++)
          if (strncmp(list[i], "astro", 5) == 0)
          {
               printf("Found: %s\n", list[i]);
               count++;
          }
     printf("The list contained %d words beginning"
               " with astro.\n", count);
     return 0;
}
```

下面是该程序的输出：

```c
Found: astronomy
Found: astrophysics
Found: astrophobia
The list contained 3 words beginning with astro.
```

