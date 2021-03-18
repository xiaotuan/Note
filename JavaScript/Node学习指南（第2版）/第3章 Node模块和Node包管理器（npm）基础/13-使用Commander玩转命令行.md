[toc]

### 3.4.2　使用Commander玩转命令行

Commander提供了对命令行参数的支持，命令行参数就是运行一个程序时所附加的参数，比如被普遍使用的用于展示程序用法的-h或--help参数。

通过npm来安装：

```python
npm install commander
```

然后通过require来加载：

```python
var program = require('commander');
```

使用时，将程序所支持的参数用参数调用连接起来就可以了。在下面的代码中，我们的程序支持两个默认参数：-V或者--version用来显示版本号，-h或者--help用来显示帮助信息。还有两个自定义参数：-s或者--source用来提供网址，-f或者--file用来提供文件名。

```python
var program = require('commander');
program
   .version ('0.0.1')
   .option ('-s, --source [web site]', 'Source web site')
   .option ('-f, --file [file name]', 'File name')
   .parse(process.argv);
console.log(program.source);
console.log(program.file);
```

我们要手动提供自定义参数，而Commander给我们提供了默认的版本号参数和帮助信息参数。如果这样运行我们的程序：

```python
node options –h
```

Commander就会打印出下面的参数列表：

```python
Usage: options [options]
Options:
  -h, --help             output usage information
-V, --version            output the version number
-s, --source [web site]  Source web site
-f, --file [file name]   File name
```

短参数可以连起来使用，比如-sf命令可以处理这种情况。它还可以接收多单词的参数，比如--file-name。在获取参数内容时使用驼峰命名法：program. fileName。

Commander还支持强制类型转换

```python
.option('-i, --integer <n>', 'An integer argument', parseInt)
```

和正则表达式：

```python
.option('-d --drink [drink]', 'Drink', /^(coke|pepsi|izze)$/i)
```

你还可以在最后一个参数的位置指定一个可变参数，也就是它可以有任意多的参数。或许你的程序要支持未知数量的多个关键字，那么你可以像这样创建一个Commander参数：

```python
var program = require('commander');
program
  .version('0.0.1')
  .command('keyword <keywork> [otherKeywords...]')
  .action(function (keyword, otherKeywords) {
    console.log('keyword %s', keyword);
    if (otherKeywords) {
      otherKeywords.forEach(function (oKey) {
        console.log('keyword %s', oKey);
      });
    } 
  }); 
program.parse(process.argv);
```

然后，运行下面这行命令：

```python
node options2 keyword one two three
```

会得到这样的结果：

```python
keyword one
keyword two
keyword three
```

> <img class="my_markdown" src="../images/54.png" style="zoom:50%;" />
> **下载Commander**
> 如果你想直接下载Commander，你可以通过它的GitHub代码库下载。Commander对于命令行程序来说格外有用，我们将在第6章进行展示。

