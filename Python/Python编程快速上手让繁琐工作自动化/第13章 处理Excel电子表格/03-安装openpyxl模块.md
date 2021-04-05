### 13.2　安装openpyxl模块

Python没有自带 `openpyxl` ，所以必须安装。请按照附录A中安装第三方模块的说明来安装。模块的名称是  `openpyxl` 。

本书使用的是 `openpyxl` 的2.6.2版本。重要的是，你必须通过运行 `pip install --user --U openpyxl==2.6.2` 来安装这个版本，因为较新版本的 `openpyxl` 与本书中的信息不兼容。要测试它是否安装正确，就在交互式环境中输入以下代码：

```javascript
>>> import openpyxl
```

如果该模块正确安装，就不会产生错误信息。记得在运行本章的交互式环境例子之前，要导入 `openpyxl` 模块，否则会出现错误 `NameError: name 'openpyxl'is not defined` 。

