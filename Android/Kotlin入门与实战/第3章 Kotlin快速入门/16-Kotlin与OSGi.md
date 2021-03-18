### 3.4.4　Kotlin与OSGi

本书说到的OSGi（Open Service Gateway initiative，开放服务网关协议）是指一系列用于定义Java动态化组件系统的标准，这些标准为大型分布式系统以及嵌入式系统提供一种模块化架构，以减少软件的复杂度。

要在Kotlin中启用OSGi支持，需要在项目中引入kotlin-osgi-bundle库而不是常规的Kotlin库。如果在Gradle构建的项目中引入Kotlin OSGi，则需要在配置文件中添加如下脚本。

```python
compile "org.jetbrains.kotlin:kotlin-osgi-bundle:$kotlinVersion"
```

如果要排除项目中传递的依赖Kotlin库，可以使用以下方式。

```python
dependencies {
 compile (
   [group: 'some.group.id', name: 'some.library', version: 'someversion'],
   ……) {
  exclude group: 'org.jetbrains.kotlin'
}
```

如果要在Maven构建的项目中使用Kotlin OSGi，则需要在pom配置文件中添加如下内容。

```python
<dependencies>
   <dependency>
      <groupId>org.jetbrains.kotlin</groupId>
      <artifactId>kotlin-osgi-bundle</artifactId>
      <version>${kotlin.version}</version>
   </dependency>
</dependencies>
```

如果要排除某些标准库，则可以添加如下配置。

```python
<dependency>
    <!-- 需要排除的库 -->
    <groupId>some.group.id</groupId>
    <artifactId>some.library</artifactId>
    <version>some.library.version</version>
    <exclusions>
      <exclusion>
        <groupId>org.jetbrains.kotlin</groupId>
            <!--  *排除方式只在Maven 3起作用 -->
            <artifactId>*</artifactId>
            </exclusion>
      </exclusions>
</dependency>
```

