### 5.2.1　摆脱LXC

对LXC的依赖自始至终都是个问题。

首先，LXC是基于Linux的。这对于一个立志于跨平台的项目来说是个问题。

其次，如此核心的组件依赖于外部工具，这会给项目带来巨大风险，甚至影响其发展。

因此，Docker公司开发了名为Libcontainer的自研工具，用于替代LXC。Libcontainer的目标是成为与平台无关的工具，可基于不同内核为Docker上层提供必要的容器交互功能。

在Docker 0.9版本中，Libcontainer取代LXC成为默认的执行驱动。

