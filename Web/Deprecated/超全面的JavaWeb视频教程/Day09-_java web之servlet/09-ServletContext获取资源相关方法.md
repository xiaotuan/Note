### 17. ServeltContext 获取资源相关方法

#### 17.1 获取真实路径

**DServlet.java**

```java
package com.qty.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * 使用 ServletContext 获取资源路径
 */
public class DServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        /*
         * 它得到的是有盘符的路径：F:/xxx/xxx/xxx
         * C:\Workspace\TempSpace\MyWeb\out\artifacts\MyWeb_war_exploded\index.jsp
         */
        String path = getServletContext().getRealPath("/index.jsp");
        System.out.println(path);
    }
}
```

#### 17.2 获取资源流 

**DServlet.java**

```java
package com.qty.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.InputStream;

/**
 * 使用 ServletContext 获取资源路径
 */
public class DServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        /*
         * 获取资源的路径后，再创建出输入流对象！
         */
        InputStream input = getServletContext().getResourceAsStream("/index.jsp");
    }
}
```

#### 17.3 获取指定目录下所有资源路径

**DServlet.java**

```java
package com.qty.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.InputStream;
import java.util.Set;

/**
 * 使用 ServletContext 获取资源路径
 */
public class DServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        /*
         * 获取当前路径下所有资源的路径！
         * [/WEB-INF/classes/, /WEB-INF/web.xml]
         */
        Set<String> paths = getServletContext().getResourcePaths("/WEB-INF");
        System.out.println(paths);
    }
}
```



