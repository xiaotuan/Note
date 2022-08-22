如果 APN 参数中名称包含 `&` 字符，编译将会报错：

```xml
<apn carrier="AT&T"
       mcc="310"
       mnc="410"
       apn="phone"
       mmsc="http://mmsc.mobile.att.net"
       mmsproxy="proxy.mobile.att.net"
       mmsport="80"
       type="default,mms,supl"
  />
```

需要使用 `&amp;` 转义符对其进行转义才行：

```xml
<apn carrier="AT&amp;T"
     mcc="310"
     mnc="410"
     apn="phone"
     mmsc="http://mmsc.mobile.att.net"
     mmsproxy="proxy.mobile.att.net"
     mmsport="80"
     type="default,mms,supl" />
```

