### I.1.2　使用inline而不是# define来定义小型函数

在创建类似于内联函数的东西时，传统的C语言方式是使用一个#define宏定义：

```css
#define Cube(X) X*X*X
```

这将导致预处理器进行文本置换，将X替换为Cube()的参数：

```css
y = Cube(x);       // replaced with y = x*x*x;
y = Cube(x + z++); // replaced with x + z++*x + z++*x + z++;
```

由于预处理器使用文本置换，而不是真正地传递参数，因此使用这种宏可能导致意外的、错误的结果。要避免这种错误，可以在宏中使用大量的圆括号来确保正确的运算顺序：

```css
#define Cube(X) ((X)*(X)*(X))
```

但即使这样做，也无法处理使用诸如Z++等值的情况。

C++方法是使用关键字inline来标识内联函数，这种方法更可靠，因为它采用的是真正的参数传递。另外，C++内联函数可以是常规函数，也可以是类方法：

```css
class dormant
{
private:
    int period;
    ...
public:
    int Period() const { return period; } // automatically inline
    ...
};
```

\#define宏的一个优点是，它是无类型的，因此将其用于任何类型，运算都是有意义的。在C++中，可以创建内联模板来使函数独立于类型，同时传递参数。

总之，请使用C++内联技术，而不是C语言中的#define宏。

