假设你有一个 `C` 或者 `C++` 的程序，并且想要调用一些 `Java` 代码。调用 `API`（`invocation API`）使你能够把 `Java` 虚拟机嵌入到 `C` 或者 `C++` 程序中。下面是你初始化虚拟机所需的基本代码：

```c
JavaVMOption options[1];
JavaVMInitArgs vm_args;
JavaVM* jvm;
JNIEnv* env;

options[0].optionString = "-Djava.class.path=.";

memset(&vm_args, 0, sizeof(vm_args));
vm_args.version = JNI_VERSION_1_2;
vm_args.nOptions = 1;
vm_args.options = options;

JNI_CreateJavaVM(&jvm, (void**) &env, &vm_args);
```

可以给虚拟机提供任意数目的选项，这只需增加选项数组的大小和 `vm_args.nOptions` 的值。例如：

```c
options[i].optionString = "-Djava.compiler=NONE";
```

> 提示：当你陷入麻烦导致程序崩溃，从而不能初始化 `JVM` 或者不能装载你的类时，请打开 `JNI` 调试模式。设置一个选项如下：
>
> ```c
> options[i].optionString = "-verbose:jni";
> ```

一旦设置完虚拟机，只要按常规方法使用 `env` 指针即可。

只有在调用 `invocation API` 中的其他函数时，才需要 `jvm` 指针。目前，只有四个这样的函数。最重要的一个是终止虚拟机的函数：

```c
(*jvm)->DestroyJavaVM(jvm);
```

遗憾的是，在 `Windows` 下，动态链接到 `jre/bin/client/jvm.dll` 中的 `JNI_CreateJavaVM` 函数变得非常困难，因为 `Vista` 改变了链接规则，而 `Oracle` 的类库仍旧依赖于旧版本的 `C` 运行时类库。下面示例程序通过手工加载该类库解决了这个问题，这种方式与 `Java` 程序所使用的方式一样，请参阅 `JDK` 中的 `src.jar` 文件里的 `launcher/java_md.c` 文件。

**示例程序：InvocationTest.c**

```c
```



