下表列出了存在于所有浏览器中的属性和方法，以及支持它们的浏览器版本。

| 属性或方法 | 说明 | IE | Firefox | Safari / Chrome | Opera |
| :- | :- | :-: | :-: | :-: | :-: |
| appCodeName | 浏览器的名称。通常都是 Mozilla，即使在非 Mozilla 浏览器中也是如此 | 3.0+ | 1.0+ | 1.0+ | 7.0+ |
| appMinorVersion | 次版本信息 | 4.0+ | - | - | 9.5+ |
| appName | 完整的浏览器名称 | 3.0+ | 1.0+ | 1.0+ | 7.0+ |
| appVersion | 浏览器的版本。一般不与实际的浏览器版本对应 | 3.0+ |1.0+ |1.0+ | 7.0+ |
| buildID | 浏览器编译版本 | - | 2.0+ | - | - |
| cookieEnabled | 表示 cookie 是否启用 | 4.0+ | 1.0+ | 1.0+ | 7.0+ |
| cupClass | 客户端计算机中使用的 CPU 类型（x86、68k、Alpha、PPC 或 Other ） | 4.0+ | - | - | - |
| javaEnabled() | 表示当前浏览器中是否启用了 Java | 4.0+ | 1.0+ | 1.0+ |7.0+ |
| language | 浏览器的主语言 | - | 1.0+ | 1.0+ | 7.0+ |
| mimeTypes | 在浏览器中注册的MIME类型 | 4.0+ | 1.0+ | 1.0+ | 7.0+ |
| onLine | 表示浏览器是否连接到了因特网 | 4.0+ | 1.0+ | - | 9.5+ |
| opsProfile | 似乎早就不用了。查不到相关文档 | 4.0+ | - | - | - |
| oscpu | 客户端计算机的操作系统或使用的 CPU | - | 1.0+ | - | - |
| Platform | 浏览器所在的系统平台 | 4.0+ | 1.0+ | 1.0+ | 7.0+ |
| plugins | 浏览器中安装的插件信息的数组 | 4.0+ | 1.0+ | 1.0+ | 7.0+ |
| preference() | 设置用户的首选项 | - | 1.5+ | - | - |
| product | 产品名称（如 Gecko） | - | 1.0+ | 1.0+ | - |
| productSub | 关于产品的次要信息（如 Gecko 的版本）| - | 1.0+ | 1.0+ | - |
| registerContentHandler() | 针对特定的 MIME 类型将一个站点注册为处理程序 | - | 2.0+ | - | - |
| registerProtocolHandler() | 针对特定的协议将一个站点注册为处理程序 | - | 2.0 | - | - |
| securityPolicy | 已经废弃。安全策略的名称。为了与 Netscape Navigator 4 向后兼容而保留下来 | - | 1.0+ | - | - |
| systemLanguage | 操作系统的语言 | 4.0+ | - | - | - |
| taintEnabled() | 已经废弃。表示是否允许变量被修改（taint）。为了与 Netscape Navigator 3 向后兼容而保留下来 | 4.0+ | 1.0+ | - | 7.0+ |
| userAgent | 浏览器的用户代理字符串 | 3.0+ | 1.0+ | 1.0+ | 7.0+ |
| userLanguage | 操作系统的默认语言 | 4.0+ | - | - | 7.0+ |
| userProfile | 借以访问用户个人信息的对象 | 4.0+ | - | - | - |
| vendor | 浏览器品牌 | - | 1.0+ | 1.0+ | - |
| vendorSub | 有关供应商的次要信息 | - | 1.0+ | 1.0+ | - |

对于非 IE 浏览器，可以使用 `plugins` 数组来检测是否按照了特定的插件。该数组中的每一项都包含下列属性：
+ name：插件的名字
+ description：插件的描述
+ filename：插件的文件名
+ length：插件所处理的 MIME 类型数量