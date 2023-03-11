Tab 在栏目面板中比较常用，因为它能够在有限的空间内包含更多分类信息，适合商业网站的版面集成设计。
设计思路：利用 CSS 隐藏或显示栏目的部分内容，实际 Tab 面板所包含的全部内容都已经下载到客户端浏览器中。一般 Tab 面板仅显示一个 Tab 菜单项，当用户选择对应的菜单项之后，才会显示对应的内容。

**【操作步骤】**

第1步，启动 Dreamweaver，新建网页，保存为 test.html，在 `<body>` 标签内编写如下结构，构建HTML文档。

```html
<div id="tab">
    <div class="Menubox">
        <ul>
            <li id="tab_1" class="hover" onclick="setTab(1,4)">明星</li>
            <li id="tab_2" onclick="setTab(2,4)">搞笑</li>
            <li id="tab_3" onclick="setTab(3,4)">美女</li>
            <li id="tab_4" onclick="setTab(4,4)">摄影</li>
        </ul>
    </div>
    <div class="Contentbox">
        <div id="con_1" class="hover" ><img src="images/1.png" /></div>
        <div id="con_2" class="hide"><img src="images/2.png" /></div>
        <div id="con_3" class="hide"><img src="images/3.png" /></div>
        <div id="con_4" class="hide"><img src="images/4.png" /></div>
    </div>
</div>
```

在Tab面板中，`<div class="Menubox">` 框包含的内容是菜单栏，`<div class="Contentbox">` 框包含的是面板内容。

第2步，在 `<head>` 标签内添加 `<style type="text/css">` 标签，定义内部样式表，准备编写样式。
第3步，定义 Tab 菜单的 CSS 样式。这里包含3部分 CSS 代码：第 1 部分重置列表框、列表项和超链接默认样式，第 2 部分定义 Tab 选项卡基本结构，第 3 部分定义与 Tab 菜单相关的几个类样式。详细代码如下：

```css
/* 页面元素的默认样式
-------------------------------------------------------------------------------------*/
a {/* 超链接的默认样式 */
    color:#00F; 								/* 定义超链接的默认颜色 */
    text-decoration:none; 						/* 清除超链接的下划线样式 */
}
a:hover {/* 鼠标经过超链接的默认样式 */
    color: #c00; 								/* 定义鼠标经过超链接的默认颜色 */
}
ul {/* 定义列表结构基本样式 */
    list-style:none; 							/* 清除默认的项目符号 */
    padding:0; 								/* 清除补白 */
    margin:0px; 								/* 清除边界 */
    text-align:center; 							/* 定义包含文本居中显示 */
}
/* 选项卡结构
------------------------------------------------------------------------------------*/
#tab {/* 定义选项卡的包含框样式 */
    width:920px; 								/* 定义Tab面板的宽度 */
    margin:0 auto; 							/* 定义Tab面板居中显示 */
    font-size:12px; 							/* 定义Tab面板的字体大小 */
    overflow:hidden;							/* 隐藏超出区域的内容 */
}
/* 菜单样式类
-------------------------------------------------------------------------------------*/
.Menubox {/* Tab菜单栏的类样式 */
    width:100%;								/* 定义宽度，满包含框宽度显示 */
    background:url(images/tab1.gif); 				/* 定义Tab菜单栏的背景图像 */
    height:28px; 								/* 固定高度 */
    line-height:28px; 							/* 定义行高，间接实现垂直文本居中显示 */
}
.Menubox ul {/* Tab菜单栏包含的列表结构基本样式 */
    margin:0px; 								/* 清除边界 */
    padding:0px; 								/* 清除补白 */
}
.Menubox li {/* Tab菜单栏包含的列表项基本样式 */
    float:left; 								/* 向左浮动，实现并列显示 */
    display:block; 								/* 块状显示 */
    cursor:pointer; 							/* 定义手形指针样式 */
    width:114px; 								/* 固定宽度 */
    text-align:center; 							/* 定义文本居中显示 */
    color:#949694; 							/* 字体颜色 */
    font-weight:bold; 							/* 加粗字体 */
}
.Menubox li img{ width:100%;}
.Menubox li.hover {/* 鼠标经过列表项的样式类 */
    padding:0px; 								/* 清除补白 */
    background:#fff; 							/* 加亮背景色 */
    width:116px; 								/* 固定宽度显示 */
    border:1px solid #A8C29F; 					/* 定义边框线 */
    border-bottom:none; 						/* 清除底边框线样式 */
    background:url(images/tab2.gif); 				/* 定义背景图像 */
    color:#739242; 							/* 定义字体颜色 */
    height:27px; 								/* 固定高度 */
    line-height:27px; 							/* 定义行高，实现文本垂直居中 */
}
.Contentbox {/* 定义Tab面板中内容包含框基本样式类 */
    clear:both; 								/* 清除左右浮动元素 */
    margin-top:0px; 							/* 清除顶边界 */
    border:1px solid #A8C29F; 					/* 定义边框线样式 */
    border-top:none; 							/* 清除顶部边框线样式 */
    padding-top:8px; 							/* 定义顶部补白，增加与Tab菜单距离 */
}
.hide {/* 隐藏样式类 */
    display:none; 								/* 隐藏元素显示 */
}
```

第4步，使用 JavaScript 设计 Tab 交互效果。

下面函数定义了两个参数，第一个参数定义要隐藏或显示的面板，第二个参数定义当前 Tab 面板包含几个 Tab 选项卡，并定义当前选项卡包含的列表项的类样式为 hover，最后为每个 Tab 菜单中的li元素调用该函数即可，从而实现单击对应的菜单项，即可自动激活该脚本函数，并把当前列表项的类样式设置为 hover，同时显示该菜单对应的面板内容，而隐藏其他面板内容。

```html
<script>
function setTab(cursel,n){
	    for(i=1;i<=n;i++){
	        	var menu=document.getElementById("tab_"+i);
	        	var con=document.getElementById("con_"+i);
	        	menu.className=i==cursel?"hover":"";
	        	con.style.display=i==cursel?"block":"none";
	    }
}
</script>
```

**完整代码如下：**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>列表布局</title>
        <style type="text/css"> 
        /* 页面元素的默认样式
        -------------------------------------------------------------------------------------*/
        a {/* 超链接的默认样式 */
            color:#00F; 								/* 定义超链接的默认颜色 */
            text-decoration:none; 						/* 清除超链接的下划线样式 */
        }
        a:hover {/* 鼠标经过超链接的默认样式 */
            color: #c00; 								/* 定义鼠标经过超链接的默认颜色 */
        }
        ul {/* 定义列表结构基本样式 */
            list-style:none; 							/* 清除默认的项目符号 */
            padding:0; 								/* 清除补白 */
            margin:0px; 								/* 清除边界 */
            text-align:center; 							/* 定义包含文本居中显示 */
        }
        /* 选项卡结构
        ------------------------------------------------------------------------------------*/
        #tab {/* 定义选项卡的包含框样式 */
            width:920px; 								/* 定义Tab面板的宽度 */
            margin:0 auto; 							/* 定义Tab面板居中显示 */
            font-size:12px; 							/* 定义Tab面板的字体大小 */
            overflow:hidden;							/* 隐藏超出区域的内容 */
        }
        /* 菜单样式类
        -------------------------------------------------------------------------------------*/
        .Menubox {/* Tab菜单栏的类样式 */
            width:100%;								/* 定义宽度，满包含框宽度显示 */
            background:url(images/tab1.gif); 				/* 定义Tab菜单栏的背景图像 */
            height:28px; 								/* 固定高度 */
            line-height:28px; 							/* 定义行高，间接实现垂直文本居中显示 */
        }
        .Menubox ul {/* Tab菜单栏包含的列表结构基本样式 */
            margin:0px; 								/* 清除边界 */
            padding:0px; 								/* 清除补白 */
        }
        .Menubox li {/* Tab菜单栏包含的列表项基本样式 */
            float:left; 								/* 向左浮动，实现并列显示 */
            display:block; 								/* 块状显示 */
            cursor:pointer; 							/* 定义手形指针样式 */
            width:114px; 								/* 固定宽度 */
            text-align:center; 							/* 定义文本居中显示 */
            color:#949694; 							/* 字体颜色 */
            font-weight:bold; 							/* 加粗字体 */
        }
        .Menubox li img{ width:100%;}
        .Menubox li.hover {/* 鼠标经过列表项的样式类 */
            padding:0px; 								/* 清除补白 */
            background:#fff; 							/* 加亮背景色 */
            width:116px; 								/* 固定宽度显示 */
            border:1px solid #A8C29F; 					/* 定义边框线 */
            border-bottom:none; 						/* 清除底边框线样式 */
            background:url(images/tab2.gif); 				/* 定义背景图像 */
            color:#739242; 							/* 定义字体颜色 */
            height:27px; 								/* 固定高度 */
            line-height:27px; 							/* 定义行高，实现文本垂直居中 */
        }
        .Contentbox {/* 定义Tab面板中内容包含框基本样式类 */
            clear:both; 								/* 清除左右浮动元素 */
            margin-top:0px; 							/* 清除顶边界 */
            border:1px solid #A8C29F; 					/* 定义边框线样式 */
            border-top:none; 							/* 清除顶部边框线样式 */
            padding-top:8px; 							/* 定义顶部补白，增加与Tab菜单距离 */
        }
        .hide {/* 隐藏样式类 */
            display:none; 								/* 隐藏元素显示 */
        }
        </style>
        <script>
        function setTab(cursel,n){
                for(i=1;i<=n;i++){
                        var menu=document.getElementById("tab_"+i);
                        var con=document.getElementById("con_"+i);
                        menu.className=i==cursel?"hover":"";
                        con.style.display=i==cursel?"block":"none";
                }
        }
        </script>
    </head>
    <body>
        <div id="tab">
            <div class="Menubox">
                <ul>
                    <li id="tab_1" class="hover" onclick="setTab(1,4)">明星</li>
                    <li id="tab_2" onclick="setTab(2,4)">搞笑</li>
                    <li id="tab_3" onclick="setTab(3,4)">美女</li>
                    <li id="tab_4" onclick="setTab(4,4)">摄影</li>
                </ul>
            </div>
            <div class="Contentbox">
                <div id="con_1" class="hover" ><img src="images/1.png" /></div>
                <div id="con_2" class="hide"><img src="images/2.png" /></div>
                <div id="con_3" class="hide"><img src="images/3.png" /></div>
                <div id="con_4" class="hide"><img src="images/4.png" /></div>
            </div>
        </div>
    </body>
</html>
```

**运行效果如下：**

![17](./images/17.png)