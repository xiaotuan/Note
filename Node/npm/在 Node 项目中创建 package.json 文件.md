`npm` 要求 `Node` 项目所在的目录下有一个 `package.json` 文件。创建 `package.json` 文件的最简单方法是使用 `npm`。在命令行中输入下面这些命令：

```shell
$ mkdir example-project
$ cd example-project/
$ npm init -y
```

如果你现在用带有参数 `--save` 的 `npm` 命令从 `npm` 网站上安装一个包，它会自动更新你的 `package.json` 文件。试着输入 `npm install`，或简写为 `npm i`：

```shell
$ npm i --save express
```

你也可以用 `--global` 参数做全局安装。