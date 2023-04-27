Element 和 HTMLDocument 等类型都像 String 和 Array 一样是类。它们不是构造函数，但它们有原型对象，可以用自定义方法扩展它：

```js
Element.prototype.next = function() {
    if (this.nextElementSibling) {
        return this.nextElementSibling;
    }
    var sib = this.nextSibling;
    while (sib && sib.nodeType !== 1) {
        sib = sib.nextSibling;
    }
    return sib;
};
```

