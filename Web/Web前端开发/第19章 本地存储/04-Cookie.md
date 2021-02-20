[toc]

### 1. 数据操作

#### 1.1 创建 Cookie

PHP 创建 Cookie 的方法具体如下。

Setcookie(name, value, expire, path, domain, secure)：该方法有 6 个参数， name 规定 Cookie 的名称，是必需参数；value 规定 Cookie 的值，是必需参数；expire 规定 Cookie 有效期，不设置过期时间时，表示当浏览器关闭后 Cookie 从计算机中删除，是可选参数；path 规定 Cookie 的服务器路径，是可选参数；domain 规定 Cookie 的域名，是可选参数；secure 规定是否通过安全的 HTTPS 连接来传输 Cookie，是可选参数。

① PHP 创建简单 Cookie。

```php
setcookie('username', 'sdsd');
```

② PHP 创建一个 5 分钟过期的 Cookie。

```php
setcookie('cookietest', '5分钟有效', time() + 5 * 60);
exit();
```

③ JavaScript 创建简单 Cookie，其使用的方法为：`document.cookie = "name=" + value`;

```js
document.cookie = "user=demo";
```

④ JavaScript 创建一个 5 分钟过期的 Cookie。

```js
/*设置cookie*/
function addCookie(name, value, expireHours) {
    var cookieString = name + "=" + escape(value);
    //判断是否设置过期时间
    if (expireHours) {
        var date = new Date();
        date.setTime(date.getTime() + expireHours * 3600 * 100);
        cookieString = cookieString + ";  expire=" + date.toGMTString();
    }
    document.cookie = cookieString;
}

addCookie('user1', 'demo', 5/60);
```

#### 1.2 数据修改

修改 Cookie 数据的方法与创建 Cookie 的方法相同。

① PHP 使用 setcookie()，当 Cookie 名称已存在，且新值与旧值不同时，更新 cookie。

```php
setcookie('username', 'change');
exit();
```

② JavaScript 修改 cookie。

```js
document.cookie = "user=demo1";
```

#### 1.3 Cookie 读取

① PHP 通过 \$HTTP_COOKIE_VARS["user"] 或 \$_COOKIE["user"] 来访问名为 "user" 的 Cookie 的值。

```php
// 读取并输出 cookie
echo $_COOKIE['username'];
echo '<br/>';
echo $_COOKIE['cookietest'];
exit();
```

② JavaScript 读取 Cookie。

```js
//获取指定名称的cookie值
function getCookie(name) {
    var arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
    if (arr != null)
        return unescape(arr[2]);
    return null;
}
```

**cookie.php**

```php+HTML
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Cookie</title>
    </head>
    <body>
        <?php
        setcookie('username', 'sdsd');
        setcookie('cookietest', '5分钟有效', time() + 5 * 60);
        //修改cookie
        setcookie('username', 'change');
        //读取并输出cookie
        echo $_COOKIE['username'];
        echo '<br/>';
        echo $_COOKIE['cookietest'];
        //清除cookie
        setcookie('cookietest', '5分钟有效', time());
        echo $_COOKIE['cookietest'];
        ?>
    </body>
    <script type="text/javascript">
        /*设置cookie*/
        function addCookie(name, value, expireHours) {
            var cookieString = name + "=" + escape(value);
            //判断是否设置过期时间
            if (expireHours) {
                var date = new Date();
                date.setTime(date.getTime() + expireHours * 3600 * 1000);
                cookieString = cookieString + ";expires=" + date.toGMTString();
            }
            document.cookie = cookieString;
        }
        //获取指定名称的cookie值
        function getCookie(name) {
            var arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
            if (arr != null)
                return unescape(arr[2]);
            return null;
        }
        //删除cookies
        function delCookie(name) {
            var exp = new Date();
            exp.setTime(exp.getTime());
            var cval = getCookie(name);
            if (cval != null)
                document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
        }
    </script>
</html>
```

#### 1.4 清除 Cookie

当删除 Cookie 时，用户应当使过期日期变更为过去的时间点。

① PHP 清除 Cookie。

```php
// 清除 cookie
setcookie('cookietest', '5 分钟有效', time());
echo $_COOKIE['cookietest'];
```

②  JavaScript 清除 Cookie。

```js
// 删除 cookie
function delCookie(name) {
    var exp = new Date();
    exp.setTime(exp.getTime());
    var cval = getCookie(name);
    if (cval != null) {
        document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
    }
}

alert(getCookie('user'));
delCoolie('user');
alert(getCookie('user'));
```

### 3. 案例：在网站中自动记录用户状态

**案例：示例 19-05：在网站中自动记录用户状态**

**autologin.php**

```php+HTML
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>案例：网站中自动记录登录状态</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
        <script type="text/javascript" src="js/jquery-1.11.3.js"></script>
    </head>
    <body>
        <?php
        if (isset($_COOKIE['userID']) && $_COOKIE['userID'] == md5('2015181018')) {
            echo '<div class="center">
            <div class="addItem">
                    <span class="descibe">&nbsp;</span>
                    <span><input type="button" onclick="logOut()" value="退出" /></span>                    
                    <span style="margin-left:5px;">登录成功!</span>
                </div>
            </div>';
        } else {
            echo '<div class="center">
            <p class="pageTitle">学生成绩列表登录</p>
            <!--成绩录入区-->
            <div class="addScore">
                <div class="addItem"><span class="descibe">账号：</span><span><input type="text" id="stuID" value="2015181018" /></span></div>
                <div class="addItem"><span class="descibe">密码：</span><span><input type="password" id="password" value="2015181018" /></span></div>
                <div class="addItem"><span class="descibe">2小时免登录：</span><span><input type="checkbox" id="nextAuto" /></span></div>
                <div class="addItem">
                    <span class="descibe">&nbsp;</span>
                    <span><input type="button" onclick="coimmit()" value="确定" /></span>
                    <span id="checkNotPass" class="checkNotPass">学号不能为空</span>
                </div>
            </div>
        </div>';
        }
        ?>
    </body>
    <script type="text/javascript">
        //登录
        function coimmit() {
            var username = $('#stuID').val();
            var password = $('#password').val();
            var nextAuto = $('#nextAuto').prop('checked') ? 1 : 0;
            var flag = true;
            if (username == '') {
                showInfo('账号不能为空！', 'stuID');
                flag = false;
            }
            if (flag) {
                if (password == '') {
                    showInfo('密码不能为空！', 'password');
                    flag = false;
                }
            }
            if (flag) {
                $.post('logincheck.php', {
                    username: username,
                    password: password,
                    nextAuto: nextAuto,
                }, function (data) {
                    data = JSON.parse(data);
                    switch (data.checkID) {
                        case 1:
                            if('userID' in data){
                                addCookie('userID', data.userID,2);
                            }                            
                            $('body').html('<div class="center">' +
                                    '<div class="addItem">' +
                                    '<span class="descibe">&nbsp;</span>' +
                                    '<span><input type="button" onclick="logOut()" value="退出" /></span>    ' +
                                    '<span style="margin-left:5px;">登录成功!</span>' +
                                    '</div>' +
                                    '</div>');
                            break;
                        case -1:
                            showInfo('密码不能为空！');
                            break;
                        case -2:
                            showInfo('密码不能为空！');
                            break;
                    }
                })
            }
        }

        //退出
        function logOut() {
            delCookie('userID');
            window.location.href = 'autologin.php';
        }
        //信息提示
        function showInfo(str, contentId) {
            $('#' + contentId).val('');
            $('#checkNotPass').show().text(str);
            setTimeout(function () {
                $('#checkNotPass').hide();
            }, 2000);
        }

        /*设置cookie*/
        function addCookie(name, value, expireHours) {
            var cookieString = name + "=" + escape(value);
            //判断是否设置过期时间
            if (expireHours) {
                var date = new Date();
                date.setTime(date.getTime() + expireHours * 3600 * 1000);
                cookieString = cookieString + ";expires=" + date.toGMTString();
            }
            document.cookie = cookieString;
        }

        //获取指定名称的cookie值
        function getCookie(name) {
            var arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
            if (arr != null)
                return unescape(arr[2]);
            return null;
        }

        //删除cookies
        function delCookie(name) {
            var exp = new Date();
            exp.setTime(exp.getTime());
            var cval = getCookie(name);
            if (cval != null)
                document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
        }
    </script>
</html>
```

**19-05.html**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta keywords="Canvas" />
        <meta content="实现自动登录的autologin.php的页面" />
        <title>实现自动登录的autologin.php的页面</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
        <script type="text/javascript" src="js/jquery-1.11.3.js"></script>
    </head>

    <body>
        <div class="center">
            <p class="pageTitle">学生成绩列表登录</p>
            <!--成绩录入区-->
            <div class="addScore">
                <div class="addItem"><span class="descibe">账号：</span><span><input type="text" id="stuID"
                            value="2015181018" /></span></div>
                <div class="addItem"><span class="descibe">密码：</span><span><input type="password" id="stuName"
                            value="2015181018" /></span></div>
                <div class="addItem"><span class="descibe">下次自动登录：</span><span><input type="checkbox"
                            id="nextAuto" /></span></div>
                <div class="addItem">
                    <span class="descibe">&nbsp;</span>
                    <span><input type="button" onclick="coimmit()" value="确定" /></span>
                    <span id="checkNotPass" class="checkNotPass">学号不能为空</span>
                </div>
            </div>
        </div>
        <script type="text/javascript">
            function coimmit() {
                var username = $('#stuID').val();
                var password = $('#stuName').val();
                var nextAuto = $('#nextAuto').prop('checked') ? 1 : 0;
                var flag = true;
                if (username == '') {
                    showInfo('账号不能为空！');
                    flag = false;
                }
                if (flag) {
                    if (password == '') {
                        showInfo('密码不能为空！');
                        flag = false;
                    }
                }
                if (flag) {
                    $.post('autologin.php', {
                        username: username,
                        password: password,
                        nextAuto: nextAuto,
                    }, function (data) {

                    })
                }
            }

            //信息提示
            function showInfo(str) {
                $('#checkNotPass').show().text(str);
                setTimeout(function () {
                    $('#checkNotPass').hide();
                }, 2000);
            }

            /*设置cookie*/
            function addCookie(name, value, expireHours) {
                var cookieString = name + "=" + escape(value);
                //判断是否设置过期时间
                if (expireHours) {
                    var date = new Date();
                    date.setTime(date.getTime() + expireHours * 3600 * 100);
                    cookieString = cookieString + ";  expire=" + date.toGMTString();
                }
                document.cookie = cookieString;
            }

            //获取指定名称的cookie值
            function getCookie(name) {
                var arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
                if (arr != null)
                    return unescape(arr[2]);
                return null;
            }
        </script>
    </body>
</html>
```

