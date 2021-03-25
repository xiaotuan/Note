### 18.3.5　管理虚方法：override和final

虚方法对实现多态类层次结构很重要，让基类引用或指针能够根据指向的对象类型调用相应的方法，但虚方法也带来了一些编程陷阱。例如，假设基类声明了一个虚方法，而您决定在派生类中提供不同的版本，这将覆盖旧版本。但正如第13章讨论的，如果特征标不匹配，将隐藏而不是覆盖旧版本：

```css
class Action
{
    int a;
public:
    Action(int i = 0) : a(i) {}
    int val() const {return a;};
    virtual void f(char ch) const { std::cout << val() << ch << "\n";}
};
class Bingo : public Action
{
public:
    Bingo(int i = 0) : Action(i) {}
    virtual void f(char * ch) const { std::cout << val() << ch << "!\n"; }
};
```

由于类Bingo定义的是f(char * ch)而不是f(char ch)，将对Bingo对象隐藏f(char ch)，这导致程序不能使用类似于下面的代码：

```css
Bingo b(10);
b.f('@'); // works for Action object, fails for Bingo object
```

在C++11中，可使用虚说明符override指出您要覆盖一个虚函数：将其放在参数列表后面。如果声明与基类方法不匹配，编译器将视为错误。因此，下面的Bingo::f()版本将生成一条编译错误消息：

```css
virtual void f(char * ch) const override { std::cout << val()
                                          << ch << "!\n";
```

例如，在Microsoft Visual C++ 2010中，出现的错误消息如下：

```css
method with override specifier 'override' did not override any
base class methods
```

说明符final解决了另一个问题。您可能想禁止派生类覆盖特定的虚方法，为此可在参数列表后面加上final。例如，下面的代码禁止Action的派生类重新定义函数f()：

```css
virtual void f(char ch) const final { std::cout << val() << ch << "\n";}
```

说明符override和final并非关键字，而是具有特殊含义的标识符。这意味着编译器根据上下文确定它们是否有特殊含义；在其他上下文中，可将它们用作常规标识符，如变量名或枚举。

