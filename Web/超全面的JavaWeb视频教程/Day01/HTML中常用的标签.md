<center><font size="5"><b>HTML 中常用的标签</b></font></center>

1. 文字标签和注释标签
    + 文字标签：修改文字的样式。
        + \<font\>\</font\>
        + 属性：
            + size：文字大小。取值范围: 1-7，超出了7，默认还是7
            + color：文字颜色。两种表示方式：英文单词（比如 red、green）和十六进制数表示（比如 #66cc66）
        
    + 注释标签
      
        + \<!-- html注释 --\>
    
2. 标题标签
    + \<h1\>\<h1/\>、\<h2\>\<h2/\> ...... \<h6\>\<h6/\>
    + 从 h1 到 h6，大小是依次变小，同时会自动换行。
    
3. 水平线标签
    + \<hr/\>
    + 属性：
        + size：水平线的粗细，取值范围 1 - 7
        + color：颜色
        ```html
        <hr size="5" color="blue" />
        ```
    
4. 特殊字符
    + < ： \&lt;
    + \> ： \&gt;
    + 空格 ： \&nbsp;
    + \& ：\&amp;
    + 双引号&quot; ： \&quot;
    + 注册符 &reg;： \&reg;
    + 版权符&copy; ： \&copy;
    
5. 列表标签
    + \<dl\>\<dl/\>
        + 在 dl 里面 \<dt\>\</dt\>：上层内容
        + 在 dl 里面 \<dd\>\</dd\>：下层内容
        ```html
        <dl>
            <dt>传智播客</dt>
            <dd>财务部</dd>
            <dd>学工部</dd>
            <dd>人事部</dd>
        </dl>
        ```
    + \<ol\>\</ol\>：有序列表的范围
        + 属性 type：设置排序方式，1（默认）、a、i
        + 在 ol 标签里面 \<li\>具体内容\</li\>
            ```html
            <ol>
                <li>财务部</li>
                <li>学工部</li>
                <li>人事部</li>
            </ol>
            ```
    + \<ul\>\</ul\>：无序列表的范围
        + 属性 type：空心圆 circle、实心圆 disc、实心方块 square、默认 disc
        + 在 ul 里面 \<li\>\</li\>
        ```html
        <ul>
            <li>财务部</li>
            <li>学工部</li>
            <li>人事部</li>
        </ul>
        ```
    
6. 图像标签
    ```
    <img src="图片的路径" />
    ```

    + src：图片的路径
    + width：图片的宽度
    + height：图片的高度
    + alt：图片上显示的文字，把鼠标移动到图片上，停留片刻显示内容（有些浏览器下不显示，没有效果）
    
7. 超链接标签
    + 链接资源
        + \<a href="链接到资源的路径">显示在页面上的内容\</a\>
        + href：链接的资源的地址
        + target：设置打开的方式，默认是在当前页打开。
            + blank：在一个新窗口打开
            + self：在当前页打开（默认）
        + 当超链接不需要到任何的地址，在 href 里面加 #（`<a href="#">这是一个超链接2</a>
    + 定位资源
        如果想要定位资源：定义一个位置（`<a name="top">顶部</a>），回到这个位置（`<a href="#top">回到顶部</a>`）
    
8. 原样输出标签
    \<pre\>内容\</pre\>
    
9. 表格标签
  
    + \<table\>\</table\>：表示表格的范围
        + border：表格线
        + bordercolor：表格线的颜色
        + cellspacing：单元格直接的距离
        + width：表格的宽度
        + height：表格的高度
        
    + 在 table 里面 \<tr\>\</tr\>
        + 设置对齐方式 align：left、center、right
        + 在 tr 里面 \<td\>\</td\>
            + 设置对齐方式 align：left、center、right
        + 使用 th 也可以表示单元格：表示可以实现居中和加粗
        ```html
        <table border="1" bordercolor="blue" cellspacing="0" width = "200" height="150">
        ```
    + 表格的标题：\<caption\>\</caption\>
    + 合并单元格
        + rowspan：跨行
        + colspan：跨列
        ```html
        <td colspan="3">人员信息</td>
        ```
    
10. 表单标签
    + \<form\>\</form\>：定义一个表单的范围
    + 输入项：可以输入内容或者选择内容的部分
        + 大部分的输入项使用 \<input type="输入项的类型" /\>
        + 普通输入项：\<input type="text" /\>
        + 密码输入项：\<input type="password" /\>
        + 单选输入项：\<input type="radio" /\>
            + 在里面需要属性 name
            + name 的属性值必须要相同
        + 复选输入项：\<input type="checkbox" /\>
            + 在里面需要属性 name
            + name 的属性值必须要相同
        + 文件输入项（在后面上传时候用到）
            
            + \<input type="file" /\>
        + 下拉输入项（不是在 input 标签里面的）
            ```html
            <select name="birth">
                <option value="1991">1991</option>
                <option value="1992">1992</option>
                <option value="1993">1993</option>
            </select>
            ```
        + 文本域
            `<textarea cols="10" rows="10"></textarea>`
        + 隐藏项（不会显示在页面上，但是存在于 html 代码里面）
            `<input type="hidden" />`

