### 17.8　Spring Boot热部署与日志管理

热部署和日志是Web开发中常用的功能之一，Spring Boot提供了spring-boot-devtools模块用于热部署开发，当需要重新编译修改后的代码时，工程就会重新启动加载。

```python
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <optional>true</optional>
</dependency>
```

除了devtools插件外，另一个使用频率较高的插件是springloaded，添加插件依赖后，完成项目编译即可实现热部署。

默认情况下，Spring Boot会用Logback来记录日志并通过INFO级别输出到控制台，在应用程序运行过程中，可以看到很多INFO级别的日志。Logback是继Log4j框架之后的新一代日志框架，它效率更高、适应诸多的运行环境，同时天然支持SLF4J。

Logback可以根据进程ID输出日志并将这些日志分为ERROR、WARN、INFO、DEBUG、TRACE和FATAL等几个级别，日志级别由低到高分为TRACE < DEBUG < INFO < WARN < ERROR < FATAL。

Logback的默认输出级别是INFO，也就是说低于INFO级别的信息都不会输出。Logback的默认配置可以在“org.springframework.boot.logging.logback”包的base.xml文件中找到。

```python
<?xml version="1.0" encoding="UTF-8"?><included>
    <include resource="org/springframework/boot/logging/logback/defaults.xml" />
    <property name="LOG_FILE" value="${LOG_FILE:-${LOG_PATH:-${LOG_TEMP:-${java. io.tmpdir:-/tmp}}}/spring.log}"/>
    <include resource="org/springframework/boot/logging/logback/console-appender. xml" />
    <include resource="org/springframework/boot/logging/logback/file-appender. xml" />
    <root level="INFO">
          <appender-ref ref="CONSOLE" />
          <appender-ref ref="FILE" />
    </root>
</included>
```

如果需要修改日志的输出级别，则可以在配置文件application.properties中进行修改。

```python
logging.file=test.log
logging.level.com.fyft.wx.controller=warn   //修改日志输出级别
```

使用该配置，当项目运行时会在工程的根目录生成对应的日志文件，把com.fyft.wx.controller包的日志级别设置为WARN。

```python
@RestController
class LogController {
     companion object {
        private val LOG = LoggerFactory.getLogger(LogController::class.java)
    }
    @RequestMapping("logTest")
    fun log() {
         LOG.info("i am info…")
         LOG.error("i am error…")
         LOG.debug("i am debug…")
         LOG.warn("i am warn…")
         LOG.trace("i am trace…")
    } 
}
```

在浏览器中输入“http://localhost:8080/logTest”并访问该接口，可以发现只会输出WARN和高于WARN级别的日志。

如果系统默认的日志功能无法满足项目要求，则可以自己写一个XML文件来覆盖默认配置，在resource下新建一个logback.xml配置文件并添加如下配置。

```python
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <include resource="org/springframework/boot/logging/logback/base.xml"/>
    <logger name="org.springframework.web" level="WARN"/>
    <!-- 日志存储路径 -->
    <property name="LOG_HOME" value="C:\\logs" />
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <File>${LOG_HOME}\\fyft-wx.log</File>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <FileNamePattern>${LOG_HOME}\\temp\\fyft-wx.%d{yyyy-MM-dd}.%i.log</FileNamePattern>
            <maxHistory>30</maxHistory>
            <!-- 日志大小 -->
            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>2MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
        </rollingPolicy>
        <encoder>
            <Pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{35} - %msg %n</Pattern>
            <charset>UTF-8</charset> 
        </encoder>
    </appender>
    <!-- root节点，配置日志级别，添加输出节点 -->
    <root level="INFO">
          <appender-ref ref="FILE"></appender-ref>
    </root>
</configuration>
```

如果输出到控制台的日志也需要自定义，可以在root节点上再新增一个appender配置，不过需要注意，添加自定义配置时需要将Spring Boot默认的配置删掉。

