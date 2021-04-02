### 13.2.3　基于QReadWriteLock的线程同步

使用互斥量时存在一个问题：每次只能有一个线程获得互斥量的权限。如果在一个程序中有多个线程读取某个变量，使用互斥量时也必须排队。而实际上若只是读取一个变量，是可以让多个线程同时访问的，这样互斥量就会降低程序的性能。

例如，假设有一个数据采集程序，一个线程负责采集数据到缓冲区，一个线程负责读取缓冲区的数据并显示，另一个线程负责读取缓冲区的数据并保存到文件，示意代码如下：

```css
int   buffer[100];
QMutex  mutex;
void   threadDAQ::run()
{   ...
   mutex.lock();
   get_data_and_write_in_buffer();   //数据写入buffer
   mutex.unlock();
   ...   
}
void   threadShow::run()
{   ...
   mutex.lock();
   show _buffer();   //读取 buffer里的数据并显示
   mutex.unlock();
   ...   
}
void   threadSaveFile::run()
{   ...
   mutex.lock();
   Save_buffer_toFile();   //读取 buffer里的数据并保存到文件
   mutex.unlock();
   ...  
}
```

数据缓冲区buffer和互斥量mutex都是全局变量，线程threadDAQ将数据写到buffer，线程threadShow和threadSaveFile只是读取buffer，但是因为使用互斥量，这3个线程任何时候都只能有一个线程可以访问buffer。而实际上，threadShow和threadSaveFile都只是读取buffer的数据，它们同时访问buffer是不会发生冲突的。

Qt提供了QReadWriteLock类，它是基于读或写的模式进行代码段锁定的，在多个线程读写一个共享数据时，可以解决上面所说的互斥量存在的问题。

QReadWriteLock以读或写锁定的同步方法允许以读或写的方式保护一段代码，它可以允许多个线程以只读方式同步访问资源，但是只要有一个线程在以写方式访问资源时，其他线程就必须等待直到写操作结束。

QReadWriteLock提供以下几个主要的函数：

+ lockForRead()，以只读方式锁定资源，如果有其他线程以写入方式锁定，这个函数会阻塞；
+ lockForWrite()，以写入方式锁定资源，如果本线程或其他线程以读或写模式锁定资源，这个函数就阻塞；
+ unlock()，解锁；
+ tryLockForRead()，是lockForRead()的非阻塞版本；
+ tryLockForWrite()，是lockForWrite()的非阻塞版本。

使用QReadWriteLock，上面的三线程代码可以改写为如下的形式：

```css
int   buffer[100];
QReadWriteLock   Lock;
void   threadDAQ::run()
{   ...
   Lock.lockForWrite();
   get_data_and_write_in_buffer();   //数据写入buffer
   Lock.unlock();
   ...   
}
void   threadShow::run()
{   ...
   Lock.lockForRead();
   show_buffer();   //读取 buffer里的数据并显示
   Lock.unlock();
   ...   
}
void   threadSaveFile::run()
{   ...
   Lock.lockForRead();
   Save_buffer_toFile();   //读取 buffer里的数据并保存到文件
   Lock.unlock();
   ...  
}
```

这样，如果threadDAQ没有以lockForWrite()锁定Lock，threadShow和threadSaveFile可以同时访问buffer，否则threadShow和threadSaveFile都被阻塞；如果threadShow和threadSaveFile都没有锁定，那么threadDAQ能以写入方式锁定，否则threadDAQ就被阻塞。

QReadLocker和QWriteLocker是QReadWriteLock的简便形式，如同QMutexLocker是QMutex的简便版本一样，无需与unlock()配对使用。使用QReadLocker 和QWriteLocker，则上面的代码改写为：

```css
int   buffer[100];
QReadWriteLock   Lock;
void   threadDAQ::run()
{   ...
   QWriteLocker  Locker(&Lock);
   get_data_and_write_in_buffer();   //数据写入buffer
   ...   
}
void   threadShow::run()
{   ...
QReadLocker Locker(&Lock);
   show _buffer();   //读取 buffer里的数据并显示
   ...   
}
void   threadSaveFile::run()
{   ...
QReadLocker Locker(&Lock);
   Save_buffer_toFile();   //读取 buffer里的数据并保存到文件
   ...  
}
```

