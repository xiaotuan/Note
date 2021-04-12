### 6.2.8　过滤 `docker image ls` 的输出内容

Docker提供 `--filter` 参数来过滤 `docker image ls` 命令返回的镜像列表内容。

下面的示例只会返回悬虚（dangling）镜像。

```rust
$ docker image ls --filter dangling=true
REPOSITORY    TAG       IMAGE ID       CREATED      SIZE
<none>        <none>    4fd34165afe0   7 days ago   14.5MB
```

那些没有标签的镜像被称为悬虚镜像，在列表中展示为 `<none>:<none>` 。通常出现这种情况，是因为构建了一个新镜像，然后为该镜像打了一个已经存在的标签。当此情况出现，Docker会构建新的镜像，然后发现已经有镜像包含相同的标签，接着Docker会移除旧镜像上面的标签，将该标签标在新的镜像之上。例如，首先基于 `alpine:3.4` 构建一个新的镜像，并打上 `dodge:challenger` 标签。然后更新Dockerfile，将 `alpine:3.4` 替换为 `alpine:3.5` ，并且再次执行 `docker image build` 命令。该命令会构建一个新的镜像，并且标签为 `dodge:challenger` ，同时移除了旧镜像上面对应的标签，旧镜像就变成了悬虚镜像。

可以通过 `docker image prune` 命令移除全部的悬虚镜像。如果添加了 `-a` 参数，Docker会额外移除没有被使用的镜像（那些没有被任何容器使用的镜像）。

Docker目前支持如下的过滤器。

+ `dangling` ：可以指定 `true` 或者 `false` ，仅返回悬虚镜像（true），或者非悬虚镜像（false）。
+ `before` ：需要镜像名称或者ID作为参数，返回在之前被创建的全部镜像。
+ `since` ：与 `before` 类似，不过返回的是指定镜像之后创建的全部镜像。
+ `label` ：根据标注（label）的名称或者值，对镜像进行过滤。 `docker image ls` 命令输出中不显示标注内容。

其他的过滤方式可以使用 `reference` 。

下面就是使用 `reference` 完成过滤并且仅显示标签为 `latest` 的示例。

```rust
$ docker image ls --filter=reference="*:latest"
REPOSITORY   TAG      IMAGE ID        CREATED      SIZE
alpine       latest   3fd9065eaf02    8 days ago   4.15MB
test         latest   8426e7efb777    3 days ago   122MB
```

读者也可以使用 `--format` 参数来通过Go模板对输出内容进行格式化。例如，下面的指令将只返回Docker主机上镜像的大小属性。

```rust
$ docker image ls --format "{{.Size}}"
99.3MB
111MB
82.6MB
88.8MB
4.15MB
108MB
```

使用下面命令返回全部镜像，但是只显示仓库、标签和大小信息。

```rust
$ docker image ls --format "{{.Repository}}: {{.Tag}}: {{.Size}}"
dodge:  challenger: 99.3MB
ubuntu: latest:     111MB
python: 3.4-alpine: 82.6MB
python: 3.5-alpine: 88.8MB
alpine: latest:     4.15MB
nginx:  latest:     108MB
```

如果读者需要更复杂的过滤，可以使用OS或者Shell自带的工具，比如 `Grep` 或者 `AWK`  。

