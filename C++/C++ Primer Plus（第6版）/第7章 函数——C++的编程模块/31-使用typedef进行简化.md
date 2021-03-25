### 7.10.4　使用typedef进行简化

除auto外，C++还提供了其他简化声明的工具。您可能还记得，第5章说过，关键字typedef让您能够创建类型别名：

```css
typedef double real; // makes real another name for double
```

这里采用的方法是，将别名当做标识符进行声明，并在开头使用关键字typedef。因此，可将p_fun声明为程序清单7.19使用的函数指针类型的别名：

```css
typedef const double *(*p_fun)(const double *, int); // p_fun now a type name
p_fun p1 = f1; // p1 points to the f1() function
```

然后使用这个别名来简化代码：

```css
p_fun pa[3] = {f1,f2,f3}; // pa an array of 3 function pointers
p_fun (*pd)[3] = &pa; // pd points to an array of 3 function pointers
```

使用typedef可减少输入量，让您编写代码时不容易犯错，并让程序更容易理解。

