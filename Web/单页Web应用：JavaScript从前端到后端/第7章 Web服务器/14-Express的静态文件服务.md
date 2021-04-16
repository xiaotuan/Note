

#### 
  7.2.8 Express的静态文件服务


正如你所料想的，Express的静态文件服务需要添加一些中间件和重定向。我们把第6章spa目录中的内容复制到public目录里面，如代码清单7-12所示。

代码清单7-12 添加存放静态文件的public 目录

![figure_0255_0356.jpg](../images/figure_0255_0356.jpg)
现在可以修改应用，提供静态文件的服务，如代码清单 7-13 所示。修改部分以粗体显示。

代码清单7-13 Express 的静态文件服务——webapp/app.js

![figure_0255_0357.jpg](../images/figure_0255_0357.jpg)
![figure_0256_0358.jpg](../images/figure_0256_0358.jpg)
现在当我们运行应用（node app.js）并在浏览器中打开 http://localhost:3000 的时候，将会看到第6章的单页应用。然而还不能登入，因为后端还没准备好。

现在已经对Express中间件有了不错的感觉，我们来看一下高级路由，Web数据服务会用到这个功能。

