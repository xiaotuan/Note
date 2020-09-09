```shell
#!/usr/bin/env bash
# 文件位置：cmdc/small/platform/on-project/build/project_priv.sh
###
### Vars Define
###
TOP=${1}
BUILD_ID=${2}
# 引入 Read.sh 脚本
. ${TOP}/platform/build/Read.sh  

# 设置 OUT_DIR 和 SYSTEM_DIR 变量
if [ "$3" = "user" ];then
	OUT_DIR=out_user
	SYSTEM_DIR=system_user
elif [ "$3" = "l2_user" ];then
	OUT_DIR=out_user
	SYSTEM_DIR=system_user
elif [ "$3" = "all_user" ];then
	OUT_DIR=out_user
	SYSTEM_DIR=system_user
elif [ "$3" = "debug" ];then
	OUT_DIR=out
	SYSTEM_DIR=system
elif [ "$3" = "l2_debug" ];then
	OUT_DIR=out
	SYSTEM_DIR=system
elif [ "$3" = "all_debug" ];then
	OUT_DIR=out
	SYSTEM_DIR=system
else
	SYSTEM_DIR=system_user
fi

build_sw_brand=$(Read_Value ${TOP}/platform/on-project/build/build_id.mk  BUILD_SW_BRAND)

project_flag=$(Read_Value ${TOP}/platform/on-project/build/build_id.mk  PROJECT_FLAG)
LOADER=$(Read_Value ${TOP}/platform/on-project/build/build_id.mk LOADER)
BUILD_SUPPORT_MUL=$(Read_Value ${TOP}/platform/on-project/build/build_id.mk BUILD_SUPPORT_MUL)
BUILD_SUPPORT_ERRORCODE=$(Read_Value ${TOP}/platform/on-project/build/build_id.mk BUILD_SUPPORT_ERRORCODE)
if [ ${project_flag} ]
then
    export PUBLISH=publish_${project_flag}
    export  TARGET=target_${project_flag}
else
    export PUBLISH=publish
    export TARGET=target
fi
echo "publish path: ${PUBLISH}"

Target=${TOP}/platform/${OUT_DIR}/${TARGET}/target-${BUILD_ID}
SYSTEM=${Target}/SYSTEM

BUILD_SUPPORT_XIRI=$(Read_Value ${TOP}/platform/on-project/build/build_id.mk BUILD_SUPPORT_XIRI)
BUILD_CWMP_TR069=$(Read_Value ${TOP}/platform/on-project/build/build_id.mk BUILD_CWMP_TR069)
BUILD_SUPPORT_HIDE_WIFI=$(Read_Value ${TOP}/platform/on-project/build/build_id.mk BUILD_SUPPORT_HIDE_WIFI)

INSTALL_THIRDPATY=${TOP}/platform/on-project/tools/install_app

###
### Functions Define
###

#=================================================

# 拷贝 APK 文件
function Copy_Apk_Files
{
	cp ${TOP}/platform/on-project/apk/* ${SYSTEM}/app/

}
#拷贝第三方文件
function Copy_ThirdParty_Files
{
	export PATH=${TOP}/platform/on-project/tools:$PATH

	#拷贝apk和apk自身so文件,如果出现so冲突对应的apk不会被自动集成到盒子里面
	#默认集成MiguGameTV应用里面的so
	libs_conflict="[libijkffmpeg.so, libijkplayer.so, libijksdl.so, libiflyblesvc_xiri_d.so, libxdriver_xiri_d.so]"

	#"libimagepipeline.so" "libgifimage.so")
	export COPY_THIRD_APK_PATH="
	${TOP}/platform/on-project/third-party-apk/iflytek_xiri
	${TOP}/platform/on-project/third-party-apk/softdetector
	${TOP}/platform/on-project/third-party-apk/softdetector_mobile
	${TOP}/platform/on-project/third-party-apk/huawei
	${TOP}/platform/on-project/third-party-apk/miguAd
	${TOP}/platform/on-project/third-party-apk/zteAuth"

	# 使用 cmdc\small\platform\on-project\tools\install_app 脚本拷贝 APK
	${INSTALL_THIRDPATY} -o "${SYSTEM}" -p "${TOP}" -c "${libs_conflict}" ${COPY_THIRD_APK_PATH}

	if [ ! $? == 0 ];then
		echo "Install error";  
		exit 1;
	fi

	#install方式集成组播apk
	if [[ ${BUILD_SUPPORT_MUL} == "y" ]]
	then
		cp -arf ${TOP}/platform/on-project/third-party-apk/live_app/*  ${SYSTEM}/
	else
		rm ${SYSTEM}/app/SWAppInitService_base*.apk
	fi
	if [[ $BUILD_SUPPORT_HIDE_WIFI != "y" ]]
	then
		# 删除 swdefaultparam.txt 文件中对应的内容
		sed -i 's/publish_region=cmcc_hb//g' ${SYSTEM}/etc/swdefaultparam.txt
		sed -i 's/publish_region=cmcc_hb//g' ${SYSTEM}/etc/swupgradeparam.txt
		sed -i 's/hide_settings_wifi_cfg=1//g' ${SYSTEM}/etc/swdefaultparam.txt
		sed -i 's/hide_settings_wifi_cfg=1//g' ${SYSTEM}/etc/swupgradeparam.txt
		rm -rf ${SYSTEM}/app/SWKeyPressService.apk
	fi

	rm -rf ${SYSTEM}/app/SWAuth_sd.apk

}
# 拷贝工程 boot 相关文件
function Copy_Project_Boot_Files
{
	cp -arf ${TOP}/platform/on-project/pub/boot/root/* ${Target}/BOOT/${chip_name}/RAMDISK
	cp -arf ${TOP}/platform/on-project/pub/image/${chip_name}/uImage ${Target}/BOOT/${chip_name}/kernel

	if [[ "${build_sw_brand}" != "" ]]
	then
		cp -arf ${TOP}/platform/on-project/pub_${build_sw_brand}/boot/root/* ${Target}/BOOT/${chip_name}/RAMDISK
		cp -arf ${TOP}/platform/on-project/pub_${build_sw_brand}/image/${chip_name}/uImage ${Target}/${chip_name}/BOOT/kernel
	fi
}
# 拷贝 recovery 相关文件
function Copy_Project_Recovery_Files
{
	cp -arf ${TOP}/platform/on-project/pub/recovery/root/* ${Target}/RECOVERY/${chip_name}/RAMDISK
	cp -arf ${TOP}/platform/on-project/pub/image/${chip_name}/uImage ${Target}/RECOVERY/${chip_name}/kernel
	#cp key.xml to recovery/etc
	cp -arf ${TOP}/platform/on-project/pub/${SYSTEM_DIR}/etc/key.xml ${Target}/RECOVERY/${chip_name}/RAMDISK/etc

    if [[ "${build_sw_brand}" != "" ]]
	then
		cp -arf ${TOP}/platform/on-project/pub_${build_sw_brand}/recovery/root/* ${Target}/RECOVERY/${chip_name}/RAMDISK
		cp -arf ${TOP}/platform/on-project/pub_${build_sw_brand}/image/${chip_name}/uImage ${Target}/RECOVERY/${chip_name}/kernel
	fi

	rm -rf ${Target}/RECOVERY/${chip_name}/RAMDISK/sbin/adbd
}
# 拷贝工程相关的 xml 文件
function Copy_Project_Xml_Files
{
	cp -arf ${TOP}/platform/on-project/pub/image/*.xml ${TOP}/platform/${OUT_DIR}/${PUBLISH}

	if [[ "${build_sw_brand}" != "" ]]
	then
		cp -arf ${TOP}/platform/on-project/pub_${build_sw_brand}/image/*.xml ${TOP}/platform/${OUT_DIR}/${PUBLISH}
	fi
}
# 拷贝工程 RootServer 文件
function Copy_Project_RootServer_Files
{
	cp -arf ${TOP}/platform/on-project/pub/swproduct/*.apk ${SYSTEM}/app/
	cp -arf ${TOP}/platform/on-project/pub/${SYSTEM_DIR}/* ${SYSTEM}

	if [[ "${build_sw_brand}" != "" ]]
	then
		cp -arf ${TOP}/platform/on-project/pub_${build_sw_brand}/swproduct/*.apk ${SYSTEM}/app/
		cp -arf ${TOP}/platform/on-project/pub_${build_sw_brand}/${SYSTEM_DIR}/* ${SYSTEM}
	fi
}
# 拷贝工程 cfg 文件
function Create_Project_Cfg_Files
{
	cfg_file="${SYSTEM}/etc/swsettings.cfg"
	cfg_hide_wifi="${SYSTEM}/etc/swsettings_none_wifi.cfg"
	cfg_NoBTModule="${SYSTEM}/etc/swsettings_NoBTModule.cfg"
	cp -arf ${cfg_file} ${cfg_hide_wifi}
	cp -arf ${cfg_file} ${cfg_NoBTModule}
	sed -i 's/wifi1/wifi0/g' ${cfg_hide_wifi}
	sed -i 's/wifi1/wifi0/g' ${cfg_NoBTModule}
	sed -i 's/wifihot1/wifihot0/g' ${cfg_NoBTModule}
	sed -i 's/bluetooth1/bluetooth0/g' ${cfg_NoBTModule}
	sed -i 's/^menu_bluetooth/'\#menu_bluetooth'/g' ${cfg_NoBTModule}
	#硬件型号显示
	if [[ `grep "hardDeviceModel0" ${cfg_NoBTModule}` ]];then
		sed -i 's/hardDeviceModel0/hardDeviceModel1/g' ${cfg_NoBTModule}
	elif [[ ! `grep "hardDeviceModel" ${cfg_NoBTModule}` ]];then
		sed -i 's/menu_about .*/& hardDeviceModel1/g' ${cfg_NoBTModule}
	fi
	if [[ ${BUILD_NO_HIDE_WIFIHOT} != "y" ]];then
		sed -i 's/wifihot1/wifihot0/g' ${cfg_hide_wifi}
	fi
}
# 拷贝工程镜像文件
function Copy_Project_Images_Files
{
	cp -arf ${TOP}/platform/on-project/pub/image/baseparam.img ${TOP}/platform/${OUT_DIR}/${PUBLISH}/baseparam.img
	cp -arf ${TOP}/platform/on-project/pub/image/fastplay.img ${TOP}/platform/${OUT_DIR}/${PUBLISH}/fastplay.img
	cp -arf ${TOP}/platform/on-project/pub/image/logo.img ${TOP}/platform/${OUT_DIR}/${PUBLISH}/logo.img
	cp -arf ${TOP}/platform/on-project/pub/image/misc.img ${TOP}/platform/${OUT_DIR}/${PUBLISH}/misc.img
	cp -arf ${TOP}/platform/on-project/pub/image/${chip_name}/pq_param.bin ${TOP}/platform/${OUT_DIR}/${PUBLISH}

    if [[ ${LOADER} == '' ]]
    then
		cp -arf ${TOP}/platform/on-project/pub/image/${chip_name}/loader.bin ${TOP}/platform/${OUT_DIR}/${PUBLISH}/${chip_name}
    else
		cp -arf ${TOP}/platform/on-project/pub/image/${chip_name}/${LOADER} ${TOP}/platform/${OUT_DIR}/${PUBLISH}/${chip_name}/loader.bin
     fi

	if [[ "${build_sw_brand}" != "" ]]
	then
	    cp -arf ${TOP}/platform/on-project/pub_${build_sw_brand}/image/${chip_name}/* ${TOP}/platform/${OUT_DIR}/${PUBLISH}/${chip_name}/
	fi

}
# 生成 board.cfg、gpio.xml、devinfo.xml、board*.xml
function Board_cfg
{
	if [[ "${build_sw_brand}" != "" ]]
	then
		BOARD_DIRECTORY="${TOP}/platform/on-project/pub_${build_sw_brand}/image/"
		for filename in $(ls ${BOARD_DIRECTORY})
		do
			if [[ ${filename} == "gpio.xml" ]]
			then
				echo $filename
				GPIO_FILE_PATH=${TOP}/platform/on-project/pub_${build_sw_brand}/image/$filename
			fi

			if [[ ${filename} == board*.xml ]]
			then
				echo $filename
				BOARD_FILE_PATH=${TOP}/platform/on-project/pub_${build_sw_brand}/image/$filename
				BOARD_CFG_NAME=${filename%%.xml}".cfg"
			fi

			if [[ ${filename} == "devinfo.xml" ]]
			then
				echo $filename
				DEVINFO_FILE_PATH=${TOP}/platform/on-project/pub_${build_sw_brand}/image/$filename
			fi
		done
		if [[ -f ${BOARD_FILE_PATH} && -f ${GPIO_FILE_PATH} ]]
		then
			echo $BOARD_CFG_NAME
			${TOP}/platform/build/tool/linux-x86/bin/swmkboardcfg ${BOARD_FILE_PATH} ${GPIO_FILE_PATH} -o ${Target}/SYSTEM/etc/$BOARD_CFG_NAME
			cp -arf ${Target}/SYSTEM/etc/$BOARD_CFG_NAME ${Target}/RECOVERY/RAMDISK/etc
		fi
		if [[ -f ${DEVINFO_FILE_PATH} && -f ${GPIO_FILE_PATH} ]]
		then
			${TOP}/platform/build/tool/linux-x86/bin/swmkdevinfo ${DEVINFO_FILE_PATH} ${GPIO_FILE_PATH} -o ${PUBLISH_PATH}/deviceinfo.img -full
			${TOP}/platform/build/tool/linux-x86/bin/swmkdevinfo ${DEVINFO_FILE_PATH} ${GPIO_FILE_PATH} -o ${PUBLISH_PATH}/devinfo_patch.img -patch
		fi

	fi
}

# 删除不必要文件
function Rm_unnecessary_files
{
    rm -rf ${SYSTEM}/app/log*
    rm -rf ${SYSTEM}/app/LogUtils.*
    rm -rf ${SYSTEM}/app/SWHiFi_projector.*
    rm -rf ${SYSTEM}/app/SWHttpServer.*
    rm -rf ${SYSTEM}/app/SWIPTVPlayerTest.*
    rm -rf ${SYSTEM}/app/SWLauncher_projector.*
    rm -rf ${SYSTEM}/app/SWLocalMediaPlayer_projector.*
    rm -rf ${SYSTEM}/app/SWPlayer_projector.*
    rm -rf ${SYSTEM}/app/SWPowerManagerService.*
    rm -rf ${SYSTEM}/app/SWProductCheck.*
    rm -rf ${SYSTEM}/app/SWProductService_minsdk_L.*
    rm -rf ${SYSTEM}/app/SWProductService_ronghe_base.*
    rm -rf ${SYSTEM}/app/SWProductTest__minsdk_L.*
    rm -rf ${SYSTEM}/app/SWProductTest_restruction.*
    rm -rf ${SYSTEM}/app/SWProductTest_ronghe_base.*
    rm -rf ${SYSTEM}/app/SWSettings_base.*
    rm -rf ${SYSTEM}/app/SWSettings_base_N.*
    rm -rf ${SYSTEM}/app/SWSettings_projector.*
    rm -rf ${SYSTEM}/app/HiDMP.*
    #rm -rf ${SYSTEM}/app/HiDMR.*
    rm -rf ${SYSTEM}/app/HiDMS.*
    #rm -rf ${SYSTEM}/app/HiDlnaPlayer.*
    rm -f ${SYSTEM}/app/HiAgingTest.*
    rm -f ${SYSTEM}/app/HiDLNASettings.*
    rm -f ${SYSTEM}/app/HiDebugKit.*
    rm -f ${SYSTEM}/app/HiFileManager.*
	#rm -f ${SYSTEM}/app/HiMediaPlayer.*
	#rm -f ${SYSTEM}/app/HiMediaRender.*
	#rm -f ${SYSTEM}/app/HiMediaShare.*
	#rm -f ${SYSTEM}/app/HiMusic.*
	rm -f ${SYSTEM}/app/HiPQTools.*
	#rm -f ${SYSTEM}/app/HiVideoPlayer.*
	rm -f ${SYSTEM}/app/HiFactoryTest.*
	rm -f ${SYSTEM}/app/HiErrorReport.*
	rm -f ${SYSTEM}/app/HiGallery*
	rm -f ${SYSTEM}/app/MediaCenter.*
	#rm -f ${SYSTEM}/app/Miracast.*
	#rm -f ${SYSTEM}/app/SpeechRecorder.*
	rm -f ${SYSTEM}/app/Launcher_Rainbow_0711.*
	#rm -f ${SYSTEM}/app/SWIME2.*
	rm -f ${SYSTEM}/app/VST*
	rm -f ${SYSTEM}/app/Shafa.market.*
	rm -f ${SYSTEM}/app/LatinIME.*
	#rm -f ${SYSTEM}/app/HiPinyinIME.*
	rm -f ${SYSTEM}/app/SWIPTV_Base.apk
	rm -f ${SYSTEM}/app/NetworkInfo.apk
	#rm -f ${SYSTEM}/app/GoogleContactsSyncAdapter.*
	rm -f ${SYSTEM}/app/com.moretv.android*
	rm -f ${SYSTEM}/app/com.shafa.market*
	rm -f ${SYSTEM}/app/tvlive2-haisi*
    rm -f ${SYSTEM}/app/VIME*
	rm -f ${SYSTEM}/app/TestVideo.*
	rm -f ${SYSTEM}/app/SkyPlayer.*
	rm -f ${SYSTEM}/app/MultiScreenServer.*
	rm -f ${SYSTEM}/app/xmxwangluocesu_1.1_2.apk
	rm -f ${SYSTEM}/app/XCgamecenter.apk
	rm -f ${SYSTEM}/app/HardwareTest.apk
	#rm -f ${SYSTEM}/app/Bluetooth.apk
	rm -f ${SYSTEM}/app/Email.apk
	rm -f ${SYSTEM}/app/Browser.apk
	rm -f ${SYSTEM}/app/Gallery2.apk
	rm -f ${SYSTEM}/app/Camera2.apk
	rm -f ${SYSTEM}/app/Calendar.apk
	rm -f ${SYSTEM}/app/Exchange2.apk
	rm -f ${SYSTEM}/app/Galaxy4.apk
	rm -f ${SYSTEM}/app/VideoPhone.apk
	rm -f ${SYSTEM}/app/WAPPushManager.apk
	rm -f ${SYSTEM}/app/SWUpgrade_base.apk
	rm -f ${SYSTEM}/app/CopyPaniclog.apk
	rm -f ${SYSTEM}/app/SWSettings_base_back.apk
	rm -f ${SYSTEM}/app/DeskClock.apk
	rm -f ${SYSTEM}/app/HoloSpiralWallpaper.apk
	rm -f ${SYSTEM}/app/LiveWallpapers*
	rm -f ${SYSTEM}/app/LiveWallpapersPicker*
	rm -f ${SYSTEM}/app/MagicSmokeWallpapers*
	rm -f ${SYSTEM}/app/Music*
	rm -f ${SYSTEM}/app/NoiseField*
	rm -f ${SYSTEM}/app/PacProcessor*
	rm -f ${SYSTEM}/app/PhaseBeam*
	rm -f ${SYSTEM}/app/PhotoTable*
	#rm -f ${SYSTEM}/app/PackageInstaller.apk 
	rm -f ${SYSTEM}/app/PicoTts*
	rm -f ${SYSTEM}/app/PrintSpooler.*
	rm -f ${SYSTEM}/app/QuickSearchBox.*
	rm -f ${SYSTEM}/app/SoundRecorder.*
	rm -f ${SYSTEM}/app/SpeechRecorder.*
	rm -f ${SYSTEM}/app/VisualizationWallpapers.*
	rm -f ${SYSTEM}/app/hianimation.apk
	rm -f ${SYSTEM}/app/TelephonyProvider.apk
	rm -f ${SYSTEM}/app/ServiceSettings.apk
	rm -f ${SYSTEM}/app/Development.apk
	rm -f ${SYSTEM}/app/EulerView.apk

	rm -f ${SYSTEM}/app/Hdcp1.4KeyLoadTool.apk
	rm -f ${SYSTEM}/app/HiVideoPhoneTest.apk
	rm -f ${SYSTEM}/app/MultiVideoTest.apk
	rm -f ${SYSTEM}/app/KeyChain.apk
	rm -f ${SYSTEM}/app/CertInstaller.apk
	rm -f ${SYSTEM}/app/AndroidAudioRecordTest.apk

	#rm -f ${SYSTEM}/priv-app/Settings.*
	#rm -f ${SYSTEM}/priv-app/HiSettings.*
	#rm -f ${SYSTEM}/priv-app/Launcher2.*
	#rm -f ${SYSTEM}/priv-app/Google*
	#rm -f ${SYSTEM}/priv-app/GmsCore.*
	rm -f ${SYSTEM}/priv-app/SetupWizard.*

	rm -f ${SYSTEM}/bin/gpio-led

	#rm -f ${SYSTEM}/lib/modules/xhci-hcd.ko

    ####for cts,frontPanel own the permission s####
    rm -f ${SYSTEM}/bin/frontPanel

	rm -f ${SYSTEM}/priv-app/Settings.*
	rm -f ${SYSTEM}/priv-app/HiSettings.*
	rm -f ${SYSTEM}/priv-app/Launcher2.*
	rm -f ${SYSTEM}/priv-app/Google*
	rm -f ${SYSTEM}/priv-app/GmsCore.*
	rm -f ${SYSTEM}/priv-app/SetupWizard.*
	rm -f ${SYSTEM}/priv-app/MusicFX.apk
	rm -f ${SYSTEM}/priv-app/CalendarProvider.apk
	rm -rf ${SYSTEM}/app/rtkbtAutoPairUIDemo.apk
	rm -rf ${SYSTEM}/app/rtkbtAutoPairService.apk
	rm -rf ${SYSTEM}/app/log  
	rm -rf ${SYSTEM}/app/init.txt 
	rm -rf ${SYSTEM}/app/SWProductTest*.apk
	rm -rf ${SYSTEM}/lib/modules_${chip_name}/modules

	if [[ -d ${TOP}/platform/release/system/lib/modules_Hi3798MV310 ]]
	then 
		rm -rf ${TOP}/platform/release/system/lib/modules_Hi3798MV310
	fi 
	if [[ -d ${TOP}/platform/on-project/pub/system/lib/modules_Hi3798MV300H ]]
	then 
		cp -arf ${TOP}/platform/on-project/pub/system/lib/modules_Hi3798MV300H/* ${SYSTEM}/lib/modules_Hi3798MV310/
	fi 

	sed -i "/ro.revert.support=true/d" ${SYSTEM}/build.prop
	sed -i "/ro.support.sampkg=Hi3798MV300H/i\ro.revert.support=true" ${SYSTEM}/build.prop
	defaultparam=${SYSTEM}/etc/swdefaultparam.txt

    rm -rf ${SYSTEM}/app/SWBootConfig.apk
	rm -rf ${SYSTEM}/app/SWTR069_sd.apk
    rm -rf ${SYSTEM}/app/SWBootAnimation_sd.apk
    rm -rf ${SYSTEM}/app/MultiScreenServer.apk
    rm -rf ${SYSTEM}/app/HiPinyinIME.apk

}

###
### Main Logic
###
	Board_cfg
	Copy_Project_Boot_Files
	Copy_Project_Recovery_Files
	Copy_Project_Xml_Files
	Copy_Project_RootServer_Files
	Create_Project_Cfg_Files
	Copy_Project_Images_Files
	Copy_Apk_Files
	Copy_ThirdParty_Files
    Rm_unnecessary_files
```

