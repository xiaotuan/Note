```shell
#!/usr/bin/env bash
# 文件位置：cmdc/small/platform/build/tool/advca/telecom_ca.sh
OUT=${1}
if [ "$2" = "user" ];then
	OUT_DIR=out_user
	RELEASE_DIR=release_user
else
	OUT_DIR=out
	RELEASE_DIR=release
fi

BUILD_ID=${3}
chip_name=${4}
Target=${OUT}/${OUT_DIR}/target/target-${BUILD_ID}
SYSTEM=${Target}/SYSTEM

# 创建system_list镜像，该镜像主要用于系统校验
function make_system_list
{
    ###
    ###制作system_list
    ###
    echo ----- Hash System Begin ------
    rm ${SYSTEM}/etc/system_list*
    # 生成 publish 目录下所有文件的 hash 值文件
    ${OUT}/build/tool/linux-x86/bin/hash_tool 1 ${SYSTEM}/ ${OUT}/${OUT_DIR}/publish/
    if [ $? != 0 ]
    then
        echo "make hash file fail !!!"
        exit -1;
    fi
    # 生成 system_list_Sign.img 镜像文件并对其签名
    ${OUT}/build/tool/linux-x86/bin/CASignTool 2 \
        -K	${OUT}/build/tool/security/extern_rsa_priv.txt	\
        -R ${OUT}/${OUT_DIR}/publish/system_list.txt  \
        -O ${OUT}/${OUT_DIR}/publish/system_list
    cp ${OUT}/${OUT_DIR}/publish/system_list_Sign.img ${SYSTEM}/etc/system_list
    #rm  ${PLATFORM}/${OUT_DIR}/publish/system_list*
    echo ----- Hash System Success ------
}

# 对 boot.img 文件进行签名
function sign_boot_img
{
    if [[ ${chip_name} != "" ]];then
        BOOT_FILE=${PUBLISH_PATH}/boot_${chip_name}.img
        cp -arf ${BOOT_FILE} ${PUBLISH_PATH}/boot.img
    else
        BOOT_FILE=${PUBLISH_PATH}/boot.img
    fi
    ###
    ###签名boot.img
    ###

    ${OUT}/build/tool/linux-x86/bin/CASignTool 3 \
        ${OUT}/build/tool/advca/special_kernel_config.cfg	\
        -m  s \
        -K	${OUT}/build/tool/security/extern_rsa_priv.txt	\
        -r	${PUBLISH_PATH}/	\
        -o	${PUBLISH_PATH}/
    mv ${PUBLISH_PATH}/boot.sig ${BOOT_FILE}
    if [[ ${chip_name} != "" ]];then
        rm -rf ${PUBLISH_PATH}/boot.img
    fi
}

# 对 recovery.img 文件进行签名
function sign_recovery_img
{
    if [[ ${chip_name} != "" ]];then
        RECOVERY_FILE=${PUBLISH_PATH}/recovery_${chip_name}.img
        cp -arf ${RECOVERY_FILE} ${PUBLISH_PATH}/recovery.img
    else
        RECOVERY_FILE=${PUBLISH_PATH}/recovery.img
    fi
    ###
    ###签名recovery
    ###

    ${OUT}/build/tool/linux-x86/bin/CASignTool 3 \
        ${OUT}/build/tool/advca/special_recovery_config.cfg	\
        -m  s \
        -K	${OUT}/build/tool/security/extern_rsa_priv.txt	\
        -r	${PUBLISH_PATH}/	\
        -o	${PUBLISH_PATH}/

    mv ${PUBLISH_PATH}/recovery.sig ${RECOVERY_FILE}
    if [[ ${chip_name} != "" ]];then
        rm -rf ${PUBLISH_PATH}/recovery.img
    fi
}
```

