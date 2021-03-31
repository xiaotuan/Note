### 1.0.2　jQuery原则

jQuery的原则是“用更少的代码做更多的事”。这一原则可以进一步分为三个概念：

+ （通过CSS选择器）寻找一些元素，（通过jQuery方法）对其进行某些处理。
+ 链接一组元素上的多个jQuery方法。
+ 使用jQuery包装器和隐式迭代。

详细了解这三个概念是编写你自己的jQuery代码和扩展本书中学到的秘诀的基础。下面详细地解释这些概念。

#### 1．寻找一些元素并对其进行某些处理

更具体地讲，这条原则是指在DOM中找到一组元素，然后对这组元素进行某种处理。例如，研究一下这样的场景：你想要对用户隐藏一个<div>元素，在隐含的<div>中加载一些新的文本内容，修改<div>的属性，最后让隐藏的<div>再次可见。

上面的最后一句话转换成的jQuery代码如下：

```css
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<script type="text/JavaScript"
src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
</head>
<body>
<div>old content</div>
<script>
//隐藏页面上的所有div
jQuery('div').hide();
//更新所有div中包含的文本
jQuery('div').text('new content');
//为所有div添加值为updatedContent的class属性
jQuery('div').addClass("updatedContent");
//显示页面上的所有div
jQuery('div').show();
</script>
</body>
</html>

```

我们逐条查看这4条jQuery语句：

+ 隐藏页面上的 `<div>` 元素，使用户无法看到它。
+ 用新的文本（ `new content` ）替换隐藏 `<div>` 元素中的文本。
+ 用新的属性（ `class` ）和值（ `updatedContent` ）更新 `<div>` 元素。
+ 在页面上显示 `<div>` 元素，使用户又能看到它。

如果现在这些jQuery代码还让你觉得深奥，也没有关系。我们将在本章的第一个秘诀中介绍这些基础知识。另外，从这个代码示例中，你需要了解的是jQuery“找到一些元素并对其进行某些处理”的概念。在读例子中，用jQuery函数（ `jQuery()` ）找出HTML页面中所有的 `<div>` 元素，然后用jQuery方法对它们进行了一些处理（例如， `hide()` 、 `text()` 、 `addClass()` 、 `show()` ）。

#### 2．链

jQuery的构造方式允许jQuery方法链。例如，为什么不在找到元素之后，将该元素上的操作链接起来呢？上一个代码示例阐述了“找到一些元素并对其进行某些处理”的概念，它可以用链改写为一条JavaScript命令。

利用链，下面的代码原来如下：

```css
//隐藏页面上的所有div
jQuery('div').hide();
//更新所有div中包含的文本
jQuery('div').text('new content');
//为所有div添加值为updatedContent的class属性
jQuery('div').addClass("updatedContent");
//显示页面上的所有div
jQuery('div').show();

```

更改后的代码如下：

```css
jQuery('div').hide().text('new content').addClass("updatedContent").show();

```

或者加上缩进和换行，如下所示：

```css
jQuery('div')
　　 .hide()
　　 .text('new content')
　　 .addClass("updatedContent")
　　 .show();

```

简而言之，链允许你在目前用jQuery函数选择（当前用jQuery功能包装起来）的元素上应用无限的jQuery方法链。在后台，每当应用jQuery方法之前，总是返回以前选择的元素，使链能够继续下去。在未来的秘诀中你将会看到，因为插件也以这种方式构造（返回包装的元素），所以使用插件也不会破坏这一链条。

虽然并非显而易见，但是根据对代码的研究，通过一次性选择一组DOM元素，由jQuery方法以链的方式进行多次操作，能够减少处理开销。避免不必要的DOM遍历是网页性能改进的关键部分，一定要尽可能重用或者缓存选中的DOM元素集。

#### 3．jQuery包装器集

大部分时候，如果jQuery很复杂，你会使用所谓的“包装器”。换句话说，你会从一个HTML页面上选择一组用jQuery功能包装的DOM元素。我个人常常将其称为“包装器集”或者“包装集”，因为它是一组由jQuery功能包装的元素。有时候这种包装器集包含单个DOM元素，其他时候则包含多个元素，甚至还有包装器集没有包含任何元素的情况。在这种情况下，jQuery提供的方法/属性在空包装器集中将会“无提示”地失败，这就可以避免不必要的if语句。

现在，以我们用于解释“寻找一些元素并对其进行某些处理”的代码为基础，如果在网页上添加几个<div>元素，你认为会发生什么情况呢？在下面这段更新过的代码示例中，添加了三个<div>元素，这样网页上一共有4个<div>元素：

```css
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<script type="text/JavaScript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.0/jquery.min.js"></script> </head>
<body>
<div>old content</div>
<div>old content</div>
<div>old content</div>
<div>old content</div>
<script>
//隐藏页面上的所有div
jQuery('div').hide().text('new content').addClass("updatedContent").show();
</script>
</body>
</html>

```

你在这里没有显式编写任何循环代码，但是猜猜看会怎么样？jQuery扫描网页，将所有<div>元素放在包装器集中，这样我所使用的jQuery方法在集合中的每个DOM元素上执行（亦称隐式迭代）。例如，.hide()方法实际上应用到集合中的每个元素。所以，如果再次查看代码，就会发现每个方法都应用到页面上的每个<div>元素，就像你编写了一个循环在每个DOM元素上调用各个jQuery方法一样。更新后的代码示例将导致页面中的所有<div>被隐藏，更新文本内容，指定一个新的类值，然后再次显示。

对包装器集和默认的循环系统（隐式迭代）的理解对于围绕循环的高级概念是至关重要的。你只要记住，在真正进行更多的循环（例如， `jQuery('div').each(function(){}` ）之前，已经发生了简单的循环。你也可以这样看：包装器中的每个元素一般都会被所调用的jQuery方法所改变。

还要记住一点，在以后的章节中你将会学习到，某些情况下只有第一个元素（而不是包装器集中的所有元素）受到jQuery方法（例如， `attr()` ）的影响。

