可以使用如下命令查看 apk 的签名信息：

```shell
PS C:\Users\Admin\Desktop>  keytool -printcert -jarfile .\MtkSettings.apk
签名者 #1:

签名:

所有者: EMAILADDRESS=demo@mediatek.com, CN=demo, OU=WCD, O=MediaTek, L=HaiDian, ST=BeiJing, C=CN
发布者: EMAILADDRESS=demo@mediatek.com, CN=demo, OU=WCD, O=MediaTek, L=HaiDian, ST=BeiJing, C=CN
序列号: 84b4e672a85ac780
生效时间: Fri Dec 13 17:47:52 CST 2019, 失效时间: Tue Apr 30 17:47:52 CST 2047
证书指纹:
         SHA1: 78:71:78:2A:CF:E9:83:97:92:7C:56:0B:58:2C:96:C2:BA:17:BB:3A
         SHA256: 32:18:BE:77:47:E3:1C:21:9C:43:07:65:86:AE:45:8F:E9:6A:36:BA:1B:D0:46:3E:58:C0:3F:E0:72:CE:91:9E
签名算法名称: SHA256withRSA
主体公共密钥算法: 2048 位 RSA 密钥
版本: 3

扩展:

#1: ObjectId: 2.5.29.35 Criticality=false
AuthorityKeyIdentifier [
KeyIdentifier [
0000: 3E A7 D6 06 8F AD C6 1D   9B 33 48 FF E3 58 52 27  >........3H..XR'
0010: 2A 54 D7 12                                        *T..
]
]

#2: ObjectId: 2.5.29.19 Criticality=false
BasicConstraints:[
  CA:true
  PathLen:2147483647
]

#3: ObjectId: 2.5.29.14 Criticality=false
SubjectKeyIdentifier [
KeyIdentifier [
0000: 3E A7 D6 06 8F AD C6 1D   9B 33 48 FF E3 58 52 27  >........3H..XR'
0010: 2A 54 D7 12                                        *T..
]
]

```

