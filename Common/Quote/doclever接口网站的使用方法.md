<center><font size="5"><b>doclever接口网站的使用方法</b></font></center>

> 摘自：<https://www.cnblogs.com/tengyuxin/p/11172272.html>

1. 为什么使用 doclever

我本身做前端，后台我以前自己写demo式的项目时，可以写一些接口，大三进入公司实习。

发现，公司项目学起来成本很高，公司后台接口有严格定义，没法像以前一样用nodejs搭一个简单的后台。

那么mock充当临时后台的角色 。

 

2.
（1）第一步，注册账号
（2）第二步，新建一个项目
![img](https://img2018.cnblogs.com/blog/1723157/201907/1723157-20190711185927148-887613797.png)



（3）点击进入，自己的项目
![img](https://img2018.cnblogs.com/blog/1723157/201907/1723157-20190711190046378-579090602.png)



（4）在myproject里面新建一个分组
![img](https://img2018.cnblogs.com/blog/1723157/201907/1723157-20190711190312871-1484302595.png)





（5）新建接口，并配置
![img](https://img2018.cnblogs.com/blog/1723157/201907/1723157-20190711191714632-1588215734.png)







（6）其它地方默认，直接点击“导入json”
![img](https://img2018.cnblogs.com/blog/1723157/201907/1723157-20190711191819063-74285175.png)





（7）使用json格式化工具就是 ： 推荐 https://www.json.cn/  和 [http://www.bejson.com/
](http://www.bejson.com/)![img](https://img2018.cnblogs.com/blog/1723157/201907/1723157-20190711193504624-2013090761.png)







（8）导入“json数据”，之后，看一下json下面的变化
之后 ， 保存你的配置 ， 运行一下 ， 只要运行成功，就确保，模拟后台准确完成
![img](https://img2018.cnblogs.com/blog/1723157/201907/1723157-20190711194035908-1075435083.png)








（9）运行时前，将BaseUrl 填好 ， 去“设置”的Mock 找到 mock serve 地址

![img](https://img2018.cnblogs.com/blog/1723157/201907/1723157-20190711194803729-235903337.png)




复制粘贴你的，mock server 地址吧

![img](https://img2018.cnblogs.com/blog/1723157/201907/1723157-20190711194851588-290016236.png)






（10） 填好BaseUrl , 点击运行 , 看成功的标志
![img](https://img2018.cnblogs.com/blog/1723157/201907/1723157-20190711195112277-1889851494.png)


（11） 接口弄好了 ， 剩下就是根据不同项目配置 ， 访问就行了。