#### 14.7.7　结构、指针和 `malloc()` 

如果使用 `malloc()` 分配内存并使用指针存储该地址，那么在结构中使用指针处理字符串就比较合理。这种方法的优点是，可以请求 `malloc()` 为字符串分配合适的存储空间。可以要求用4字节存储 `"Joe"` 和用18字节存储 `"Rasolofomasoandro"` 。用这种方法改写程序清单14.9并不费劲。主要是更改结构声明（用指针代替数组）和提供一个新版本的 `getinfo()` 函数。新的结构声明如下：

```c
struct namect {
     char * fname;    // 用指针代替数组
     char * lname;
     int letters;
};
```

新版本的 `getinfo()` 把用户的输入读入临时数组中，调用 `malloc()` 函数分配存储空间，并把字符串拷贝到新分配的存储空间中。对名和姓都要这样做：

```c
void getinfo (struct namect * pst)
{
     char temp[SLEN];
     printf("Please enter your first name.\n");
     s_gets(temp, SLEN);
     // 分配内存存储名
     pst->fname = (char *) malloc(strlen(temp) + 1);
     // 把名拷贝到已分配的内存
     strcpy(pst->fname, temp);
     printf("Please enter your last name.\n");
     s_gets(temp, SLEN);
     pst->lname = (char *) malloc(strlen(temp) + 1);
     strcpy(pst->lname, temp);
}
```

要理解这两个字符串都未存储在结构中，它们存储在 `malloc()` 分配的内存块中。然而，结构中存储着这两个字符串的地址，处理字符串的函数通常都要使用字符串的地址。因此，不用修改程序中的其他函数。

第12章建议应该成对使用 `malloc()` 和 `free()` 。因此，还要在程序中添加一个新的函数 `cleanup()` ，用于释放程序动态分配的内存。如程序清单14.10所示。

程序清单14.10　 `names3.c` 程序

```c
// names3.c -- 使用指针和 malloc()
#include <stdio.h>
#include <string.h>   // 提供 strcpy()、strlen() 的原型
#include <stdlib.h>   // 提供 malloc()、free() 的原型
#define SLEN 81
struct namect {
     char * fname;  // 使用指针
     char * lname;
     int letters;
};
void getinfo(struct namect *);        // 分配内存
void makeinfo(struct namect *);
void showinfo(const struct namect *);
void cleanup(struct namect *);        // 调用该函数时释放内存
char * s_gets(char * st, int n);
int main(void)
{
     struct namect person;
     getinfo(&person);
     makeinfo(&person);
     showinfo(&person);
     cleanup(&person);
     return 0;
}
void getinfo(struct namect * pst)
{
     char temp[SLEN];
     printf("Please enter your first name.\n");
     s_gets(temp, SLEN);
     // 分配内存以存储名
     pst->fname = (char *) malloc(strlen(temp) + 1);
     // 把名拷贝到动态分配的内存中
     strcpy(pst->fname, temp);
     printf("Please enter your last name.\n");
     s_gets(temp, SLEN);
     pst->lname = (char *) malloc(strlen(temp) + 1);
     strcpy(pst->lname, temp);
}
void makeinfo(struct namect * pst)
{
     pst->letters = strlen(pst->fname) +
          strlen(pst->lname);
}
void showinfo(const struct namect * pst)
{
     printf("%s %s, your name contains %d letters.\n",
          pst->fname, pst->lname, pst->letters);
}
void cleanup(struct namect * pst)
{
     free(pst->fname);
     free(pst->lname);
}
char * s_gets(char * st, int n)
{
     char * ret_val;
     char * find;
     ret_val = fgets(st, n, stdin);
     if (ret_val)
     {
          find = strchr(st, '\n');    // 查找换行符
          if (find)                   // 如果地址不是 NULL，
               *find = '\0';          // 在此处放置一个空字符
          else
               while (getchar() != '\n')
                    continue;         // 处理输入行的剩余部分
     }
     return ret_val;
}
```

下面是该程序的输出：

```c
Please enter your first name.
Floresiensis
Please enter your last name.
Mann
Floresiensis Mann, your name contains 16 letters.

```

