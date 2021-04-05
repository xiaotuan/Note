**案例：示例 15-27：使用 jQuery 进行表单验证**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="HTML5 video" />
        <meta content="Web前端开发技术与实践,表单验证" />
        <title>使用jQuery进行表单验证</title>
        <style>
            .MainTable {
                width: 500px;
                line-height: 45px;
                margin: auto;
                border: 1px solid #E1E1E1;
                padding: 20px;
            }

            .MainTable td {
                padding: 0 10px 0 0;
            }

            .MainTable td font {
                padding-left: 10px;
            }

            .MainTable input {
                width: 191px;
                height: 30px;
                padding-left: 10px;
                padding-right: 10px;
                border: 1px #E1E1E1 solid;
            }

            .body {
                /*设置页面宽度为100%*/
                width: 100%;
                /*设置页面宽度为100%*/
                height: 100%;
            }

            .td_left {
                width: 150px;
                text-align: right;
            }
        </style>
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
    </head>

    <body>
        <!--页面内容 begin-->
        <div id="bodyContent" class="body-content">
            <form method="post">
                <table class="MainTable">
                    <tr>
                        <td class="td_left">用户名：</td>
                        <td><input type="text" name="form_loginname" id="form_loginname" /></td>
                    </tr>
                    <tr>
                        <td class="td_left">姓名：</td>
                        <td><input type="text" name="form_username" id="form_username" /></td>
                    </tr>
                    <tr>
                        <td class="td_left">密码：</td>
                        <td><input type="password" name="form_password" id="form_password" /></td>
                    </tr>
                    <tr>
                        <td class="td_left">确认密码：</td>
                        <td><input type="password" name="form_checkpassword" id="form_checkpassword" /></td>
                    </tr>
                    <tr>
                        <td class="td_left">邮箱：</td>
                        <td><input type="email" name="form_email" id="form_email" /></td>
                    </tr>
                    <tr>
                        <td class="td_left">手机：</td>
                        <td><input type="tel" name="form_tel" id="form_tel" /></td>
                    </tr>
                    <tr>
                        <td class="td_left">出生日期：</td>
                        <td><input type="date" name="form_date" id="form_date" /></td>
                    </tr>
                    <tr>
                        <td class="td_left"></td>
                        <td><input type="button" name="form_save" onClick="return saveform(this.form)" value="提交"
                                style="cursor:pointer" /></td>
                    </tr>
                    <tr>
                        <td class="td_left"></td>
                        <td><span id="save_info"></span></td>
                    </tr>
                </table>
            </form>
        </div>
        <!--页面内容 end-->
        <!--JS 执行-->
        <script>
            function saveform(form) {
                var check = true;
                //获取提示信息对象
                var info = $("#save_info");
                //得到用户名信息
                var loginname = $("#form_loginname").val();
                //得到姓名信息
                var username = $("#form_username").val();
                //得到密码值
                var password = $("#form_password").val();
                //得到确定密码值
                var confirmpassword = $("#form_checkpassword").val();
                //得到邮箱值
                var email = $("#form_email").val();
                //得到电话
                var usertel = $("#form_tel").val();
                //得到出生日期
                var userdate = $("#form_date").val();
                //清空提示信息
                info.html("");
                //验证用户名
                if (loginname == "") {
                    info.css("color", "#f00");
                    info.html("用户名不能为空");
                    return false;
                } else {
                    if (!checkloginname(loginname)) {
                        info.css("color", "#f00");
                        info.html("用户名只能为英文字符、数字");
                        return false;
                    }
                }
                //验证姓名
                if (username == "") {
                    info.css("color", "#f00");
                    info.html("姓名不能为空");
                    return false;
                }
                //验证密码
                var checkpasswordinfo = checkpassword(password, confirmpassword);
                if (checkpasswordinfo != "success") {
                    info.css("color", "#f00");
                    info.html(checkpasswordinfo);
                    return false;
                }
                //验证邮箱
                if (email != "" && !checkemail(email)) {
                    info.css("color", "#f00");
                    info.html("邮箱格式错误，请重新填写");
                    return false;
                }
                //验证手机
                if (usertel != "" && !checktel(usertel)) {
                    info.css("color", "#f00");
                    info.html("手机格式错误，请重新填写");
                    return false;
                }
                //验证出生日期
                if (userdate != "" && !checkdate(userdate)) {
                    info.css("color", "#f00");
                    info.html("出生日期格式错误，请重新填写");
                    return false;
                }
                info.css("color", "#18A70D");
                info.html("验证通过");
                return true;
            }
            //验证用户名只能为英文字符、数字
            function checkloginname(name) {
                var regu = "^[A-Za-z0-9]+$";
                var re = new RegExp(regu);
                return re.test(name);
            }
            //验证密码
            function checkpassword(password, confirmpassword) {
                var info = "success";
                if (password == "" || confirmpassword == "") {
                    info = "密码/确认密码不能为空";
                } else {
                    if (password != confirmpassword) {
                        info = "密码/确认密码请保持一致";
                    }
                }
                return info;
            }
            //验证邮箱
            function checkemail(email) {
                var regu = "^([\.a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+";
                var re = new RegExp(regu);
                return re.test(email);
            }
            //验证手机
            function checktel(tel) {
                var regu = "^13[0-9]{9}$|14[0-9]{9}|15[0-9]{9}$|18[0-9]{9}|17[0-9]{9}$";
                var re = new RegExp(regu);
                return re.test(tel);
            }
            //验证出生日期
            function checkdate(date) {
                return (new Date(date).getDate() == date.substring(date.length - 2));
            }
        </script>
    </body>
</html>
```

