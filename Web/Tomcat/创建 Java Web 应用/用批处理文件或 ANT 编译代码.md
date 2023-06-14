下面是一个编译源代码的脚步 `compile.bat`：

```bat
set catalina_home=C:\tomcat
set path=%path%;C:\jdk\bin

set currpath=.\
if "%OS%" == "Windows_NT" set currpath=%~dp0%

set src=%currpath%helloapp\src
set dest = %currpath%\helloapp\WEB-INF\classes
set classpath=%catalina_home%\lib\servlet-api.jar;%catalina_home%\lib\jsp-api.jar

javac -sourcepath %src% -d %dest% %src%\mypack\DispatcherServlet.java
javac -sourcepath %src% -d %dest% %src%\mypack\HelloTag.java
```

运行这个批处理文件时，只要先重新设置以上 `Tomcat` 目录和 `JDK` 的根目录即可。

除了用上述批处理文件编译范例，还可以使用 `ANT` 工具来编译范例。在 `Web` 应用的根目录下创建一个 `build.xml` 文件，其内容如下：

```xml
<project name="helloapp" default="compile" basedir=".">
	<property name="tomcat.home" value="C:/tomcat" />
    <property name="app.home" value="." />
    
    <property name="src.home" value="${app.home}/src" />
    <property name="classes.home" value="${app.home}/WEB-INF/classes" />
    
    <!-- 设置 classpath  -->
    <path id="compile.classpath">
    	<pathelement location="${classes.home}" />
        <fileset dir="${tomcat.home}/lib">
        	<include name="*.jar" />
        </fileset>
    </path>
    
    <!-- 编译任务  -->
    <target name="compile">
    	<javac srcdir="${src.home}" destdir="${classes.home}" debug="yes" includeAntRuntime="false">
        	<classpath refid="compile.classpath" />
        </javac>
    </target>
</project>
```

用 `ANT` 工具来编译范例的步骤如下：

（1）安装和配置 `ANT`。

（2）打开 `helloapp` 应用下的 `build.xml` 文件，确认 `tomcat.home` 属性的值为本地 `Tomcat` 的根目录：

```xml
<property name="tomcat.home" value="C:/tomcat" />
```

（3）在 `DOS` 下，转到 `helloapp` 目录下，运行命令 `ant`，该命令会执行 `build.xml` 文件中的 `compile` 任务，编译 `src` 子目录下的所有 `Java` 源文件，编译生成的 `.class` 文件位于 `WEB-INF/classes` 子目录下。