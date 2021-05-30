[toc]

### 1. 工程文件目录结构

```console
tantuanyedeMacBook-Pro:helloworld qintuanye$ tree
.
├── binding.gyp
├── build
│   ├── Makefile
│   ├── Release
│   │   ├── addon.node
│   │   └── obj.target
│   │       └── addon
│   │           └── hello.o
│   ├── addon.target.mk
│   ├── binding.Makefile
│   ├── config.gypi
│   └── gyp-mac-tool
├── hello.cc
└── hello.js
```

### 2. 创建插件步骤

#### 2.1 创建插件目录 `helloworld`，并切换到该目录

```shell
$ mkdir helloworld
$ cd helloworld
```

#### 2.2 在 `helloworld` 目录下创建 `binding.gyp` 工程配置文件

```shell
$ touch binding.gyp
```

`binding.gyp` 文件的内容如下：

```json
{
  "targets": [
    {
      "target_name": "addon",
      "sources": [ "hello.cc" ]
    }
  ]
}
```

#### 2.3 在 `helloworld` 目录下创建 `hello.cc` 插件实现代码

```shell
$ touch hello.cc
```

`hello.cc` 文件内容如下：

```cpp
// hello.cc
#include <node.h>

namespace demo {

using v8::FunctionCallbackInfo;
using v8::Isolate;
using v8::Local;
using v8::Object;
using v8::String;
using v8::Value;

void Method(const FunctionCallbackInfo<Value>& args) {
  Isolate* isolate = args.GetIsolate();
  args.GetReturnValue().Set(String::NewFromUtf8(
      isolate, "world").ToLocalChecked());
}

void Initialize(Local<Object> exports) {
  NODE_SET_METHOD(exports, "hello", Method);
}

NODE_MODULE(NODE_GYP_MODULE_NAME, Initialize)

}  // 命名空间示例
```

使用 `node-gyp` 进行配置和构建：

```shell
$ node-gyp configure build
gyp info it worked if it ends with ok
gyp info using node-gyp@8.1.0
gyp info using node@13.5.0 | darwin | x64
gyp info find Python using Python version 3.7.6 found at "/usr/local/opt/python/bin/python3.7"
gyp info spawn /usr/local/opt/python/bin/python3.7
gyp info spawn args [
gyp info spawn args   '/usr/local/lib/node_modules/node-gyp/gyp/gyp_main.py',
gyp info spawn args   'binding.gyp',
gyp info spawn args   '-f',
gyp info spawn args   'make',
gyp info spawn args   '-I',
gyp info spawn args   '/Users/qintuanye/Documents/TempSpace/nodelib/build/config.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/usr/local/lib/node_modules/node-gyp/addon.gypi',
gyp info spawn args   '-I',
gyp info spawn args   '/Users/qintuanye/Library/Caches/node-gyp/13.5.0/include/node/common.gypi',
gyp info spawn args   '-Dlibrary=shared_library',
gyp info spawn args   '-Dvisibility=default',
gyp info spawn args   '-Dnode_root_dir=/Users/qintuanye/Library/Caches/node-gyp/13.5.0',
gyp info spawn args   '-Dnode_gyp_dir=/usr/local/lib/node_modules/node-gyp',
gyp info spawn args   '-Dnode_lib_file=/Users/qintuanye/Library/Caches/node-gyp/13.5.0/<(target_arch)/node.lib',
gyp info spawn args   '-Dmodule_root_dir=/Users/qintuanye/Documents/TempSpace/nodelib',
gyp info spawn args   '-Dnode_engine=v8',
gyp info spawn args   '--depth=.',
gyp info spawn args   '--no-parallel',
gyp info spawn args   '--generator-output',
gyp info spawn args   'build',
gyp info spawn args   '-Goutput_dir=.'
gyp info spawn args ]
gyp info spawn make
gyp info spawn args [ 'BUILDTYPE=Release', '-C', 'build' ]
  CXX(target) Release/obj.target/addon/hello.o
  SOLINK_MODULE(target) Release/addon.node
gyp info ok 
```

#### 2.4 创建测试插件脚本 `hello.js`

在 `helloworld` 目录下创建 `hello.js` 文件：

```shell
$ touch hello.js
```

`hello.js` 的文件内容如下所示：

```js
// hello.js
const addon = require('./build/Release/addon')

console.log(addon.hello())
// 打印：'world'
```

#### 2.5 运行测试脚本

```shell
$ node hello.js
world
```

