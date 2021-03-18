### 16.2.6　用命令行方式编译Kotlin Native

对于Kotlin Native项目来说，除了允许通过Gradle方式构建编译外，还可以通过命令行的方式来编译。具体来说，编写完Kotlin代码之后，可以采用Shell脚本的方式来构建，也可以通过Makefile或build.sh的方式来构建，官方推荐使用Shell脚本构建方式，这里采用与之类似的Makefile脚本方式。代码如下。

```python
build : src/kotlin/main.kt kotliner.kt.bc
    konanc src/kotlin/main.kt -library build/kotliner/kotliner.kt.bc 
-nativelibrary build/kotliner/cn_kotliner.bc -o build/kotliner/kotliner.kexe
kotliner.kt.bc : kotliner.bc kotliner.def
    cinterop -def ./kotliner.def -o build/kotliner/kotliner.kt.bc
kotliner.bc : src/c/cn_kotliner.c src/c/cn_kotliner.h
    mkdir -p build/kotliner
    clang -std=c99  -c src/c/cn_kotliner.c -o build/kotliner/cn_kotliner.bc 
-emit-llvm
clean:
      rm -rf build/kotliner
```

采用命令行方式编译Kotlin Native时，需要先把编译器<konan.home>/bin目录加入系统的path环境中，然后再执行make命令，编译完成就可以在项目的build/kotliner目录中找到kotliner.kexe。

