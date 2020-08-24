```shell
# usage: 在需要system上层目录调用本接口
#
## prepare bootjars' .odex
PRODUCT_BOOT_JARS="core:conscrypt:okhttp:core-junit:bouncycastle:ext:framework:framework2:telephony-common:voip-common:mms-common:android.policy:qb:services:apache-xml:webviewchromium"
optimizeFlags="v=a,o=v,m=y,u=n"
BOOTJARS=${PRODUCT_BOOT_JARS//:/ }
TOP_DIR=""
SYSTEM_DIR=""
BOOTJARS_DIR=""
FRAMEWORK_DIR=""

APP_DIR=""
PRIV_APP_DIR=""
APP_OUT_DIR=""
PRIV_APP_OUT_DIR=""
#local function
function predex_bootjars
{
	for JAR in ${BOOTJARS}
	do
		JAR=$(basename ${JAR}.jar .jar )
		${ACP} ${FRAMEWORK_DIR}/${JAR}.jar ${BOOTJARS_DIR}
		inputFile="${BOOTJARS_DIR}/${JAR}.jar"
		outputFile="${BOOTJARS_DIR}/${JAR}.odex"
		echo "predexopt on ${JAR}"
		${TOP_DIR}/platform/build/tool/linux-x86/bin/dexopt  --preopt ${inputFile} ${outputFile} ${optimizeFlags}
	done              

	echo "-----preodexopt boot jars ok"
}
#param1: TOP_DIR directory
#param2: system directory
function do_preodex
{
	if [ $# != 2 ]
	then
		echo $#
		echo "usage: top-dir system-dir "
		exit -1
	fi

	TOP_DIR=$1

	ACP=${TOP_DIR}/platform/build/tool/linux-x86/bin/acp
	DEXOPT=${TOP_DIR}/platform/build/tool/linux-x86/bin/dexopt
	AAPT=${TOP_DIR}/platform/build/tool/linux-x86/bin/aapt
	BASE_DIR=$2
	ODEX_OUT=${BASE_DIR}/odexout
	rm -rf ${ODEX_OUT}
	
	SYSTEM_DIR=$2
	BOOTJARS_DIR=system/odexout/dex_bootjars/./system/framework
	FRAMEWORK_DIR=${SYSTEM_DIR}/framework

	APP_DIR=${SYSTEM_DIR}/app
	PRIV_APP_DIR=${SYSTEM_DIR}/priv-app
	APP_OUT_DIR=${ODEX_OUT}/app
	PRIV_APP_OUT_DIR=${ODEX_OUT}/priv-app
	FRAMEWORK_OUT_DIR=${ODEX_OUT}/framework

	mkdir -p  ${ODEX_OUT} 
	mkdir -p  ${BOOTJARS_DIR}

	BOOTCLASSPATH=`echo ":${PRODUCT_BOOT_JARS}" | \
		        sed "s!:\([^:]*\)!:${BOOTJARS_DIR}/\1.jar!g"|\
	sed 's/^://'`
	export BOOTCLASSPATH

	predex_bootjars

	filename=""
	isbootjar=0

	mkdir -p ${FRAMEWORK_OUT_DIR}
 for f in `ls ${FRAMEWORK_DIR}`
 do
	 subfix=${f##*.}
	 if [ ${subfix} ==  "odex" ]
	 then
		 echo "drop odex file: ${f}"
		 continue
	 fi
	 if [ ${f%*_nodex*} != ${f} ]
	 then
		 echo "drop nodex file: ${f}"
		 continue
	 fi

	 if [ ${subfix} == "jar" ]
	 then
		 filename=$(basename $f .jar)

		 for JAR in ${BOOTJARS}
		 do
			 if [ $filename == $JAR ]
			 then
				 echo "$f has preopted as BOOTJARS"
				 isbootjar=1;
				break 
			 fi
		 done

		 if [ $isbootjar == 1 ]
		 then
			 isbootjar=0
			 continue
		 fi
	elif [ ${subfix} == "apk" ]
	then
		 filename=$(basename $f .apk)
	else
	 continue
	fi

	
#	 ${ACP} ${FRAMEWORK_DIR}/${filename}.${subfix} ${BOOTJARS_DIR}
#	 rm -f ${BOOTJARS_DIR}/${filename}.odex

#	 inputFile="${BOOTJARS_DIR}/${filename}.${subfix}"
#	 outputFile="${BOOTJARS_DIR}/${filename}.odex"
	 ${ACP} ${FRAMEWORK_DIR}/${filename}.${subfix} ${FRAMEWORK_OUT_DIR}
	 rm -f ${FRAMEWORK_OUT_DIR}/${filename}.odex
#
	 inputFile="${FRAMEWORK_OUT_DIR}/${filename}.${subfix}"
     outputFile="${FRAMEWORK_OUT_DIR}/${filename}.odex"

	 echo "preodexopt on $f"
	${DEXOPT}  --preopt ${inputFile} ${outputFile} ${optimizeFlags}
 done              
# echo "----------predexopt other jars ok"

# 	predex_on_apk "app" 
	
# echo "----------predexopt app/*apk ok"
#	predex_on_apk "priv-app" 
# echo "----------predexopt priv-app/*apk ok"
  cp -rf ${BOOTJARS_DIR}/* ${FRAMEWORK_DIR}
  cp -rf ${FRAMEWORK_OUT_DIR}/* ${FRAMEWORK_DIR}
#  cp ${APP_OUT_DIR}/* ${APP_DIR}
#  cp ${PRIV_APP_OUT_DIR}/* ${PRIV_APP_DIR}
  rm -rf ${ODEX_OUT}
}
#param1: directory name base on "system", ex: app priv_app
 function predex_on_apk
 {

	 apkout=${ODEX_OUT}/$1
	 mkdir -p ${apkout} 

	 for apk  in `ls ${SYSTEM_DIR}/${1}/*.apk`
	 do
		 filename=$(basename ${apk} ".apk")

		 ${ACP} ${apk}  ${apkout}
		 inputFile="${apkout}/${filename}.apk"
		 outputFile="${apkout}/${filename}.odex"

	 echo "preodexopt on $apk"

		 ${DEXOPT}  --preopt ${inputFile} ${outputFile} ${optimizeFlags}
		 ${AAPT} remove $apk classes.dex

	 done
}



```

