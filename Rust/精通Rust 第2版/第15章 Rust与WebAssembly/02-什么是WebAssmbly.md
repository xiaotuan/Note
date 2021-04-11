### 15.1　什么是WebAssmbly

“保持好奇心，广泛阅读，尝试新事物，人们所谓的智慧很多情况下都可以归结为好奇心。”

——Aaron Swartz

WebAssembly是一套技术和规范，它允许用户将原生代码编译为名为wasm的低级语言在Web上运行。从可用性的角度来看，它是一组技术，允许你使用其他非Web编程语言编写的程序在Web浏览器上运行。从技术的角度来看，WebAssembly是一种虚拟机规范，具有二进制、加载期效率指令集架构（Instruction Set Architecture，ISA）。接下来让我们稍微简化一下这个定义。众所周知，编译器是一个复杂的“机器”，它把人类可读的编程语言编写的代码转换为由0和1组成的机器代码，不过此转换需要经过多个步骤。它在编译的几个阶段完成此任务，最后这些代码会被编译成特定于某种计算机的汇编语言。然后，针对特定计算机的汇编程序按照ISA中为目标计算机指定的规则将其编码为机器代码。在这里，编译器针对实际的计算机，但是，它并不一定是真实的机器，它也可以是在真实计算机上执行虚拟指令集的虚拟机（Virtual Machine，VM）。虚拟机的一个用例是视频游戏模拟器，例如在普通计算机上运行并模拟Gameboy硬件的Gameboy模拟器。WebAssembly虚拟机与此类似。这里，浏览器引擎实现了WebAssembly虚拟机，这使得用户能够与JavaScript一起运行wasm代码。





![170.png](../images/170.png)
**注意**

ISA定义计算机如何执行指令，以及其在最底层支持的操作类型。此ISA虚拟机不一定总是适用于真实的物理硬件，也可以适用于虚拟机。wasm是WebAssembly虚拟机的ISA。



过去5年来，人们越来越依赖互联网及其各种应用程序，这导致开发人员努力尝试将其代码转换为JavaScript。这是因为JavaScript是最受欢迎的，并且是网络上唯一的跨平台技术。asm.js项目（一个更快捷的JavaScript子集）来自Mozilla，它是第一个使网络更加高效和满足不断增长的性能需求的项目。而从asm.js及其创立的原则和吸取的教训中，WebAssembly诞生了。

WebAssembly 是诸多科技“巨头”组成的浏览器委员会共同努力的成果，其中包括Mozilla、Google、Apple及Microsoft。自2018年初以来，作为多种语言的编译目标，它的受欢迎程度大幅提高，其中包括使用Emscripten工具链的C++、使用LLVM/Emscripten的Rust、使用汇编脚本的TypeScript，以及其他诸多语言。截至2019年，所有主流的浏览器都在其Web浏览器引擎中实现了WebAssembly虚拟机。

WebAssembly的名称中包含Assembly，因为它是一种类似于汇编指令的低级编程语言。它具有一组有限的原始类型，这使得它易于解析和运行。它为以下类型提供了原生支持：

+ ** **i32** ** ：32位整型。
+ ** **i64** ** ：64位整型。
+ ** **f32** ** ：32位浮点型。
+ ** **f64** ** ：64位浮点型。

它不是像 JavaScript 那样的开发者经常会用到的编程语言，而是编译器的编译目标。WebAssembly平台和生态系统目前专注于在互联网上使用这项技术，但它不会局限于互联网。如果平台将WebAssembly虚拟机规范实现为程序，那么wasm程序将能够在该虚拟机上运行。

要让某个平台支持WebAssembly，需要让该平台支持的语言实现虚拟机。这就像JVM的平台无关的代码那样——编写一次，运行速度更快、运行更安全！但它目前主要的目标就是浏览器。大多数Web浏览器带有一个JavaScript解析器，可以解析浏览器引擎中的.js文件，为用户实现各种交互。为了允许Web解析wasm文件，这些引擎在其中实现了WebAssembly虚拟机，允许浏览器解析和运行wasm代码和JavaScript代码。

解析JavaScript和解析WebAssembly代码的一个明显区别是，由于wasm代码紧凑表示，因此解析速度要快一个数量级。动态网站上的大多数初始页面加载时间都花在解析JavaScript代码上，使用 WebAssembly 可以为这些网站提供巨大的性能提升体验。然而，WebAssembly的目标不是取代JavaScript，而是在对性能至关重要的地方成为JavaScript的得力助手。

根据规范WebAssembly有两种语言格式，包含如下定义：人类可读的文本格式.wat，适用于在最终部署之前查看和调试WebAssembly代码；结构紧凑的底层机器格式，它被称为wasm。该格式是由WebAssembly虚拟机解释和执行的格式。

WebAssembly程序通常以模块开头。在模块中，你可以定义变量、函数及常量等。wasm程序被表示成s表达式，s表达式是通过嵌套的圆括号分隔块序列表示程序的简明方法。例如，单个(1)表示返回值是1的s表达式。WebAssembly中的每个s表达式都返回一个值。让我们来看一个可读的.wat格式的WebAssembly简单程序：

```rust
(module
 (table 0 anyfunc)
 (memory $0 1)
 (export "memory" (memory $0))
 (export "one" (func $one))
 (func $one (; 0 ;) (result i32)
  (i32.const 1)
 )
)
```

在上述代码中，我们有一个包含其他嵌套s表达式的父级s表达式块（模块）。在模块内部包含table、memory和export的部分，以及一个名为$one的func函数定义，它会返回一个i32。我们不会详细介绍它们，因为这与本节的主题偏离太远。

关于 wasm 程序需要重点关注的一点是，它们在表示方面非常高效，并且可以在浏览器中比JavaScript更快地传送和解析。不过WebAssembly的设计目标是专注于特定领域，而不是成为通用编程语言。

