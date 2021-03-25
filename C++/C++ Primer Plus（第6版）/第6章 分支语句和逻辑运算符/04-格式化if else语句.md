### 6.1.2　格式化if else语句

if else中的两种操作都必须是一条语句。如果需要多条语句，需要用大括号将它们括起来，组成一个块语句。和有些语言（如BASIC和FORTRAN）不同的是，由于C++不会自动将if和else之间的所有代码视为一个代码块，因此必须使用大括号将这些语句组合成一个语句块。例如，下面的代码将出现编译器错误：

```css
if (ch == 'Z')
    zorro++;    // if ends here
    cout << "Another Zorro candidate\n";
else            // wrong
    dull++;
    cout << "Not a Zorro candidate\n";
```

编译器把它看作是一条以zorro ++;语句结尾的简单if语句，接下来是一条cout语句。到目前为止，一切正常。但之后编译器发现一个独立的else，这被视为语法错误。

请添加大括号，将语句组合成一个语句块：

```css
if (ch == 'Z')
{                        // if true block
    zorro++;
    cout << "Another Zorro candidate\n";
}
else
{                        // if false block
    dull++;
    cout << "Not a Zorro candidate\n";
}
```

由于C++是自由格式语言，因此只要使用大括号将语句括起，对大括号的位置没有任何限制。上述代码演示了一种流行的格式，下面是另一种流行的格式：

```css
if (ch == 'Z') {
    zorro++;
    cout << "Another Zorro candidate\n";
    }
else {
    dull++;
    cout << "Not a Zorro candidate\n";
    }
```

第一种格式强调的是语句的块结构，第二种格式则将语句块与关键字if和else更紧密地结合在一起。这两种风格清晰、一致，应该能够满足要求；然而，可能会有老师或雇主在这个问题上的观点强硬而固执。

