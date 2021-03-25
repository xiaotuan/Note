### 14.2.4　使用using重新定义访问权限

使用保护派生或私有派生时，基类的公有成员将成为保护成员或私有成员。假设要让基类的方法在派生类外面可用，方法之一是定义一个使用该基类方法的派生类方法。例如，假设希望Student类能够使用valarray类的sum()方法，可以在Student类的声明中声明一个sum()方法，然后像下面这样定义该方法：

```css
double Student::sum() const // public Student method
{
    return std::valarray<double>::sum(); // use privately-inherited method
}
```

这样Student对象便能够调用Student::sum()，后者进而将valarray<double>::sum()方法应用于被包含的valarray对象（如果ArrayDb typedef在作用域中，也可以使用ArrayDb而不是std::valarray<double>）。

另一种方法是，将函数调用包装在另一个函数调用中，即使用一个using声明（就像名称空间那样）来指出派生类可以使用特定的基类成员，即使采用的是私有派生。例如，假设希望通过Student类能够使用valarray的方法min()和max()，可以在studenti.h的公有部分加入如下using声明：

```css
class Student : private std::string, private std::valarray<double>
{
...
public:
    using std::valarray<double>::min;
    using std::valarray<double>::max;
    ...
};
```

上述using声明使得valarray<double>::min()和valarray<double>::max()可用，就像它们是Student的公有方法一样：

```css
cout << "high score: " << ada[i].max() << endl;
```

注意，using声明只使用成员名——没有圆括号、函数特征标和返回类型。例如，为使Student类可以使用valarray的operator 方法，只需在Student类声明的公有部分包含下面的using声明：

```css
using std::valarray<double>::operator[];
```

这将使两个版本（const和非const）都可用。这样，便可以删除Student::operator[] ()的原型和定义。using声明只适用于继承，而不适用于包含。

有一种老式方式可用于在私有派生类中重新声明基类方法，即将方法名放在派生类的公有部分，如下所示：

```css
class Student : private std::string, private std::valarray<double>
{
public:
    std::valarray<double>::operator[]; // redeclare as public, just use name
    ...
};
```

这看起来像不包含关键字using的using声明。这种方法已被摒弃，即将停止使用。因此，如果编译器支持using声明，应使用它来使派生类可以使用私有基类中的方法。

