**inout.js**

```js
process.stdin.setEncoding('utf8');
process.stdin.on('readable', function() {
   var input = process.stdin.read();
   if (input !== null) {
      // edho the text
      process.stdout.write(input);
      var command = input.trim();
      if (command == 'exit')
         process.exit(0);
   }
});
```

执行命令如下：

```shell
$ node inout.js
```



