

（1）在manager上配置到所有Node节点的无密码验证：

ssh-keygen -t rsa

ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.7.185

ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.7.83

ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.7.81

（2）在MHA Node ip81上：

ssh-keygen -t rsa

ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.7.83

ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.7.185

（3）在MHA Node ip83上：

ssh-keygen -t rsa

ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.7.81

ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.7.185

（4）在MHA Node ip185上：

ssh-keygen -t rsa

ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.7.81

ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.7.83



