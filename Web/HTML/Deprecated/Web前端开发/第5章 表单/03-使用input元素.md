[toc]

### 1. input 类型总览

<center><b>表 5-2 input 输入类型</b></center>

| 输入类型   | HTML代码                  | 描述                                                         |
| ---------- | ------------------------- | ------------------------------------------------------------ |
| 文本域     | `<input type=text">`      | 定义单行输入文本域，用于在表单中输入字母、数字等内容。默认宽度为 20 个字符 |
| 单选按钮   | `<input type="radio">`    | 定义单选按钮，用于从若干给定的选项中选取其一，常由多个标签构成一组使用 |
| 复选框     | `<input type="checkbox">` | 定义复选框，用于从若干给定的选择中选取一项或若干选项         |
| 密码域     | `<input type="password">` | 定义密码字段，用于输入密码，元素的内容会以点或星号的形式出现，即被掩码 |
| 提交按钮   | `<input type="submit">`   | 定义提交按钮，用于将表单数据发送到服务器                     |
| 可单击按钮 | `<input type="button">`   | 定义普通可单击按钮，多数情况下，用于通过 JavaScript 启动脚本 |
| 图像按钮   | `<input type="image">`    | 定义图像形式的提交按钮。用户可以通过选择不同的图像来自定义这种按钮的样式 |
| 隐藏域     | `<input type="hidden">`   | 定义隐藏的输入字段                                           |
| 重置按钮   | `<input type="reset">`    | 定义重置按钮。用户可以通过单击重置按钮以清除表单中的所有数据 |
| 文件域     | `<input type="file">`     | 定义输入字段和 "浏览" 按钮，用于上传文件                     |

### 2. 新增 input 类型

#### 2.1 email

email 类型的 input 元素是专门用于输入 E-mail 地址的文本输入框，在提交表单的时候，会自动验证 email 输入框的值。如果不是一个有效的 E-mail 地址，则该输入框不允许提交表单。

**案例：示例 5-11：email 类型**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 form" />
        <meta content="email类型" />
        <title>email类型</title>
    </head>

    <body>
        <form action="form.php" method="post" name="FomeDemo">
            <p>请输入电子邮件地址：<input type="email" name="AddressEmail">
            <p><input type="submit" value="确定" name="FormSubmit">
        </form>
    </body>
</html>
```

#### 2.2 url

url 类型的 input 元素提供用于输入 url 地址这类特殊文本的文本框。当提交表单时，如果所输入的内容是 url 地址格式的文本，则会提交数据到服务器；如果不是 url 地址格式的文本，则给出提示信息，并不允许提交数据。

**案例：示例 5-12：url 类型**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 form" />
        <meta content="url类型" />
        <title>url类型</title>
    </head>

    <body>
        <form action="form.php" method="post" name="FomeDemo">
            <p>请输入个人网站地址：<input type="url" name="AddressURL">
            <p><input type="submit" value="确定" name="FormSubmit">
        </form>
    </body>
</html>
```

#### 2.3 number

number 类型的 input 元素提供用于输入纯数值的文本框。可以设定对所接受的数字的限制，包括规定允许的最大值和最小值、合法的数字间隔或默认值等，如果所输入的数字不在限定范围之内，则会出现错误提示。

<center><b>表 5-3 number 类型的属性</b></center>

| 属性名称 | 值     | 描述                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| max      | number | 规定允许的最大值                                             |
| min      | number | 规定允许的最小值                                             |
| step     | number | 规定合法的数字间隔（如果 step="4"，则合法的数是 -4、0、4、8等） |
| value    | number | 规定默认值                                                   |

**案例：示例 5-13：number 类型**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 form" />
        <meta content="number" />
        <title>number</title>
    </head>

    <body>
        <form action="form.php" method="post" name="FomeDemo">
            <p>请输入数字：<input type="number" name="InputNum">
            <p>请输入10-15之间的数字：<input type="number" min="10" max="15" name="InputNum2">
            <p>请输入10-20之间的偶数：<input type="number" min="10" max="20" step="2" name="InputNum3">
            <p><input type="submit" value="确定" name="FormSubmit">
        </form>
    </body>
</html>
```

#### 2.4 range

range 类型的 input 元素提供用于输入包含一定范围内数字值的文本框，在网页中显示为滑动条。可以设定对数字的限制，包括规定允许的最大值和最小值、合法的数字间隔或默认值等。如果所输入的数字不在限制范围之内，则会出现错误提示。

<center><b>表 5-4 range 类型的属性</b></center>

| 属性名称 | 值     | 描述                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| max      | number | 规定允许的最大值                                             |
| min      | number | 规定允许的最小值                                             |
| step     | number | 规定合法的数字间隔（如果 step="4"，则合法的数是 -4、0、4、8等） |
| value    | number | 规定默认值                                                   |

**案例：示例 5-14：range 类型**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 form" />
        <meta content="范围类型" />
        <title>范围类型</title>
    </head>

    <body>
        <form action="form.php" method="post" name="FomeDemo">
            <p>请输入数字：<input type="range" min="1" max="100" step="5" name="RangeNum">
            <p><input type="submit" value="确定" name="FormSubmit">
        </form>
    </body>
</html>
```

#### 2.5 日期检出器

<center><b>表 5-5 日期检出器类型</b></center>

| 输入类型       | HTML代码                        | 描述                             |
| -------------- | ------------------------------- | -------------------------------- |
| date           | `<input type="date">`           | 选取日、月、年                   |
| month          | `<input type="month">`          | 选取月、年                       |
| week           | `<input type="week">`           | 选取周、年                       |
| time           | `<input type="time">`           | 选取时间（小时和分钟）           |
| datetime       | `<input type="datetime">`       | 选取时间、日、月、年（UTC时间）  |
| datetime-local | `<input type="datetime-local">` | 选取时间、日、月、年（本地时间） |

##### 2.5.1 date 类型

**案例：示例 5-15：date 类型**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="date类型" />
		<title>date类型</title>
	</head>

	<body>
		<form action="date.php" method="get">
			请输入日期：<input type="date" name="date1" />
			<input type="submit" />
		</form>
	</body>
</html>
```

##### 2.5.2 month 类型

**案例：示例 5-16：month 类型**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="month类型" />
		<title>month类型</title>
	</head>

	<body>
		<form action="date.php" method="get">
			请输入月份：<input type="month" name="month1" />
			<input type="submit" />
		</form>
	</body>
</html>
```

##### 2.5.3 week 类型

**案例：示例 5-17：week 类型**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="week类型" />
		<title>week类型</title>
	</head>

	<body>
		<form action="date.php" method="get">
			请选择年份和周数：<input type="week" name="week1" />
			<input type="submit" />
		</form>
	</body>
</html>
```

##### 2.5.4 time 类型

<center><b>表 5-6 time 类型的属性</b></center>

| 属性名称 | 值     | 描述               |
| -------- | ------ | ------------------ |
| max      | time   | 规定允许的最大值   |
| min      | time   | 规定允许的最小值   |
| step     | number | 规定合法的时间间隔 |
| value    | time   | 规定默认值         |

**案例：示例 5-18：time 类型**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="time类型" />
		<title>time类型</title>
	</head>

	<body>
		<form action="date.php" method="get">
			请选择或输入时间：<input type="time" name="time1" />
			<input type="submit" />
		</form>
	</body>
</html>
```

**案例：示例 5-19：time 限定时间**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="time限定时间" />
		<title>time限定时间</title>
	</head>

	<body>
		<form action="date.php" method="get">
			请选择或输入时间：<input type="time" name="time1" step="5" value="12:05:15" />
			<input type="submit" />
		</form>
	</body>
</html>
```

##### 2.5.5 datetime 类型

**案例：示例 5-20：datetime 类型**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="datetime类型" />
		<title>datetime类型</title>
	</head>

	<body>
		<form action="date.php" method="get">
			请选择或输入时间：<input type="datetime" name="datetime1" />
			<input type="submit" />
		</form>
	</body>
</html>
```

> 注意：datetime 类型无效。

##### 2.5.6 datetime-local 类型

**案例：示例 5-21：datetime-local 类型**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="datetime-local类型" />
		<title>datetime-local类型</title>
	</head>

	<body>
		<form action="date.php" method="get">
			请选择或输入时间：<input type="datetime-local" name="datetime-local1" />
			<input type="submit" />
		</form>
	</body>
</html>
```

#### 2.6 search

Search 类型的 input 元素可提供用于输入搜索关键词的文本框。

**案例：示例 5-22：search 类型**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 form" />
        <meta content="search类型" />
        <title>search类型</title>
    </head>

    <body>
        <form action="form.php" method="post" name="FomeDemo">
            <p>请输入搜索内容：<input type="search" name="SearchText">
            <p><input type="submit" value="进行搜索" name="FormSubmit">
        </form>
    </body>
</html>
```

#### 2.7 tel

tel 类型的 input 元素提供专门用于输入电话号码的文本框。

**案例：示例 5-23：tel 类型**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 form" />
        <meta content="tel类型" />
        <title>tel类型</title>
    </head>

    <body>
        <form action="form.php" method="post" name="FomeDemo">
            <p>请输入电话号码：<input type="tel" name="telphoneNum">
            <p><input type="submit" value="确定" name="FormSubmit">
        </form>
    </body>
</html>
```

#### 2.8 color

color 类型的 input 元素提供专门用于设置颜色的文本框。

**案例：示例 5-24：color 类型**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 form" />
        <meta content="color类型" />
        <title>color类型</title>
    </head>

    <body>
        <form action="form.php" method="post" name="FomeDemo">
            <p>请选择色彩值：<input type="color" name="ColorValue">
            <p><input type="submit" value="确定" name="FormSubmit">
        </form>
    </body>
</html>
```

### 3. input 属性总览

<center><b>表 5-7 input 属性总览</b></center>

| 属性名称       | 属性值                                                       | 描述                                                         |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| accept         | list_of_mime_types                                           | 规定可通过文件上传控件提交的文件类型<br />（仅适用于 type="file"） |
| alt            | text                                                         | 规定图像输入控件的替代文本<br />（仅适用于 type="image"）    |
| autocomplete   | on<br />off                                                  | 规定是否使用输入字段的自动完成功能                           |
| autofocus      | autofocus                                                    | 规定输入字段在页面加载时是否获得焦点<br />（不适用于 type="hidden"） |
| checked        | checked                                                      | 规定当页面加载时是否预先选择该 input 元素<br />（适用于 type="checkbox" 或 type="radio"） |
| disabled       | disabled                                                     | 规定当页面加载时是否禁用该 input 元素<br />（不适用于 type="hidden"） |
| form           | formname                                                     | 规定输入字段所属的一个或多个表单                             |
| formaction     | URL                                                          | 覆盖表单的 action 属性<br />（适用于 type="submit" 和 type="image"） |
| formenctype    | 见描述                                                       | 覆盖表单的 enctype 属性<br />（适用于 type="submit" 和 type="image"） |
| formmethod     | get<br />post                                                | 覆盖表单的 method 属性<br />（适用于 type="submit" 和 type="image"） |
| formnovalidate | formnovalidate                                               | 覆盖表单的 novalidate 属性<br />如果使用该属性，则提交表单时不进行验证 |
| formtarget     | \_blank、\_self、\_parent<br />、 \_top、framename           | 覆盖表单的 target 属性<br />（适用于 type="submit" 和 type="image"） |
| height         | pixels、%                                                    | 定义 input 字段的高度（适用于 type="image"）                 |
| list           | datalist-id                                                  | 引用包含输入字段的预定义选项的 datalist                      |
| max            | number<br />date                                             | 规定输入字段的最大值<br />请与 "min" 属性配合使用，来创建合法值的范围 |
| maxlength      | number                                                       | 规定文本字段中允许的最大字符数                               |
| min            | number<br />date                                             | 规定输入字段的最小值<br />请与 "max" 属性配合使用，来创建合法值的范围 |
| multiple       | multiple                                                     | 如果使用该属性，则允许一个以上的值                           |
| name           | field_name                                                   | 规定 input 元素的名称<br />name 属性用于在提交表单时搜索字段的值 |
| pattern        | regexp_pattern                                               | 规定输入字段的值的模式或格式<br />例如 pattern="[0-9]" 表示输入值必须是 0 与 0 之间的数字 |
| placeholder    | text                                                         | 规定帮助用户填写字段的提示                                   |
| readonly       | readonly                                                     | 指示输入字段的值无法修改                                     |
| required       | required                                                     | 指示输入字段的值是必需的                                     |
| size           | number_of_char                                               | 规定输入字段中的可见字符数                                   |
| src            | URL                                                          | 规定图像的 URL （适用于 type="image"）                       |
| step           | number                                                       | 规定输入字段的合法数字间隔                                   |
| type           | button、checkbox、date、<br />datetime、datatime-local、<br />email、file、hidden、<br />image、month、number、<br />password、radio、range<br />reset、submit、text、time<br />url、week | 规定 input 元素的类型                                        |
| value          | value                                                        | 对于按钮：规定按钮上的文本<br />对于图像按钮：传递到脚本的字段的符号结果<br />对于复选框和单选按钮：定义 input 元素被单击时的结果。<br />对于隐藏、密码和文本字段：规定元素的默认值<br />注释：不能与 type="file" 一同使用<br />注释：对于 type="checkbox" 以及 type="radio"，是必需的 |
| width          | pixels<br />%                                                | 定义 input 字段的宽度（适用于 type="image"）                 |

### 4. 新增的 input 属性

 #### 4.1 autocomplete

autocomplete 属性可以应用于 text、search、url、telephone、email、password、datepickers、range 以及 color 的 input 类型。只要开启了该功能，用户下次输入相同的内容时，浏览器就会自动完成内容的输入。

autocomplete 的属性值可以指定为 "on"、"off" 与 "" （不指定）这三种值。不指定时，使用浏览器的默认值。使用 datalist 元素与 list 属性提供候补输入的数据列表，自动完成时，可以将该 datalist 元素中的数据作为候补输入的数据在文本框中自动显示：

```html
<input type="text" name="greeting" autocomplete="on" list="greeting">
```

**案例：示例 5-25：autocomplete 属性**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="autocomplete属性" />
		<title>autocomplete属性</title>
	</head>

	<body>
		<h2>HTML 5自动完成功能示例</h2>
		输入你最喜欢的城市名称<br><br>
		<form autocomplete="on">
			<input type="text" id="city" list="citylist">
			<datalist id="citylist" style="display:none;">
				<option value="BeiJing">BeiJing</option>
				<option value="ShangHai">ShangHai</option>
				<option value="HeNan">HeNan</option>
				<option value="GuangZhou">GuangZhou</option>
			</datalist>
		</form>
	</body>
</html>
```

#### 4.2 autofocus

autofocus 属性值是一个布尔值，可以使得在页面加载时某个表单控件自动获得焦点。这些控件可以是文本框、复选框、单选按钮和普通按钮等所有 `<input>` 标签的类型。

```html
<input type="text" name="user_name" autofocus="autofocus">
```

**案例：示例 5-26：autofocus 属性**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="autofocus属性" />
		<title>autofocus属性</title>
	</head>

	<body>
		<form action="form.php" method="post" name="FomeDemo">
			<p>
				<input type="search" id="SearchText" placeholder="请输入搜索关键词" size="50" required autofocus>
				<script>
					if (!("autofocus" in document.createElement("input"))) {
						document.getElementById("SearchText").focus();
					}
				</script>
				<input type="submit" value="进行搜索" name="FormSubmit">
		</form>
	</body>
</html>
```

#### 4.3 form

使用 form 属性，便可以把表单内表单控件元素写在页面中的任一位置，然后只需为这个元素指定 form 属性并设置属性值为该表单的 id 即可。此外，form 属性也允许规定一个表单控件元素从属于多个表单。form 属性适用于所有的 input 输入类型，在使用时，必须引用所属表单的 id。

**案例：示例 5-27：form 属性**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="form属性" />
		<title>form属性</title>
	</head>

	<body>
		<nav>
			<p><input type="search" name="SearchText" placeholder="请输入搜索关键词" form="FormDemo">
		</nav>
		<form action="Form.php" method="get" id="FormDemo">
			<p>请输入邮编：
				<input type="text" name="PostalCode" size="20" pattern="[0-9]{6}" title="请输入六位数字的邮政编码。" autofocus>
				<script>
					if (!("autofocus" in document.createElement("input"))) {
						document.getElementById("PostalCode").focus();
					}
				</script>
				<input type="submit" value="确定">
		</form>
	</body>
</html>
```

如果一个 form 属性需要引用两个或两个以上的表单，则需要使用空格将表单的 id 分隔开。

```html
<input type="text" name="user_name" form="form1 form2 form3">
```

#### 4.4 表单重写

用于重写 form 元素的某些属性设定，这些表单重写属性包括以下几种。

+ formaction：用于重写表单的 action 属性。
+ formenctype：用于重写表单的 enctype 属性。
+ formmethod：用于重写表单的 method 属性。
+ formnovalidate：用于重写表单的 novalidate 属性。
+ formtarget：用于重写表单的 target 属性。

表单重写属性只使用于 submit 和 image 输入类型。

**案例：示例 5-28：新增重写属性**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="HTML5新增重写属性" />
		<title>HTML5新增重写属性</title>
	</head>

	<body>
		<form action="demo.asp" id="testform">
			请输入电子邮件地址：<input type="email" name="userid"><br>
			<input type="submit" value="提交到页面1" formaction="demo1.asp">
			<input type="submit" value="提交到页面2" formaction="demo2.asp">
			<input type="submit" value="提交到页面3" formaction="demo3.asp">
		</form>
	</body>
</html>
```

#### 4.5 height 与 width

height 和 width 属性可用于规定 image 类型和 imput 标签的图像高度和宽度，这两个属性只适用于 image 类型的 `<input>` 标签。

**案例：示例 5-29：height 与 width 属性**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="HTML5新增 height与width属性" />
		<title>HTML5新增 height与width属性
		</title>
	</head>

	<body>
		<form action="" method="get">
			请输入用户名：<input type="text" name="user_name"><br>
			<input type="image" src="image/submit.jpg" width="50" height="50">
		</form>
	</body>
</html>
```

#### 4.6 list

list 属性用于指定输入框所绑定的 datalist 元素，其值是某个 datalist 的 id。

**案例：示例 5-30：list 属性**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="list属性" />
		<title>list属性</title>
	</head>

	<body>
		<form action="testform.asp" method="get">
			请输入网址:<input type="url" list="url_list" name="weblink">
			<datalist id="url_list">
				<option label="新浪" value="http://www.sina.com.cn">
				<option label="网易" value="http://www.sohu.com">
				<option label="搜狐" value="http://www.163.com">
			</datalist>
			<input type="submit" value="提交">
		</form>
	</body>
</html>
```

#### 4.7 min、max 和 step

**案例：示例 5-31：min、max 和 step 属性**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="min、max和step属性" />
		<title>min、max和step属性</title>
	</head>

	<body>
		<form action="testform.asp" method="get">
			请输入数值：<input type="number" name="number1" min="0" max="20" step="4">
			<input type="submit" value="提交">
		</form>
	</body>
</html>
```

#### 4.8 multiple

在 HTML5 之前，input 输入类型中 file 类型只支持单个文件上传，而新增的 multiple 属性支持一次选择多个文件，并且该属性同样支持新增的 email 类型。

**案例：示例 5-32：multiple 属性**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="multiple属性" />
		<title>multiple属性</title>
	</head>

	<body>
		<form action="testform.asp" method="get">
			请选择要上传的多个文件：<input type="file" name="img" multiple="multiple">
			<input type="submit" value="提交">
		</form>
	</body>
</html>
```

#### 4.9 pattern

pattern 属性用于验证 input 类型输入框中用户输入的内容是否与自定义的正则表达式相匹配，该属性适用于 text、search、url、telephone、email、password 类型的 `<input>` 标签。

**案例：示例 5-33：pattern 属性**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 form" />
		<meta content="pattern属性" />
		<title>pattern属性</title>
	</head>

	<body>
		<form action="form.php" method="post" name="FomeDemo">
			<p>请输入邮编：
				<input type="text" id="PostalCode" size="20" pattern="[0-9]{6}" title="请输入六位数字的邮政编码。" required autofocus>
				<script>
					if (!("autofocus" in document.createElement("input"))) {
						document.getElementById("PostalCode").focus();
					}
				</script>
				<input type="submit" value="确定" name="FormSubmit">
		</form>
	</body>
</html>
```

#### 4.10 placeholder

placeholder 属性用于为输入框提供一种提示，这种提示可以描述输入框期待用户输入何种内容，在输入框为空时显示出现，而当输入框获得焦点时则会消失。placeholder 属性适用于 text、search、url、telephone、email 和 password 类型的 `<input>` 标签。

**案例：示例 5-34：placeholder 属性**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 form" />
        <meta content="占位字符" />
        <title>占位字符</title>
    </head>

    <body>
        <form action="form.php" method="post" name="FomeDemo">
            <p><input type="search" name="SearchText" placeholder="请输入搜索关键词">
            <p><input type="submit" value="进行搜索" name="FormSubmit">
        </form>
    </body>
</html>
```

#### 4.11 required

用于规定输入框填写的内容不能为空，否则不允许用户提交表单。该属性用于 text、search、url、telephone、email、password、datepickers、number、checkbox、radio 和 file 类型的 `<input>` 标签。

**案例：示例 5-35：required 属性**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 form" />
        <meta content="required属性" />
        <title>required属性</title>
    </head>

    <body>
        <form action="form.php" method="post" name="FomeDemo">
            <p><input type="search" name="SearchText" placeholder="请输入搜索关键词" required>
            <p><input type="submit" value="进行搜索" name="FormSubmit">
        </form>
    </body>
</html>
```



