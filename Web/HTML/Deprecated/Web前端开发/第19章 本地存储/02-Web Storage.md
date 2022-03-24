[toc]

### 1. sessionStorage

#### 1.1 数据存储的实现

W3C 组织为 sessionStorage 制定的接口定义如下所示：

```js
[NoInterfaceObject]
interface WindowSessionStorage {
    readonly attribute Storage sessionStorage;
};
Window implements WindowSessionStorage;
```

**案例：示例 19-01：sessionStorage 示例演示程序**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="Canvas" />
        <meta content="sessionStorage示例演示程序" />
        <title>sessionStorage示例演示程序</title>
    </head>

    <body>

    </body>
    <script type="text/javascript">
        //存储简单数据
        function saveSimpleString() {
            sessionStorage.setItem("course", "Web前端技术开发与实践");
        }
        //存储结构化数据
        function saveStructuredData() {
            var studentInfo = [
                { "courseNum": "0", "name": "学号" },
                { "courseNum": "1", "name": "姓名" },
                { "courseNum": "2", "name": "性别" },
                { "courseNum": "3", "name": "专业" },
                { "courseNum": "4", "name": "Web前端开发" },
                { "courseNum": "5", "name": "操作系统" },
                { "courseNum": "6", "name": "网络" },
                { "courseNum": "7", "name": "数据库" }
            ]
            sessionStorage.setItem("studentInfo", JSON.stringify(studentInfo));
        }    
    </script>
</html>
```

#### 1.2 创建数据项

sessionStorage 创建数据项使用 setItem() 方法，具体如下。

① 创建数据项，存储简单字符串。

```js
// 存储简单数据
function saveSimpleString() {
    sessionStorage.setItem("course", "Web 前端技术开发与实际");
}
```

② 创建数据项，存储结构化数据。使用 JSON.stringify() 方法将复杂的 JSON 数据对象转换为字符串，再用 setItem() 方法保存到本地。

```js
//存储结构化数据
function saveStructuredData() {
    var studentCourse = [
        { "courseNum": "0", "name": "离散数学" },
        { "courseNum": "1", "name": "高级语言程序设计" },
        { "courseNum": "2", "name": "算法与数据结构" },
        { "courseNum": "3", "name": "编译技术" },
        { "courseNum": "4", "name": "软件工程" },
        { "courseNum": "5", "name": "软件文档规范与标准" }
    ]
    sessionStorage.setItem("courseList", JSON.stringify(studentCourse));
}
```

#### 1.3 读取数据

① 使用 length 属性获取当期数据项数目。

```js
alert(sessionStorage.length)
```

② 使用 key() 方法输出指定编号数据项的键名称。

```js
alert(sessionStorage.key(0))
alert(sessionStorage.key(1))
```

③ 使用 getItem() 方法输出数据项的值。

```js
alert(sessionStorage.getItem("course"));
alert(sessionStorage.getItem("studentInfo"));
```

#### 1.4 删除数据

① 调用 removeItem() 方法删除一个数据项，并输出 sessionStorage 数据项数和第一项的内容。

```js
sessionStorage.removeItem("course");
alert(sessionStorage.length);
alert(sessionStorage.key(0));
```

② 调用 clear() 方法清空 sessionStorage 数据项列表，并输出结果。

```js
sessionStorage.clear();
alert(sessionStorage.length);
```

### 2. localStorage

#### 2.1 数据存储的实现

localStorage 是 Storage 对象的一个实例，对应 windows 对象的 localStorage 属性。

**案例：示例 19-02：localStorage 示例演示程序**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="Canvas" />
        <meta content="localStorage示例演示程序" />
        <title>localStorage示例演示程序</title>
    </head>

    <body>

    </body>
    <script type="text/javascript">
        //存储简单数据
        function saveSimpleString() {
            localStorage.setItem("course", "Web前端技术开发与实践");
        }
        //存储结构化数据
        function saveStructuredData() {
            var studentInfo = [
                { "courseNum": "0", "name": "学号" },
                { "courseNum": "1", "name": "姓名" },
                { "courseNum": "2", "name": "性别" },
                { "courseNum": "3", "name": "专业" },
                { "courseNum": "4", "name": "Web前端开发" },
                { "courseNum": "5", "name": "操作系统" },
                { "courseNum": "6", "name": "网络" },
                { "courseNum": "7", "name": "数据库" }
            ]
            localStorage.setItem("studentInfo", JSON.stringify(studentInfo));
        }
    </script>
</html>
```

#### 2.2 创建数据项

创建 localStorage 数据项使用 setItem() 方法，具体如下所示。

**案例：示例 19-03：创建 localStorage 数据项**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="Canvas" />
        <meta content="创建localStorage数据项" />
        <title>创建localStorage数据项</title>
    </head>

    <body>

    </body>
    <script type="text/javascript">

        saveSimpleString();
        saveStructuredData();
        //存储简单数据
        function saveSimpleString() {
            sessionStorage.setItem("course", "Web前端技术开发与实践");
        }
        //存储结构化数据
        function saveStructuredData() {
            var studentInfo = [
                { "courseNum": "0", "name": "学号" },
                { "courseNum": "1", "name": "姓名" },
                { "courseNum": "2", "name": "性别" },
                { "courseNum": "3", "name": "专业" },
                { "courseNum": "4", "name": "Web前端开发" },
                { "courseNum": "5", "name": "操作系统" },
                { "courseNum": "6", "name": "网络" },
                { "courseNum": "7", "name": "数据库" }
            ]
            sessionStorage.setItem("studentInfo", JSON.stringify(studentInfo));
            sessionStorage.removeItem("courseList");
            console.log(studentInfo);
        }
    </script>
</html>
```

#### 2.3 读取数据

① 使用 length 属性获取当前数据项数目。

```js
alert(localStorage.length);
```

② 使用 key() 方法输出指定编号数据项的键名称。

```js
alert(localStorage.key(0));
alert(localStorage.key(1));
```

③ 使用 getItem() 方法输出数据项的值。

```js
alert(localStorage.getItem("course"));
alert(localStorage.getItem("studentInfo"));
```

#### 2.4 删除数据

① 调用 removeItem() 方法删除一个数据项，并输出 sessionStorage 数据项数目和第一项的内容。

```js
localStorage.removeItem("course");
alert(localStorage.length);
alert(localStorage.key(0));
```

② 调用 clear() 方法清空 localStorage 数据项列表，并输出相应的内容。

```js
localStorage.clear();
alert(localStorage.length);
```

### 3. 对比分析

#### 3.1 区别

sessionStorage 是将数据保存在会话中，在会话期间有效，浏览器关闭后，数据消失；localStorage 是将数据存储在磁盘中，除非用户或程序进行主动清除，否则仅仅关闭浏览器是不会造成数据丢失的。

#### 3.2 联系

sessionStorage 和 localStorage 都是 Storage 对象的实例，使用相同的 API，数据操作方式基本相同，都是以键/值对存储数据。