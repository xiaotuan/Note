[toc]

本示例由如下两部分组成：

+ 位于内核空间将数据写入 `Relay` 文件的程序，使用时需要作为一个内核模块被加载。
+ 位于用户空间从 `Relay` 文件中读取数据的程序，使用时作为普通用户太程序运行。

### 1. 实现内核空间代码

内核空间程序的主要操作如下：

+ 当加载模块时，打开一个 Relay 通道，并且往打开的 Relay 通道中写入消息。
+ 当卸载模块时，关闭 Relay 通道。

**hello-mod.c**

```c
#include <linux/module.h>
#include <linux/relayfs_fs.h>

static struct rchan *hello_rchan;

int init_module(void)
{
    const char *msg = "Hello world\n";
    hello_rchan = relay_open("cpu", NULL, 8192, 2, NULL);
    if (!hello_rchan) {
        printk("relay_open() failed.\n");
        return -ENOMEM;
    }
    relay_write(hello_rchan, msg, strlen(msg));
    return 0;
}

void cleanup_module(void)
{
    if (hello_rchan) {
        relay_close(hello_rchan);
        hello_rchan = NULL;
    }
    return;
}

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Simple example of Relay");
```

### 2. 实现用户空间代码

用户空间的函数主要操作过程如下：

如果 relayfs 文件系统还没有被 mount （是一个命令）处理，则将其 mount 到 /mnt/relay 目录上。首先遍历每一个 CPU 对应的缓冲文件，然后打开文件，接着读取所有文件内容，关闭文件，最后，umount 掉 Relay 文件系统。

**audience.c**

```c
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mount.h>
#include <fcntl.h>
#include <sched.h>
#include <errno.h>
#include <stdio.h>

#define MAX_BUFLEN 256

const char filename_base[] = "/mnt/relay/cpu";

// implement your own get_cputotal() before compilation
static int get_cputotal(void);

int main(void)
{
    char filename[128] = {0};
    char buf[MAX_BUFLEN];
    int fd, c, i, bytesread, cputotal = 0;
    if (mount("relayfs", "/mnt/relay", "relayfs", 0, NULL) && (errno != EBUSY)) {
        printf("mount() failed: %s\n", strerror(errno));
        return 1;
    }
    cputotal = get_cputotal();
    if (cputotal <= 0) {
        printf("invalid cputotal value: %d\n", cputotal);
        return 1;
    }
    for (i = 0; i < cputotal; i++) {
        // open per-cpu file
        sprintf(filename, "%s%d", filename_base, i);
        fd = open(filename, O_RDONLY);
        if (fd < 0) {
            printf("fopen() failed: %s\n", strerror(errno));
            return 1;
        }
        // read per-cpu file
        bytesread = read(fd, buf, MAX_BUFLEN);
        while (bytesread > 0) {
            buf[bytesread] = '\0';
            puts(buf);
            bytesread = read(fd, buf, MAX_BUFLEN);
        }
        // close per-cpu file
        if (fd > 0) {
            close(fd);
            fd = 0;
        }
    }
    if (umount("/mnt/relay") && (errno != EINVAL)) {
        printf("umount() failed: %s\n", strerror(errno));
        return 1;
    }
    return 0;
}
```

