[toc]

### 1. 查看帮助信息

```shell
$ node --help 
or
$ node -h
```

### 2. 查看 `Node` 版本

```shell
$ node --version
or
$ node -v
```

### 3. 查看某个 `Node` 应用的语法

```shell
$ node -c script.js
or 
$ node --check script.js
```

### 4. 查看 V8 参数

```shell
$ node --v8-options
```

### 5. 运行一行 `Node` 脚本并打印结果

```shell
$ node -p "process.env"
{
  TERM_PROGRAM: 'Apple_Terminal',
  ANDROID_HOME: '/Users/qintuanye/Library/Android/sdk',
  TERM: 'xterm-256color',
  SHELL: '/bin/bash',
  TMPDIR: '/var/folders/x3/qxwt6yrx4cz8gzgf3c_r0zwc0000gn/T/',
  TERM_PROGRAM_VERSION: '440',
  OLDPWD: '/Users/qintuanye/Documents/GitSpace',
  TERM_SESSION_ID: '29754B38-F597-4F9F-B754-F9AA430C5A13',
  USER: 'qintuanye',
  SSH_AUTH_SOCK: '/private/tmp/com.apple.launchd.lBeKs4yRH6/Listeners',
  PATH: '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin:/Users/qintuanye/Library/Android/sdk/platform-tools:/Users/qintuanye/Library/Android/sdk/tools:/Users/qintuanye/Library/Android/sdk/build-tools:/Users/qintuanye/Flutter/bin',
  LaunchInstanceID: 'E0A9E95A-24A8-4464-8E10-78444AAC93DD',
  __CFBundleIdentifier: 'com.apple.Terminal',
  PWD: '/Users/qintuanye/Documents',
  LANG: 'zh_CN.UTF-8',
  XPC_FLAGS: '0x0',
  XPC_SERVICE_NAME: '0',
  HOME: '/Users/qintuanye',
  SHLVL: '1',
  LOGNAME: 'qintuanye',
  SECURITYSESSIONID: '186aa',
  _: '/usr/local/bin/node',
  __CF_USER_TEXT_ENCODING: '0x1F5:0x19:0x34'
}
```

