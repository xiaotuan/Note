[toc]

CSS 属性取值具体类型包括长度、角度、时间、频率、布局、分辨率、颜色、文本、函数、生成内容、图像和数字。

### 1. 长度值

长度值包括绝对值和相对值两类：

+ 绝对值

  常见绝对单位如下所示：

  + 英寸（in）：使用最广泛的长度单位。
  + 厘米（cm）：最常用的长度单位。
  + 毫米（mm）：在研究领域使用广泛。
  + 磅（pt）：也称点，在印刷领域使用广泛。
  + pica（pc）：在印刷领域使用。

+ 相对值

  相对值是根据屏幕分辨率、可视区域、浏览器设置，以及相关元素的大小等因素确定值的大小。常见相对单位如下所示：

  + em：表示字体高度，它能够根据字体的 font-size 值来确定大小，例如：

    ```css
    p { /* 设置段落文本属性 */
    	font-size: 12px;
        line-height: 2em;	/* 行高为 24px */
    }
    ```
    
    从上面样式代码中可以看出：一个 em 等于 font-size 的属性值。如果设置  font-size 属性的单位为 em，则 em 的值将根据父元素的 font-size 属性值来确定。例如:
    
    ```html
    <!DOCTYPE html>
    <html>
    	<head> 
    		<meta charset="utf-8"> 
    		<title>CSS3</title> 
    		<style type="text/css">
    			#main {
    				font-size: 12px;
    			}
    			p {
    				font-size: 2em;	/* 字体大小将显示为 24px */
    			}
    		</style>
    	</head>
    	<body>
    		<p>At first glance, it may appear that some listings are missing—Because working examples requires both HTML and CSS, I have put most listings in an HTML file, using <style> tags for the CSS. This means that both an HTML listing and CSS listing are combined in one file in the repository.</p>
    	</body>
    </html>
    ```
    
    同理，如果父对象的 font-size 属性的单位也为 em，则将依次向上级元素寻找参考的 font-size 属性值，如果没有定义，则会根据浏览器默认字体进行换算，默认字体一般为 16px。
    
  + ex：表示字母 x 的高度。
  
  + px：根据屏幕像素点来确定大小。
  
  + %：百分比也是一个相对单位值。百分比值总是通过另一个值来确定当前值，一般参考父对象中相同属性的值。