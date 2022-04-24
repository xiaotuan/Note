`switch` 在圆括号中的测试表达式的值应该是一个整数值（包括 `char` 类型）。`case` 标签必须是整数类型（包括 `char` 类型）的常量或整型常量表达式（即，表达式中只包含整型常量）。不能用变量作为 `case` 标签。`switch` 的构造如下所示：

```c
switch (整型表达式)
{
    case 常量1:
        语句	<-- 可选
    case 常量2:
        语句	<-- 可选
    default: 
        语句	<-- 可选
}
```

例如：

```c
/* animals.c -- 使用 switch 语句 */
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char ch;
    printf("Give me a letter of the alphabet, and I will give ");
    printf("an animal name\nbeginning with that letter.\n");
    printf("Please type in a letter; type # to end my act.\n");
    while ((ch = getchar()) != '#')
    {
        if ('\n' == ch)
        {
            continue;
        }
        if (islower(ch))	/* 只接受小写字母 */
        {
            switch (ch)
            {
                case 'a':
                    printf("argali, a wild sheep of Asia\n");
                    break;
                    
                case 'c':
                    printf("coati, racoonlike mammal\n");
                    break;
                    
                case 'd':
                    printf("desman, aquatic, molelike critter\n");
                    break;
                   
                case 'e':
                    printf("echidna, the spiny anteater\n");
                    break;
                    
                case 'f':
                    printf("fisher, brownish marten\n");
                    break;
                    
                default:
                    printf("That's a stumper!\n");
            }	/* switch 结束 */
        } else {
            printf("I recognize only lowercase letters.\n");
        }
        while (getchar() != '\n')
        {
            continue;	/* 跳过输入行的剩余部分 */
        }
        printf("Please type another letter or a #.\n");
    }	/* while 循环结束 */
    printf("Bye!\n");
    return 0;
}
```

可以在 `switch` 语句中使用多重 `case` 标签。例如：

```c
// vowels.c -- 使用多重标签
#include <stdio.h>

int main(void)
{
    char ch;
    int a_ct, e_ct, i_ct, o_ct, u_ct;
    a_ct = e_ct = i_ct = o_ct = u_ct = 0;
    printf("Enter some text; enter # to quit.\n");
    while ((ch = getchar()) != '#')
    {
        switch (ch)
        {
            case 'a':
            case 'A':
                a_ct++;
                break;
                
            case 'e':
            case 'E':
                e_ct++;
                break;
                
            case 'i':
            case 'I':
                i_ct++;
                break;
                
            case 'o':
            case 'O':
                o_ct++;
                break;
                
            case 'u':
            case 'U':
                u_ct++;
                break;
                
            default:
                break;
        }	// switch 结束
    }	// while 循环结束
    printf("number of vowels:    A    E    I    O    U\n");
    printf("                  %4d %4d %4d %4d %4d\n", a_ct, e_ct, i_ct, o_ct, u_ct);
    return 0;
}

```

