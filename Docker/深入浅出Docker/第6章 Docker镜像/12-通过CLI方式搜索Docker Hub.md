### 6.2.9　通过CLI方式搜索Docker Hub

`docker search` 命令允许通过CLI的方式搜索Docker Hub。读者可以通过“ `NAME` ”字段的内容进行匹配，并且基于返回内容中任意列的值进行过滤。

简单模式下，该命令会搜索所有“NAME”字段中包含特定字符串的仓库。例如，下面的命令会查找所有“NAME”包含“nigelpoulton”的仓库。

```rust
$ docker search nigelpoulton
NAME                         DESCRIPTION                STARS    AUTOMATED
nigelpoulton/pluralsight..   Web app used in...         8        [OK]
nigelpoulton/tu-demo                                    7
nigelpoulton/k8sbook         Kubernetes Book web app    1
nigelpoulton/web-fe1         Web front end example      0
nigelpoulton/hello-cloud     Quick hello-world image    0
```

“NAME”字段是仓库名称，包含了Docker ID，或者非官方仓库的组织名称。例如，下面的命令会列出所有仓库名称中包含“alpine”的镜像。

```rust
$ docker search alpine
NAME                   DESCRIPTION          STARS    OFFICIAL    AUTOMATED
alpine                 A minimal Docker..   2988     [OK]
mhart/alpine-node      Minimal Node.js..    332
anapsix/alpine-java    Oracle Java 8...     270                  [OK]
<Snip>
```

需要注意，上面返回的镜像中既有官方的也有非官方的。读者可以使用 `--filter "is-official=true"` ，使命令返回内容只显示官方镜像。

```rust
$ docker search alpine --filter "is-official=true"
NAME                   DESCRIPTION          STARS     OFFICIAL     AUTOMATED
alpine                 A minimal Docker..   2988      [OK]
```

重复前面的操作，但这次只显示自动创建的仓库。

```rust
$ docker search alpine --filter "is-automated=true"
NAME                       DESCRIPTION               OFFICIAL      AUTOMATED
anapsix/alpine-java        Oracle Java 8 (and 7)..                 [OK]
frolvlad/alpine-glibc      Alpine Docker image..                   [OK]
kiasaki/alpine-postgres    PostgreSQL docker..                     [OK]
zzrot/alpine-caddy         Caddy Server Docker..                   [OK]
<Snip>
```

关于 `docker search` 需要注意的最后一点是，默认情况下，Docker只返回25行结果。但是，读者可以指定 `--limit` 参数来增加返回内容行数，最多为100行。

