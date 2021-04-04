### 7.6　运用线程安全的navigable map

`ConcurrentNavigableMap` 作为一个由Java API提供的并发编程接口，定义了一些有趣的数据结构。凡是实现了 `ConcurrentNavigableMap` 接口的类都会把存储的元素分为两部分：

+ 唯一标识元素的 **key** ；
+ 其余部分为 **value** 。

Java API还提供了一个 `ConcurrentSkipListMap` 接口类，它继承了 `Concurrent NavigableMap` 接口，并基于此来实现了一个非阻塞列表。更进一步来说，它是用 **Skip List** 来存储数据的。Skip List是一个基于并行列表的数据结构，其性能可以比拟二叉树。想了解更多关于Skip List的信息请访问相关网站。Skip List作为一个自排序的数据结构，可以替代传统的排序列表，拥有更好的对元素进行增删改查的性能。

> <img class="my_markdown" src="../images/55.png" style="width:73px;  height: 69px; " width="8%"/>
> Skip List由William Pugh于1990年提出。

由于将一个元素插入到一个 `map` 时，它会根据 `key` 对元素进行排序，因此所有元素都是有序的。而那些 `key` 必须实现 `Comparable` 接口，或者传递一个 `Comparator` 类到 `map` 的构造方法中。该类通常还会提供一些方法来获取一个 `map` 的子集，甚至返回某个具体的元素。

本节将介绍如何使用 `ConcurrentSkipListMap` 类来实现一个通信录。

