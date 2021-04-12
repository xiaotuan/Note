### 5.2.9　在Linux中的实现

在 Linux 系统中，前面谈到的组件由单独的二进制来实现，具体包括dockerd(Docker daemon)、docker-containerd(containerd)、docker-containerd-shim (shim)和docker-runc (runc)。

通过在Docker宿主机的Linux系统中执行 `ps` 命令可以看到以上组件的进程。当然，有些进程只有在运行容器的时候才可见。

