### 第14章　Docker与安全

**本章主要内容**

+ Docker提供的开箱即用的安全方案
+ Docker为更加安全做了哪些努力
+ 其他开发商为了安全正在付出怎样的努力
+ 为了改善安全问题，还可以采取哪些步骤
+ 在多租户环境下如何用aPaaS管理用户Docker权限

正如Docker在其文档中明确指出的，对于Docker API的调用需要root权限，这也就是为什么Docker通常需要用 `sudo` 命令来运行，或者必须把用户加入一个允许使用Docker API的用户组（该组可能叫作“docker”或“dockerroot”）。

本章中我们将看一下Docker的安全问题。

