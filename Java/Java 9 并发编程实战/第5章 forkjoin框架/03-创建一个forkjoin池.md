### 5.2 创建一个fork/join池

本节将介绍fork/join框架的基本功能的使用方法。其功能如下所示。

+ 创建一个 `ForkJoinPool` 对象来执行任务。
+ 在池内创建 `ForkJoinTask` 的一个子类并执行。

在本例中使用的fork/join框架的主要功能如下所示。

+ 使用默认构造方法创建 `ForkJoinPool` 对象。
+ 在任务内部，使用Java API文档推荐的结构。

```css
   if (problem size > default size){
     tasks=divide(task);
     execute(tasks);
   } else {
     resolve problem using another algorithm;
   }
```

+ 以同步方式执行任务。当一个任务执行两个以上的子任务时，它会等待这些子任务的结束。在本案例中，执行任务的线程（即工作线程），会寻找其他待执行的任务，从而最大化利用执行时间。
+ 将要实现的任务不会返回任何执行结果，因此需要用 `RecursiveAction` 类作为其实现的基类。

