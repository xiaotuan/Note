here 文档以两个连续的小于号 `<<` 开始，紧跟着一个特殊的字符序列，该序列将在文档的结尾再次出现。`<<` 是 shell 的标签重定向符，在这里，它强制命令的输入是一个 here 文档。这个特殊字符序列的作用就像一个标记，它告诉 shell here 文档结束的位置。因为这个标记序列不能出现在传递给命令的文档内容中，所以应该尽量使它既容易记忆又相当不寻常。

**实验 使用 here 文档**

```shell
#!/bin/sh

cat << !FUNKY!
hello
this is a here
document
!FUNKY!
```

它的输出如下所示：

```
hello
this is a here
document
```

here 文档功能可能看起来相当奇怪，但其实它的作用很大。因为它可以用来调试交互式的程序，比如一个编辑器，并向它提供一些事先定义好的输入。但它更常见的用途是再脚本程序中输出大量的文本，就像你在刚才的示例中看到的那样，从而可以避免用 echo 语句来输出每一行。你可以在标识符两端都使用感叹号（ ! ）来确保不会引起混淆。

**实验 here 文档的另一个用法**

1. a_text_file 文件的内容如下

   ```
   That is line 1
   That is line 2
   That is line 3
   That is line 4
   ```

2. 可以通过结合使用 here 文档和 ed 编辑器来编辑这个文件

   ```shell
   #!/bin/sh
   ed a_text_file <<!FunkyStuff!
   3
   d
   .,\$s/is/was/
   w
   q
   !FunkyStuff!
   exit 0
   ```

   运行这个脚本程序，现在这个文件的内容是：

   ```
   That is line 1
   That is line 2
   That was line 4
   ```

   这个脚本程序只是调用 ed 编辑器并向它传递命令，先让它一栋到第三行，然后删除该行，再把当前行（因为第三行刚刚被删除了，所以当前行现在就是原来的最后一行，即第四行）中的 is 替换为 was。

   > 注意
   >
   > 我们在 here 文档中用 `\` 字符来防止 `$` 字符被 shell 扩展。`\` 字符的作用是对 $ 进行转义，让 shell 知道不要尝试把 `$s/is/was` 扩展为它的值，而它也确实没有值。shell 把 `\$` 传递给 $，再由 ed 编辑器对它进行解释。