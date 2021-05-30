[toc]

`process` 对象是 `Node` 环境中的基础组件，它提供了当前运行环境的信息。

### 1. 查看 `Node` 中各模块的版本号

```shell
$ node -p "process.versions"
{
  node: '13.5.0',
  v8: '7.9.317.25-node.23',
  uv: '1.34.0',
  zlib: '1.2.11',
  brotli: '1.0.7',
  ares: '1.15.0',
  modules: '79',
  nghttp2: '1.40.0',
  napi: '5',
  llhttp: '2.0.1',
  openssl: '1.1.1d',
  cldr: '35.1',
  icu: '64.2',
  tz: '2019a',
  unicode: '12.1'
}
```

> 提示：在 `Windows` 的命令行窗口中 `node -p` 的参数必须使用双引号括起来。

### 2. 查看当前所处的开发/生产环境中的环境变量

```shell
$ node -p "process.env"
{
  TERM_PROGRAM: 'Apple_Terminal',
  ANDROID_HOME: '/Users/qintuanye/Library/Android/sdk',
  TERM: 'xterm-256color',
  SHELL: '/bin/bash',
  TMPDIR: '/var/folders/x3/qxwt6yrx4cz8gzgf3c_r0zwc0000gn/T/',
  TERM_PROGRAM_VERSION: '440',
  OLDPWD: '/Users/qintuanye/Documents/TempSpace',
  TERM_SESSION_ID: '29754B38-F597-4F9F-B754-F9AA430C5A13',
  USER: 'qintuanye',
  SSH_AUTH_SOCK: '/private/tmp/com.apple.launchd.lBeKs4yRH6/Listeners',
  ALL_PROXY: 'socks5://127.0.0.1:51837',
  PATH: '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin:/Users/qintuanye/Library/Android/sdk/platform-tools:/Users/qintuanye/Library/Android/sdk/tools:/Users/qintuanye/Library/Android/sdk/build-tools:/Users/qintuanye/Flutter/bin',
  LaunchInstanceID: 'E0A9E95A-24A8-4464-8E10-78444AAC93DD',
  __CFBundleIdentifier: 'com.apple.Terminal',
  PWD: '/Users/qintuanye/Documents/TempSpace/nodelib',
  LANG: 'zh_CN.UTF-8',
  XPC_FLAGS: '0x0',
  HTTPS_PROXY: 'http://127.0.0.1:58591',
  XPC_SERVICE_NAME: '0',
  HOME: '/Users/qintuanye',
  SHLVL: '1',
  HTTP_PROXY: 'http://127.0.0.1:58591',
  LOGNAME: 'qintuanye',
  SECURITYSESSIONID: '186aa',
  _: '/usr/local/bin/node',
  __CF_USER_TEXT_ENCODING: '0x1F5:0x19:0x34'
}
```

### 3. process.release

```shell
$ node -p "process.release"
{
  name: 'node',
  sourceUrl: 'https://nodejs.org/download/release/v13.5.0/node-v13.5.0.tar.gz',
  headersUrl: 'https://nodejs.org/download/release/v13.5.0/node-v13.5.0-headers.tar.gz'
}
```

### 4. process.release.lts

```shell
$ node -p "process.release.lts"
'Argon'
```

> 提示：只有在长期维护版本的环境下，该属性才有值，否则为 `undefined`。

### 5. 输入输出通道

`Node` 通过以下 3 个 `process` 函数来支持这些通道：

+ `process.stdin`：`stdin` 的可读流
+ `process.stdout`：`stdout` 的可写流
+ `process.stderr`：`stderr` 的可写流

这些流是无法在应用中关闭或者结束的，不过你可以从  `stdin` 输入流中获取输入，并写入 `stdout` 输出流和 `stderr` 错误流中。

### 6. 设置流的编码

```js
process.stdin.setEncoding('utf8')
```

### 7. 监听流的 `readable` 事件

当有数据可以读取时，该事件会通知该事件：

```js
process.stdin.on('readable', function() {
    var input = process.stdin.read();
    if (input !== null) {
        // 打印文本
        process.stdout.write(input);
    }
});
```

### 8. 退出应用

```
process.exit(0)
```

> 提示：0 代表退出码。