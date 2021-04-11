### 第15章　Rust与WebAssembly

Rust的应用范围远远超出了系统编程领域，它也可以在Web上运行。在本章中，我们将探讨一种这样的技术，它被称为WebAssembly。我们将详细介绍WebAssembly究竟是什么，以及如何使用这种技术将Rust与JavaScript一起运行。如果能在Web浏览器上运行Rust就可以被更多的受众（即Web开发者社区）使用，并使他们能够在应用程序中利用系统编程语言的性能。在本章的后半部分，我们将探索WebAssembly支持的工具和软件包，并构建一个实时的markdown编辑器，该编辑器调用Rust实现的API，将markdown文档呈现到HTML页面。

在本章中，我们将介绍以下主题。

+ 什么是WebAssembly。
+ WebAssembly的目标。
+ 如何使用WebAssembly。
+ Rust与WebAssembly的历史和可用的软件包。
+ 在Rust中构建基于WebAssembly的Web应用程序。

