1. 下面是文件 hello.c 的源代码：

   ```c
   #include <stdio.h>
   #include <stdlib.h>
   
   int main() 
   {
       printf("Hello World\n");
       exit(0);
   }
   ```

2. 编译、链接和运行程序。

    ```console
    $ gcc -o hello hello.c
    $ ./hello
    Hello World
    ```

> 注意：如果你忘记用 `-o name` 选项告诉编译器可执行程序的名字，编译器就会把程序放在一个名为 a.out 的文件里。