do while 循环的通用形式：

```
do {
	statement
} while (expression);
```

do while 语句创建一个循环， 在 expression 为假或 0 之前重复执行循环体中的内容。 do while语句是一种出口条件循环， 即在执行完循环体后才根据测试条件决定是否再次执行循环。 因此， 该循环至少必须执行一次。  

示例程序 **do_while.c**

```c
/* do_while.c -- 出口条件循环 */
#include <stdio.h>

int main(void)
{
    const int secret_code = 13;
    int code_entered;
    do
    {
        printf("To enter the triskaidekaphobia therapy club,\n");
        printf("please enter the secret code number: ");
        scanf("%d", &code_entered);
    } while (code_entered != secret_code);
    printf("Congratulations! You are cured!\n");
    return 0;
}
```

