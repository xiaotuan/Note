**模拟 GenericServlet 类的实现**

```java
package com.qty.servlet;

import java.io.IOException;

import javax.servlet.Servlet;
import javax.servlet.ServletConfig;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

/**
 * 模拟 GenericServlet
 * @author Xiaotuan
 */
public class BServlet implements Servlet {
	
	private ServletConfig config;

	/**
	 * 需要就写，不需要就不写
	 */
	@Override
	public void destroy() {
		System.out.println("啊~我要死了！");
	}

	/**
	 * 请放心，这个方法一定会在 init() 方法之后被调用！
	 * init() 被调用后，本类的成员 this.config 已经有值了！
	 */
	@Override
	public ServletConfig getServletConfig() {
		return this.config;
	}

	/**
	 * 没有用的东西，爱实现不实现
	 */
	@Override
	public String getServletInfo() {
		return "我是一个快乐的Servlet";
	}

	/**
	 * 由 Tomcat 来调用，并且只调用一次
	 * 它是这些方法中第一个被调用的，它会在构造器之后马上被调用！
	 */
	@Override
	public void init(ServletConfig config) throws ServletException {
		// 把 Tomcat 传递的 ServletConfig 赋值给本类的一个成员，
		// 其实就是把它保存起来，方便在其他方法中调用。
		this.config = config;
		init();
	}
 
	@Override
	public void service(ServletRequest arg0, ServletResponse arg1) throws ServletException, IOException {
		/**
		 * 这里是否可以使用 ServletConfig 的成员呢？
		 */
		System.out.println("每次处理请求都会被调用！");
	}
	
	/**
	 * 这个方法是本类自己定义的！不是 Servlet 接口提供的方法
	 */
	public void init() {
		
	}
	
	public ServletContext getServletContext() {
		return config.getServletContext();
	}
	
	public String getServletName() {
		return config.getServletName();
	}
	
	public String getInitParameter(String name) {
		return config.getInitParameter(name);
	}
	
}
```

