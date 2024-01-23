[toc]

### 1. 创建 Node 项目

```shell
$ npm init -y
```

### 2. 安装 electron

```shell
$ npm install electron --save-dev
```

> 注意：
>
> 在执行这步时可能会提示网络错误问题，这是由于安装依赖时会从GitHub 网站下载其他依赖导致的。可以通过设置 `ELECTRON_MIRROR` 环境变量的值为：<https://npm.taobao.org/mirrors/electron/> 或者 <https://mirrors.huaweicloud.com/electron/>。
>
> 或执行如下命令：
>
> ```shell
> $ npm install --location=global cnpm --registry=https://registry.npmmirror.com
> $ cnpm install --save-dev electron
> ```

### 3. 添加 electron 依赖

在当前项目中的 `package.json` 文件中添加如下代码：

```json
"devDependencies": {
	"electron": "^28.1.4"
}
```

完整代码如下：

```json
{
  "name": "electrontest",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "electron": "^28.1.4"
  }
}
```

### 4. 测试 Electron

1. 在当前项目中的 `package.json` 文件内添加一段脚本，代码如下所示：

   ```json
   "scripts": {
       "dev": "electron ./index.js"
   }
   ```

2. 在这个项目的根目录下创建一个名为 `index.js` 的 `JavaScript` 文件，并录入如下代码：

   ```js
   const { app, BrowserWindow } = require('electron')
   let win
   app.whenReady().then(() => {
   	win = new BrowserWindow({
   		width: 800,
   		height: 600,
   	});
   	win.loadURL('https://www.baidu.com');
   });
   ```

3. 在项目根目录下开启一个命令行工具，使用如下指令启动 `Electron` 应用：

   ```shell
   $ npm run dev
   ```

   

