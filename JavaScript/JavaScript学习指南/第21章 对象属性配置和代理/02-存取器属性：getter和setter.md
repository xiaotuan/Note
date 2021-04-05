### 21.1　存取器属性：getter和setter

JavaScript中有两种对象属性：数据属性和存取器属性。其实前面已经见过这两种属性了，只不过存取器属性被隐藏在一些ES6的语法背后了（在第9章，称之为“动态属性”）。

前面大家已经熟悉了函数属性（或方法），存取器属性也是类似的，只不过有两个函数——getter和setter。当被访问的时候，它们的行为更像是一个数据属性而非函数。

先来回顾一下动态属性。假设有一个User类，它有setEmail和getEmail两个方法。这里之所以使用“get”和“set”方法，而没有直接把email当做属性，是因为这里不希望用户拿到一个不合法的邮箱。User类非常简单（简单起见，将任何包含了@符号的字符串都当做合法邮箱）：

```javascript
const USER_EMAIL = Symbol();
class User {
    setEmail(value) {
        if(!/@/.test(value)) throw new Error('invalid email: ${value}');
        this[USER_EMAIL] = value;
    }
    getEmail() {
        return this[USER_EMAIL];
    }
} 
```

在这个例子中，唯一引人注目的是使用了两个方法（而不是一个属性）来防止USER_EMAIL属性接收非法的邮件地址。这里使用符号属性是为了防止意外地直接访问属性（如果有一个名为email或者是_email字符串属性，就很可能会不小心直接访问到它）。

这个模式很常见，而且很有效，不过它可能比大家所期望的笨重一些。下面是使用了这个类的一个例子：

```javascript
const u = new User();
u.setEmail("john@doe.com");
console.log('User email: ${u.getEmail()}');
```

虽然这段代码可以正常工作，不过使用下面这种写法会更自然：

```javascript
const u = new User();
u.email = "john@doe.com";
console.log('User email: ${u.email}');
```

这就是存取器属性的优势：它能让开发人员在使用后者的自然语法时，还能保持前者的优点。试着用存取器属性重写User类：

```javascript
const USER_EMAIL = Symbol();
class User {
    set email(value) {
       if(!/@/.test(value)) throw new Error('invalid email: ${value}');
       this[USER_EMAIL] = value;
    }
    get email() {
       return this[USER_EMAIL];
    }
} 
```

这里有两个不同的函数，不过它们都跟单独的email属性绑定在一起了。该属性被赋值的时候，setter函数会被调用（所赋的值作为setter的第一个参数），而getter函数被调用时，就说明有地方正在获取该属性的值。

这里也可以只提供一个getter，而不提供setter，例如有一个返回矩形周长的getter：

```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    get perimeter() {
        return this.width*2 + this.height*2;
    } 
} 
```

此处没有提供设置周长的setter函数，因为很难从周长去推断矩形的宽。这么一来，将其设置为只读属性会更容易理解。

同样，也可以只提供setter而不提供getter，虽然这种模式很少见。

