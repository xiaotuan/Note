[toc]

### 1. 新增 form 元素

HTML5 中新增了几个 form 元素，分别是 datalist、keygen 和 output。

#### 1.1 datalist

datalist 元素用于为输入框提供一个可选的列表，用户可以直接选择列表中的某一预设的项，从而免去输入的麻烦。该列表由 datalist 中的 option 元素创建。如果用户不希望从列表中选择某项，也可以自行输入其他内容。

在实际应用中，如果要把 datalist 提供的列表绑定到某一输入框，则使用输入框的 list 属性来引用 datalist 元素的 id 就可以了。

**案例：示例 5-07：datalist 元素**

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta keywords="HTML5 form" />
    <meta content="datalist元素" />
    <title>datalist元素</title>
  </head>

  <body>
    <form>
      <datalist id="TelephoneInfo">
        <option value="13526688704" label="Mobile Phone"></option>
        <option value="0371-65962530" label="Office Phone"></option>
        <option value="0371-63068118" label="House Phone"></option>
      </datalist>
      <p>请选择联系方式：<input type="tel" name="Telephone" id="Telephone" list="TelephoneInfo">
      <p><input type="submit" value="确定">
    </form>
  </body>
</html>
```

#### 1.2 keygen

keygen 元素是秘钥对生成器，能够使用户验证更为可靠。用户提交表单时会生成两个键，一个私钥，其中私钥会被存储在客户端，而公钥则会被发送到服务器。公钥可用于验证用户的客户端证书。

**案例：示例 5-08：keygen 元素**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="keygen属性" />
		<title>keygen属性</title>
	</head>

	<body>
		<form action="testform.asp" method="get">
			请输入用户名：<input type="text" name="user_name"><br>
			请选择加密强度：<keygen name="security"><br>
			<input type="submit" value="提交">
		</form>
	</body>
</html>
```

> 注意：浏览器不支持 keygen 元素。

#### 1.3 output

Output 元素定义不同类型的输出，比如计算结果或者脚本的输出。output 元素必须从属于某个表单，也就是说，必须将它书写在表单内部，或者对它添加 form 属性。

**案例：示例 5-09：output 元素**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 form" />
        <meta content="output元素" />
        <title>output元素</title>
    </head>

    <body>
        <form oninput="x.value=parseInt(a.value)+parseInt(b.value)">0
            <input type="range" id="a" value="50">100
            +<input type="number" id="b" value="50">
            =<output name="x" for="a b"></output>
        </form>
    </body>
</html>
```

### 2. form 属性总览

<center><b>表 5-1 form 属性总览</b></center>

| 属性名称     | 描述                                         |
| ------------ | -------------------------------------------- |
| name         | 设置表单名称                                 |
| method       | 设置表单发送的方法，可以是 "post" 或者 "get" |
| action       | 设置表单处理程序                             |
| enctype      | 设置表单的编码方式                           |
| target       | 设置表单显示目标                             |
| autocomplete | 规定 form 或 input 域应该拥有自动完成功能    |
| novalidate   | 规定在提交表单时不应该验证 form 或 input 域  |

### 3. 新增 form 属性

#### 3.1  autocomplete

form 元素的 autocomplete 属性用于规定 form 中所有元素都拥有自动完成功能。该属性和 input 中的 autocomplete 属性用法相同，只不过当 autocomplete 属性用于整个 form 时，所有从属于该 form 的元素便都具备自动完成功能。如果要使个别元素关闭自动完成功能，则单独为该元素指定 `autocomplete="off"` 即可。

#### 3.2 novalidate

form 元素的 novalidate 属性用于提交表单时取消整个表单的验证，即关闭对表单内所有的有效性检查。如果只取消表单中较少部分内容的验证而不妨碍提交大部分内容，则可以将 novalidate 属性单独用于 form 中的这些元素。

**案例：示例 5-10：novalidate 属性**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="novalidate属性" />
		<title>novalidate属性</title>
	</head>

	<body>
		<form action="testform.asp" method="get" novalidate="true">
			请输入电子邮件地址：<input type="email" name="user_email">
			<input type="submit" value="提交">
		</form>
	</body>
</html>
```

