```shell
#! /bin/bash

jenkinsPath="ssh jenkins@192.168.40.138 ls -tr workspace/stb_app_version_bak/"
scppath="jenkins@192.168.40.138:/home/jenkins/workspace/stb_app_version_bak/"

lastapk=""
tmp=""

# 该函数的功能是：
# 删除旧的 apk 文件
function rm_old_apk(){
    echo "start rm old apk"
    rm -f ../on-project/apk/*SWContentprovider_sd*
    rm -f ../on-project/apk/*SWGuide_sd*
    rm -f ../on-project/apk/*SWKeyPressService*
    rm -f ../on-project/apk/*SWNetSpeed_sd*
    rm -f ../on-project/apk/*SWNtp_sd*
    rm -f ../on-project/apk/*SWPowerManager_sd*
    rm -f ../on-project/apk/*SWSettings_mv300*
    rm -f ../on-project/apk/*SWTR069_sd_sunniwell*
    rm -f ../on-project/apk/*SWUpgrade_sd*
    rm -f ../on-project/apk/*SWUpgrade_usb_sd*
    rm -f ../on-project/apk/*CmdcSTBService*
    rm -f ../on-project/apk/*SWInformation*
    echo "end rm old apk"
}

# 该函数的功能是：
# 拷贝最新的 apk 文件
function copy_last_apk(){
path=$jenkinsPath$1
echo "filepath=$path"

for file in `$path`;
do
#    echo "this is dir="$file
    lastapk=$file
done

tmp=`echo $lastapk |awk -F '.' '{print $NF}'`
echo "tmp=$tmp"

if [ "$tmp" == "apk" ];then
    echo "lastapk=$lastapk" 
    scp $scppath$1${lastapk} ./tmpapk/signapk${lastapk}
    if [ ! -e "./tmpapk/signapk${lastapk}" ];
    then
        echo "ERROR: no such file $scppath$lastapk" 
        exit 1
    fi
	java -jar ./tool/linux-x86/framework/signapk.jar ./tool/security/platform.x509.pem ./tool/security/platform.pk8 ./tmpapk/signapk${lastapk} ../on-project/apk/${lastapk}
else
       echo "ERROE:not find apk, $jenkinsPath"
       exit 1
fi
}

# 该函数的功能是：
# 签名系统应用
function signed_pub_system_app(){
echo "signed_pub_system_app=$1$2"
java -jar ./tool/linux-x86/framework/signapk.jar ./tool/security/platform.x509.pem ./tool/security/platform.pk8 $1$2  ./tmpapk/signed-$2
cp -f ./tmpapk/signed-$2 $1$2
}

# 执行删除旧的 apk 文件函数
rm_old_apk

# 创建目录 tmpapk
mkdir tmpapk
# 拷贝最新 apk
copy_last_apk "SWContentprovider_sd/"
copy_last_apk "SWSettings_mv300/"
copy_last_apk "SWTR069_sd_sunniwell/"
copy_last_apk "SWGuide_sd/"
copy_last_apk "SWUpgrade_usb_sd/"
copy_last_apk "SWUpgrade_sd/"
copy_last_apk "SWPowerManager_sd/"
copy_last_apk "SWKeyPressService/"
copy_last_apk "SWNetSpeed_sd/"
copy_last_apk "SWNtp_sd/"
copy_last_apk "CmdcSTBService/"
copy_last_apk "SWInformation/"

#对on-project/pub/system/app 需要系统签名的文件进行签名
signed_pub_system_app "../on-project/pub/system/app/" HiDMR.apk
signed_pub_system_app "../on-project/pub/system/app/" HiRMService.apk
signed_pub_system_app "../on-project/pub/system/app/" SWAppInitService_base.apk
signed_pub_system_app "../on-project/pub/system/app/" SWBTAutoPairService.apk
signed_pub_system_app "../on-project/pub/system/app/" SWIME2.apk
signed_pub_system_app "../on-project/pub/system/app/" SWSTBManagerService.apk
signed_pub_system_app "../on-project/pub/system/app/" SWSystemManager_base.apk
signed_pub_system_app "../on-project/pub/system/priv-app/" PackageInstaller.apk
signed_pub_system_app "../on-project/pub/system/priv-app/" SettingsProvider.apk
rm -rf tmpapk

```

