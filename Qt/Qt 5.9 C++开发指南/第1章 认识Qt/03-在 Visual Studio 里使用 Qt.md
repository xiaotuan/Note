要在 Visual Studio 中使用 Qt，需要安装一个 Visual Stuido 的 Qt 插件，这个插件程序由 Qt 公司提供。

在首次使用 Visual Studio 编译 Qt 项目之前，必须先进行一些设置，否则会提示没有设置 Qt 版本，无法编译项目。

首先要设置 Qt 版本。单击 Visual Studio 菜单项 "Qt VS Tools" -> "Qt Options"。Qt Versions 页面显示了可以使用的 Qt 版本，在未设置之前了，框里是空白的。单击 "Add" 按钮出行的添加 Qt 版本对话框。

单击 "Path" 文本框后面的按钮，在出行的目录选择对话框里选择 Qt 5.9.1 安装目录下的 MSVC 编译器目录，如 "D:\Qt\Qt5.9.1\5.9.1\msvc2015_64"。选择目录后，Version name 编辑框里会自动出现版本名称，可以修改此名称为意义更明显的名称，如 "msvc2015-64bit"。

然后，再单击 Visual Studio 菜单项 "Qt VS Tools" -> "Qt Project Settings"，为项目设置 Qt 版本。在出现的对话框中的 Properties 分页下的列表框里，在 Version 下拉列表框中选择某个 Qt 版本。