### 2.3.1　使用Gulp运行Babel

现在可以使用Gulp做一些有意思的事情：把ES6代码转换成对应的ES5代码。接下来会将所有在es6文件夹或者public/es6文件夹下的代码转换成ES5代码，生成的代码分别放在dist和public/dist目录下。由于会使用一个叫作 `gulp-babel` 的包，所以首先要运行 `npm install --save-dev` 来安装它，接着在gulpfile.js里加入下面的内容：

```javascript
const gulp = require('gulp');
const babel = require('gulp-babel');
gulp.task('default', function() {
  // Node source
gulp.src("es6/**/*.js")
  .pipe(babel())
  .pipe(gulp.dest("dist"));
// browser source
gulp.src("public/es6/**/*.js")
  .pipe(babel())
  .pipe(gulp.dest("public/dist"));
});
```

在这里Gulp使用了管道的概念。首先需要告诉Gulp要处理哪些文件：src（“ `es6/**/*.js` ”）。大家可能会问**是什么意思，它是一个通配符，表示“任何目录，包含子目录。”所以这里的数据源过滤器会解析es6文件夹下所有后缀为.js的文件，包括所有子目录里的文件，而且不管文件的目录层次有多深都能找到。接下来，把这些文件传送给Babel。最后一步是把已经转换的ES5代码输出到它的目标文件夹，也就是dist目录。Gulp会保存源文件的文件名和目录结构。比如，es6/a.js这个文件经过转换后会输出到dist/a.js，而es6/a/b/c.js则会输出到dist/a/b/c.js。同理，对于public/es6目录也会重复相同的过程。

到目前为止还没有真正地学习ES6，不过可以先试着创建一个ES6文件来验证Gulp配置的正确性。创建es6/test.js文件，并写入以下可以展现ES6特性的代码。（如果读者还不理解这些代码，不用担心，看完这本书后就会明白了！）

```javascript
'use strict';
// es6 特性: 基于块作用域的"let" 声明
const sentences = [
    { subject: 'JavaScript', verb: 'is', object: 'great' },
    { subject: 'Elephants', verb: 'are', object: 'large' },
];
// es6 特性: 对象解构
function say({ subject, verb, object }) {
    // es6 特性: 模板字符串
    console.log('${subject} ${verb} ${object}');
}
// es6 特性: for..of
for(let s of sentences) {
    say(s); 
}
```

接下来把这个文件复制到public/es6文件夹下（可以试着改变sentances数组中的内容，以验证使用了不同文件）。然后在命令行窗口敲入 `gulp` 命令。执行完毕后，查看dist和public/dist目录。会发现里面各有一个test.js目录。如果仔细看那个文件就会发现它跟原始的ES6文件不一样。

下面试着直接运行ES6代码：

```javascript
$ node es6/test.js
/home/ethan/lje3/es6/test.js:8
function say({ subject, verb, object }) {
             ^ 
SyntaxError: Unexpected token {
    at exports.runInThisContext (vm.js:53:16)
    at Module._compile (module.js:374:25)
    at Object.Module._extensions..js (module.js:417:10)
    at Module.load (module.js:344:32)
    at Function.Module._load (module.js:301:12)
    at Function.Module.runMain (module.js:442:10)
    at startup (node.js:136:18)
    at node.js:966:3
```

这个错误提示是Node输出的，大家得到的错误提示可能跟书中的不一样，这是因为Node还未完全实现ES6的特性（如果在足够远的未来读这本书，Node可能已经完全实现了ES6的特性！）接下来试试运行ES5吧：

```javascript
$ node dist\test.js
JavaScript is great
Elephants are large
```

至此已经成功将ES6代码转换成更轻量的ES5代码，这样它就能在任何地方运行了。最后将dist和public/dist添加到.gitignore文件中：因为想跟踪的是ES6源码，而不是生成的ES5代码。

