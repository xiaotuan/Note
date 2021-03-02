 

[toc]

### Servlet概述

生命周期方法：

+ void init(ServletConfig)：出生之后（1次）；

+ void service(ServletRequest request, ServletResponse response)：每次处理请求时都会被调用；

+ void destroy()：临死之前（1次）；

 

特性：

+ 单例，一个类只有一个对象；当然可能存在多个 Servlet 类！

+ 线程不案例的，所以它的效率是高的！

**Servlet ** 类由我们来写，但对象由服务器来创建，并且由服务器来调用相应的方法。

#### 1　什么是Servlet

Servlet 是 JavaWeb 的**三大组件之一**，它属于动态资源。Servlet 的作用是处理请求，服务器会把接收到的请求交给 Servlet 来处理，在 Servlet 中通常需要：

+ 接收请求数据；

+ 处理请求；

+ 完成响应。

例如客户端发出登录请求，或者输出注册请求，这些请求都应该由 Servlet 来完成处理！Servlet 需要我们自己来编写，每个 Servlet 必须实现 `javax.servlet.Servlet` 接口。

#### 2　实现Servlet的方式（由我们自己来写！）

实现 Servlet 有三种方式：

+ 实现 javax.servlet.Servlet 接口；

+ 继承 javax.servlet.GenericServlet 类；

+ 继承 javax.servlet.http.HttpServlet 类；

通常我们会去继承 HttpServlet 类来完成我们的 Servlet，但学习 Servlet 还要从 javax.servlet.Servlet 接口开始学习。

**Servlet.java**

```java
public interface Servlet() {
    public void init(ServletConfig config) throws ServletException;
    public ServletConfig  getServletConfig();
    public void service(ServletRequest req,  ServletResponse res) throws ServletException,  IOException;
    public String getServletInfo();
    public void destroy();
}  
```

#### 3　创建helloservlet应用

我们开始第一个 Servlet 应用吧！首先在 webapps 目录下创建 helloservlet 目录，它就是我们的应用目录了，然后在 helloservlet 目录中创建准备JavaWeb应用所需内容：

+ 创建 /helloservlet/WEB-INF 目录；

+ 创建 /helloservlet/WEB-INF/classes 目录；

+ 创建 /helloservlet/WEB-INF/lib 目录；

+ 创建 /helloservlet/WEB-INF/web.xml 文件；

接下来我们开始准备完成 Servlet，完成 Servlet 需要分为两步：

+ 编写 Servlet 类；

+ 在 web.xml 文件中配置 Servlet；

**HelloServlet.java**

```java
public class HelloServlet implements Servlet {
    public void init(ServletConfig config) throws ServletException {}
    public ServletConfig  getServletConfig() { return null;}
    public void destroy() {}
    public String getServletInfo() { return null ;}
    public void service(ServletRequest req,  ServletResponse res) throws ServletException,  IOException { System.out.println("hello servlet!");    }
}  
```

我们暂时忽略 Servlet 中其他四个方法，只关心 service() 方法，因为它是用来处理请求的方法。我们在该方法内给出一条输出语句！

web.xml（下面内容需要背下来）

```xml
<servlet>      
    <servlet-name>hello</servlet-name>
    <servlet-class>cn.itcast.servlet.HelloServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>hello</servlet-name>
    <url-pattern>/helloworld</url-pattern>
</servlet-mapping>   
```

在 web.xml 中配置 Servlet 的目的其实只有一个，就是把访问路径与一个 Servlet 绑定到一起，上面配置是把访问路径：“/helloworld”与“cn.itcast.servlet.HelloServlet” 绑定到一起。

+ `<servlet>`：指定 HelloServlet 这个 Servlet 的名称为 hello；

+ `<servlet-mapping>`：指定 /helloworld 访问路径所以访问的 Servlet 名为 hello。

`<servlet>` 和 `<servlet-mapping>` 通过 `<servlet-name>` 这个元素关联在一起了！

接下来，我们编译 HelloServlet，注意，编译 HelloServlet 时需要导入 servlet-api.jar，因为 Servlet.class 等类都在 servlet-api.jar 中。

```shell
javac -classpath F:/tomcat6/lib/servlet-api.jar -d . HelloServlet.java
```

然后把 HelloServlet.class 放到 /helloworld/WEB-INF/classes/ 目录下，然后启动 Tomcat，在浏览器中访问：http://localhost:8080/helloservlet/helloworld 即可在控制台上看到输出！

+ /helloservlet/WEB-INF/classes/cn/itcast/servlet/HelloServlet.class；

### Servlet接口 

#### 1    Servlet的生命周期

所谓 xxx 的生命周期，就是说 xxx 的出生、服务，以及死亡。Servlet 生命周期也是如此！与 Servlet 的生命周期相关的方法有：

+ void init(ServletConfig)；

+ void service(ServletRequest,ServletResponse)；

+ void destroy()；

##### 1.1　Servlet的出生

服务器会在 Servlet 第一次被访问时创建 Servlet，或者是在服务器启动时创建 Servlet。如果服务器启动时就创建 Servlet，那么还需要在 web.xml 文件中配置。也就是说默认情况下，Servlet 是在第一次被访问时由服务器创建的。

而且一个 Servlet 类型，服务器只创建一个实例对象，例如在我们首次访问 <http://localhost:8080/helloservlet/helloworld? 时，服务器通过 “/helloworld” 找到了绑定的 Servlet 名称为cn.itcast.servlet.HelloServlet，然后服务器查看这个类型的 Servlet 是否已经创建过，如果没有创建过，那么服务器才会通过反射来创建 HelloServlet 的实例。当我们再次访问 <http://localhost:8080/helloservlet/helloworld> 时，服务器就不会再次创建 HelloServlet 实例了，而是直接使用上次创建的实例。

在 Servlet 被创建后，服务器会马上调用 Servlet 的 `void init(ServletConfig)` 方法。请记住， Servlet 出生后马上就会调用 `init()` 方法，而且一个 Servlet 的一生。这个方法只会被调用一次。这好比小孩子出生后马上就要去剪脐带一样，而且剪脐带一生只有一次。

我们可以把一些对 Servlet 的初始化工作放到init方法中！

##### 1.2　Servlet服务

　　当服务器每次接收到请求时，都会去调用 Servlet 的 service() 方法来处理请求。服务器接收到一次请求，就会调用 service() 方法一次，所以 service() 方法是会被调用多次的。正因为如此，所以我们才需要把处理请求的代码写到 service() 方法中！

##### 1.3　Servlet的离去

　　Servlet 是不会轻易离去的，通常都是在服务器关闭时 Servlet 才会离去！在服务器被关闭时，服务器会去销毁 Servlet，在销毁 Servlet 之前服务器会先去调用 Servlet 的 destroy() 方法，我们可以把Servlet的临终遗言放到 destroy() 方法中，例如对某些资源的释放等代码放到 destroy() 方法中。

##### 1.4　测试生命周期方法

修改 HelloServlet 如下，然后再去访问 <http://localhost:8080/helloservlet/helloworld>

```java
public class HelloServlet implements Servlet {
    public void init(ServletConfig config) throws ServletException {
        System.out.println("Servlet被创建了！");
    }
    
    public ServletConfig  getServletConfig() {
        return null ;
    }
    
    public void destroy() {
        System.out.println("Servlet要离去了！");
    }
    
    public String getServletInfo() {
        return null;
    }
    
    public void service(ServletRequest req,  ServletResponse res) throws** ServletException,  IOException {
        System.out.println("hello servlet!");
    }
}  
```

在首次访问 HelloServlet 时，init 方法会被执行，而且也会执行 service 方法。再次访问时，只会执行service 方法，不再执行 init 方法。在关闭 Tomcat 时会调用 destroy 方法。

#### 2　Servlet接口相关类型

在 Servlet 接口中还存在三个我们不熟悉的类型：

+ ServletRequest：service() 方法的参数，它表示请求对象，它封装了所有与请求相关的数据，它是由服务器创建的；

+ ServletResponse：service() 方法的参数，它表示响应对象，在 service() 方法中完成对客户端的响应需要使用这个对象；

+ ServletConfig：init()方法的参数，它表示 Servlet 配置对象，它对应 Servlet 的配置信息，那对应web.xml 文件中的 `<servlet>` 元素。

##### 2.1　ServletRequest 和 ServletResponse（第五天会详细讲解这两个对象）

ServletRequest 和 ServletResponse 是 Servlet#service() 方法的两个参数，一个是请求对象，一个是响应对象，可以从 ServletRequest 对象中获取请求数据，可以使用 ServletResponse 对象完成响应。你以后会发现，这两个对象就像是一对恩爱的夫妻，永远不分离，总是成对出现。

ServletRequest 和 ServletResponse 的实例由服务器创建，然后传递给 service() 方法。如果在service() 方法中希望使用 HTTP 相关的功能，那么可以把 ServletRequest 和 ServletResponse 强转成HttpServletRequest 和 HttpServletResponse。这也说明我们经常需要在 service() 方法中对ServletRequest 和 ServletResponse 进行强转，这是很心烦的事情。不过后面会有一个类来帮我们解决这一问题的。

HttpServletRequest 方法：

+ String getParameter(String paramName)：获取指定请求参数的值；

+ String getMethod()：获取请求方法，例如GET或POST；

+ String getHeader(String name)：获取指定请求头的值；

+ void setCharacterEncoding(String encoding)：设置请求体的编码！因为 GET 请求没有请求体，所以这个方法只只对 POST 请求有效。当调用 request.setCharacterEncoding(“utf-8”) 之后，再通过getParameter() 方法获取参数值时，那么参数值都已经通过了转码，即转换成了 UTF-8 编码。所以，这个方法必须在调用 getParameter() 方法之前调用！

HttpServletResponse方法：

+ PrintWriter getWriter()：获取字符响应流，使用该流可以向客户端输出响应信息。例如`response.getWriter().print(“<h1>Hello JavaWeb!</h1>”)`；

+ ServletOutputStream getOutputStream()：获取字节响应流，当需要向客户端响应字节数据时，需要使用这个流，例如要向客户端响应图片；

+ void setCharacterEncoding(String encoding)：用来设置字符响应流的编码，例如在调用`setCharacterEncoding(“utf-8”);` 之后，再 `response.getWriter()` 获取字符响应流对象，这时的响应流的编码为 utf-8，使用 `response.getWriter()` 输出的中文都会转换成 utf-8 编码后发送给客户端；

+ void setHeader(String name, String value)：向客户端添加响应头信息，例如`setHeader(“Refresh”, “3;url=http://www.itcast.cn”)`，表示 3 秒后自动刷新到 <http://www.itcast.cn>；

+ void setContentType(String contentType)：该方法是 `setHeader(“content-type”, “xxx”)` 的简便方法，即用来添加名为 content-type 响应头的方法。content-type 响应头用来设置响应数据的MIME 类型，例如要向客户端响应 jpg 的图片，那么可以 `setContentType(“image/jepg”)`，如果响应数据为文本类型，那么还要台同时设置编码，例如`setContentType(“text/html;chartset=utf-8”)` 表示响应数据类型为文本类型中的html类型，并且该方法会调用 `setCharacterEncoding(“utf-8”)` 方法；

+ void sendError(int code, String errorMsg)：向客户端发送状态码，以及错误消息。例如给客户端发送 404：response(404, “您要查找的资源不存在！”)。

##### 2.2　ServletConfig

ServletConfig 对象对应 web.xml 文件中的 `<servlet>` 元素。例如你想获取当前 Servlet 在 web.xml 文件中的配置名，那么可以使用 `servletConfig.getServletName()` 方法获取！

![img](.\images\clip_image002.jpg)

ServletConfig 对象是由服务器创建的，然后传递给 Servlet 的 init() 方法，你可以在 init() 方法中使用它！

+ String getServletName()：获取 Servlet 在 web.xml 文件中的配置名称，即 `<servlet-name>` 指定的名称；

+ ServletContext getServletContext()：用来获取 ServletContext 对象，ServletContext 会在后面讲解；

+ String getInitParameter(String name)：用来获取在 web.xml 中配置的初始化参数，通过参数名来获取参数值；

+ Enumeration getInitParameterNames()：用来获取在 web.xml 中配置的所有初始化参数名称；

在 `<servlet>` 元素中还可以配置初始化参数：

```xml
 <servlet>    
     <servlet-name>One</servlet-name>
     <servlet-class>cn.itcast.servlet.OneServlet</servlet-class>
     <init-param>
         <param-name>paramName1</param-name>
         <param-value>paramValue1</param-value>
     </init-param>
     <init-param>
         <param-name>paramName2</param-name>
         <param-value>paramValue2</param-value>
     </init-param>
</servlet>  
```

在 OneServlet 中，可以使用 ServletConfig 对象的 `getInitParameter()` 方法来获取初始化参数，例如：

```java 
String value1 = servletConfig.getInitParameter(“paramName1”);//获取到paramValue1
```

#### 3. GenericServlet

##### 3.1 GenericServlet概述

GenericServlet 是 Servlet 接口的实现类，我们可以通过继承 GenericServlet 来编写自己的 Servlet。下面是 GenericServlet 类的源代码：

**GenericServlet.java**

```java
public abstract class GenericServlet implements Servlet,  ServletConfig, java.io.Serializable {
    private static final long serialVersionUID = 1L;
    private transient ServletConfig config;
    
    public GenericServlet() {}    
    
    @Override
    public void destroy() {}    
    
    @Override
    public String getInitParameter(String name) {
        return etServletConfig().getInitParameter(name);
    }
    
    @Override
    public Enumeration<String> getInitParameterNames() {
        return getServletConfig().getInitParameterNames();
    }
    
    @Override
    public ServletConfig getServletConfig() {
        return config;
    }
    
    @Override
    public ServletContext getServletContext() {
        return getServletConfig().getServletContext();
    }
    
    @Override
    public String getServletInfo() {
        return "";
    }
    
    @Override
    public void init(ServletConfig config) throws ServletException {
        this.config = config;
        this.init();
    }
    
    public void init() throws ServletException {}
    
    public void log(String msg) {
        getServletContext().log(getServletName() + ": " + msg);
    }
    
    public void log(String message, Throwable t) {
        getServletContext().log(getServletName() + ": " + message, t);
    }
    
    @Override
    public abstract void service(ServletRequest req, ServletResponse res) throws ServletException, IOException;
    
    @Override
    public String getServletName() {
        return config.getServletName();
    }
}  
```

##### 3.2　GenericServlet 的 init() 方法

在 GenericServlet 中，定义了一个 `ServletConfig config` 实例变量，并在 `init(ServletConfig)` 方法中把参数 ServletConfig 赋给了实例变量。然后在该类的很多方法中使用了实例变量 config。

如果子类覆盖了 GenericServlet 的 `init(StringConfig)` 方法，那么` this.config=config` 这一条语句就会被覆盖了，也就是说 GenericServlet 的实例变量 config 的值为 null，那么所有依赖 config 的方法都不能使用了。如果真的希望完成一些初始化操作，那么去覆盖 GenericServlet 提供的 init() 方法，它是没有参数的 init() 方法，它会在 init(ServletConfig) 方法中被调用。

##### 3.3　实现了 ServletConfig 接口

GenericServlet 还实现了 ServletConfig 接口，所以可以直接调用 `getInitParameter()`、`getServletContext()` 等 ServletConfig 的方法。

#### 4. HttpServlet

##### 4.1 HttpServlet概述

HttpServlet 类是 GenericServlet 的子类，它提供了对 HTTP 请求的特殊支持，所以通常我们都会通过继承 HttpServlet 来完成自定义的 Servlet。

##### 4.2 HttpServlet覆盖了service()方法

HttpServle t类中提供了 `service(HttpServletRequest,HttpServletResponse)` 方法，这个方法是HttpServlet 自己的方法，不是从 Servlet 继承来的。在 HttpServlet 的 `service(ServletRequest,ServletResponse)` 方法中会把 ServletRequest 和 ServletResponse 强转成 HttpServletRequest 和 HttpServletResponse，然后调用 `service(HttpServletRequest,HttpServletResponse)` 方法，这说明子类可以去覆盖`service(HttpServletRequest,HttpServletResponse)` 方法即可，这就不用自己去强转请求和响应对象了。

其实子类也不用去覆盖 `service(HttpServletRequest,HttpServletResponse)` 方法，因为HttpServlet 还要做另一步简化操作，下面会介绍。

**HttpServlet.java**

```java
public abstract class HttpServlet extends GenericServlet {
    
    protected void service(HttpServletRequest  req, HttpServletResponse resp) throws ServletException, IOException {
    	......
    }    
    
    @Override
    public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException {
        HttpServletRequest request;
        HttpServletResponse response;
        try {
            request = (HttpServletRequest) req;
            response = (HttpServletResponse) res;
        } catch (ClassCastException e) {
            throw new ServletException("non-HTTP request or response");
        }
        service(request, response);
    }
    ......
}  
```

##### 4.3 doGet()和doPost()

在 HttpServlet 的 `service(HttpServletRequest,HttpServletResponse)` 方法会去判断当前请求是GET 还是 POST，如果是 GET 请求，那么会去调用本类的 `doGet()` 方法，如果是 POST 请求会去调用`doPost()` 方法，这说明我们在子类中去覆盖 `doGet()` 或 `doPost()` 方法即可。

 ```java
public class AServlet extends HttpServlet {
    
    public void doGet(HttpServletRequest  request, HttpServletResponse response) throws ServletException, IOException {
        System.*out*.println("hello doGet()...");
    }  
}  
 ```

```java
public class BServlet extends HttpServlet {
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("hello doPost()...");
    }
}
```

###  Servlet细节

+ 不要在Servlet中创建成员！创建局部变量即可！

+ 可以创建无状态成员！

+ 可以创建有状态的成员，但状态必须为只读的！

#### 1　Servlet与线程安全

因为一个类型的 Servlet 只有一个实例对象，那么就有可能会现时出一个 Servlet 同时处理多个请求，那么 Servlet 是否为线程安全的呢？答案是：“不是线程安全的”。这说明 Servlet 的工作效率很高，但也存在线程安全问题！

所以我们不应该在 Servlet 中便宜创建成员变量，因为可能会存在一个线程对这个成员变量进行写操作，另一个线程对这个成员变量进行读操作。

#### 2　让服务器在启动时就创建 Servlet

默认情况下，服务器会在某个 Servlet 第一次收到请求时创建它。也可以在 web.xml 中对 Servlet 进行配置，使服务器启动时就创建 Servlet。

```xml
<servlet>
    <servlet-name>hello1</servlet-name>
    <servlet-class>cn.itcast.servlet.Hello1Servlet</servlet-class>
    <load-on-startup>0</load-on-startup>
</servlet>

<servlet-mapping>
    <servlet-name>hello1</servlet-name>
    <url-pattern>/hello1</url-pattern>
</servlet-mapping>

<servlet>
    <servlet-name>hello2</servlet-name>
    <servlet-class>cn.itcast.servlet.Hello2Servlet</servlet-class>
    <load-on-startup>1</load-on-startup>
</servlet>

<servlet-mapping>
    <servlet-name>hello2</servlet-name>
    <url-pattern>/hello2</url-pattern>
</servlet-mapping>

<servlet>
    <servlet-name>hello3</servlet-name>
    <servlet-class>cn.itcast.servlet.Hello3Servlet</servlet-class>
    <load-on-startup>2</load-on-startup>
</servlet>

<servlet-mapping>
    <servlet-name>hello3</servlet-name>
    <url-pattern>/hello3</url-pattern>
</servlet-mapping>  
```

在 `<servlet>` 元素中配置 `<load-on-startup>` 元素可以让服务器在启动时就创建该 Servlet，其中`<load-on-startup>` 元素的值必须是大于等于的整数，它的使用是服务器启动时创建 Servlet 的顺序。上例中，根据 `<load-on-startup>` 的值可以得知服务器创建 Servlet 的顺序为 Hello1Servlet、Hello2Servlet、Hello3Servlet。

#### 3 `<url-pattern>`

`<url-pattern>` 是 `<servlet-mapping>` 的子元素，用来指定 Servlet 的访问路径，即 URL。它必须是以 “/” 开头！

1)    可以在 `<servlet-mapping>`中给出多个 `<url-pattern>`，例如：

   ```xml
<servlet-mapping>
    <servlet-name>AServlet</servlet-name>
    <url-pattern>/AServlet</url-pattern>
    <url-pattern>/BServlet</url-pattern>
</servlet-mapping>  
   ```

那么这说明一个 Servlet 绑定了两个 URL，无论访问 /AServlet 还是 /BServlet，访问的都是 AServlet。

2)    还可以在 `<url-pattern>` 中使用通配符，所谓通配符就是星号 “*”，星号可以匹配任何URL前缀或后缀，使用通配符可以命名一个 ``Servlet` 绑定一组 URL，例如：

+ `<url-pattern>/servlet/*<url-patter>`：/servlet/a、/servlet/b，都匹配 /servlet/*；

+ `<url-pattern>*.do</url-pattern>`：/abc/def/ghi.do、/a.do，都匹配 *.do；

+ `<url-pattern>/*<url-pattern>`：匹配所有 URL；

请注意，通配符要么为前缀，要么为后缀，不能出现在URL中间位置，也不能只有通配符。例如：\*.do就是错误的，因为星号出现在 URL 的中间位置上了。\*.\* 也是不对的，因为一个URL中最多只能出现一个通配符。

注意，通配符是一种模糊匹配 URL 的方式，如果存在更具体的 `<url-pattern>`，那么访问路径会去匹配具体的 `<url-pattern>`。例如：

```xml
<servlet>
    <servlet-name>hello1</servlet-name>
    <servlet-class>cn.itcast.servlet.Hello1Servlet</servlet-class>
</servlet>

<servlet-mapping>
    <servlet-name>hello1</servlet-name>
    <url-pattern>/servlet/hello1</url-pattern>
</servlet-mapping>

<servlet>
    <servlet-name>hello2</servlet-name>
    <servlet-class>cn.itcast.servlet.Hello2Servlet</servlet-class>
</servlet>

<servlet-mapping>
    <servlet-name>hello2</servlet-name>
    <url-pattern>/servlet/*</url-pattern>
</servlet-mapping>
```

　当访问路径为 <http://localhost:8080/hello/servlet/hello1> 时，因为访问路径即匹配 hello1 的 `<url-pattern>`，又匹配 hello2 的 `<url-pattern>`，但因为 hello1 的 `<url-pattern>` 中没有通配符，所以优先匹配，即设置 hello1。

#### 4　web.xml文件的继承（了解）

　　在 `${CATALINA_HOME}\conf\web.xml` 中的内容，相当于写到了每个项目的 web.xml 中，它是所有 web.xml 的父文件。

每个完整的 JavaWeb 应用中都需要有 web.xml，但我们不知道所有的 web.xml 文件都有一个共同的父文件，它在 Tomcat 的 conf/web.xml 路径。

**conf/web.xml**

```xml
<?xml version=*"1.0"*  encoding=*"ISO-8859-1"*?>     
<web-app xmlns="http://java.sun.com/xml/ns/javaee"
         xmlns:xsi=*"http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
                              http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
         version="3.0">
    <servlet>
        <servlet-name>default</servlet-name>
        <servlet-class>org.apache.catalina.servlets.DefaultServlet</servlet-class>
        <init-param>
            <param-name>debug</param-name>
            <param-value>0</param-value>
        </init-param>
        <init-param>
            <param-name>listings</param-name>
            <param-value>false</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>
    
    <servlet>
        <servlet-name>jsp</servlet-name>
        <servlet-class>org.apache.jasper.servlet.JspServlet</servlet-class>
        <init-param>  
            <param-name>fork</param-name>
            <param-value>false</param-value>
        </init-param>
        <init-param>
            <param-name>xpoweredBy</param-name>
            <param-value>false</param-value>
        </init-param>
        <load-on-startup>3</load-on-startup>
    </servlet>
    
    <servlet-mapping>
        <servlet-name>default</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
    
    <servlet-mapping>
        <servlet-name>jsp</servlet-name>
        <url-pattern>*.jsp</url-pattern>
        <url-pattern>*.jspx</url-pattern>
    </servlet-mapping>
    <session-config>
        <session-timeout>30</session-timeout>
    </session-config>
    
    <!-- 这里省略了大概4000多行的MIME类型的定义,这里只给出两种MIME类型的定义 -->
    <mime-mapping>
        <extension>bmp</extension>
        <mime-type>image/bmp</mime-type>
    </mime-mapping>
    
    <mime-mapping>
        <extension>htm</extension>
        <mime-type>text/html</mime-type>
    </mime-mapping>
    
    <welcome-file-list>
        <welcome-file>index.html</welcome-file>
        <welcome-file>index.htm</welcome-file>
        <welcome-file>index.jsp</welcome-file>
    </welcome-file-list>
</web-app>  
```

### ServletContext（重要）

一个项目只有一个ServletContext对象！

我们可以在N多个Servlet中来获取这个唯一的对象，使用它可以给多个Servlet传递数据！

与天地同寿！！！这个对象在Tomcat启动时就创建，在Tomcat关闭时才会死去！

 

 

###### 1　ServletContext概述

服务器会为每个应用创建一个ServletContext对象：

l ServletContext对象的创建是在服务器启动时完成的；

l ServletContext对象的销毁是在服务器关闭时完成的。

 

　　 ServletContext对象的作用是在整个Web应用的动态资源之间共享数据！例如在AServlet中向ServletContext对象中保存一个值，然后在BServlet中就可以获取这个值，这就是共享数据了。

 

###### 2　获取ServletContext

l ServletConfig#getServletContext()；

l GenericServlet#getServletContext();

l HttpSession#getServletContext()

l ServletContextEvent#getServletContext()

[[c18\]](#_msocom_18) 

 

在Servlet中获取ServletContext对象：

l 在void init(ServletConfig config)中：ServletContext context = config.getServletContext();，ServletConfig类的getServletContext()方法可以用来获取ServletContext对象；

在GenericeServlet或HttpServlet中获取ServletContext对象：

l GenericServlet类有getServletContext()方法，所以可以直接使用this.getServletContext()来获取；

　　

| public class MyServlet implements Servlet  {  public void  init(ServletConfig config) {    ServletContext context =  config.getServletContext();  }  …  } |
| ------------------------------------------------------------ |
| public class MyServlet extends  HttpServlet {  public void  doGet(HttpServletRequest request, HttpServletResponse response) {    ServletContext context =  this.getServletContext();  }  } |

 

###### 3　域[[c19\]](#_msocom_19) 对象的功能

ServletContext是JavaWeb四大域对象之一：

l PageContext；

l ServletRequest；

l HttpSession；

l ServletContext；

所有域对象都有存取数据的功能，因为域对象内部有一个Map，用来存储数据，下面是ServletContext对象用来操作数据的方法：

l void setAttribute(String name, Object value)：用来存储一个对象，也可以称之为存储一个域属性，例如：servletContext.setAttribute(“xxx”, “XXX”)，在ServletContext中保存了一个域属性，域属性名称为xxx，域属性的值为XXX。请注意，如果多次调用该方法，并且使用相同的name，那么会覆盖上一次的值，这一特性与Map相同；

l Object getAttribute(String name)：用来获取ServletContext中的数据，当前在获取之前需要先去存储才行，例如：String value = (String)servletContext.getAttribute(“xxx”);，获取名为xxx的域属性；

l void removeAttribute(String name)：用来移除ServletContext中的域属性，如果参数name指定的域属性不存在，那么本方法什么都不做；

l Enumeration getAttributeNames()：获取所有域属性的名称；

 

###### 4　获取应用初始化参数

l Servlet也可以获取初始化参数，但它是局部的参数；也就是说，一个Servlet只能获取自己的初始化参数，不能获取别人的，即初始化参数只为一个Servlet准备！

l 可以配置公共的初始化参数，为所有Servlet而用！这需要使用ServletContext才能使用！

还可以使用ServletContext来获取在web.xml文件中配置的应用初始化参数！注意，应用初始化参数与Servlet初始化参数不同：

web.xml

| <web-app  ...>   ...   <context-param>    <param-name>paramName1</param-name>    <param-value>paramValue1</param-value>     </context-param>   <context-param>    <param-name>paramName2</param-name>    <param-value>paramValue2</param-value>     </context-param>  [[崔20\]](#_msocom_20) </web-app> |
| ------------------------------------------------------------ |
| ServletContext context = **this**.getServletContext();[[崔21\]](#_msocom_21)       String  value1 = context.getInitParameter("paramName1");      String  value2 = context.getInitParameter("paramName2");  [[崔22\]](#_msocom_22)    System.*out*.println(value1 +  ", " + value2);            Enumeration names =  context.getInitParameterNames();[[崔23\]](#_msocom_23)       **while**(names.hasMoreElements()) {        System.*out*.println(names.nextElement());      } |

 

###### 5　获取资源相关方法

![img](file:///C:/Users/Xiaotuan/AppData/Local/Temp/msohtmlclip1/01/clip_image004.jpg)

5.1　获取真实路径（*****）

还可以使用ServletContext对象来获取Web应用下的资源，例如在hello应用的根目录下创建a.txt文件，现在想在Servlet中获取这个资源，就可以使用ServletContext来获取。

 

l 获取a.txt的真实路径：String realPath = servletContext.getRealPath(“/a.txt”)，realPath的值为a.txt文件的绝对路径：F:\tomcat6\webapps\hello\a.txt；

l 获取b.txt的真实路径：String realPath = servletContext.getRealPath(“/WEB-INF/b.txt”)；

 

5.2　获取资源流

不只可以获取资源的路径，还可以通过ServletContext获取资源流，即把资源以输入流的方式获取：

l 获取a.txt资源流：InputStream in = servletContext.getResourceAsStream(“/a.txt”)；

l 获取b.txt资源流：InputStream in = servletContext.getResourceAsStream(“/WEB-INF/b.txt”)；

 

5.3　获取指定目录下所有资源路径

还可以使用ServletContext获取指定目录下所有资源路径，例如获取/WEB-INF下所有资源的路径：

| Set set = context.getResourcePaths("/WEB-INF");      System.*out*.println(set); |
| ------------------------------------------------------------ |
| [/WEB-INF/lib/,  /WEB-INF/classes/, /WEB-INF/b.txt, /WEB-INF/web.xml] |

 

注意，本方法必须以“/”开头！！！

 

###### 6　练习：访问量统计

一个项目中所有的资源被访问都要对访问量进行累加！

创建一个int类型的变量，用来保存访问量，然后把它保存到ServletContext的域中，这样可以保存所有的Servlet都可以访问到！

l 最初时，ServletContext中没有保存访问量相关的属性；

l 当本站第一次被访问时，创建一个变量，设置其值为1；保存到ServletContext中；

l 当以后的访问时，就可以从ServletContext中获取这个变量，然后在其基础之上加１。

 

 

l 获取ServletContext对象，查看是否存在名为count的属性，如果存在，说明不是第一次访问，如果不存在，说明是第一次访问；

Ø 第一次访问：调用Servletcontext的setAttribute()传递一个属性，名为count，值为1；

Ø 第2~N次访问：调用ServletContext的getAttribute()方法获取原来的访问量，给访问量加1，再调用Servletcontext的setAttribute()方法完成设置。

 

 

相信各位一定见过很多访问量统计的网站，即“本页面被访问过XXX次”。因为无论是哪个用户访问指定页面，都会累计访问量，所以这个访问量统计应该是整个项目共享的！很明显，这需要使用ServletContext来保存访问量。

​      ServletContext application = **this**.getServletContext();[[崔24\]](#_msocom_24)       Integer count =  (Integer)application.getAttribute("count")[[崔25\]](#_msocom_25) ;      **if**(count == **null**) {        count = 1;[[崔26\]](#_msocom_26)       } **else** {        count++[[崔27\]](#_msocom_27) ;      }      response.setContentType("text/html;charset=utf-8");      response.getWriter().print("<h1>本页面一共被访问" + count + "次！</h1>")[[崔28\]](#_msocom_28) ;      application.setAttribute("count", count);[[崔29\]](#_msocom_29)   

 

## 获取类路径下资源

　　获取类路径资源，类路径对一个JavaWeb项目而言，就是/WEB-INF/classes和/WEB-INF/lib/每个jar包！

l Class

l ClassLoader：

　　这里要讲的是获取类路径下的资源，对于JavaWeb应用而言，就是获取classes目录下的资源。

![img](file:///C:/Users/Xiaotuan/AppData/Local/Temp/msohtmlclip1/01/clip_image006.jpg)

 

| InputStream in = **this**.getClass().getResourceAsStream("/xxx.txt");      System.*out*.println(IOUtils.*toString*(in)); |
| ------------------------------------------------------------ |
| InputStream in = **this**.getClass().getClassLoader().getResourceAsStream("xxx.txt");      System.*out*.println(IOUtils.*toString*(in)); |

 

l Class类的getResourceAsStream(String path)：

Ø 路径以“/”开头，相对classes路径；

Ø 路径不以“/”开头，相对当前class文件所有路径，例如在cn.itcast.servlet.MyServlet中执行，那么相对/classes/cn/itcast/servlet/路径；

l ClassLoader类的getResourceAsStream(String path)：

Ø 相对classes路径；

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

------



 [[c1\]](#_msoanchor_1)Servlet中的方法大多数不由我们来调用，而是由Tomcat来调用。并且Servlet的对象也不由我们来创建，由Tomcat来创建！



 [[崔2\]](#_msoanchor_2)配置了两个初始化参数



 [[崔3\]](#_msoanchor_3)实现了Servlet的init(ServletConfig)方法，把参数config赋给了本类的成员config，然后再调用本类自己的无参的init()方法。



 [[崔4\]](#_msoanchor_4)这个方法是GenericServlet自己的方法，而不是从Servlet继承下来的。当我们自定义Servlet时，如果想完成初始化作用就不要再重复init(ServletConfig)方法了，而是应该去重写init()方法。因为在GenericServlet中的init(ServletConfig)方法中保存了ServletConfig对象，如果覆盖了保存ServletConfig的代码，那么就不能再使用ServletConfig了。



 [[崔5\]](#_msoanchor_5)强转



 [[崔6\]](#_msoanchor_6)调用上面service()方法



 [[c7\]](#_msoanchor_7)在<servlet>中配置<load-on-startup>，其中给出一个非负整数！



 [[c8\]](#_msoanchor_8)路径匹配



 [[c9\]](#_msoanchor_9)扩展名匹配



 [[c10\]](#_msoanchor_10)啥都匹配



 [[c11\]](#_msoanchor_11)它的优先级最低，如果一个请求没有人处理，那么它来处理！它显示404。



 [[崔12\]](#_msoanchor_12)当访问路径不存在时，会执行该Servlet！其实我们在访问index.html时也是在执行这个Servlet。 



 [[崔13\]](#_msoanchor_13)匹配所有URL，也就是说用户访问的URL路径没有匹配的页面时，那么执行的就是名为default的Servlet，即org.apache.catalina.servlets.DefaultServlet



 [[崔14\]](#_msoanchor_14)任何URL后缀为jsp的访问，都会执行名为jsp的Servlet，即org.apache.jasper.servlet.JspServlet



 [[崔15\]](#_msoanchor_15)session的默认超时时间为30分钟，后面讲session时再深入。



 [[崔16\]](#_msoanchor_16)MIME类型用来标识网络上资源的媒体类型，这里举例为bmp和html两种MIME类型。



 [[崔17\]](#_msoanchor_17)在应用的web.xml中如果没有对<welcome-file-list>进行覆盖，那么默认主页为index.html、index.html、index.jsp



 [[c18\]](#_msoanchor_18)不及！



 [[c19\]](#_msoanchor_19)域对象就是用来在多个Servlet中传递数据！！！

l 域对象必须有要存数据功能

l 域对象必须要有取数据功能

域对象内部其实有一个Map



 [[崔20\]](#_msoanchor_20)配置了两个应用初始化参数



 [[崔21\]](#_msoanchor_21)获取ServletContext对象



 [[崔22\]](#_msoanchor_22)通过参数名，获取参数值



 [[崔23\]](#_msoanchor_23)获取所有应用初始化参数名称



 [[崔24\]](#_msoanchor_24)获取ServletContext对象



 [[崔25\]](#_msoanchor_25)获取ServletContext对象中的count属性



 [[崔26\]](#_msoanchor_26)如果在ServletContext中不存在count属性，那么设置count的值为1，表示第一次被访问。



 [[崔27\]](#_msoanchor_27)如果在ServletContext中存在count属性，说明以前被访问过，那么让count在原来的基础上加1。



 [[崔28\]](#_msoanchor_28)向客户端响应本页面被访问的次数。



 [[崔29\]](#_msoanchor_29)保存count的值到ServletContext对象中。