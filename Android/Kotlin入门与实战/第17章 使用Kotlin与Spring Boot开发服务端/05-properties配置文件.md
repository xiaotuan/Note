### 17.1.5　properties配置文件

Spring Boot让软件开发者从烦琐的XML配置中解脱出来，但并非所有内容都可以自动配置。为此SpringBoot提供了application.properties配置文件，方便开发者进行自定义配置，而且对于application.peroperties文件中的所有配置内容Spring Boot都可以自动加载，免去了手动编码加载带来的烦恼。

Spring Boot提供了两种格式的配置文件，分别是.yml文件和.properties文件，它们都位于项目的src/main/resource目录下。application.properties文件和application.yml文件是可以互换的，但是语法格式上略微有一些区别。这两种文件都可以被Spring Boot自动识别并加载，但是如果需要使用自定义配置文件，最好还是使用properties格式的文件来进行编写。

application.properties配置文件在Spring Boot项目启动时被自动加载到Spring容器之中，当需要某个配置选项时可以随时取用，而自定义的相关配置会自动覆盖Spring Boot默认的配置选项。application.properties默认提供了一些常用的配置选项。

+ spring.datasource.auto-commit：指定数据源updates是否自动提交。
+ spring.datasource.driver-class-name：指定driver的类名，默认从JDBC的URL中自动探测。
+ spring.datasource.url：指定JDBC数据源的URL地址。
+ spring.datasource.username：指定数据库名称。
+ spring.datasource.password：指定数据库密码。
+ spring.jpa.show-sql：运行时是否显示SQL语句。
+ spring.datasource.pool-name：指定连接池名称。

除了上面列举的内容外，Spring Boot还提供了很多实用的配置，此处不再一一介绍。前面说过，如果想要自定义一个properties配置文件，那么这个自定义的×××.properties配置文件是不会被Spring Boot自动加载的，需要手动进行加载。

在resources目录下，新建一个test.properties文件并添加如下内容。

```python
jack.name=jack
jack.sex=man
jack.age=30
```

其实，无论是系统提供的application.properties配置文件还是自定义的×××.properties文件，当需要使用配置文件中内容的时候，都需要在当前类的顶部添加该注解，以便在程序启动的时候将该配置文件加载到内存中。

系统要想加载自定义的配置文件，就需要将自定义的配置属性绑定到具体的JavaBean上，使用@PropertySource注解设置配置文件的加载路径，使用@ConfigurationProperties注解将properties或yml配置转换成实体类的对象。代码如下。

```python
@PropertySource("classpath:test.properties")
@ConfigurationProperties(prefix = "test")
@Configuration
class UserConfig {
      @Value("\${jack.name}")
      var name: String? = null
      @Value("\${jack.sex}")
      var sex: String? = null
      @Value("\${jack.age}")
      var age: Int = 0
}
```

使用@Value注解是为了直接引用properties文件的属性值。为了能够在应用程序启动后获得properties文件的内容，还需要提供一个测试的方法，该部分内容如下。

```python
    @Autowired
    private UserConfig userConfig;
    @GetMapping("/test")
    public String test() {
        return "name: "+userConfig.getName()+", age: "+
                 userConfig.getAge()+", sex: "+userConfig.getSex();
    }
```

此时，启动Spring Boot应用程序，等待程序启动完成后，在浏览器中输入“http:// localhost:8888/test”即可获取到properties文件的相关内容。

```python
name: jack, age: 30, sex: man
```

