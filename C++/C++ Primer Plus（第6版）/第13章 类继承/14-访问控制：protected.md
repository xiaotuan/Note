### 13.5　访问控制：protected

到目前为止，本书的类示例已经使用了关键字public和private来控制对类成员的访问。还存在另一个访问类别，这种类别用关键字protected表示。关键字protected与private相似，在类外只能用公有类成员来访问protected部分中的类成员。private和protected之间的区别只有在基类派生的类中才会表现出来。派生类的成员可以直接访问基类的保护成员，但不能直接访问基类的私有成员。因此，对于外部世界来说，保护成员的行为与私有成员相似；但对于派生类来说，保护成员的行为与公有成员相似。

例如，假如Brass类将balance成员声明为保护的：

```css
class Brass
{
protected:
    double balance;
...
};
```

在这种情况下，BrassPlus类可以直接访问balance，而不需要使用Brass方法。例如，可以这样编写BrassPlus::Withdraw()的核心：

```css
void BrassPlus::Withdraw(double amt)
{
    if (amt < 0)
        cout << "Withdrawal amount must be positive; "
             << "withdrawal canceled.\n";
    else if (amt <= balance) // access balance directly
        balance -= amt;
    else if ( amt <= balance + maxLoan - owesBank)
    {
        double advance = amt - balance;
        owesBank += advance * (1.0 + rate);
        cout << "Bank advance: $" << advance << endl;
        cout << "Finance charge: $" << advance * rate << endl;
        Deposit(advance);
        balance -= amt;
    }
    else
        cout << "Credit limit exceeded. Transaction cancelled.\n";
}
```

使用保护数据成员可以简化代码的编写工作，但存在设计缺陷。例如，继续以BrassPlus为例，如果balance是受保护的，则可以按下面的方式编写代码：

```css
void BrassPlus::Reset(double amt)
{
    balance = amt;
}
```

Brass类被设计成只能通过Deposit()和Withdraw()才能修改balance。但对于BrassPlus对象，Reset()方法将忽略Withdraw()中的保护措施，实际上使balance成为公有变量，。

> **警告：**
> 最好对类数据成员采用私有访问控制，不要使用保护访问控制；同时通过基类方法使派生类能够访问基类数据。

然而，对于成员函数来说，保护访问控制很有用，它让派生类能够访问公众不能使用的内部函数。

