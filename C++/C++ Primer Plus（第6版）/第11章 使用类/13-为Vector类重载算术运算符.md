### 11.5.2　为Vector类重载算术运算符

在使用x、y坐标时，将两个矢量相加将非常简单，只要将两个x分量相加，得到最终的x分量，将两个y分量相加，得到最终的y分量即可。根据这种描述，可能使用下面的代码：

```css
Vector Vector::operator+(const Vector & b) const
{
    Vector sum;
    sum.x = x + b.x;
    sum.y = y + b.y;
    return sum; // incomplete version
}
```

如果对象只存储x和y分量，则这很好。遗憾的是，上述代码无法设置极坐标值。可以通过添加另外一些代码来解决这种问题：

```css
Vector Vector::operator+(const Vector & b) const
{
    Vector sum;
    sum.x = x + b.x;
    sum.y = y + b.y;
    sum.set_ang(sum.x, sum.y);
    sum.set_mag(sum.x, sum.y);
    return sum; // version duplicates needlessly
}
```

然而，使用构造函数来完成这种工作，将更简单、更可靠：

```css
Vector Vector::operator+(const Vector & b) const
{
    return Vector(x + b.x, y + b.y); // return the constructed Vector
}
```

上述代码将新的x分量和y分量传递给Vector构造函数，而后者将使用这些值来创建无名的新对象，并返回该对象的副本。这确保了新的Vector对象是根据构造函数制定的标准规则创建的。

> **提示：**
> 如果方法通过计算得到一个新的类对象，则应考虑是否可以使用类构造函数来完成这种工作。这样做不仅可以避免麻烦，而且可以确保新的对象是按照正确的方式创建的。

#### 1．乘法

将矢量与一个数相乘，将使该矢量加长或缩短（取决于这个数）。因此，将矢量乘以3得到的矢量的长度为原来的三倍，而方向不变。要在Vector类中实现矢量的这种行为很容易。对于极坐标，只要将长度进行伸缩，并保持角度不变即可；对于直角坐标，只需将x和y分量进行伸缩即可。也就是说，如果矢量的分量为5和12，则将其乘以3后，分量将分别是15和36。这正是重载的乘法运算符要完成的工作：

```css
Vector Vector::operator*(double n) const
{
    return Vector(n * x, n * y);
}
```

和重载加法一样，上述代码允许构造函数使用新的x和y分量来创建正确的Vector对象。上述函数用于处理Vector值和double值相乘。可以像Time示例那样，使用一个内联友元函数来处理double与Vector相乘：

```css
Vector operator*(double n, const Vector & a) // friend function
{
    return a * n; // convert double times Vector to Vector times double
}
```

#### 2．对已重载的运算符进行重载

在C++中，−运算符已经有两种含义。首先，使用两个操作数，它是减法运算符。减法运算符是一个二元运算符，因为它有两个操作数。其次，使用一个操作数时（如−x），它是负号运算符。这种形式被称为一元运算符，即只有一个操作数。对于矢量来说，这两种操作（减法和符号反转）都是有意义的，因此Vector类有这两种操作。

要从矢量A中减去矢量B，只要将分量相减即可，因此重载减法与重载加法相似：

```css
Vector operator-(const Vector & b) const;        // prototype
Vector Vector::operator-(const Vector & b) const // definition
{
    return Vector(x - b.x, y - b.y);             // return the constructed Vector
}
```

操作数的顺序非常重要。下面的语句：

```css
diff = v1 - v2;
```

将被转换为下面的成员函数调用：

```css
diff = v1.operator-(v2);
```

这意味着将从隐式矢量参数减去以显式参数传递的矢量，所以应使用x − b.x，而不是b.x − x。

接下来，来看一元负号运算符，它只使用一个操作数。将这个运算符用于数字（如−x）时，将改变它的符号。因此，将这个运算符用于矢量时，将反转矢量的每个分量的符号。更准确地说，函数应返回一个与原来的矢量相反的矢量（对于极坐标，长度不变，但方向相反）。下面是重载负号的原型和定义：

```css
Vector operator-() const;
Vector Vector::operator-() const
{
    return Vector (-x, -y);
}
```

现在，operator-()有两种不同的定义。这是可行的，因为它们的特征标不同。可以定义−运算符的一元和二元版本，因为C++提供了该运算符的一元和二元版本。对于只有二元形式的运算符（如除法运算符），只能将其重载为二元运算符。

> **注意：**
> 因为运算符重载是通过函数来实现的，所以只要运算符函数的特征标不同，使用的运算符数量与相应的内置C++运算符相同，就可以多次重载同一个运算符。

