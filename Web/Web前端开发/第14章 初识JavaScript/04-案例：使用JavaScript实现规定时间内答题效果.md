**案例：示例 14-02：使用 JavaScript 实现规定时间内答题效果**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta content="使用JavaScript实现规定时间内答题效果" />
        <title>使用JavaScript实现规定时间内答题效果</title>
        <style type="text/css">
            .body_content {
                width: 400px;
                border: 1px solid #E1E1E1;
                margin: auto;
                padding: 20px;
            }

            .MainTable {
                line-height: 45px;
            }

            .nextdiv {
                margin-top: 20px;
            }

            .body {
                /*设置页面宽度为100%*/
                width: 100%;
                /*设置页面宽度为100%*/
                height: 100%;
            }
        </style>
    </head>

    <body>
        <!--页面内容 begin-->
        <div id="bodyContent" class="body_content">
            <form method="post">
                <table class="MainTable" id="QuestionBox">
                    <tbody>
                        <tr>
                            <td style="font-weight: bold">第一题：</td>
                        </tr>
                        <tr>
                            <td>下列哪种语言在目前应用中不区分大小写：</td>
                        </tr>
                        <tr>
                            <td>
                                <label>
                                    <input type="radio" />
                                    A、HTML5</label>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label>
                                    <input type="radio" />
                                    B、CSS3</label>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label>
                                    <input type="radio" />
                                    C、JavaScript</label>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <div id="TimingInfo">
                    <div><span>倒计时：<span id="save_info">20</span>秒</span></div>
                    <div class="nextdiv">
                        <input type="button" name="form_save" onclick="next()" value="下一题" />
                    </div>
                </div>
            </form>
            <table id="question_3" style="display: none;">
                <tbody>
                    <tr>
                        <td style="font-weight: bold">第二题：</td>
                    </tr>
                    <tr>
                        <td>在HTML文档中，引用外部样式表的标准位置是：</td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                <input type="radio" />
                                A、文档尾部</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                <input type="radio" />
                                B、文档顶部</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                <input type="radio" />
                                C、head元素部分</label>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table id="question_2" style="display: none;">
                <tbody>
                    <tr>
                        <td style="font-weight: bold">第三题：</td>
                    </tr>
                    <tr>
                        <td>下面的元素标记中，哪一个元素标记可以正确的换行：</td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                <input type="radio" />
                                A、br</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                <input type="radio" />
                                B、break</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                <input type="radio" />
                                C、bt</label>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table id="question_1" style="display: none;">
                <tbody>
                    <tr>
                        <td style="font-weight: bold">第四题：</td>
                    </tr>
                    <tr>
                        <td>下面的语句中，哪一个不能获取元素对象：</td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                <input type="radio" />
                                A、getElementById</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                <input type="radio" />
                                B、getElementsByTagName</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>
                                <input type="radio" />
                                C、getElementsByTag</label>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <!--页面内容 end-->
        <!--JS 执行-->
        <script>
            var num = 3;
            var i = 20;
            //声明计时函数
            var intervalid;
            intervalid = setInterval("Timing()", 1000);
            function Timing() {
                document.getElementById("save_info").innerHTML = i;
                if (i == 0) {
                    //执行隐藏函数
                    next();
                    //清除计时函数
                    clearInterval(intervalid);
                }
                i--;
            }
            //执行答题结束操作
            function next() {
                //获取展示内容元素对象
                var main = document.getElementById("QuestionBox");
                //判断是否为最后一题
                if (num == 0) {
                    //隐藏倒计时及答题按钮
                    document.getElementById("TimingInfo").style.display = "none";
                    main.innerHTML = "答题结束";
                } else {
                    //显示下一道题目
                    var content = document.getElementById("question_" + num).innerHTML;
                    main.innerHTML = content;
                    //重新执行计时语句
                    i = 20;
                    document.getElementById("save_info").innerHTML = i;
                    intervalid = setInterval("Timing()", 1000);
                }
                num--;
            }
        </script>
    </body>
</html>
```

