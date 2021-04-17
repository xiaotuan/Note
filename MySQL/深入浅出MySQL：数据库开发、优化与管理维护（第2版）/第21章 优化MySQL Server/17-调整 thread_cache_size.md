

为加快连接数据库的速度，MySQL 会缓存一定数量的客户服务线程以备重用，通过参数thread_cache_size可控制MySQL缓存客户服务线程的数量。

可以通过计算线程cache的失效率***threads_created/connections***来衡量thread_cache_size的设置是否合适。该值越接近1，说明线程cache命中率越低，应考虑适当增加thread_cache_size的值。



