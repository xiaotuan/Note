```shell
#!/usr/bin/env bash
# 文件位置：cmdc\small\platform\on-project\build\project_priv_ota.sh
###
### Vars Define
###
TOP=${1}
Target=${2}
. ${TOP}/platform/build/Read.sh 

# 未定义该宏
gateway_type=$(Read_Value  ${BUILD_ID_MK}  BUILD_GateWay_TYPE)

if [[ "${gateway_type}" != "" ]]
then
	# 未找到该脚本文件
    PROJECT_PUBLIC_PRIV_OTA_SH=${TOP}/platform/public-project-router/build/project_public_priv_ota.sh
	bash ${PROJECT_PUBLIC_PRIV_OTA_SH} ${TOP} ${Target}
fi
```

