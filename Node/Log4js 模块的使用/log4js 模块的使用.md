[toc]

### 1. 基本使用

```js
const log4js = require("log4js");
log4js.configure({
  appenders: { cheese: { type: "file", filename: "cheese.log" } },
  categories: { default: { appenders: ["cheese"], level: "error" } }
});

const logger = log4js.getLogger("cheese");
logger.trace("Entering cheese testing");
logger.debug("Got cheese.");
logger.info("Cheese is Comté.");
logger.warn("Cheese is quite smelly.");
logger.error("Cheese is too ripe!");
logger.fatal("Cheese was breeding ground for listeria.");
```

执行上面命令后输出结果如下：

```console
[2021-06-10T23:01:18.088] [ERROR] cheese - Cheese is too ripe!
[2021-06-10T23:01:18.089] [FATAL] cheese - Cheese was breeding ground for listeria.
```

下面解析下这段代码：

```js
log4js.configure({
  appenders: { cheese: { type: "file", filename: "cheese.log" } },
  categories: { default: { appenders: ["cheese"], level: "error" } }
});
```

在 `appenders` 项中定义了一个 `cheese` 的`TAG` ，这个 `TAG` 的日志将会存储在 `cheese.log` 的文件中。

> 注意：
>
> + 如果 `type` 的值为 `file` ，代表日志将只会写入文件中，执行程序后在终端中不会显示日志。
> + `filename` 的值定义了日志文件的位置，可以使用相对位置，也可以使用绝对位置。

`categories` 项用于定义日志的输出级别。

> 提示：
>
> 具体 `type` 和 `categories` 可设置的值请参阅源代码。

通过 `log4js.getLogger("cheese")` 方法可以获取 `cheese` 标签的日志引用，使用该日志对象输出的日志都会写入到 `cheese.log` 文件中。

### 2. 定义多个 TAG

可以参照如下代码定义多个 TAG 的日志输出：

```js
const log4js = require("log4js");
log4js.configure({
  appenders: { cheese: { type: "file", filename: "./data/cheese.log" }, Info: { type: "file", filename: "info.log"} },
  categories: { default: { appenders: ["cheese"], level: "error" }, Info: {appenders: ["Info"], level: "all"} }
});

const logger = log4js.getLogger("cheese");
logger.trace("Entering cheese testing");
logger.debug("Got cheese.");
logger.info("Cheese is Comté.");
logger.error("Cheese is too ripe!");
const info = log4js.getLogger("Info");
info.warn("Cheese is quite smelly.");
info.fatal("Cheese was breeding ground for listeria.")
info.debug("Info is debug.");
```

### 3. 直接使用 log4js

我们也可以在使用前不对 `log4js` 进行配置，直接调用 `var logger = log4js.getLogger()` 获取日志输出对象，然后再设置日志输出级别 `logger.level = 'all'`。这样日志将会输出到终端中：

```js
const log4js = require("log4js");

const logger = log4js.getLogger();
logger.level = "all";
logger.trace("Entering cheese testing");
logger.debug("Got cheese.");
logger.info("Cheese is Comté.");
logger.warn("Cheese is quite smelly.");
logger.error("Cheese is too ripe!");
logger.fatal("Cheese was breeding ground for listeria.");
```

日志输出如下：

```console
[2021-06-10T23:13:32.810] [TRACE] default - Entering cheese testing
[2021-06-10T23:13:32.813] [DEBUG] default - Got cheese.
[2021-06-10T23:13:32.813] [INFO] default - Cheese is Comté.
[2021-06-10T23:13:32.813] [WARN] default - Cheese is quite smelly.
[2021-06-10T23:13:32.814] [ERROR] default - Cheese is too ripe!
[2021-06-10T23:13:32.814] [FATAL] default - Cheese was breeding ground for listeria.
```

