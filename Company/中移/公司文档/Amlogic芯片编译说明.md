[toc]

### compile.sh 编译脚本

```shell
#! /bin/bash

# 是否在编译前删除 out 目录
DELETE_OUT=true
# 是否 checkout 仓库
CHECK_OUT_REPOSITORY=true
# 是否需要更新仓库代码
UPDATE_REPOSITORY=true
# 软件版本号
VERSION=100.463.36
# 签名类型
SIGNED_TYPE="cmdcSigned"
# 过渡版本设置为 open_backup，统一ROM版本设置为 close_backup
PARAMETERS_BACKUP=close_backup
#过渡版本设置为1  统一ROM版本设置为2
GD='set_prop "ro.custom.version" "1"'
TY='set_prop "ro.custom.version" "2"'

# 大系统代码目录
SDK_PATH="/home/qintuanye/workspace/amlogic/sdk/amlogic_905l2/sdk"
# 小系统代码目录
SMALL_PATH="/home/qintuanye/workspace/amlogic/small/cmdc/small"
# 应用代码目录
APP_PATH="/home/qintuanye/workspace/hisimv300/sdk/sduntiyrom/sdk/packages/cmdc"

#编译大系统
function makeSDK() {
    echo "Execute makeSDK."
    deleteSdkOutDirectory && checkoutSdkRepository && updateSdkRepository && checkoutSdkCmdcApp && copyAppProject && setBackUpParam && setCustomVersion && setBuildVersion && cd $SDK_PATH && source ./make.sh
    if [ $? -eq 0 ];then
        cd $SDK_PATH
        echo "cp sdk release img pwd=$PWD"
        #拷贝大系统中release下的文件到小系统
        rm -rf $SMALL_PATH/platform/release && mkdir $SMALL_PATH/platform/release && cp -rfp ./out/target/product/release/* $SMALL_PATH/platform/release/
    else
        return 1
    fi
}

# 编译小系统
function makeSamll() {
    echo "Execute makeSamll."
    cd $SMALL_PATH
    echo $PWD
    git clean -fd && git checkout . && git pull --rebase && rm -rf platform/out && make -j12
}

# 替换签名文件
function makeSigned() {
    echo "Execute makeSigned."
    echo "SIGNED_TYPE is $SIGNED_TYPE"
    if [ ${SIGNED_TYPE} = "default" ]; then
        echo "user amlogic signed"
        cp -f $SMALL_PATH/platform/build/tool/swsecurity/media* $SMALL_PATH/platform/build/tool/security/
        cp -f $SMALL_PATH/platform/build/tool/swsecurity/platform* $SMALL_PATH/platform/build/tool/security/
        cp -f $SMALL_PATH/platform/build/tool/swsecurity/shared* $SMALL_PATH/platform/build/tool/security/
        cp -f $SMALL_PATH/platform/build/tool/swsecurity/testkey* $SMALL_PATH/platform/build/tool/security/
        cp -f $SMALL_PATH/platform/build/tool/swsecurity/media* $SDK_PATH/build/target/product/security/
        cp -f $SMALL_PATH/platform/build/tool/swsecurity/platform* $SDK_PATH/build/target/product/security/
        cp -f $SMALL_PATH/platform/build/tool/swsecurity/shared* $SDK_PATH/build/target/product/security/
        cp -f $SMALL_PATH/platform/build/tool/swsecurity/testkey* $SDK_PATH/build/target/product/security/
    elif [ ${SIGNED_TYPE} = "cmdcSigned" ]; then
        echo "user cmdcsigned"
        cp -f $SMALL_PATH/platform/build/tool/cmdcsecurity/media* $SMALL_PATH/platform/build/tool/security/
        cp -f $SMALL_PATH/platform/build/tool/cmdcsecurity/platform* $SMALL_PATH/platform/build/tool/security/
        cp -f $SMALL_PATH/platform/build/tool/cmdcsecurity/shared* $SMALL_PATH/platform/build/tool/security/
        cp -f $SMALL_PATH/platform/build/tool/cmdcsecurity/testkey* $SMALL_PATH/platform/build/tool/security/
        cp -f $SMALL_PATH/platform/build/tool/cmdcsecurity/media* $SDK_PATH/build/target/product/security/
        cp -f $SMALL_PATH/platform/build/tool/cmdcsecurity/platform* $SDK_PATH/build/target/product/security/
        cp -f $SMALL_PATH/platform/build/tool/cmdcsecurity/shared* $SDK_PATH/build/target/product/security/
        cp -f $SMALL_PATH/platform/build/tool/cmdcsecurity/testkey* $SDK_PATH/build/target/product/security/
    fi
}

# 删除大系统out目录
function deleteSdkOutDirectory() {
    cd $SDK_PATH
    file1="out"
    if [[ $DELETE_OUT = "true" ]]; then
        echo -e "rm -rf $file1 \n" && rm -rf $file1
    fi
}

# 拷贝应用代码
function copyAppProject() {
    cd $SDK_PATH
    rm -rf ./packages/cmdc
    mkdir ./packages/cmdc
    cd $APP_PATH
    echo "copyAppProject $APP_PATH"
    echo $PWD
    for dir in $(ls -l | awk '/^d/ { print $NF }')
    do
        cp -rfp "$APP_PATH/$dir" $SDK_PATH/packages/cmdc
        if [ $? -ne 0 ];then
        	return 1
        fi
    done
}

# checkout 大系统仓库
function checkoutSdkRepository() {
    cd $SDK_PATH
    if [[ $CHECK_OUT_REPOSITORY = "true" ]];then
        git clean -fd
        git checkout .
        checkoutSdkCmdcApp
    fi
}

function checkoutRepository() {
    echo "checkout $1"
    cd "$APP_PATH/$1"
    echo "checkoutRepository $PWD"
    git clean -fd && git checkout . && git pull --rebase
}

# checkout packages/cmdc下的应用
function checkoutSdkCmdcApp() {
    cd $APP_PATH
    echo $PWD
    for dir in $(ls -l | awk '/^d/ { print $NF }')
    do
        checkoutRepository $dir
        if [ $? -ne 0 ];then
        	return 1
        fi
    done
}

# 更新大系统仓库代码
function updateSdkRepository() {
    cd $SDK_PATH
    if [[ $UPDATE_REPOSITORY = "true" ]];then
        git pull --rebase
    fi
}

# 设置备份参数
function setBackUpParam() {
    echo "Execute setBackUpParam"
    cd $SMALL_PATH
    if [ ${PARAMETERS_BACKUP} = "open_backup" ]; then
        echo "Set PARAMETERS_BACKUP to y"
        sed -i "s/`awk -F " := " '{if($1=="PARAMETERS_BACKUP"){print $0}}' ./platform/on-project/build/build_id.mk`/PARAMETERS_BACKUP := y/g" ./platform/on-project/build/build_id.mk
    elif [ ${PARAMETERS_BACKUP} = "close_backup" ]; then
        echo "Set PARAMETERS_BACKUP to n"
        sed -i "s/`awk -F " := " '{if($1=="PARAMETERS_BACKUP"){print $0}}' ./platform/on-project/build/build_id.mk`/PARAMETERS_BACKUP := n/g" ./platform/on-project/build/build_id.mk
    fi
}

# 设置 ro.custom.version 的值
# set_prop "ro.custom.version" "2"
function setCustomVersion() {
    echo "Execute setCustomVersion"
    cd $SMALL_PATH
    result=$(grep "ro.custom.version" ./platform/on-project/build/build_prop.sh)
    echo "grep result: $result, fisrt char: ${result:0:1}"

    if [ ${PARAMETERS_BACKUP} = "open_backup" ]; then
        echo "Set ro.custom.version to $GD"
        if [[ -n $result ]] && [[ ${result:0:1} != '#' ]];then
            sed -i "s/`awk '$2 ~/"ro.custom.version"/ {print $0}' ./platform/on-project/build/build_prop.sh`/$GD/g" ./platform/on-project/build/build_prop.sh
        else 
            echo "\n$GD" >> ./platform/on-project/build/build_prop.sh
        fi
    elif [ ${PARAMETERS_BACKUP} = "close_backup" ]; then
        echo "Set ro.custom.version to $TY"
        if [[ -n $result ]] && [[ ${result:0:1} != '#' ]];then
            sed -i "s/`awk '$2 ~/"ro.custom.version"/ {print $0}' ./platform/on-project/build/build_prop.sh`/$TY/g" ./platform/on-project/build/build_prop.sh
        else 
            echo -e "\n$TY" >> ./platform/on-project/build/build_prop.sh
        fi
    fi
}

# 设置版本号
function setBuildVersion() {
    echo "Execute setBuildVersion."
    echo "Set the software version number: $VERSION"
    cd $SMALL_PATH
    sed -i "s/`awk -F " := " '{if($1=="BUILD_NUMBER"){print $NF}}' ./platform/on-project/build/build_id.mk`/$VERSION/g" ./platform/on-project/build/build_id.mk
}

# 格式化时间
function formatTime() {
    if [ $1 -le 0 ]; then
        echo "0 second"
    else
        HOUR=3600
        MINUTE=60
        let hour=$(($1/$HOUR))
        let minute=$((($1-$hour*$HOUR)/$MINUTE))
        let second=$(($1%$MINUTE))
        if [ $hour -gt 0 ]; then
            echo "$hour hour, $minute minute, $second second"
        else 
            if [ $minute -gt 0 ]; then
                echo "$minute minute, $second second"
            else
                echo "$second second"
            fi
        fi
    fi
}

# 执行编译
function makeAll() {
    start=$(date +%s)
    makeSigned && makeSDK && makeSamll
    result=$?
    end=$(date +%s)
    useTime=$((end - start))
    useTimeStr=$(formatTime $useTime)
    echo ""
    echo "====================== Compile Completed ======================"
    echo ""
    if [ $result -eq 0 ];then
        echo -e "\e[1;32m Compile Successed!!! Use Time: $useTimeStr \e[0m"
    else
        echo -e "\e[1;31m Compile Fail!!! Use Time: $useTimeStr \e[0m"
    fi
    echo ""
    echo "==============================================================="
    echo ""
}

# 编译
makeAll | tee ./build.log
```
