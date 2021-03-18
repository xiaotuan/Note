### 3.4.3　使用Ant方式构建Kotlin

Kotlin提供了3种任务来支持Ant方式构建项目：\<kotlinc>用于编译纯Kotlin的模块，\<kotlin2js>用于编译JavaScript相关的模块，而\<withKotlin>作为javac的扩展用于编译混合的Kotlin/Java模块。下面是使用kotlinc任务编译项目的一个简单的示例。

```python
<project name="Ant Task Test" default="build">
    <typedef resource="org/jetbrains/kotlin/ant/antlib.xml" classpath="${kotlin. lib}/kotlin-ant.jar"/>
    <target name="build">
        <kotlinc src="hello.kt" output="hello.jar"/>
    </target>
</project>
```

示例中， `$` {kotlin.lib}指向Kotlin独立编译器所在文件夹的位置。如果项目由多个源代码组成，那么需要多个src作为元素路径。

```python
<project name="Ant Task Test" default="build">
   …//省略其他配置
<target name="build">
        <kotlinc output="hello.jar">
            <src path="root1"/>
            <src path="root2"/>
        </kotlinc>
  </target>
  </project>
```

使用Ant任务方式构建Kotlin项目时，\<kotlinc>会自动添加标准库依赖，不必在配置时添加额外的参数，使用\<withKotlin>任务来构建混合的Java / Kotlin模块的示例如下。

```python
<project name="Ant Task Test" default="build">
    <typedef resource="org/jetbrains/kotlin/ant/antlib.xml"   
        classpath="${kotlin.lib}/kotlin-ant.jar"/>
    <target name="build">
        <delete dir="classes" failonerror="false"/>
        <mkdir dir="classes"/>
        <javac destdir="classes" includeAntRuntime="false" srcdir="src">
            <withKotlin/>
        </javac>
        <jar destfile="hello.jar">
            <fileset dir="classes"/>
        </jar>
    </target>
</project>
```

如果要为\<withKotlin>指定额外的命令行参数，则可以使用\<compilerarg>参数，还可以为编译的模块指定moduleName名称属性。

```python
<withKotlin moduleName="myModule">
    <compilerarg value="-no-stdlib"/>
</withKotlin>
```

和\<kotlinc>不同的是，\<withKotlin>并不支持自动打包编译的类，因此可以使用\<jar>任务来替换。

