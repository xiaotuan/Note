[toc]

> 提示：详细教程请参阅 <http://nodejs.cn/api/addons.html#addons_c_addons>。

### 1. 创建 `binding.gyp` 配置文件

`binding.gyp` 配置文件使用类 `JSON` 的格式提供了插件的信息：

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

### 2. 创建 `hello.cc` 文件

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

### 3. 配置并构建插件

```shell
$ node-gyp configure build
```

> 提示：编译后的文件将安装在 `build/Release` 目录中。

### 4. 示例代码

详细构建及使用 C/C++ 插件的示例代码请查阅 [Hello World插件示例](./Simple/Hello World插件示例/README.md)。

