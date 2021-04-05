### 20.2　模块（Module）

模块（Module）是一种打包和命名空间的机制。命名空间（Namespace）可以有效避免命名冲突。比如，如果Amanda和Tyler都写了一个名为 `calculate` 的函数，把这些函数复制粘贴到程序中，那么第二个函数就会覆盖第一个函数。而命名空间则允许分别引用“Amanda的calculate”和“Tyler的calculate”。下面看看如何通过Node module来解决这个问题。首先创建一个名为amanda.js的文件：

```javascript
function calculate(a, x, n) {
    if(x === 1) return a*n;
    return a*(1 - Math.pow(x, n))/(1 - x);
} 
    module.exports = calculate;
```

添加tyler.js文件：

```javascript
function calculate(r) {
    return 4/3*Math.PI*Math.pow(r, 3);
}
module.exports = calculate;
```

看到这些代码后，可以得出一个合理的结论：Amanda和Tyler在命名上都很懒，他们的函数都没什么特点，但是为了讲解这个例子，就纵容他们一回吧。这些文件中都有一行很重要的代码： `modules.export = calculate.module` ，它是Node中一个可以实现模块化的特殊对象。给exports这个属性赋的值，将会暴露到该module之外。前面已经写了一些module了，下面来看看如何在第三个程序中使用它们。创建一个名为app.js的文件，并引入这些module：

```javascript
const amanda_calculate = require('./amanda.js');
const tyler_calculate = require('./tyler.js');
console.log(amanda_calculate(1, 2, 5));   // logs 31
console.log(tyler_calculate(2));          // logs 33.510321638291124
```

注意，这里随便起了几个名字（ `amanda_calculate` 和 `tyler_calculate` ），因为它们只是变量，它们的值就是Node执行完 `require` 函数之后的结果。

有数学背景的读者可能已经发现这两个calculate函数的不同了：Amanda的函数计算了一个等比数列的和：a+ax+ax<sup class="my_markdown">2</sup> + … +axn<sup>−1</sup>，而Tyler则提供了一个根据球体半径r来计算体积的算法。知道了函数的用法后，就可以跟Amanda和Tyler的不良命名说再见了，然后在app.js中给它们一个合适的名字：

```javascript
const geometricSum = require('./amanda.js');
const sphereVolume = require('./tyler.js');
console.log(geometricSum(1, 2, 5));     // logs 31
console.log(sphereVolume(2));           // logs 33.510321638291124
```

module可以对外暴露任何类型的值（甚至是基本类型，虽然没有什么理由去这么做）。一般情况下，开发人员会希望自己的module包含多个函数，但是大多数情况下，这样会暴露一个带有函数属性的对象。想象一下如果Amanda是一个代数学家，那么除了等比数列求和之外，他还能提供很多有用的代数函数：

```javascript
module.exports = {
    geometricSum(a, x, n) {
        if(x === 1) return a*n;
        return a*(1 - Math.pow(x, n))/(1 - x);
    },
    arithmeticSum(n) {
        return (n + 1)*n/2;
    },
    quadraticFormula(a, b, c) {
        const D = Math.sqrt(b*b - 4*a*c);
        return [(-b + D)/(2*a), (-b - D)/(2*a)];
    },
}; 
```

讲到这里，已经越来越接近传统的命名空间了，开发人员给返回值命名，而返回值（一个对象）通常会包含自己的名字：

```javascript
const amanda = require('./amanda.js');
console.log(amanda.geometricSum(1, 2, 5));          // logs 31
console.log(amanda.quadraticFormula(1, 2, -15));    // logs [ 3, -5 ]
```

这并不是魔法：module只暴露包含函数属性的原始对象（不要被缩写的ES6语法所迷惑，他们只是一个函数）。这种范例太常见了，所以又有一个关于它的快捷语法：一个叫作exports的特殊变量。可以用一种更加简洁（但是是等价的）的方式重写Amanda的exports：

```javascript
exports.geometricSum = function(a, x, n) {
    if(x === 1) return a*n;
    return a*(1 - Math.pow(x, n))/(1 - x);
}; 
exports.arithmeticSum = function(n) {
    return (n + 1)*n/2;
}; 
exports.quadraticFormula = function(a, b, c) {
    const D = Math.sqrt(b*b - 4*a*c);
    return [(-b + D)/(2*a), (-b - D)/(2*a)];
}; 
```

> <img class="my_markdown" src="../images/2.png" style="width:116px;  height: 151px; " width="10%"/>
> exports的快捷语法只能导出对象，如果想导出函数或者其他值，必须使用module.exports。此外，这两个不能混用：只能二选其一。

