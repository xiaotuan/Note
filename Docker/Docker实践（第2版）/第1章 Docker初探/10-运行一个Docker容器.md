### 1.2.4　运行一个Docker容器

读者已经构建出Docker镜像并为其打上了标签。现在可以以容器的形式来运行它了。运行后的输出结果如代码清单1-2所示。

代码清单1-2　todoapp的docker run输出

```c
$ docker run -i -t -p 8000:8000 --name example1 todoapp　　⇽---　 docker run子命令启动容器，-p将容器的 8000 端口映射到宿主机的8000端口上，--name给容器赋予一个唯一的名字，最后一个参数是镜像
npm install
npm info it worked if it ends with ok
npm info using npm@2.14.4
npm info using node@v4.1.1
npm info prestart todomvc-swarm@0.0.1
> todomvc-swarm@0.0.1 prestart /todo　　⇽---　容器的启动进程的输出被发送到终端中
> make all
npm install
npm info it worked if it ends with ok
npm info using npm@2.14.4
npm info using node@v4.1.1
npm WARN package.json todomvc-swarm@0.0.1 No repository field.
npm WARN package.json todomvc-swarm@0.0.1 license should be a valid SPDX
➥ license expression
npm info preinstall todomvc-swarm@0.0.1
npm info package.json statics@0.1.0 license should be a valid SPDX license
➥ expression
npm info package.json react-tools@0.11.2 No license field.
npm info package.json react@0.11.2 No license field.
npm info package.json node-
     jsx@0.11.0 license should be a valid SPDX license expression
npm info package.json ws@0.4.32 No license field.
npm info build /todo
npm info linkStuff todomvc-swarm@0.0.1
npm info install todomvc-swarm@0.0.1
npm info postinstall todomvc-swarm@0.0.1
npm info prepublish todomvc-swarm@0.0.1
npm info ok
if [ ! -e dist/ ]; then mkdir dist; fi
cp node_modules/react/dist/react.min.js dist/react.min.js
LocalTodoApp.js:9:    // TODO: default english version
LocalTodoApp.js:84:            fwdList = this.host.get('/TodoList#'+listId);
 // TODO fn+id sig
TodoApp.js:117:        // TODO scroll into view
TodoApp.js:176:        if (i>=list.length()) { i=list.length()-1; } // TODO
➥ .length
local.html:30:    <!-- TODO 2-split, 3-split -->
model/TodoList.js:29:        // TODO one op - repeated spec? long spec?
view/Footer.jsx:61:        // TODO: show the entry's metadata
view/Footer.jsx:80:            todoList.addObject(new TodoItem()); // TODO
➥ create default
view/Header.jsx:25:        // TODO list some meaningful header (apart from the
➥ id)
npm info start todomvc-swarm@0.0.1
> todomvc-swarm@0.0.1 start /todo
> node TodoAppServer.js
Swarm server started port 8000
^Cshutting down http-server... 　　⇽---　在此按组合键Ctrl+C终止进程和容器
 closing swarm host...
swarm host closed
npm info lifecycle todomvc-swarm@0.0.1~poststart: todomvc-swarm@0.0.1
npm info ok
$ docker ps -a　　⇽---　执行这个命令查看已经启动和移除的容器，以及其ID和状态（就像进程一样）
 CONTAINER ID  IMAGE    COMMAND      CREATED        STATUS PORTS NAMES
b9db5ada0461  todoapp  "npm start"  2 minutes ago  Exited (0) 2 minutes ago
➥                example1
$ docker start example1　　⇽---　重新启动容器，这次是在后台运行
 example1
$ docker ps
CONTAINER ID  IMAGE    COMMAND      CREATED       STATUS
➥ PORTS                    NAMES
b9db5ada0461  todoapp  "npm start"  8 minutes ago  Up 10 seconds
➥ 0.0.0.0:8000->8000/tcp example1　　⇽---　再次执行ps命令查看发生变化的状态
$ docker diff example1　　⇽---　 docker diff子命令显示了自镜像被实例化成一个容器以来哪些文件受到了影响
C /root
C /root/.npm
C /root/.npm/_locks
C /root/.npm/anonymous-cli-metrics.json
C /todo　　⇽---　修改了/todo目录（C）
A /todo/.swarm　　⇽---　增加了/todo/.swarm目录（A）
A /todo/.swarm/_log
A /todo/dist
A /todo/dist/LocalTodoApp.app.js
A /todo/dist/TodoApp.app.js
A /todo/dist/react.min.js
C /todo/node_modules
```

`docker run` 子命令启动容器。 `-p` 标志将容器的8000端口映射到宿主机的8000端口上，读者现在应该可以使用浏览器访问http://localhost:8000来查看这个应用程序了。 `--name` 标志赋予了容器一个唯一的名称，以便后面引用。最后的参数是镜像名称。

一旦容器启动，我们就可以按组合键Ctrl+C终止进程和容器。读者可以执行 `ps` 命令查看被启动且未被移除的容器。注意，每个容器都具有自己的容器 ID 和状态，与进程类似。它的状态是 `Exited` （已退出），不过读者可以重新启动它。这么做之后，注意状态已经改变为 `Up` （运行中），且容器到宿主机的端口映射现在也显示出来了。

`docker diff` 子命令显示了自镜像被实例化成一个容器以来哪些文件受到了影响。在这个示例中，todo目录被修改了（C），而其他列出的文件是新增的（A）。没有文件被删除（D），这是另一种可能性。

如读者所见，Docker“包含”环境的事实意味着用户可以将其视为一个实体，在其上执行的动作是可预见的。这赋予了Docker宽广的能力——用户可以影响从开发到生产再到维护的整个软件生命周期。这种改变正是本书所要描述的，在实践中展示Docker所能完成的东西。

接下来读者将了解Docker的另一个核心概念——分层。

