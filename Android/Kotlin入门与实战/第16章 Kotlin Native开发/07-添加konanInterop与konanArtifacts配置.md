### 16.2.4　添加konanInterop与konanArtifacts配置

接下来，还需要添加konanInterop和konanArtifacts相关的配置信息，其中，konanInterop主要用来配置Kotlin调用C的接口。相关的代码如下。

```python
konanInterop {
    ckotlinor {
        defFile 'kotlinor.def'     // konanInterop配置文件
        includeDirs "src/c"      // C头文件目录，可以传入多个
    }
}
```

在上面的配置文件中，ckotlinor是插件中的KonanInteropConfig对象，在konanArtifacts配置中会引用这个ckotlinor。而kotlinor.def是Kotlin Native与C语言互操作的配置文件，可以在kotlinor.def中配置C到Kotlin的映射关系，该配置文件的内容如下。

```python
headers=cn_kotlinor.h
compilerOpts=-Isrc/c
```

除上面使用的选项之外，konanInterop还提供了如下常用的选项。

```python
konanInterop {
       pkgName {
           defFile <def-file>  
           pkg <package with stubs>
           target <target: linux/macbook/iphone/iphone_sim>
           compilerOpts <Options for native stubs compilation>
           linkerOpts <Options for native stubs >
           headers <headers to process> 
           includeDirs <directories where headers are located> 
           linkFiles <files which will be linked with native stubs>
           dumpParameters <Option to print parameters of task before execution>
       }   
 }
```

konanInterop配置参数选项对应的具体含义如表16-2所示。

<center class="my_markdown"><b class="my_markdown">表16-2　konanInterop配置选项说明</b></center>

| 配置选项 | 选项说明 | 配置选项 | 选项说明 |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| defFile | 互操作映射关系配置文件 | headers | 需要处理的头文件 |
| pkg | C头文件编译后映射为Kotlin的包名 | includeDirs | 包括头文件的目录 |
| target | 编译目标平台： MacBook、iPhone等 | linkFiles | 与native stubs链接的文件 |
| compilerOpts | 编译选项 | dumpParameters | 打印Gradle任务参数的选项配置 |
| linkerOpts | 链接选项 |

接下来，需要为项目添加konanArtifacts相关的配置，该配置主要用来处理编译任务的执行。

```python
konanArtifacts { 
    KotlinorClient {   
         inputFiles fileTree("src/kotlin")  //Kotlin代码配置，项目入口main()
         useInterop 'ckotlinor'   //前面的konanInterop配置
         nativeLibrary fileTree('src/c/cn_kotlinor.bc')   //本地库文件配置
         target 'macbook'   // 编译的目标平台
    }
}
```

konan编译任务配置的处理类是KonanCompileTask.kt，可以在Kotlin Native的kotlin-native- gradle-plugin插件中找到该类。

