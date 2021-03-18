### 14.4.1　Maven构建方式

kotlinx.html项目发布在“https://jcenter.bintray.com/”仓库中，可以通过该地址来获取最新版本，添加仓库配置脚本如下。

```python
<repository>
   <id>jcenter</id>
   <name>jcenter</name>
   <url>https://jcenter.bintray.com</url>
</repository>
```

然后，在Maven项目的pom文件中添加kotlinx.html依赖配置。

```python
<dependency>
  <groupId>org.jetbrains.kotlinx</groupId>
  <artifactId>kotlinx-html</artifactId>
  <version>0.6.8</version>
  <type>pom</type>
</dependency>
```

使用kotlinx.html只是构建服务端的DSL，则只需要添加kotlinx-html-jvm相关配置。

```python
<dependency>
   <groupId>org.jetbrains.kotlinx</groupId>
   <artifactId>kotlinx-html-jvm</artifactId>   //针对JVM的DSL
   <version>${kotlinx.html.version}</version>
</dependency>
```

同理，如果使用kotlinx.html只是为了构建针对JavaScript的DSL项目，则只需要添加kotlinx-html-js相关配置。

```python
<dependency>
   <groupId>org.jetbrains.kotlinx</groupId>
   <artifactId>kotlinx-html-js</artifactId>   //针对JS的DSL
   <version>${kotlinx.html.version}</version>
</dependency>
```

如果通过使用war插件的方式构建Web应用程序，则可以使用类似于下面的配置来打包。

```python
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-war-plugin</artifactId>
    <version>2.6</version>
    <configuration>
    <dependentWarExcludes>META-INF/*,META-INF/**/*,*meta.js,**/*class</dependen-
tWarExcludes>
    <webXml>src/main/resources/web.xml</webXml>
    <webResources>
       <resource>
          <directory>src/main/webapp</directory>
       </resource>
    </webResources>
        <overlays>
           <overlay>
              <groupId>org.jetbrains.kotlin</groupId>
               <artifactId>kotlin-js-library</artifactId>
               <type>jar</type>
                 <includes>
                 <include>kotlin.js</include>
              </includes>
                 <targetPath>js/</targetPath>
               </overlay>
               <overlay>
                  <groupId>org.jetbrains.kotlinx</groupId>
                  <artifactId>kotlinx-html-assembly</artifactId>
                  <classifier>webjar</classifier>
                  <type>jar</type>
                  <targetPath>js/</targetPath>
                </overlay>
               </overlays>
              </configuration>
</plugin>
```

