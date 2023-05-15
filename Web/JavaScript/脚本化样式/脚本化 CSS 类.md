改变元素的 `class` 就改变了应用于元素的一组样式表选择器，它能在同一时刻改变多个 CSS 属性。首先，为任意元素定义一个名为 “attention” 的类：  

```css
.attention { /* 吸引用户注意力的样式 */
    background-color: yellow; /* 黄色高亮背景 */
    font-weight: bold; /* 粗体 */
    border: solid black 2px; /* 黑框*/
}
```

如下代码设置和清除元素的 `className` 属性来为元素添加和移除 “attention” 类：  

```js
function grabAttention(e) { 
    e.className = "attention"; 
}

function releaseAttention(e) { 
    e.className = ""; 
}
```

如果元素已经有一个类了，为该元素调用 `grabAttention()` 函数将覆盖已存在的类。HTML5 解决了这个问题，为每个元素定义了 `classList` 属性。该属性值是 DOMTokenList 对象：一个只读的类数组对象，它包含元素的单独类名。但是，和数组元素相比，DOMTokenList 定义的方法更加重要。`add()` 和 `remove()` 从元素的 `class` 属性中添加和清除一个类名。`toggle()` 表示如果不存在类名就添加一个；否则，删除它。最后，`contains()` 方法检测 `class` 属性中是否包含一个指定的类名。

类似其他 DOM 集合类型，DOMTokenList 对象“实时地”代表了元素类名集合，而并非是在查询 `classList` 属性时类名的一个静态快照。  

**示例代码：classList()：将 className 当做一个 CSS 类集合**

```js
/*
* 如果e有classList属性则返回它。否则，返回一个为e模拟DOMTokenList API的对象
* 返回的对象有contains()、add()、remove()、toggle()和toString()等方法
* 来检测和修改元素e的类集合。如果classList属性是原生支持的，
* 返回的类数组对象有length和数组索引属性。模拟DOMTokenList不是类数组对象，
* 但是它有一个toArray()方法来返回一个含元素类名的纯数组快照
*/
function classList(e) {
	if (e.classList) {
        return e.classList; // 如果e.classList存在，则返回它
    } else {
        return new CSSClassList(e); // 否则，就伪造一个
    } 
}

// CSSClassList是一个模拟DOMTokenList的JavaScript类
function CSSClassList(e) { 
    this.e = e; 
}
// 如果e.className包含类名c则返回true；否则返回false
CSSClassList.prototype.contains = function(c) {
    // 检查c是否是合法的类名
    if (c.length === 0 || c.indexOf(" ") != -1) {
        throw new Error("Invalid class name: '" + c + "'");
    }
    // 首先是常规检查
    var classes = this.e.className;
    if (!classes) {
        return false; // e不含类名
    }
    if (classes === c) {
        return true; // e有一个完全匹配的类名
    }
    // 否则，把c自身看做一个单词，利用正则表达式搜索c
    // \b在正则表达式里代表单词的边界
    return classes.search("\\b" + c + "\\b") != -1;
};

// 如果c不存在，将c添加到e.className中
CSSClassList.prototype.add = function(c) {
    if (this.contains(c)) {
        return; // 如果存在，什么都不做
    }
    var classes = this.e.className;
    if (classes && classes[classes.length-1] != " ") {
        c = " " + c; // 如果需要加一个空格
    }
    this.e.className += c; // 将c添加到className中
};

// 将在e.className中出现的所有c都删除
CSSClassList.prototype.remove = function(c) {
    // 检查c是否是合法的类名
    if (c.length === 0 || c.indexOf(" ") != -1) {
        throw new Error("Invalid class name: '" + c + "'");
    }
    // 将所有作为单词的c和多余的尾随空格全部删除
    var pattern = new RegExp("\\b" + c + "\\b\\s*", "g");
    this.e.className = this.e.className.replace(pattern, "");
};

// 如果c不存在，将c添加到e.className中，并返回true
// 否则，将在e.className中出现的所有c都删除，并返回false
CSSClassList.prototype.toggle = function(c) {
    if (this.contains(c)) { // 如果e.className包含c
        this.remove(c); // 删除它
        return false;
    } else { // 否则
        this.add(c); // 添加它
        return true;
    }
};

// 返回e.className本身
CSSClassList.prototype.toString = function() { 
    return this.e.className; 
};

// 返回在e.className中的类名
CSSClassList.prototype.toArray = function() {
    return this.e.className.match(/\b\w+\b/g) || [];
};
```

