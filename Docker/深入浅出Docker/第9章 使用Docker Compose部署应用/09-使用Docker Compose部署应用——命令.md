## 9.3　使用Docker Compose部署应用——命令

+ `docker-compose up` 命令用于部署一个Compose应用。默认情况下该命令会读取名为 `docker-compose.yml` 或 `docker-compose.yaml` 的文件，当然用户也可以使用 `-f` 指定其他文件名。通常情况下，会使用-d参数令应用在后台启动。
+ `docker-compose stop` 命令会停止Compose应用相关的所有容器，但不会删除它们。被停止的应用可以很容易地通过 `docker-compose restart` 命令重新启动。
+ `docker-compose rm` 命令用于删除已停止的Compose应用。它会删除容器和网络，但是不会删除卷和镜像。
+ `docker-compose restart` 命令会重启已停止的Compose应用。如果用户在停止该应用后对其进行了变更，那么变更的内容不会反映在重启后的应用中，这时需要重新部署应用使变更生效。
+ `docker-compose ps` 命令用于列出Compose应用中的各个容器。输出内容包括当前状态、容器运行的命令以及网络端口。
+ `docker-compose down` 会停止并删除运行中的Compose应用。它会删除容器和网络，但是不会删除卷和镜像。

