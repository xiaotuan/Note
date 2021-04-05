[toc]

### 1. HTML5 主体结构元素

#### 1.1 article

`article` 元素代表文档、页面或应用程序中独立的、完整的、可以独自被外部引用的内容。它可以是一篇博客或报刊中的文章、一篇论坛帖子、一段用户评论或独立的插件，或者其他任何独立的内容。一个 `article` 元素通常有它自己的标题（一般放在一个 header 元素里面），有时还有自己的脚注。

`article` 元素是可以嵌套使用的，内层的内容在原则上需要与外层的内容想关联。

**案例：实例 4-02： article 元素**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="HTML5 article" />
        <meta content="article元素示例" />
        <title>article元素示例</title>
    </head>

    <body>
        <article>
            <header>
                <h1>假如生活欺骗了你</h1>
                <p>1825年</p>
            </header>
            <p>假如生活欺骗了你</p>
            <p>假如生活欺骗了你，</p>
            <p>不要悲伤，不要心急！</p>
            <p>忧郁的日子里须要镇静：</p>
            <p>相信吧，快乐的日子将会来临！</p>
            <p>心儿永远向往着未来；</p>
            <p>现在却常是忧郁。</p>
            <p>一切都是瞬息，一切都将会过去；</p>
            <p>而那过去了的，就会成为亲切的怀恋。</p>
            <section>
                <h2>文章评论内容：</h2>
                <article>
                    <header>
                        <h3>诗歌写的很好</h3>
                        <h4>发表人：张三</h4>
                        <p>
                            <time pubdate datetime="2013-03-25T09:45:23">发表时间：2013-03-25 09:45:23</time>
                        </p>
                    </header>
                    <p>假如生活欺骗了你</p>
                </article>
            </section>
            <footer>
                <p><small>普希金诗文选</small></p>
            </footer>
        </article>
    </body>
</html>
```

article 元素也可以用来表示插件，它的作用是使插件看起来好像内嵌在页面中一样。

**案例：示例 4-03：article 元素插件**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>article 元素插件</title>
    </head>
    <body>
        <article>
            <h1>PuXiJin</h1>
            <object>
                <param name="allowFullScreen" value="true">
                <embed src="#" width="300" height="300">
            </object>
        </article>
    </body>
</html>
```

#### 1.2 section

`section` 元素用于对网站或应用程序中页面上的内容进行分块。一个 `section` 元素通常由内容及其标题组成。`section` 在没有标题的情况下建议不要使用。

**案例：示例 4-04：section 元素**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>section 元素</title>
    </head>
    <body>
        <article>
            <h1>普希金</h1>
            <section>
                <h3>假如生活欺骗了</h3>
                <p>假如生活欺骗了你，假如生活欺骗了你，不要悲伤，不要心急！忧郁的日子里须要镇静：相信吧，快乐的日子将会来临！</p>
            </section>
            <section>
                <h3>致大海</h3>
                <p>再见吧，自由奔放的大海！这是你最后一次在我的眼前，翻滚着蔚蓝色的波浪，和闪耀着娇美的容光。</p>
            </section>
        </article>
    </body>
</html>
```

关于 `section` 元素的使用禁忌总结如下：

+ 不要将 `section` 元素用作设置样式的页面容器，那是 `div` 元素的工作。
+ 如果 `article` 元素、`aside` 元素或 `nav` 元素更符合使用条件，不要使用 `section` 元素。
+ 不要为没有标题的内容区块使用 `section` 元素。

#### 1.3 nav

`nav` 元素是一个可以用作页面导航的链接组，其中导航元素链接到其他页面或当前页面的其他部分。并不是所有的链接组都要放进 `nav` 元素，只需要将主要的、基本的链接组放进 `nav` 元素即可。

**案例：示例 4-05：nav 元素**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 nav" />
        <meta content="nav元素" />
        <title>nav元素</title>
    </head>

    <body>
        <h1>Web前端开发</h1>
        <nav>
            <ul>
                <li><a href="http://www.w3school.com.cn">首页</a></li>
                <li><a href="http://www.w3school.com.cn/html/index.asp">HTML 5</a></li>
                <li><a href="http://www.w3school.com.cn/css/index.asp">CSS 3</a></li>
                <li><a href="http://www.w3school.com.cn/b.asp">JavaScript</a></li>
                <li><a href="http://www.w3school.com.cn/jquery/index.asp">jQuery</a></li>
            </ul>
        </nav>
    </body>
</html>
```

`nav` 元素可用于以下这些场合：

+ 传统导航条。现在主流网站上都有不同层级的导航条，其作用是将当前画面跳转到网站的其他主要页面上去。
+ 侧边栏导航。现在主流博客网站及商品网站上都有侧边栏导航，其作用是将页面从当前文章或当前商品跳转到其他文章或其他商品页面上去。
+ 页内导航。页内导航的作用是在本页面几个主要的组成部分之间进行跳转。
+ 翻页操作。翻页操作是指在多个页面的前后页面或博客网站的前后篇文章间滚动。

#### 1.4 aside

`aside` 元素用来表示当前页面或文章的附属信息部分，它可以包含与当前页面或主要内容相关的引用、侧边栏、广告、导航条，以及其他类似的有别于主要内容的部分。

`aside` 元素主要有以下两种使用方法：

+ 被包含在 `article` 元素中作为主要内容的附属信息部分，其中的内容可以是与当前文章有关的参考资料、名词解释等。
+ 在 `article` 元素之外使用，作为页面或站点全局的附属信息部分。最典型的形式是侧边栏。

**案例：示例 4-06：aside 元素**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 aside" />
        <meta content="aside元素" />
        <title>aside元素</title>
    </head>

    <body>
        <header>
            <h1>关于HTML 5</h1>
            <p>文章来源：http://www.w3school.com.cn/</p>
        </header>
        <article>
            <h2>HTML5是下一代的HTML</h2>
            <p>HTML5仍处于完善之中。然而，大部分现代浏览器已经具备了某些 HTML5 支持。</p>
            <p>在W3School的HTML 5教程中，您将了解 HTML5 中的新特性。</p>
            <h2>CSS3</h2>
            <p>CSS3 是最新的 CSS 标准。</p>
            <aside>
                <h3>参考资料</h3>
                <p>W3school</p>
                <p>HTML5开发手册</p>
            </aside>
        </article>
    </body>
</html>
```

#### 1.5 time

`time` 元素代表 24 小时中的某个时刻或者某个日期，它表示时间时允许带时差。

`datetime` 属性中日期与时间之间要用 "T" 分隔。时间加上 Z 文字表示给机器编码时使用 UTC 标准时间；如果加上了时差，表示向机器编码另一地区时间；如果是编码本地时间，则不需要添加时差。

**案例：示例 4-07：time 元素**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 time" />
        <meta content="time元素" />
        <title>time元素</title>
    </head>

    <body>
        <time datetime="2015-10-1">2015年10月1日</time>
        <time datetime="2015-10-1">10月1日</time>
        <time datetime="2015-10-1">国庆节</time>
        <time datetime="2015-10-1T09:00">国庆节是10月1日</time>
        <time datetime="2015-10-1T09:00Z">国庆节是10月1日</time>
        <time datetime="2015-10-1T09:00+09:00">外国今天不是国庆节</time>
    </body>
</html>
```

`pubdate` 属性是一个可选的、bool 值的属性，可以用到 `article` 元素中的 `time` 元素上，意思是 `time` 元素代表了文章或整个网页的发布日期。

**案例：示例 4-08: pubdate 元素**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 time pubdate" />
        <meta content="pubdate元素" />
        <title>pubdate元素</title>
    </head>

    <body>
        <article>
            <header>
                <h1>关于<time datetime="2015-10-1">10月1日</time>国庆节放假通知</h1>
                <p>发布日期：<time datetime="2015-09-29" pubdate="">2015年9月29日</time></p>
            </header>
            <p>10月1日，举国欢庆...(关于国庆节放假的通知)</p>
        </article>
    </body>
</html>
```

### 2. HTML5 非主体结构元素

#### 2.1 header

`header` 元素是一种具有引导和导航作用的结构元素，通常用来放置整个页面或页面内的一个内容区块的标题，但也可以包含其他内容。

**案例：示例 4-09：header 元素**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 header" />
        <meta content="header元素" />
        <title>header元素</title>
    </head>

    <body>
        <header>
            <h1>网页标题</h1>
        </header>
        <article>
            <header>
                <h1>文章标题</h1>
            </header>
            <p>文章内容</p>
        </article>
    </body>
</html>
```

#### 2.2 hgroup

`hgroup` 元素是将标题及其子标题进行分组的元素。

**案例：示例 4-10：hgroup 元素**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 hgroup" />
        <meta content="hgroup元素" />
        <title>hgroup元素</title>
    </head>

    <body>
        <article>
            <header>
                <hgroup>
                    <h1>文章主标题</h1>
                    <h5>文章子标题</h2>
                    <p><time datetime="2015-10-1">2015年10月1日</time></p>
                </hgroup>
            </header>
            <p>文章内容</p>
        </article>
    </body>
</html>
```

#### 2.3 footer

`footer` 元素可以作为其父级内容区块或是一个根区块的脚注。

**案例：示例 4-11：footer 元素**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 footer" />
        <meta content="footer元素" />
        <title>footer元素</title>
    </head>

    <body>
        <footer>
            <ul>
                <li>版权信息</li>
                <li>网站地图</li>
                <li>联系方式</li>
            </ul>
        </footer>
    </body>
</html>
```

#### 2.4 address

`address` 元素用来在文档中呈现联系信息，包括文档作者或文档维护者的名字、他们的网站链接、电子邮箱、真实地址、电话号码等。

**案例：示例 4-12：address 元素**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 address" />
        <meta content="address元素" />
        <title>address元素</title>
    </head>

    <body>
        <footer>
            <address>
                <p>文章作者：<a title="文章作者：张三" href="#">张三</a></p>
                <p>发表时间：<time datetime="2013-10-1">2015年10月日</time>
            </address>
        </footer>
    </body>
</html>
```

### 3. 案例：使用结构元素进行网页布局（新闻列表+新闻列表内容呈现）

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 " />
        <meta content="使用结构元素进行网页布局" />
        <title>使用结构元素进行网页布局</title>
    </head>
    <style type="text/css">
        * {
            padding: 0px;
            margin: 0px;
        }

        a {
            text-decoration: none;
        }

        ul {
            list-style: none;
        }

        .main {
            width: 1000px;
            margin: 40px auto;
        }

        .main nav {
            width: 1000px;
            height: 40px;
            background: #999;
            border-radius: 5px;
        }

        .main nav ul li {
            width: 70px;
            height: 40px;
            float: left;
            text-align: center;
            line-height: 40px;
        }

        .main nav ul li a {
            color: #fff;
            font-family: "Microsoft YaHei UI";
            font-size: 14px;
        }

        .main nav ul li a:hover {
            font-weight: bold;
        }

        .main .block1 {
            width: 430px;
            height: 250px;
            margin-top: 20px;
            float: left;
        }

        .main .block2 {
            width: 430px;
            height: 250px;
            margin-top: 20px;
            float: right;
        }

        .main .block1 h1,
        .main .block2 h1 {
            color: #333;
            font-size: 20px;
            font-family: "Microsoft YaHei UI";
            line-height: 50px;
            text-indent: 1em;
        }

        .main .block1 ul,
        .main .block2 ul {
            width: 390px;
            margin: 0 19px 10px 19px;
        }

        .main .block1 ul li,
        .main .block2 ul li {
            width: 390px;
            height: 40px;
        }

        .main .block1 ul li a,
        .main .block1 ul li time,
        .main .block2 ul li a,
        .main .block2 ul li time {
            color: #333;
            font-size: 14px;
            font-family: "Microsoft YaHei UI";
            line-height: 40px;
        }

        .main .block1 ul li a,
        .main .block2 ul li a {
            float: left;
        }

        .main .block1 ul li a:hover,
        .main .block2 ul li a:hover {
            color: red;
        }

        .main .block1 ul li time,
        .main .block2 ul li time {
            float: right;
        }

        footer {
            clear: both;
            width: 1000px;
            height: 200px;
            margin: 0 auto;
            text-align: center;
        }

        footer h1 span {
            margin-right: 20px;
        }

        footer h1 span a {
            color: #333;
            font-family: "Microsoft YaHei UI";
            font-size: 14px;
            line-height: 200px;
        }

        footer h1 span a:hover {
            color: red;
        }
    </style>

    <body>
        <div class="main">
            <header>
                <nav>
                    <ul>
                        <li><a href="#">首页</a></li>
                        <li><a href="#" style="color:#EF2D36;">新闻</a></li>
                        <li><a href="#">体育</a></li>
                        <li><a href="#">娱乐</a></li>
                        <li><a href="#">财经</a></li>
                        <li><a href="#">科技</a></li>
                        <li><a href="#">手机</a></li>
                        <li><a href="#">数码</a></li>
                    </ul>
                </nav>
            </header>
            <div class="block1">
                <section>
                    <h1>娱乐新闻</h1>
                    <ul>
                        <li><a href="#">香港已没有黑帮 大家都不想在里面混</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">《碟中谍5》曝外景地花絮</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">灾难发生后该不该禁播娱乐节目</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">多部好莱坞大片登陆中国</a><time datetime="2015-10-1">2015-10-1</time></li>
                    </ul>
                </section>
            </div>
            <div class="block2">
                <section>
                    <h1>军事新闻</h1>
                    <ul>
                        <li><a href="#">2015阅兵在9月3日09:00开始</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">习近平对县委书记十二句严厉告诫</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">日本在政府网站开设关于钓鱼岛网页</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">中国坦克打先锋巴铁反恐精锐尽出</a><time datetime="2015-10-1">2015-10-1</time></li>
                    </ul>
                </section>
            </div>
            <div class="block1">
                <section>
                    <h1>数码新闻</h1>
                    <ul>
                        <li><a href="#">微软已在秘密测试Android版Edge浏览器</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">平板电脑五年走到市场拐点</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">苹果邀请函解密 Hint有新释义</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">IDF2015英特尔谷歌联手</a><time datetime="2015-10-1">2015-10-1</time></li>
                    </ul>
                </section>
            </div>
            <div class="block2">
                <section>
                    <h1>手机新闻</h1>
                    <ul>
                        <li><a href="#">超大运行内存手机推荐</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">国产旗舰手机盘点</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">西门子归来 首款智能机配置强跑分出色</a><time datetime="2015-10-1">2015-10-1</time></li>
                        <li><a href="#">骗子植入手机木马的10大招术</a><time datetime="2015-10-1">2015-10-1</time></li>
                    </ul>
                </section>
            </div>
        </div>
        <footer>
            <h1><span><a href="#">关于我们</a></span><span><a href="#">联系我们</a></span></h1>
        </footer>
    </body>
</html>
```

