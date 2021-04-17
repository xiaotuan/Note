

前面讲过，锁和多版本数据是 InnoDB实现一致性读和 ISO/ANSI SQL92隔离级别的手段，因此，在不同的隔离级别下，InnoDB处理SQL时采用的一致性读策略和需要的锁是不同的。同时，数据恢复和复制机制的特点，也对一些 SQL 的一致性读策略和锁策略有很大影响。将这些特性归纳成如表20-16所示的内容，以便读者查阅。

表20-16 InnoDB存储引擎中不同SQL在不同隔离级别下锁比较



![figure_0361_0165.jpg](../images/figure_0361_0165.jpg)
从表20-16中可以看出，对于许多SQL，隔离级别越高，InnoDB给记录集加的锁就越严格（尤其是使用范围条件的时候），产生锁冲突的可能性也就越高，从而对并发性事务处理性能的影响也就越大。因此，我们在应用中，应该尽量使用较低的隔离级别，以减少锁争用的机率。实际上，通过优化事务逻辑，大部分应用使用Read Committed隔离级别就足够了。对于一些确实需要更高隔离级别的事务，可以通过在程序中执行 SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ或SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE动态改变隔离级别的方式满足需求。



