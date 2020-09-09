```shell
#!/usr/bin/env bash
# 文件位置：cmdc/small/platform/build/make.sh
# 下面的注释都是基于小系统的目录结构为：
# /home/qintuanye/workspace/zhaoge_mv300_2020/cmdc/small
# 作为说明的
#
# 设置编译类型、输出目录、正式版目录、用户标志
#
# $0 的值为命令本身，$1 ... $n 值为命令参数
# 例如：执行下面命令：./make.sh user，$0 的值为 ./make.sh，$1 的值为 user
# 下面的脚本意思是：
# 如果以 ./make.sh user 方式编译小系统，则将构建类型设置为 user，设置输出文件夹名称为 out_user 并
# 将其导入环境中，设置发布文件夹名称为 release_user，设置用户标志为 _user；
# 如果以 ./make.sh cts 方式编译小系统，则将构建类型设置为 cts，设置输出文件夹名称为 out_cts 并将
# 其导入环境中，设置发布文件夹名称为 release_user，设置用户标志为 _user_cts；
# 如果以 ./make.sh 方式编译小系统，则将构建类型设置为 debug 设置输出文件夹名称为 out 并将其导入环境
# 中，设置发布文件夹名称为 release，设置用户标志为空字符

if [ "$1" = "user" ];then
	BUILD_TYPE=user
	export OUT_DIR=out_user
	RELEASE_DIR=release_user
	USER_FLAG=_user
elif [ "$1" = "cts" ];then
	BUILD_TYPE=cts
	export OUT_DIR=out_cts
	RELEASE_DIR=release_user
	USER_FLAG=_user_cts
else
	BUILD_TYPE=debug
	export OUT_DIR=out
	RELEASE_DIR=release
	USER_FLAG=""
fi

# 下面是获取输出目录的完整路径（OUT)和小程序的根目录(TOP)
# 
# dirname 命令用于获取文件路径的目录路径部分
# 例如：有文件路径为 C:\Program Files\x86\Typora.exe, 使用如下命令：
# dirname "C:\Program Files\x86\Typora.exe" 后可以获取如下信息：
# C:\Program Files\x86\
# 
# $(pwd) 命令用于获取终端环境的目录，可在终端中执行如下命令以查看当前终端环境的目录：
# $ echo $PWD
#
# ${DIR/\./$(pwd)} 命令的意思是将 DIR 中的第一个 . 替换成 $(pwd)。
# 假如在 /home/qintuanye/workspace/zhaoge_mv300_2020/cmdc 目录下执行下面的
# 命令：./small/platform/build/make.sh
# 这样的话，DIR 的值为：./small/platform/build，$(pwd) 的值为 
# /home/qintuanye/workspace/zhaoge_mv300_2020/cmdc
# 因为需要将 $(pwd) 的值替换到 DIR 中的 .，因此最后得到的值为：
# /home/qintuanye/workspace/zhaoge_mv300_2020/cmdc/small/platform/build
#
# ". ${FULL_DIR}/color" 命令表示引入 ${FULL_DIR}/color 脚本，并执行该脚本。
# 意思是说执行这条命令后，在 color 脚本中定义的变量和函数，在当前脚本中都是可见的。
#
# ${FULL_DIR%%/build} 命令表示从 FULL_DIR 字符串中删除 /build 部分
#
# 下面以 ./small/platform/build/make.sh 方式执行脚本说明：
# DIR 的值为: ./small/platform/build
# $(pwd) 的值为：/home/qintuanye/workspace/zhaoge_mv300_2020/cmdc
# 因此 FULL_DIR 的值为：
# /home/qintuanye/workspace/zhaoge_mv300_2020/cmdc/small/platform/built
# OUT的值为：/home/qintuanye/workspace/zhaoge_mv300_2020/cmdc/small/platform
# TOP的值为：/home/qintuanye/workspace/zhaoge_mv300_2020/cmdc/small
#
### Get ${PATH} ###
DIR=$(dirname $0)
export FULL_DIR=${DIR/\./$(pwd)}
. ${FULL_DIR}/color
OUT=${FULL_DIR%%/build}
echo "out [${OUT}]"

TOP=${FULL_DIR%%/platform/build}
echo "top [${TOP}]"

# 判断如果构建类型是 user的话，发布目录名称是否是 release_user
#
# 从本脚本开头可以看到，如果编译类型是 user，那么发布目录应该是 release_user
# 
# 下面命令判断如果构建类型是 user，但是发布目录不存在的话，将会打印错误信息，
# 并退出编译
if [[ "${BUILD_TYPE}" = "user" && ! -d ${OUT}/${RELEASE_DIR} ]];then
	echo "Do not build user version!"
	exit 1
fi

# 设置编译文件和编译脚本文件变量
#
# 如果设置了工程名（PROJECT_NAME），则将编译文件和编译脚本文件变量设置为
# 对于工程的编译文件路径和编译脚本文件路径；否则，直接设置为 on-project/build
# 目录下相对应的文件路径
#
if [ ${PROJECT_NAME} ]
then
    echo "project:${PROJECT_NAME}"
    ON_PROJECT_PATH=${OUT}/on-project/${PROJECT_NAME}
    BUILD_ID_MK=${OUT}/on-project/${PROJECT_NAME}/build/build_id.mk
    BACKUP_IMG=${OUT}/on-project/${PROJECT_NAME}/pub/image/backup.ext4
    PROJECT_PRIV_SH=${OUT}/on-project/${PROJECT_NAME}/build/project_priv.sh
	PROJECT_PRIV_OTA_SH=${OUT}/on-project/${PROJECT_NAME}/build/project_priv_ota.sh
    BUILDINFO_RECOVERY=${OUT}/on-project/${PROJECT_NAME}/build/buildinfo_recovery.sh
    PROJECT_TELECOM_CA_SH=${OUT}/on-project/${PROJECT_NAME}/build/telecom_ca.sh
    PROJECT_VMX_CA_SH=${OUT}/on-project/${PROJECT_NAME}/build/vmx_ca.sh
    BOOTARGS_PATH=${OUT}/on-project/${PROJECT_NAME}/build/bootargs
    PROJECT_TOOLS=${OUT}/on-project/${PROJECT_NAME}/tools
    BUILD_PROJECT_NAME="-${PROJECT_NAME}"
	project_later=${OUT}/on-project/${PROJECT_NAME}/build/project_later.sh
else
    ##compatible with the old version
    ON_PROJECT_PATH=${OUT}/on-project
    BUILD_ID_MK=${OUT}/on-project/build/build_id.mk
    BACKUP_IMG=${OUT}/on-project/pub/image/backup.ext4
    PROJECT_PRIV_SH=${OUT}/on-project/build/project_priv.sh
    PROJECT_PRIV_OTA_SH=${OUT}/on-project/build/project_priv_ota.sh
    BUILDINFO_RECOVERY=${OUT}/on-project/build/buildinfo_recovery.sh
    PROJECT_TELECOM_CA_SH=${OUT}/on-project/build/telecom_ca.sh
    PROJECT_VMX_CA_SH=${OUT}/on-project/build/vmx_ca.sh
    BOOTARGS_PATH=${OUT}/on-project/build/bootargs
    PROJECT_TOOLS=${OUT}/on-project/tools
	project_later=${OUT}/on-project/build/project_later.sh
fi

# 如果设置了 CA_TYPE 变量的值，则设置 BUILD_CA_TYPE 的值为 "-${CA_TYPE}"
if [ ${CA_TYPE} ]
then
    echo "ca type:${CA_TYPE}"
    BUILD_CA_TYPE="-${CA_TYPE}" 
fi

# 判断 BUILD_ID_MK 对应的文件是否存在，如果不存在，则打印错误信息，并退出编译
if [ ! -f ${BUILD_ID_MK} ];
then
    echo "${BUILD_ID_MK}:No such file!"
    echo ">>>>>>>>>> exit <<<<<<<<<<"
    exit 1
fi

# 判断小系统目录下是否存在 configure 脚本，如果存在，则执行 configure build 命令，
# 然后判断命令执行返回码是否是 0，如果不是，说明 configure buidl 命令执行失败，
# 打印错误信息，并退出编译
if [ -f ${TOP}/platform/build-apk/configure ];then
	echo "goto config apk gradle...";
	${TOP}/platform/build-apk/configure build;
	if [ ! $? == 0 ];then
		echo "Load config apk gradle ERROR!";
		exit 1;
	fi
fi

# 引入 PartitionCreate.sh 和 Read.sh 环境，并执行里面的脚本，
# 引入的脚本环境一直存在从这里到本脚本结束
. ${FULL_DIR}/PartitionCreate.sh
. ${FULL_DIR}/Read.sh

# 判断 BOOTARGS_PATH 对应的脚本文件是否存在，如果存在则引入该脚本环境，
# 并执行该脚本；如果该脚本文件不存在，则执行默认的 bootargs 脚本
if [ -f ${BOOTARGS_PATH} ];then
    . ${BOOTARGS_PATH}
else
    . ${OUT}/on-project/build/bootargs
fi

Time=$(date +%Y%m%d%H%M%S)

### Get ${PATH} ###
# 获取芯片名称
#
# ls -l ${OUT}/${RELEASE_DIR}/boot |awk '/^d/ {print $NF}' 命令说明
# $NF 表示最后一项
# awk '/^d/ {print $NF}' 表示只打印 ls -l 输出信息中每行最后一项数据，
# 如果最后一项是数字则忽略掉（主要是为了去掉 ls -l 输出的第一行数据，该行数据是一个统计信息）
# 在我的工程中可以看到两项：Hi3798MV300 和 Hi3798MV300H
#
# ${chip_name_dir:0:8} 命令表示从chip_name_dir中截取第1个到第8个字符， 例如：
# 假如 chip_name_dir 的值为 Hi3798MV300，执行该命令后则是 Hi3798MV
#
# 下面是这段脚本的说明：
# 遍历 boot 文件夹下的文件或文件夹，如果文件夹下的文件或文件夹名称是 root，则从 BUILD_ID_MK 文件中
# 读取 CHIP_NAME 变量的值，并赋予 chip_name_array 变量，否则检查文件名称的前8个字符是否是 
# Hi3798MV，且存在以该名称命名的文件夹，且该文件夹下存在 root 文件夹和 uImage 文件，这时如果
# chip_name_array 的值为空，则将该文件名称设置给 chip_name_array；如果不为空，则将该文件名添加至
# 该变量值后面。如果这个检测失败，则打印错误信息，并退出编译
# 
# 如果遍历完 boot 目录后，chip_name_array 的值依然为空，则将其值设置为 Hi3798MV300
#
for chip_name_dir in $(ls -l ${OUT}/${RELEASE_DIR}/boot |awk '/^d/ {print $NF}')
do
    if [[ ${chip_name_dir} == "root" && -f ${OUT}/${RELEASE_DIR}/boot/uImage ]];then
        chip_name_array=$(Read_Array_Value ${BUILD_ID_MK} CHIP_NAME)
    else
        if [[ ${chip_name_dir:0:8} == "Hi3798MV" ]] && [ -d ${OUT}/${RELEASE_DIR}/boot/${chip_name_dir}/root ] && [ -f ${OUT}/${RELEASE_DIR}/boot/${chip_name_dir}/uImage ];then
            if [[ ${chip_name_array} == "" ]];then
                chip_name_array=${chip_name_dir}
            else
                chip_name_array=${chip_name_array}" "${chip_name_dir}
            fi
        else
            echo "boot directory is Failed!"
            exit 1
        fi
    fi
done
if [ "${chip_name_array}" == "" ]
then
	chip_name_array="Hi3798MV300"
fi
echo "chip_name_array:[${chip_name_array}]"
# 将芯片名字数组变量导入环境变量中
export CHIP_NAME_ARRAY=${chip_name_array}
# 将字符串转换成数组
chip_name_array=(${chip_name_array})
# 获取数组大小
chip_name_num=${#chip_name_array[@]}
# 从 BUILD_ID_MK 文件中读取 PROJECT_FLAG 变量的值，并将其赋值给 project_flat
project_flag=$(Read_Value ${BUILD_ID_MK} PROJECT_FLAG)
# 从 BUILD_ID_MK 文件中读取 BUILD_SUPPORT_UNITE 变量的值，将其赋值给 SUPPORT_UNITE
# 并导入环境变量中
export SUPPORT_UNITE=$(Read_Value ${BUILD_ID_MK} BUILD_SUPPORT_UNITE)
# 通过 project_flag 的值设置对应的 PUBLISH 和 TARGET 变量的值，并导入环境变量中
if [ ${project_flag} ]
then
    export PUBLISH=publish_${project_flag}
    export  TARGET=target_${project_flag}
else
    export PUBLISH=publish
    export TARGET=target
fi

# 从 BUILD_ID_MK 文件中读取 ROUTER_TYPE 变量值，并将其赋值给 router_type
# 根据 router_type 的值设置对应的 ROUTER值，并将其导入环境变量中
router_type=$(Read_Value ${BUILD_ID_MK} ROUTER_TYPE)
if [ ${router_type} ]
then
	ROUTER=router_${router_type}
else
	ROUTER=router
fi

# 将 PUBLISH_PATH 变量导入环境变量中
export PUBLISH_PATH=${OUT}/${OUT_DIR}/${PUBLISH}
echo "publish path: ${PUBLISH_PATH}"

# 删除旧文件目录，并创建需要的目录
### Create Output Directory ###
rm -rf ${PUBLISH_PATH}
rm -rf ${OUT}/${OUT_DIR}/obj
mkdir -p ${OUT}/${OUT_DIR}
mkdir -p ${OUT}/${OUT_DIR}/obj
mkdir -p ${OUT}/${OUT_DIR}/${TARGET}
mkdir -p ${PUBLISH_PATH}

# 从 BUILD_ID_MK 文件中读取 NAND_BLOCK 和 NAND_PAGE 的值，并将其赋值给
# Nand_Block 和 Nand_Page
Nand_Block=$(Read_Value ${BUILD_ID_MK} NAND_BLOCK)
Nand_Page=$(Read_Value ${BUILD_ID_MK} NAND_PAGE)
echo "Nand_Block = ${Nand_Block} ; Nand_Page = ${Nand_Page}"

# BootArgs 和 BaseAddress 在 small\platform\on-project\build\bootargs 脚本中定义，在上面有引入该脚本的命令
# 其值为：
# export BootArgs="mem=1G mmz=ddr,0,0,36M vmalloc=500M flashcache=10 quiet console=ttyAMA0,115200 blkdevparts=mmcblk0:"
# export BaseAddress="0x3E00000"
#
# =~ 运算符的意思是判断 "blkdevparts=mmcblk0:" 是否是 ${BootArgs} 的子类
#
if [[ ! ${BootArgs} =~ "blkdevparts=mmcblk0:" ]]
then
	BootArgs="${BootArgs}""blkdevparts=mmcblk0:"
fi
echo "bootargs : [${BootArgs}] "
echo "address : [${BaseAddress}] "

# 生成 uimages 相关文件
function uimages_creator()
{
	# 将参数1赋给 val_flash_type
	local val_flash_type=$1
	# 将参数2赋给 val_partinfo_name
	local val_partinfo_name=$2
	
	# 获取 val_partinfo_name 文件的绝对路径，并赋给 var_partinfo_conf
	local var_partinfo_conf=$(Get_Project_File ${OUT}/on-project/pub/swproduct/${val_partinfo_name})

	# 获取存放 uImage 的文件夹名称
    local var_uimages_path=uimages-${chip_name}-partinfo-${build_number}-${Time}
	local val_product_loader=""

	# 如果未设置 flash，则将其值设置为 emmc
	if [ "${val_flash_type}" == "" ];then
		val_flash_type="emmc"
	fi
	# 从 BUILD_ID_MK 指定的文件中读取 PRODUCT_LOADER 的值，并赋给 val_product_loader
	val_product_loader=$(Read_Value ${BUILD_ID_MK} PRODUCT_LOADER)
	
	# 如果 val_product_loader 的值为空，则打印提示信息，并结束该函数
	if [ "${val_product_loader}" == "" ];then
		echo "uimage: no product loader \"${val_product_loader}\""
		return
	fi

	# 根据芯片名称数组的大小设置 val_product_loader 的值
    if [ ${chip_name_num} -eq 1 ];then
        val_product_loader=${OUT}/on-project/pub/image${USER_FLAG}/${val_product_loader}
    else
        val_product_loader=${OUT}/on-project/pub/image${USER_FLAG}/${chip_name}/${val_product_loader}
    fi
    # 如果 val_product_loader 指定的文件不存在，则打印相关信息
	if [ ! -f ${val_product_loader} ];then
		echo "uimage: \"${val_product_loader}\" does not exists"
	fi
	# 创建 uimages 相关文件夹
	mkdir -p ${PUBLISH_PATH}/${var_uimages_path}/uimages_${val_flash_type}
	# 拷贝 val_product_loader 中指定的文件到 fastboot.bin 中
	cp -arf ${val_product_loader} ${PUBLISH_PATH}/${var_uimages_path}/fastboot.bin

	# 根据 Flash 类型， 通过调用 mkmiscimg 可执行文件生成 misc.img
	if [ "${val_flash_type}" == "nand" ];then
		${OUT}/build/tool/linux-x86/bin/mkmiscimg \
			--command "boot-recovery" \
			--recovery "recovery\n--on_product_upgrade\n" \
			--offset 8192 \
			${PUBLISH_PATH}/${var_uimages_path}/uimages_${val_flash_type}/misc.img
	else
		${OUT}/build/tool/linux-x86/bin/mkmiscimg \
			--command "boot-recovery" \
			--recovery "recovery\n--on_product_upgrade\n" \
			${PUBLISH_PATH}/${var_uimages_path}/uimages_${val_flash_type}/misc.img
	fi

	# 执行 uimage_generator.py 脚本生成 uImage
	${OUT}/build/tool/releasetools/uimage_generator.py \
		-s ${PUBLISH_PATH} \
		-d ${PUBLISH_PATH}/${var_uimages_path}/uimages_${val_flash_type} \
		-p ${var_partinfo_conf}

	# 如果存在 factory 目录，则执行下面语句
    if [ -d ${PUBLISH_PATH}/factory ];then
        echo "OTA_Full_Package_zip:${OTA_Full_Package_zip##*/}"
        # 使用 FileName=${OTA_Full_Package_zip##*/} 替换掉 config.ini
        # 文件中的 FileName=.*
        sed -i "s/FileName=.*/FileName=${OTA_Full_Package_zip##*/}/g" ${PUBLISH_PATH}/factory/config.ini
        # 拷贝文件
        cp -arf ${PUBLISH_PATH}/factory ${PUBLISH_PATH}/${var_uimages_path}/
		cp ${OTA_Full_Package_zip} ${PUBLISH_PATH}/${var_uimages_path}/factory
		cp -r ${PUBLISH_PATH}/product/sw_product_check  ${PUBLISH_PATH}/${var_uimages_path}

    fi
	
	# 切换目录到 ${PUBLISH_PATH}/${var_uimages_path}
    pushd ${PUBLISH_PATH}/${var_uimages_path}
    # 将该目录下的内容压缩成压缩包
    zip -r ${PUBLISH_PATH}/${var_uimages_path}.zip *
    # 恢复原先目录
    popd

	# 删除 var_uimages_path 对应的目录
    rm -rf ${PUBLISH_PATH}/${var_uimages_path}

}

# 该函数未使用
function get_image_name()
{
	if [[ "$1" == "" || "$2" == "" || ! -f $2 ]];then
		echo ""
		return
	fi
	local var_name=$1
	local var_conf=$2
	local part_name=""
	local partition=""

	while read line
	do
		part_name=$(echo ${line} | dos2unix | awk '{print $1}')
		if [ "${part_name}" == "${var_name}" ];then
			partition=$(echo ${line} | awk '{print $5}' | dos2unix)
			if [ "${partition}" == "0" ] || [ "${partition}" == "1" ];then
				partition=$(echo ${line} | awk '{print $6}' | dos2unix)
			fi
			break
		fi
	done < ${var_conf}
	echo "${partition}"
}

# 这个函数是在遍历编译芯片时调用的
function copy_project_file()
{
	red "Create boot's Directory"
	# 在压缩根目录下创建 /BOOT/${chip_name} 目录，当只有一个芯片时，${chip_name}为空
	mkdir -p ${zip_root}/BOOT/${chip_name}
	green "Copy boot's Files"
	# 从发布目录中对应目录下拷贝所有文件到压缩目录下对应的目录中
	cp -arf ${OUT}/${RELEASE_DIR}/boot/${chip_name}/root ${zip_root}/BOOT/${chip_name}/RAMDISK
	# 如果 root_dir.txt 文件存在，则根据文件中的数据在指定的目录下创建对应的目录
	if [ -f ${OUT}/${RELEASE_DIR}/boot/${chip_name}/root_dir.txt ];then
		while read LINE;do
			mkdir -p ${zip_root}/BOOT/${chip_name}/RAMDISK/$LINE
		done < ${OUT}/${RELEASE_DIR}/boot/${chip_name}/root_dir.txt
	else
		red "No boot root_dir.txt"
	fi
	blue "Copy boot's kernel"
	# 获取 uImage 文件的真实路径
	uImage_file=$(Get_Project_File ${TOP}/platform/on-project/pub/boot/${chip_name}/uImage)
	# 如果 uImage 文件不存在，则使用 ${OUT}/${RELEASE_DIR}/boot/${chip_name}/uImage
	if [ ! -f ${uImage_file} ];then
		uImage_file=${OUT}/${RELEASE_DIR}/boot/${chip_name}/uImage
	fi
	blue "Copy boot's kernel \"${uImage_file}\""
	# 拷贝 uImage 文件到压缩目录下的指定文件夹中
	# cp -arf 解析：
	# -a 保留链接和文件属性，递归拷贝目录
	# -r 若源文件是一目录文件，此时cp将递归复制该目录下所有的子目录和文件。
	# -f 删除已经存在目标文件而不提示。
	cp -arf ${uImage_file} ${zip_root}/BOOT/${chip_name}/kernel
    echo

	# 开始拷贝恢复文件
	red "Create recovery's Directory"
	# 创建芯片名目录
	mkdir -p ${zip_root}/RECOVERY/${chip_name}
	green "Copy recovery's Files"
	# 拷贝发布目录下的 root 目录到压缩目录中 RAMDISK 目录中
	cp -arf ${OUT}/${RELEASE_DIR}/recovery/${chip_name}/root ${zip_root}/RECOVERY/${chip_name}/RAMDISK
	# 根据 root_dir.txt 中的内容在相对应的目录中创建目录
	if [ -f ${OUT}/${RELEASE_DIR}/recovery/${chip_name}/root_dir.txt ];then
		while read LINE;do
			mkdir -p ${zip_root}/RECOVERY/${chip_name}/RAMDISK/$LINE
		done < ${OUT}/${RELEASE_DIR}/recovery/${chip_name}/root_dir.txt
	else
		red "No recovery root_dir.txt"
	fi
	blue "Copy recovery's kernel"
	# 拷贝 uImage 文件到恢复目录中
    cp -arf ${OUT}/${RELEASE_DIR}/boot/${chip_name}/uImage ${zip_root}/RECOVERY/${chip_name}/kernel

	# 如果芯片数量为0的话，则执行下面语句
    if [ ${make_num} -eq 0 ];then
        echo
        cyan "### target SYSTEM ###"
        magenta "---------------------"
        red "Copy system's Files"
        # 拷贝发布目录下的 system 目录到压缩目录中的 SYSTEM 目录
        cp -arf ${OUT}/${RELEASE_DIR}/system ${zip_root}/SYSTEM
        echo

        cyan "### Project Files ###"
        magenta "---------------------"
        red "Copy Project apk's Files"
        # 如果 configure 文件存在，则判断 apk/system 目录是否存在，如果存在则拷贝
        # 里面的内容到压缩目录下的 SYSTEM 目录中；否则判断 apk 目录是否存在，如果存在，
        # 则将其内容拷贝到压缩目录下 SYSTEM/app 目录中
        if [ -f ${TOP}/platform/build-apk/configure ];then
            if [ -d "${TOP}/apk/system/" ];then
                cp -arf ${TOP}/apk/system/* ${zip_root}/SYSTEM/
            fi
        else
            if [ -d "${TOP}/apk/" ];then
                cp -arf ${TOP}/apk/* ${zip_root}/SYSTEM/app
            fi
        fi
        echo

		# 执行 create_board_configure 函数，创建主板配置文件
        create_board_configure

        cyan "### target images ###"
        magenta "---------------------"
        red "Copy images's Files"
        # 拷贝发布目录下 images 目录中的内容到 PUBLISH_PATH目录中
        cp -arf ${OUT}/${RELEASE_DIR}/images/* ${PUBLISH_PATH}/

		# 拷贝工具文件
        magenta "---------------------"
        red "Copy tools's Files"
        # 如果工程工具文件夹下存在 factory 目录，则拷贝其至 PUBLISH_PATH 目录中
        [ -d ${PROJECT_TOOLS}/factory ] && cp -arf ${PROJECT_TOOLS}/factory ${PUBLISH_PATH}/
        # 如果工程工具文件夹下存在 product 目录，则拷贝其至 PUBLISH_PATH 目录中
        [ -d ${PROJECT_TOOLS}/product ] && cp -arf ${PROJECT_TOOLS}/product ${PUBLISH_PATH}/
    fi

	# 如果芯片名称为 Hi3798MV300H，且存在 modules_Hi3798MV300H 目录，则拷贝
	# modules_Hi3798MV300H 目录到压缩目录下的 modules_Hi3798MV310 目录中
    if [[ ${chip_name} == "Hi3798MV300H" && -d ${OUT}/${RELEASE_DIR}/system/lib/modules_Hi3798MV300H ]];then
        red "Copy mv310's modules Files"
        cp -arf ${OUT}/${RELEASE_DIR}/system/lib/modules_Hi3798MV300H ${zip_root}/SYSTEM/lib/modules_Hi3798MV310
    fi

	# 执行 project_priv.sh 脚本
    magenta "---------------------"
    red "Call project_priv.sh "
    # 如果 PROJECT_PRIV_SH 指定的脚本文件存在，则执行该脚本；否则执行默认的
    # project_priv.sh 脚本
    if [ -f ${PROJECT_PRIV_SH} ]
    then
        . ${PROJECT_PRIV_SH} ${TOP} ${build_number} ${BUILD_TYPE} ${project_tag}
    else
        . ${OUT}/on-project/build/project_priv.sh ${TOP} ${build_number} ${BUILD_TYPE} ${project_tag}

    fi
    echo

	# 拷贝 sw_para.txt 到压缩文件夹中的 SYSTEM/etc 目录下
    red "cp sw_para.txt to system/etc "
    cp -arf ${ON_PROJECT_PATH}/pub/recovery/root/etc/sw_para.txt ${zip_root}/SYSTEM/etc/ 

	# 生成 system/build.prop 文件
    magenta "---------------------"
    red "Generate system/build.prop"
    # 如果 build_prop.sh 文件存在，则使用该脚本生成 build.prop 文件；
    # 否则执行 build.sh 脚本来生成 build.prop 文件
    if [ -f ${TOP}/platform/on-project/build/build_prop.sh ];then
        bash ${TOP}/platform/on-project/build/build_prop.sh ${zip_root}/SYSTEM/build.prop ${BUILD_TYPE}
    else
        bash ${TOP}/platform/on-project/build/build.sh ${BUILD_TYPE}> ${zip_root}/SYSTEM/build.prop
    fi
    echo
	
	red "Create fastboot's Directory"
	# 从 BUILD_ID_MK 文件中读取 LOADER 的值，并将其赋予 loader_file 变量
    loader_file=$(Read_Value ${BUILD_ID_MK} LOADER)
    # 如果 loader_file 的值不为空，则执行下面的语句
    if [[  ${loader_file} != '' ]];then
    	# 获取真实 loader_file 的文件路径
        loader_file=$(Get_Project_File ${OUT}/on-project/pub/image${USER_FLAG}/${chip_name}/${loader_file})
        # 如果 loader_file 对应的文件不存在，则将其值替换为 loader.bin 文件路径
        if [ ! -f ${loader_file} ];then
            loader_file=$(Get_Project_File ${OUT}/on-project/pub/image${USER_FLAG}/${chip_name}/loader.bin)
        fi
        # 如果 loader_file 对应的文件存在，则
        # 判断芯片是否为空，如果芯片名为空，则将 loader_file 拷贝到 
        # PUBLISH_PATH 目录下，否则将 loader_file 拷贝到对应芯片目录中
        # 否则将 loader_file 置为空
        if [ -f ${loader_file} ];then
            if [ ${chip_name} == "" ];then
                cp -arf ${loader_file} ${PUBLISH_PATH}/loader.bin
            else
                cp -arf ${loader_file} ${PUBLISH_PATH}/loader_${chip_name}.bin
            fi
        else
            loader_file=''
        fi
    fi
    # 如果 loader_file 的值为空，则执行下面的语句
    if [[  ${loader_file} == '' ]];then
    	# 如果 PUBLISH_PATH 目录下存在 loader.bin 文件，且芯片数量为 1时，只打印相关信息；
    	# 否则判断在 PUBLISH_PATH 目录下对应芯片名称的文件夹中是否存在 loader.bin 文件，
    	# 如果 loader.bin 文件存在，则将其拷贝到 PUBLISH_PATH 目录下的
        # loader_${chip_name}.bin
        # 如果对应芯片名称目录下没有 loader.bin 文件，则打印错误信息，并退出编译
        if [ -f ${PUBLISH_PATH}/loader.bin ] && [ ${chip_name_num} -eq 1 ];then
            echo " loader.bin have been!"
        else
            if [ -f ${PUBLISH_PATH}/${chip_name}/loader.bin ];then
                cp -arf ${PUBLISH_PATH}/${chip_name}/loader.bin ${PUBLISH_PATH}/loader_${chip_name}.bin
            else
                echo " loader.bin is not exist ,can't update "
                exit 1
            fi
        fi
    fi

	red "Copy pqparam.bin"
	# 如果 pq_param.bin 文件不存在，则执行下面语句
    if [ ! -f ${PUBLISH_PATH}/pq_param.bin ];then
    	# 如果芯片名对应目录下存在 pq_param.bin 文件，则将其拷贝到
    	# PUBLISH_PATH 下的 pq_param_${chip_name}.bin 文件中，
    	# 否则，打印错写信息，并停止编译
        if [ -f ${PUBLISH_PATH}/${chip_name}/pq_param.bin ];then
            cp -arf ${PUBLISH_PATH}/${chip_name}/pq_param.bin ${PUBLISH_PATH}/pq_param_${chip_name}.bin
        else
            echo "pqparam.bin is no exit "
            exit 1
        fi
    fi
}

# 创建主板配置文件
function create_board_configure()
{
	magenta "---------------------"
	red "Create Configure XML File"
	# 获取主板配置文件目录
    BOARD_DIRECTORY="${TOP}/platform/on-project/${PROJECT_NAME}/pub/image/"
    # 在主板配置文件目录中搜索主板配置文件，如果搜索结果为空，
    # 则将主板配置文件目录设置为 ${TOP}/platform/on-project/pub/image/
    # -z 用于判断字符串是否为空，如果为空，返回真
    if [ -z $(find $BOARD_DIRECTORY -name 'board*.xml') ]
    then
        BOARD_DIRECTORY="${TOP}/platform/on-project/pub/image/"
    fi
    # 遍历主板配置文件夹下的文件
    for filename in $(ls ${BOARD_DIRECTORY} )
    do   
    	# 如果文件名为 gpio.xml，则执行下面语句
        if [[ ${filename} == "gpio.xml" ]]
        then  
            green $filename
            # 获取当前工程下的 gpio.xml 文件的绝对路径
            GPIO_FILE_PATH=${TOP}/platform/on-project/${PROJECT_NAME}/pub/image/$filename
            # 如果 gpio.xml 文件不存在，则将默认的 gpio.xml 文件绝对路径赋予
            # GPIO_FILE_PATH 变量
            if [ ! -f ${GPIO_FILE_PATH} ]
            then 
                GPIO_FILE_PATH=${TOP}/platform/on-project/pub/image/$filename
            fi   
        fi   

		# 如果文件名为 board*.xml，则执行下面语句
        if [[ ${filename} == board*.xml ]]
        then  
            green $filename
            # 获取当前工程目录下的 board*.xml 文件的绝对路径
            BOARD_FILE_PATH=${TOP}/platform/on-project/${PROJECT_NAME}/pub/image/$filename
            # 如果 board*.xml 文件不存在，则将默认的 board*.xml 文件绝对路径赋予
            # BOARD_FILE_PATH 变量
            if [ ! -f ${BOARD_FILE_PATH} ]
            then 
                BOARD_FILE_PATH=${TOP}/platform/on-project/pub/image/$filename
            fi   
            # 设置 BOARD_CFG_NAME 变量值为 board*.cfg
            BOARD_CFG_NAME=${filename%%.xml}".cfg"
        fi

		# 如果文件名称是 devinfo.xml，则执行下面语句
        if [[ ${filename} == "devinfo.xml" ]]
        then
            green $filename
            # 获取当前工程下 devinfo.xml 的绝对路径
            DEVINFO_FILE_PATH=${TOP}/platform/on-project/${PROJECT_NAME}/pub/image/$filename
            # 如果 devinfo.xml 文件不存在，则将 默认的 devinfo.xml 文件绝对路径赋予
            # DEVINFO_FILE_PATH 变量
            if [ ! -f ${DEVINFO_FILE_PATH} ]
            then
                DEVINFO_FILE_PATH=${TOP}/platform/on-project/pub/image/$filename
            fi
        fi
    done
    # 如果 BOARD_FILE_PATH 和 GPIO_FILE_PATH 文件都存在，则执行下面语句
    if [[ -f ${BOARD_FILE_PATH} && -f ${GPIO_FILE_PATH} ]]
    then
        red "### Create ${BOARD_CFG_NAME} ###"
        # 执行 swmkboardcfg 可执行文件，生成 board*.cfg 文件
        ${TOP}/platform/build/tool/linux-x86/bin/swmkboardcfg ${BOARD_FILE_PATH} ${GPIO_FILE_PATH} -o ${zip_root}/SYSTEM/etc/${BOARD_CFG_NAME}
    fi
    # 如果 DEVINFO_FILE_PATH 和 GPIO_FILE_PATH 文件都存在，则执行下面语句
    if [[ -f ${DEVINFO_FILE_PATH} && -f ${GPIO_FILE_PATH} ]]
    then
        red "### make deviceinfo.img ###"
        # 执行 swmkdevinfo 可执行文件，生成 deviceinfo.img 文件
        ${TOP}/platform/build/tool/linux-x86/bin/swmkdevinfo ${DEVINFO_FILE_PATH} ${GPIO_FILE_PATH} -o ${PUBLISH_PATH}/deviceinfo.img -full
        # 执行 swmkdevinfo 可执行文件，生成 devinfo_patch.img 文件
        ${TOP}/platform/build/tool/linux-x86/bin/swmkdevinfo ${DEVINFO_FILE_PATH} ${GPIO_FILE_PATH} -o ${PUBLISH_PATH}/devinfo_patch.img -patch
    fi
    green "Create Configure XML File End"
	magenta "-------------------"
}

# 编译 bootimg
function make_bootimg()
{
	cyan "### target BOOT ###"
	magenta "-------------------"


	green "Copy on-project boot's Files"
	# 拷贝 on-project 目录下 boot 相关文件
	# 该函数是由 PROJECT_PRIV_SH 指定的脚本文件引入的
    Copy_Project_Boot_Files

    red "boot's address"
    # 将 BaseAddress 的值写入 base 文件中
    echo ${BaseAddress} > ${zip_root}/BOOT/${chip_name}/base
	green "boot's cmdline"
	# 将 BootArgs 的值写入 cmdline 文件中
	echo ${BootArgs} > ${zip_root}/BOOT/${chip_name}/cmdline

    #=================================================
    #sunniwell 内核实现的system分区文件hash值校验，不般不使用
    # 从 BUILD_ID_MK 指定的文件中读取 SYSTEM_VERIFY 的值，并赋予 system_verify 变量
	system_verify=$(Read_Value ${BUILD_ID_MK} SYSTEM_VERIFY)
    green "system verify: ${system_verify}"
    # 如果 system_verify 的值为 y， 则执行下面语句
	if [[ ${system_verify} == "y" ]]
	then
		magenta "---------------------"
		# 切换目录到 zip_root
		# pushd 命令常用于将目录加入到栈中，加入记录到目录栈顶部，并切换到该目录；
		# 若pushd命令不加任何参数，则会将位于记录栈最上面的2个目录对换位置
		pushd ${zip_root}
		# 计算 SYSTEM 目录中所有文件的 sha1sum 值，并将其输出到 system_list 文件中
		find  ./SYSTEM -type f  -print | xargs sha1sum  > ${zip_root}/BOOT/${chip_name}/RAMDISK/system_list
		# 将字符串 .\/SYSTEM 替换成 /system
		# -i 表示直接对文件进行修改
		sed -i 's/.\/SYSTEM/\/system/' ${zip_root}/BOOT/${chip_name}/RAMDISK/system_list
		# 恢复原先目录
		# popd 命令用于删除目录栈中的记录；如果popd命令不加任何参数，
		# 则会先删除目录栈最上面的记录，然后切换到删除过后的目录栈中的最上面的目录
		popd
		# 将字符串 service system_verify /sbin/system_verify 写入 init.rc 文件中
		echo "service system_verify /sbin/system_verify" >> ${zip_root}/BOOT/${chip_name}/RAMDISK/init.rc
		# 将字符串 "    class main" 写入到 init.rc 文件中
		echo "    class main" >> ${zip_root}/BOOT/${chip_name}/RAMDISK/init.rc
		# 将字符串 "    oneshot" 写入到 init.rc 文件中
		echo "    oneshot" >> ${zip_root}/BOOT/${chip_name}/RAMDISK/init.rc
	fi

    #====================海思L2方案system分区文件hash值校验================
    #system_check为init进程内建命令，读取/system/etc/system_list文件，先校验system_list文件签名，再校验/system中文件hash值，不通过重启
    # 从 BUILD_ID_MK 指定文件中读取 TELECOM_CA_SYSTEM_VERIFY 的值，
    # 并赋予 system_verify_hisi 变量
    system_verify_hisi=$(Read_Value ${BUILD_ID_MK} TELECOM_CA_SYSTEM_VERIFY)
    green "system_verify_hisi: ${system_verify_hisi}"
    # 如果 system_verify_hisi 的值为 y，则执行下面的语句
    if [[ ${system_verify_hisi} == "y" ]]
    then
        echo "enable L2 system check !"
        # 将字符串 on boot 写入 init.rc 文件中
        echo "on boot" >> ${zip_root}/BOOT/${chip_name}/RAMDISK/init.rc
        # 将字符串 "   system_check" 写入 init.rc 文件中
        echo "   system_check" >> ${zip_root}/BOOT/${chip_name}/RAMDISK/init.rc
    fi

	# 根据芯片名称设置 BOOT_RAMDISK_FILE 变量的值
    if [[ ${chip_name} == "" ]];then
        BOOT_RAMDISK_FILE=${OUT}/${OUT_DIR}/obj/ramdisk_for_boot.img
    else
        BOOT_RAMDISK_FILE=${OUT}/${OUT_DIR}/obj/ramdisk_for_boot_${chip_name}.img
    fi

	cyan "### Create boot.img -> publish Directory ###"
	red "### Create ramdisk.img for boot.img ###"
	# 执行 mkbootfs 和 minigzip 可执行文件，生成 ramdisk_for_boot*.img 文件
	${OUT}/build/tool/linux-x86/bin/mkbootfs \
		${OUT}/${OUT_DIR}/${TARGET}/${target_name}/BOOT/${chip_name}/RAMDISK | \
		${OUT}/build/tool/linux-x86/bin/minigzip > ${BOOT_RAMDISK_FILE}

    #------------------------------------------------
	###
	### make boot.img
	###
	# 开始编译 boot.img
	# 如果 telecom_ca 和 security_l3 的值都是 y，则执行下面语句，
	# 否则直接调用 mkbootimg 可执行文件生成 boot.img
    if [[ ${telecom_ca} == "y" && ${security_l3} == "y" ]];then
        cyan "### copy security boot.img ###"
        magenta "-------------------"
        # 如果 security 目录下存在 boot.img，则执行下面的命令；
        # 否则打印错误信息，并退出编译
        if [ -f "${ON_PROJECT_PATH}/pub/image${USER_FLAG}/security/${chip_name}/boot.img" ];then
            #img_magic:this is boot.img is magic = " 41 4e 44 52 4f 49 44 21 ANDROID!"
            #           img_magic can't change
            #boot_jump_sign is jump the 8196(0x2000) bytes of the signature
            # 读取下面两个文件的内容，并将其赋予对应的变量
            # od 命令会读取所给予的文件的内容，并将其内容以八进制字码呈现出来。
            # -An 指定地址基数，以何种方式显示地址,其中n表示不打印位移值
            # -tx1 指定数据的显示格式，其中x表示十六进制数，其中1表示使用一个字节作为最小单位
            # -v 输出时不省略重复的数据
            # -j0 略过设置的字符数目
            # -N16 到设置的字符数目为止
            img_magic=$(od -An -tx1 -v -j0 -N16 ${ON_PROJECT_PATH}/pub/image${USER_FLAG}/${chip_name}/boot.img)
            boot_jump_sign=$(od -An -tx1 -v -j8192 -N16 ${ON_PROJECT_PATH}/pub/image${USER_FLAG}/security/${chip_name}/boot.img)
            # 如果这两变量中的值相等，则将 security 目录中的 boot.img 文件拷到
            # BOOT_FILE 指定的文件中；否则，打印错误信息并退出编译
            if [ "${boot_jump_sign}" == "${img_magic}" ];then
                red "Success: have signature boot.img"
                cp ${ON_PROJECT_PATH}/pub/image${USER_FLAG}/security/${chip_name}/boot.img ${BOOT_FILE}
            else
                red "Failed: don't signature boot.img"
                exit 1
            fi
        else
            red "Failed: don't have boot.img"
            exit 1
        fi
    else
        green "### Create for boot.img ###"
        # 执行 mkbootimg 可执行文件生成 boot.img 文件
        ${OUT}/build/tool/linux-x86/bin/mkbootimg \
            --kernel ${OUT}/${OUT_DIR}/${TARGET}/${target_name}/BOOT/${chip_name}/kernel \
            --ramdisk ${BOOT_RAMDISK_FILE} \
            --cmdline "${BootArgs}" \
            --base "${BaseAddress}" \
            --output ${BOOT_FILE}
    fi
	magenta "--------------------------------------"
}

# 编译恢复镜像文件
function make_recoveryimg()
{
	cyan "### target RECOVERY ###"
	magenta "-----------------------"
	
	# 拷贝 recovery.emmc.fstab 文件到压缩目录对应的目录中
    cp -arf ${zip_root}/RECOVERY/${chip_name}/RAMDISK/etc/recovery.emmc.fstab ${zip_root}/RECOVERY/${chip_name}/RAMDISK/etc/recovery.fstab
    # 如果压缩目录中不存在 etc 目录，则创建它
    [ ! -d ${zip_root}/RECOVERY/RAMDISK/etc ] && mkdir -p ${zip_root}/RECOVERY/RAMDISK/etc
    # 拷贝压缩目录中芯片名称对应的 etc 目录中内容到通用 etc 目录下
    cp -arf ${zip_root}/RECOVERY/${chip_name}/RAMDISK/etc/* ${zip_root}/RECOVERY/RAMDISK/etc
    # 拷贝 BOARD_CFG_NAME 文件
    cp -arf ${zip_root}/SYSTEM/etc/$BOARD_CFG_NAME ${zip_root}/RECOVERY/${chip_name}/RAMDISK/etc

	green "Copy on-project recovery's Files"
	# 拷贝工程中与恢复镜像的文件
	# 该函数是由 PROJECT_PRIV_SH 引入的
    Copy_Project_Recovery_Files

	red "Copy recovery's address"
	# 将 BaseAddress 的值写入 base 文件中
	echo ${BaseAddress} > ${zip_root}/RECOVERY/${chip_name}/base
	green "Copy recovery's cmdline"
	# 将 BootArgs 的值写入 cmdline 文件中
	echo ${BootArgs} > ${zip_root}/RECOVERY/${chip_name}/cmdline

	cyan "### Copy partition table to recovery ###"
	# 获取分区配置目录绝对路径
    partition_directory=${zip_root}/RECOVERY/${chip_name}/RAMDISK/swpartition/
    # 创建分区配置目录
    mkdir -p ${partition_directory}
    # 从 BUILD_ID_MK 指定文件中读取 PARTINFO_ARRAY 的值，并赋予 PARTINFO_ARRAY
	PARTINFO_ARRAY=$(Read_Array_Value ${BUILD_ID_MK} PARTINFO_ARRAY)
	# 如果 PARTINFO_ARRAY 的值为空，则直接将其值设置为 partinfo.conf
    if [ "${PARTINFO_ARRAY}" == "" ]
    then
		PARTINFO_ARRAY="partinfo.conf"
	fi
	# 遍历分区信息文件数组
	for partition_name in ${PARTINFO_ARRAY}
	do
		# 获取分区信息文件的绝对路径
		PARTINFO_CONF=$(Get_Project_File ${OUT}/on-project/pub/swproduct/${partition_name})
		green "copy \"${PARTINFO_CONF}\" to \"${partition_directory}\""
		# 拷贝分区信息文件到分区配置目录中
		cp -arf ${PARTINFO_CONF} ${partition_directory}
	done

    red "Generate RECOVERY/RAMDISK/default.prop "
    # 如果 build_prop.sh 文件存在，则使用该脚本生成 default.prop 文件，
    # 否则，执行 BUILDINFO_RECOVERY 指定的脚本文件生成 default.prop
	if [ -f ${TOP}/platform/on-project/build/build_prop.sh ];then
		bash ${TOP}/platform/on-project/build/build_prop.sh ${zip_root}/RECOVERY/${chip_name}/RAMDISK/default.prop ${BUILD_TYPE}
	else

        bash ${BUILDINFO_RECOVERY} ${BUILD_TYPE}> ${zip_root}/RECOVERY/${chip_name}/RAMDISK/default.prop
	fi

	# 根据芯片名称设置 RECOVERY_RAMDISK_FILE 变量的值
    if [[ ${chip_name} == "" ]];then
        RECOVERY_RAMDISK_FILE=${OUT}/${OUT_DIR}/obj/ramdisk_for_recovery.img
    else
        RECOVERY_RAMDISK_FILE=${OUT}/${OUT_DIR}/obj/ramdisk_for_recovery_${chip_name}.img
    fi

	cyan "### Create recovery.img -> publish Directory ###"
	magenta "--------------------------------------"
	red "### Create ramdisk.img for recovery.img ###"
	# 执行 mkbootfs 可执行文件生成 ramdisk_for_recovery*.img
	${OUT}/build/tool/linux-x86/bin/mkbootfs \
		${OUT}/${OUT_DIR}/${TARGET}/${target_name}/RECOVERY/${chip_name}/RAMDISK | \
		${OUT}/build/tool/linux-x86/bin/minigzip > ${RECOVERY_RAMDISK_FILE}

    #------------------------------------------------
	###
	### make recovery.img
	###
	# 如果 telecom_ca 和 security_l3 的值为 y，则执行下面语句
	# 否则，直接执行 mkbootimg 可执行文件生成 recovery.img
    if [[ ${telecom_ca} == "y" && ${security_l3} == "y" ]];then
        cyan "### copy security recovery.img ###"
        magenta "-------------------"
        # 如果 recovery.img 文件已经存在，则执行下面语句，
        # 否则打印错误信息，并停止编译
        if [ -f "${ON_PROJECT_PATH}/pub/image${USER_FLAG}/security/${chip_name}/recovery.img" ];then
            #img_magic:this is recovery.img is magic = " 41 4e 44 52 4f 49 44 21 ANDROID!"
            #           img_magic can't change
            #recovery_jump_sign is jump the 8196(0x2000) bytes of the signature
            # 读取下面两个 recovery.img 文件的部分内容，并将其赋予变量
            img_magic=$(od -An -tx1 -v -j0 -N16 ${ON_PROJECT_PATH}/pub/image${USER_FLAG}/${chip_name}/recovery.img)
            recovery_jump_sign=$(od -An -tx1 -v -j8192 -N16 ${ON_PROJECT_PATH}/pub/image${USER_FLAG}/security/${chip_name}/recovery.img)
            # 判断上面两个变量的内容是否一致，如果一致，则拷贝 recovery.img，
            # 否则，打印错误信息并停止编译
            if [ "${recovery_jump_sign}" == "${img_magic}" ];then
                red "Success: have signature recovery.img"
                cp ${ON_PROJECT_PATH}/pub/image${USER_FLAG}/security/${chip_name}/recovery.img ${RECOVERY_FILE}
            else
                red "Failed: don't signature ecovery.img"
                exit 1
            fi
        else
            red "Failed: don't have recovery.img"
            exit 1
        fi
    else
        green "### Create for recovery.img ###"
        ${OUT}/build/tool/linux-x86/bin/mkbootimg \
            --kernel ${OUT}/${OUT_DIR}/${TARGET}/${target_name}/RECOVERY/${chip_name}/kernel \
            --ramdisk ${RECOVERY_RAMDISK_FILE} \
            --cmdline "${BootArgs}" \
            --base "${BaseAddress}" \
            --output ${RECOVERY_FILE}
    fi
	magenta "--------------------------------------"
}

# 编译 logoimg
function make_logoimg()
{
	magenta "---------------------"
    cyan "### Create for logo.img ###"
    if [ -f ${PUBLISH_PATH}/logo.img ];then
    	# logo.img 文件已经存在，无需编译
        red "logo.img have been !!"
    else
    	# 获取 logo.jpg 文件的绝对路径，并赋予 LOGO_PATH
        LOGO_PATH=${TOP}/platform/on-project/${PROJECT_NAME}/pub/image/logo.jpg
        # 如果 LOGO_PATH 文件不存在，则设置 LOGO_PATH 为另外一个 logo.jpg 文件的绝对路径
        if [ ! -f ${LOGO_PATH} ];
        then
            LOGO_PATH=${TOP}/platform/on-project/pub/image/logo.jpg
        fi
        green "logo.jpg path:${LOGO_PATH}"
        # 执行 swMakeLogo 可执行文件生成 logo.img
        ${TOP}/platform/build/tool/linux-x86/bin/swMakeLogo ${LOGO_PATH} ${PUBLISH_PATH}/logo.img
    fi
	magenta "---------------------"
}

# 在执行 make_ota_package 函数时，当 build_id.mk 
# 文件中的 VMX_ADV_CA 为 y 时执行该函数
function call_vmx_ca()
{
    magenta "---------------------"
    # 从 BUILD_ID_MK 指定文件中读取 BUILD_VMX_SIGN 和 BUILD_SUB_NUMBER 的值
    # 并将其赋给对应的变量
    vmx_sign=$(Read_Value ${BUILD_ID_MK} BUILD_VMX_SIGN)
    sub_num=$(Read_Value ${BUILD_ID_MK} BUILD_SUB_NUMBER)
    # 根据 vmx_sign 的值，给 build_sign_type 和 build_sign_flag 设置对应的值
    if [ ${vmx_sign} == "y" ];then
        build_sign_type="vmx_signed_mode1"
        build_sign_flag="-vmx_sign_${sub_num}"
    else
        build_sign_type="dummy_signed"
        build_sign_flag="-dummy_sign_${sub_num}"
    fi
    #delete zip
    # 如果压缩包存在，则删除它
    if [ -f ${zip_root}.zip ]; then
        rm -rf ${zip_root}.zip
    fi

	# 如果 PROJECT_VMX_CA_SH 指定的脚本文件存在，则执行它
    if [ -f ${PROJECT_VMX_CA_SH} ]
    then
        red "Call vmx_ca.sh "
        # 从 BUILD_ID_MK 指定文件中读取 VMX_ADV_CA_SHATABLE 的值，
        # 并赋给 vmx_advca_shatable
        vmx_advca_shatable=$(Read_Value ${BUILD_ID_MK} VMX_ADV_CA_SHATABLE)
        # 执行 PROJECT_VMX_CA_SH 指定的脚本
        bash ${PROJECT_VMX_CA_SH} ${OUT} ${BUILD_TYPE} ${zip_root} ${build_sign_type} ${vmx_advca_shatable}
    fi
    vmx_ca_flag="--vmx_ca"
    # 创建 BOOTCA 文件夹
    mkdir -p ${zip_root}/BOOTCA
    # 如果 *_boot.img 文件存在，则拷贝它；否则打印相关信息
    if [[ -f ${PUBLISH_PATH}/${build_sign_type}_boot.img ]]
    then
        cp -arf ${PUBLISH_PATH}/${build_sign_type}_boot.img ${zip_root}/BOOTCA/boot.img
    else
        echo ${PUBLISH_PATH}/${build_sign_type}"_boot.img is not exit ,can't cp"
    fi
    echo
}

# 在编译 recovery.img 后，如果 telecom_ca == y 且 security_l3 !=  r 时调用该函数
function call_telecom_ca()
{
    magenta "---------------------"
    # 从 BUILD_ID_MK 指定的文件中读取 SECURITY_L3 的值，并赋给 security_l3
    security_l3=$(Read_Value ${BUILD_ID_MK} SECURITY_L3)
    red "Call telecom_ca.sh chip_name:[${chip_name}]"
    
    if [ ! -f ${PROJECT_TELECOM_CA_SH} ];then
    	# 由于 PROJECT_TELECOM_CA_SH 中指定的文件不存在，所以将 telecom_ca.sh
    	# 文件路径赋给 TELECOM_CA_SH
        TELECOM_CA_SH=${OUT}/build/tool/advca/telecom_ca.sh
        # 引入 TELECOM_CA_SH 中指定的脚本文件，并执行它
        . ${TELECOM_CA_SH} ${OUT} ${BUILD_TYPE} ${build_number} ${chip_name}
        
        # 当 make_num 的值为 0 时，则执行 make_system_list
        # make_system_list 是由 telecom_ca.sh 脚本文件引入的
        if [ ${make_num} -eq 0 ];then
            make_system_list
        fi
        # 如果 security_l3 不等于 y, 则执行 sign_boot_img 和 sign_recovery_img
        # 函数，否则，打印相关信息
        # sign_boot_img 和 sign_recovery_img 也是由 telecom_ca.sh 脚本文件引入的
        if [[ ${security_l3} != "y" ]];then
            sign_boot_img
            sign_recovery_img
        else
            red "security l3 not sign boot and recovery"
        fi
    else
    	# 如果 security_l3 的值为 y，则执行 PROJECT_TELECOM_CA_SH 指定的脚本文件；
    	# 否则打印提示信息
        if [[ ${security_l3} != "y" ]];then
            . ${PROJECT_TELECOM_CA_SH} ${OUT} ${BUILD_TYPE} ${build_number}
        else
            red "security l3 not call on-project telecom_ca.sh"
        fi
    fi
    echo
    # 创建 BOOTCA 文件夹
    mkdir -p ${zip_root}/BOOTCA
    # 根据芯片名称定义 BOOTCA_ZIP_FILE 和 RECOVERY_ZIP_FILE 变量
    if [[ ${chip_name} == "" ]];then
        BOOTCA_ZIP_FILE=${zip_root}/BOOTCA/boot.img
        RECOVERY_ZIP_FILE=${zip_root}/BOOTCA/recovery.img
    else
        BOOTCA_ZIP_FILE=${zip_root}/BOOTCA/boot_${chip_name}.img
        RECOVERY_ZIP_FILE=${zip_root}/BOOTCA/recovery_${chip_name}.img
    fi
    # 如果 boot.img 存在，则拷贝它；否则，打印错误信息，并停止编译
    if [ -f ${BOOT_FILE} ]
    then
        cp -arf ${BOOT_FILE} ${BOOTCA_ZIP_FILE}
    else
        echo "boot.img  is not exit ,can't cp"
        exit 1
    fi
    # 如果 recovery.img 文件存在，则拷贝它；否则打印错误信息并停止编译
    if [ -f ${RECOVERY_FILE} ]
    then
        cp -arf ${RECOVERY_FILE} ${RECOVERY_ZIP_FILE}
    else
        echo "recovery.img is not exit ,can't cp"
        exit 1
    fi
    echo
}

# 编译工厂 OTA 包
function make_ota_factory_package()
{
	# 定义编译 OTA 包使用的标志
    ota_package_factory_flag="${STRICT_UPGRADE_FLAG} ${telecom_ca_flag} ${update_router_flag} \
        ${update_fastplay_flag} ${update_qbdata_flag} ${update_pqparam_flag} ${update_ctc_flag} \
        ${update_apploader_flag} ${update_system_img_flag} ${vmx_ca_flag} \
        ${set_otp_flag} ${set_rootkey_flag} ${update_securestore_flag} \
        ${update_trustedcore_flag} -l -t -g -w -z ${update_devinfo_full_flag} ${update_devinfo_patch_flag} --ota_factory"

 	# 定义 OTA 输出文件路径   
    build_name_flag_full=${build_number}${BUILD_PROJECT_NAME}${BUILD_CA_TYPE}${build_sign_flag}${USER_FLAG}
    OTA_Full_Factory_Package_zip="${PUBLISH_PATH}/full-factory-${build_id}-${build_name_flag_full}_erase${project_tag}${TIMETAG_FLAG}.zip"
    # 调用 ota_from_target_files 可执行文件生成 OTA 压缩文件
    ${OUT}/build/tool/releasetools/ota_from_target_files -v \
        -p ${OUT}/build/tool/linux-x86 \
        -k ${SECURITY_KEY} \
        ${ota_package_factory_flag}  -n \
        ${zip_root}.zip ${OTA_Full_Factory_Package_zip}
}

# 编译 OTA 预打包文件
# 该函数的功能是生成该版本对指定已发布版本的软件生成OTA
# 比如 已发布包的版本号是123 456 789, 当前版本号是980
# 执行这个函数后将会生成，123、456、789 版本直接升级到 980 的 OTA 升级包
function make_ota_pre_package()
{
	cyan "### OTA Pre Package ###"
	magenta "----------------------------------"
	# 从 BUILD_ID_MK 指定文件中读取 PRE_BUILD_NUMBER_ARRAY 的值，
	# 并赋给 PRE_BUILD_NUMBER_ARRAY
    PRE_BUILD_NUMBER_ARRAY=$(Read_Array_Value ${BUILD_ID_MK} PRE_BUILD_NUMBER_ARRAY)
	echo "zip_root [${zip_root}]"
	# 遍历 PRE_BUILD_NUMBER_ARRAY
	for pre_build_array_element in ${PRE_BUILD_NUMBER_ARRAY}
	do
		# 获取预打包文件的绝对路径
		pre_build_array_element_target_name="target-${pre_build_array_element}"
		pre_build_array_element_zip_root="${OUT}/${OUT_DIR}/${TARGET}/${pre_build_array_element_target_name}.zip"
		echo "pre_zip: [${pre_build_array_element_zip_root}]"
		# 如果预打包文件存在，则调用 ota_from_target_files 可执行文件生成对应的 OTA 包；
		# 否则，打印提示信息
		if [ -f ${pre_build_array_element_zip_root} ]
		then
			${OUT}/build/tool/releasetools/ota_from_target_files \
				-p ${OUT}/build/tool/linux-x86 \
				-k ${SECURITY_KEY} \
				${ota_package_flag} -v \
				-i ${pre_build_array_element_zip_root} ${zip_root}.zip  \
				${PUBLISH_PATH}/${pre_build_array_element}-patch-${build_name_flag}${project_tag}${TIMETAG_FLAG}.zip
		else
			echo "no such pre zip: ${pre_build_array_element_zip_root}"
		fi
	done
}

# 编译 OTA 升级包
function make_ota_package()
{
    #=================================================
    ### vmx_ca.sh existed
    # 从 BUILD_ID_MK 指定文件中读取 VMX_ADV_CA 的值，并赋给 vmx_ca
    vmx_ca=$(Read_Value ${BUILD_ID_MK} VMX_ADV_CA)
    # 如果 vmx_ca 的值为 y，则调用 call_vmx_ca 函数
    if [[ ${vmx_ca} == "y" ]]
    then
        call_vmx_ca
    fi

    ###
    ### telecom_ca.sh existed,signature
    ###
    # 从 BUILD_ID_MK 指定文件中读取 TELECOM_CA 的值，并赋给 telecom_ca
    telecom_ca=$(Read_Value ${BUILD_ID_MK} TELECOM_CA)
    # 根据 telecom_ca  的值设置 telecom_ca_flag 变量
    if [[ ${telecom_ca} == "y" ]]
    then
        telecom_ca_flag="-m"
    else
        telecom_ca_flag=""
    fi

    #=================================================
    # 从 BUILD_ID_MK 指定文件中读取 BUILD_OTA_FACTORY 的值，并赋给 ota_factory
    ota_factory=$(Read_Value ${BUILD_ID_MK} BUILD_OTA_FACTORY)
	# 根据 wipedata 的值设置 wipe_data_flag 变量
    if [[ ${wipedata} == "y" ]]
    then
        wipe_data_flag="-w"
    else
        wipe_data_flag=""
    fi
    # 从 BUILD_ID_MK 指定文件中读取 UPDATE_LOADER 的值，并赋给 update_loader
    update_loader=$(Read_Value ${BUILD_ID_MK} UPDATE_LOADER)
    # 如果 update_loader 的值为 y 或者 ota_factory 的值为 y，则执行下面语句；
    # 否则将 update_loader_flag 的值设置为空
    if [[ ${update_loader} == "y" ]] || [[ ${ota_factory} == "y" ]]
    then
    	# 根据 update_loader 的值设置 update_loader_flag 变量
        if [[ ${update_loader} == "y" ]]
        then
            update_loader_flag="-l"
        fi
        # 创建 LOADER 文件夹
        mkdir -p ${zip_root}/LOADER
        # 遍历芯片名数组
        for chip_name in ${chip_name_array[*]}
        do
        	# 根据 芯片名数组大小设置 LOADER_FILE 和 LOADER_ZIP_FILE 变量
            if [ ${chip_name_num} -eq 1 ];then
                LOADER_FILE=${PUBLISH_PATH}/loader.bin
                LOADER_ZIP_FILE=${zip_root}/LOADER/loader.bin
            else
                LOADER_FILE=${PUBLISH_PATH}/loader_${chip_name}.bin
                LOADER_ZIP_FILE=${zip_root}/LOADER/loader_${chip_name}.bin
            fi
            # 如果 LOADER_FILE 中指定的文件存在，则拷贝该文件到 LOADER_ZIP_FILE
            # 中指定的位置；否则，打印错误信息并停止编译
            if [ -f ${LOADER_FILE} ];then
                cp -arf ${LOADER_FILE} ${LOADER_ZIP_FILE}
            else
                echo " loader.bin is not exist ,can't update "
                exit 1
            fi
        done
        # 如果 SUPPORT_UNITE 的值为 y，则执行下面的语句
		if [[ ${SUPPORT_UNITE} == "y" ]];then
			unite_manu=""
			uniteloader_file="${OUT}/on-project/pub/image/unite/"
			# 如果 uniteloader_file 目录存在，则获取该目录下的所有文件和文件夹，
			# 并将其拷贝到 LOADER 目录下；同时将 uniteloader_file 目录下的文件和
			# 文件夹名字存储到 unite_manu 变量中，然后将其导入环境变量中，最后
			# 设置 support_unite_flag 标志
			if [ -d ${uniteloader_file} ];then
				unite_manu_arry=`ls -l ${OUT}/on-project/pub/image/unite|awk '/^d/{print $NF}'`		
				for manu in ${unite_manu_arry[@]}
				do
					unite_manu+=" $manu"
					cp  -arf ${OUT}/on-project/pub/image/unite/${manu}/* ${zip_root}/LOADER/ 
				done
				export UNITE_MANU_ARRY=${unite_manu}
				#cp ${PUBLISH_PATH}/unite/* ${zip_root}/LOADER/UNITE/
				support_unite_flag="--support_unite_flag"
			fi
		fi
    else
        update_loader_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 PARAMETERS_BACKUP 的值，并赋给 parameters_backup
    parameters_backup=$(Read_Value ${BUILD_ID_MK} PARAMETERS_BACKUP)
    # 如果 parameters_backup 的值为 y，则设置 parameters_backup_flag 标志
    if [[ ${parameters_backup} == "y" ]];then
        parameters_backup_flag="--parameters_backup_flag"
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_PQPARAM 的值，并赋给 update_pqparam
    update_pqparam=$(Read_Value ${BUILD_ID_MK} UPDATE_PQPARAM)
    # 如果 update_pqparam 的值为 y, 则执行里面的语句；否则设置 update_pqparam_flag
    # 的值为空
    if [[ ${update_pqparam} == "y" ]]
    then
    	# 如果 update_pqparam 的值为 y，则设置 update_pqparam_flag 标志
        if [[ ${update_pqparam} == "y" ]]
        then
            update_pqparam_flag="--update_pqparam"
        fi
        # 创建 PQPARAM 目录
        mkdir -p ${zip_root}/PQPARAM
        # 遍历芯片名数组
        for chip_name in ${chip_name_array[*]}
        do
        	# 根据芯片名数组的大小，设置 PQPARAM_FILE 的值
            if [ ${chip_name_num} -eq 1 ];then
                PQPARAM_FILE=${PUBLISH_PATH}/pq_param.bin
            else
                PQPARAM_FILE=${PUBLISH_PATH}/pq_param_${chip_name}.bin
            fi
            # 如果 PQPARAM_FILE 指定的文件存在，则将其拷贝到 PQPARAM 目录下；
            # 否则提示错误信息并停止编译
            if [ -f ${PQPARAM_FILE} ]; then
                cp -arf ${PQPARAM_FILE} ${zip_root}/PQPARAM
            else
                echo "pqparam.bin is not exit ,can't cp"
                exit 1
            fi
        done
    else
        update_pqparam_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_LOGO 的值，并赋给 update_logo
    update_logo=$(Read_Value ${BUILD_ID_MK} UPDATE_LOGO)
    # 如果 update_logo 或 ota_factory 其中一个的值为 y， 则执行下面的语句；
    # 否则设置 update_logo_flag 的值为空
    if [[ ${update_logo} == "y" ]] || [[ ${ota_factory} == "y" ]]
    then
    	# 如果 update_logo 的值为 y，则设置 update_logo_flag 标志
        if [[ ${update_logo} == "y" ]]
        then
            update_logo_flag="-g"
        fi
        # 创建 LOGO 文件夹
        mkdir -p ${zip_root}/LOGO
        # 如果 logo.img 文件存在，则将其拷贝到 LOGO 目录下；
        # 否则打印错误信息并停止编译
        if [[ -f ${PUBLISH_PATH}/logo.img ]]
        then
            cp -arf ${PUBLISH_PATH}/logo.img ${zip_root}/LOGO/logo.img
        else
            echo "logo.img is not exit ,can't cp"
            exit 1
        fi
    else
        update_logo_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_CTC 的值，并赋给 update_ctc
    update_ctc=$(Read_Value ${BUILD_ID_MK} UPDATE_CTC)
    # 如果 update_ctc 的值为 y 则执行下面语句；
    # 否则设置 update_ctc_flag 变量的值为空
    if [[ ${update_ctc} == "y" ]]
    then
        update_ctc_flag="--update_ctc"
        # 如果 ctc 目录存在，则在压缩根目录下创建 CTC 目录，
        # 并将 ctc 目录的内容拷贝到 CTC 目录中
        if [ -d ${ON_PROJECT_PATH}/pub/ctc/ ];then
            red "Create ctc's Directory"
            mkdir -p ${zip_root}/CTC
            green "Copy ctc's Files"
            cp -arf ${ON_PROJECT_PATH}/pub/ctc/* ${zip_root}/CTC
        fi
    else
        update_ctc_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_BASEPARAM 的值，
	# 并赋给 update_cupdate_baseparamtc
    update_baseparam=$(Read_Value ${BUILD_ID_MK} UPDATE_BASEPARAM)
    # 如果 update_baseparam 或 ota_factory 其中一个的值为 y，则执行下面语句；
    # 否则将 update_baseparam_flag 变量的值设置为空
    if [[ ${update_baseparam} == "y" ]] ||  [[ ${ota_factory} == "y" ]]
    then
    	# 如果 update_baseparam 的值为 y，则设置 update_baseparam_flag 标志
        if [[ ${update_baseparam} == "y" ]]
        then
            update_baseparam_flag="-t"
        fi
        # 创建 PARAM 文件夹
        mkdir -p ${zip_root}/PARAM
        # 如果 baseparam.img 文件存在，则将其拷贝到 PARAM 目录中；
        # 否则打印错误信息并停止编译
        if [[ -f ${PUBLISH_PATH}/baseparam.img ]]
        then
            cp -arf ${PUBLISH_PATH}/baseparam.img ${zip_root}/PARAM/baseparam.img
        else
            echo "baseparam.img is not exit ,can't cp"
            exit 1
        fi
    else
        update_baseparam_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_PARTITION 的值，并赋给 update_partition
    update_partition=$(Read_Value ${BUILD_ID_MK} UPDATE_PARTITION)
    # 如果 update_partition 的值为 y，则执行下面的语句，
    # 否则将 update_partition_flag 变量的值设置为空
    if [[ ${update_partition} == "y" ]]
    then
        update_partition_flag="--update_partition"
        # 创建 PARTITION 文件夹
        mkdir -p ${zip_root}/PARTITION
        ### make patition image ###
        # 如果 partition.img 文件不存在，则执行下面语句
        if [ ! -f ${PUBLISH_PATH}/partition.img ];then
            cyan "### Create partition.img ###"
            magenta "----------------------------------"
            if [[  ${PRODUCT_LOADER} == '' ]]
            then
            	# 生成 partition.img
                ${TOP}/platform/build/tool/linux-x86/bin/mkpartitionimg  ${PARTINFO_CONF} ${PUBLISH_PATH}/partition.img
            elif [[ ${flash} == "nand" ]]
            then	
            	# 生成 partition_nand.img
                ${TOP}/platform/build/tool/linux-x86/bin/mkpartitionimg  ${PARTINFO_NAND_CONF} ${PUBLISH_PATH}/partition_nand.img

            fi
        fi
        # 将 partition.img 拷贝到 PARTITION 目录下
        cp -arf ${PUBLISH_PATH}/partition.img ${zip_root}/PARTITION/partition.img
    else
        update_partition_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_CACHE 的值，并赋给 update_cache
    update_cache=$(Read_Value ${BUILD_ID_MK} UPDATE_CACHE)
    # 如果 update_cache 或 ota_factory 其中一个的值为 y，则执行下面语句；
    # 否则将 update_cache_flag 变量的值设置为空
    if [[ ${update_cache} == "y" ]] || [[ ${ota_factory} == "y" ]]
    then
    	# 如果 update_cache 的值为 y，则设置 update_cache_flag 标志
        if [[ ${update_cache} == "y" ]]
        then
            update_cache_flag="-z"
        fi
        # 创建 CACHE 文件夹
        mkdir -p ${zip_root}/CACHE
        # 将 cache 目录下的文件拷贝到 CACHE 目录下
        cp -arf ${OUT}/on-project/pub/cache/* ${zip_root}/CACHE/
    else
        update_cache_flag=""
    fi
	
	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_DEVINFO_FULL 的值，并赋给 update_devinfo_full
    update_devinfo_full=$(Read_Value ${BUILD_ID_MK} UPDATE_DEVINFO_FULL)
    # 如果 update_devinfo_full 或 ota_factory 其中一个的值为 y，则执行下面语句；
    # 否则将 update_devinfo_full_flag 变量的值设置为空
    if [[ ${update_devinfo_full} == "y" ]] ||  [[ ${ota_factory} == "y" ]]
    then
    	# 如果 update_devinfo_full 的值是 y，则设置 update_devinfo_full_flag 标志
        if [[ ${update_devinfo_full} == "y" ]]
        then
            update_devinfo_full_flag="--update_devinfo_full"
        fi
        # 创建 DEVINFO 文件夹
        mkdir -p ${zip_root}/DEVINFO
        # 如果 deviceinfo.img 文件存在，则将其拷贝至 DEVINFO 目录下；
        # 否则打印报错信息并退出编译
        if [[ -f ${PUBLISH_PATH}/deviceinfo.img ]]
        then
            cp -arf ${PUBLISH_PATH}/deviceinfo.img ${zip_root}/DEVINFO/deviceinfo.img
        else
            echo "deviceinfo.img is not exit ,can't cp"
            exit 1
        fi
    else
        update_devinfo_full_flag=""
    fi 
	
	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_DEVINFO_PATCH 的值，
	# 并赋给 update_devinfo_patch
    update_devinfo_patch=$(Read_Value ${BUILD_ID_MK} UPDATE_DEVINFO_PATCH)
    # 如果 update_devinfo_patch 的值为 y 且 update_devinfo_full 的值为 n，则执行下面语句；
    # 否则将 update_devinfo_patch_flag 变量的值设置为空
    if [[ ${update_devinfo_patch} == "y" && ${update_devinfo_full} == "n" ]]
    then
        update_devinfo_patch_flag="--update_devinfo_patch"
        # 创建 DEVINFO 文件夹
        mkdir -p ${zip_root}/DEVINFO
        # 如果 devinfo_patch.img 文件存在，则将其拷贝到 DEVINFO 目录下；
        # 否则打印报错信息并退出编译
        if [[ -f ${PUBLISH_PATH}/devinfo_patch.img ]]
        then
            cp -arf ${PUBLISH_PATH}/devinfo_patch.img ${zip_root}/DEVINFO/devinfo_patch.img
        else
            echo "devinfo_patch.img is not exit ,can't cp"
            exit 1
        fi
    else
        update_devinfo_patch_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_DATA 的值，并赋给 update_data
    update_data=$(Read_Value ${BUILD_ID_MK} UPDATE_DATA)
    # 如果 update_data 或 ota_factory 其中一个的值为 y，则执行下面语句；
    # 否则将 update_data_flag 变量的值设置为空
    if [[ ${update_data} == "y" ]] || [[ ${ota_factory} == "y" ]]
    then
    	# 如果 update_data 的值为 y， 则设置 update_data_flag 标志
        if [[ ${update_data} == "y" ]]
        then
            update_data_flag="-y"
        fi
        # 创建 DATA 目录
        mkdir -p ${zip_root}/DATA
        # 将 data 目录下的内容拷贝到 DATA 目录中
        cp -arf ${OUT}/on-project/pub/data/* ${zip_root}/DATA/
    else
        update_data_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_ROUTER 的值，并赋给 update_router
    update_router=$(Read_Value ${BUILD_ID_MK} UPDATE_ROUTER)
    # 如果 update_router 的值为 y，则创建 ROUTER 文件夹，并将 ROUTER 变量指定
    # 的目录下的内容到 ROUTER 目录中
    if [[ ${update_router} == "y" ]]
    then
        update_router_flag="--update_router"
        mkdir -p ${zip_root}/ROUTER
        cp -arf ${OUT}/on-project/pub/${ROUTER}/* ${zip_root}/ROUTER/
    else
        update_router_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_FASTPLAY 的值，并赋给 update_fastplay
    update_fastplay=$(Read_Value ${BUILD_ID_MK} UPDATE_FASTPLAY)
    # 如果 update_fastplay 的值为 y，则 执行下面语句；
    # 否则将 update_fastplay_flag 的值设置为空
    if [[ ${update_fastplay} == "y" ]]
    then
    	# 如果 update_fastplay 的值为 y，则设置 update_fastplay_flag 标志
        if [[ ${update_fastplay} == "y" ]]
        then
            update_fastplay_flag="--update_fastplay"
        fi
        # 创建 FASTPLAY 文件夹
        mkdir -p ${zip_root}/FASTPLAY
        # 如果 fastplay.img 文件存在，则将其拷贝至 FASTPLAY 目录下；
        # 否则打印错误信息并退出编译
        if [[ -f ${OUT}/on-project/pub/image/fastplay.img ]]
        then
            cp -arf ${OUT}/on-project/pub/image/fastplay.img ${zip_root}/FASTPLAY/
        else
            echo "fastplay.img is not exit ,can't cp"
            exit 1
        fi
    else
        update_fastplay_flag=""
    fi

	# 设置 update_qbdata_flag 标志
    if [[ ${USE_QBDATA} == "y" ]]
    then
        echo "use qbdata partition"
        update_qbdata_flag="--update_qbdata"
    else
        update_qbdata_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_FACTORY 的值，并赋给 update_factory
    update_factory=$(Read_Value ${BUILD_ID_MK} UPDATE_FACTORY)
    # 如果 update_factory 的值为 y， 则执行下面语句；
    # 否则将 update_factory_flag 的值设置为空
    if [[ ${update_factory} == "y" ]]
    then
        update_factory_flag="--update_factory"
        # 创建 FACTORY 文件夹
        mkdir -p ${zip_root}/FACTORY
        if [ ${vmx_ca} == "y" ];then
        	# 如果 dummy_signed_factory.img 文件存在，则将其拷贝到 FACTORY 目录下；
        	# 否则打印错误信息并退出编译
            if [[ -f ${PUBLISH_PATH}/dummy_signed_factory.img ]]
            then
                cp -arf ${PUBLISH_PATH}/dummy_signed_factory.img ${zip_root}/FACTORY/factory.img
            else
                echo "dummy_signed_factory.img is not exit ,can't cp"
                exit 1
            fi
        else
        	# 如果 factory.img 文件存在，则将其拷贝到 FACTORY 目录下；
        	# 否则打印错误信息并退出编译
            if [[ -f ${PUBLISH_PATH}/factory.img ]]
            then
                cp -arf ${PUBLISH_PATH}/factory.img ${zip_root}/FACTORY/factory.img
            else
                echo "factory.img is not exit ,can't cp"
                exit 1
            fi
        fi
    else
        update_factory_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_MISC 的值，并赋给 update_misc
    update_misc=$(Read_Value ${BUILD_ID_MK} UPDATE_MISC)
    # 如果 update_misc 的值为 y, 则执行下面语句；
    # 否则将 update_misc_flag 的值设置为空
    if [[ ${update_misc} == "y" ]]
    then
        update_misc_flag="--update_misc"
        # 创建 MISC 文件夹
        mkdir -p ${zip_root}/MISC
        # 如果 misc.img 文件存在，则将其拷贝到 misc.img；
        # 否则打印错误信息并退出编译
        if [[ -f ${PUBLISH_PATH}/misc.img ]]
        then
            cp -arf ${PUBLISH_PATH}/misc.img ${zip_root}/MISC/misc.img
        else
            echo "misc.img is not exit ,can't cp"
            exit 1
        fi
    else
        update_misc_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_MISC 的值，并赋给 update_misc
    update_apploader=$(Read_Value ${BUILD_ID_MK} UPDATE_APPLOADER)
    # 如果 update_apploader 的值为 y，则创建 APPLOADER 文件夹，并将
    # *_apploader.bin 文件拷贝到 APPLOADER 文件夹中；
    # 否则将 update_apploader_flag 的值设置为空
    if [[ ${update_apploader} == "y" ]]
    then
        update_apploader_flag="--update_apploader"
        mkdir -p ${zip_root}/APPLOADER
        cp -arf ${PUBLISH_PATH}/${build_sign_type}_apploader.bin ${zip_root}/APPLOADER/apploader.bin
    else
        update_apploader_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_TRUSTEDCORE 的值，并赋给 update_trustedcore
    update_trustedcore=$(Read_Value ${BUILD_ID_MK} UPDATE_TRUSTEDCORE)
    # 如果 update_trustedcore 的值为 y，则将 *_trustedcore.img 
    # 文件拷贝到 TRUSTEDCORE目录下，否则将 update_trustedcore_flag 设置为空
    if [[ ${update_trustedcore} == "y" ]]
    then
        update_trustedcore_flag="--update_trustedcore"
        cp -arf ${PUBLISH_PATH}/${build_sign_type}_trustedcore.img ${zip_root}/TRUSTEDCORE/trustedcore.img
    else
        update_trustedcore_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_SECURESTORE 的值，并赋给 update_securestore
    update_securestore=$(Read_Value ${BUILD_ID_MK} UPDATE_SECURESTORE)
    # 设置 update_securestore_flag 标志
    if [[ ${update_securestore} == "y" ]]
    then
        update_securestore_flag="--update_securestore"
    else
        update_securestore_flag=""
    fi
	
	# 从 BUILD_ID_MK 指定文件中读取 UPDATE_SYSTEM_IMG 的值，并赋给 update_system_img
	# 从 BUILD_ID_MK 指定文件中读取 VMX_ADV_CA_SHATABLE 的值，并赋给 vmx_advca_shatable
    update_system_img=$(Read_Value ${BUILD_ID_MK} UPDATE_SYSTEM_IMG)
    vmx_advca_shatable=$(Read_Value ${BUILD_ID_MK} VMX_ADV_CA_SHATABLE)
    # 如果 update_system_img 的值为 y，则创建 SYSTEMCA 目录，并拷贝相应的 *.squashfs 文件到
    # SYSTEMCA 目录中
    if [[ ${update_system_img} == "y" ]]
    then
        update_system_img_flag="--update_system_img --update_no_system "
        mkdir -p ${zip_root}/SYSTEMCA
        if [[ ${vmx_advca_shatable} == "y" ]]
        then
            echo "vmx advca shatable"
            cp -arf ${PUBLISH_PATH}/system.squashfs ${zip_root}/SYSTEMCA/system.squashfs
            cp -arf ${PUBLISH_PATH}/${build_sign_type}_shatable.squashfs ${zip_root}/SYSTEMCA/shatable.squashfs
        else
            cp -arf ${PUBLISH_PATH}/${build_sign_type}_system.squashfs ${zip_root}/SYSTEMCA/system.squashfs
        fi
    else
        update_system_img_flag=""
    fi

	# 从 BUILD_ID_MK 指定文件中读取 SET_OTP 的值，并赋给 set_otp
	# 从 BUILD_ID_MK 指定文件中读取 SET_ROOTKEY 的值，并赋给 set_rootkey
    set_otp=$(Read_Value ${BUILD_ID_MK} SET_OTP)
    set_rootkey=$(Read_Value ${BUILD_ID_MK} SET_ROOTKEY)
    # 设置 set_rootkey_flag 和 set_otp_flag 标志
    if [[ ${set_otp} == "y" && ${update_loader} == "y" && ${telecom_ca} == "y" && ${security_l3} != "y" ]]
    then
        if [[ ${set_rootkey} == "y" ]]
        then
            set_rootkey_flag="--set_rootkey"
        fi
        set_otp_flag="--set_otp"
    else
        set_otp_flag=""
    fi

	# 设置编译使用的标志
    ota_package_flag="${wipe_data_flag} ${update_logo_flag} ${update_ctc_flag} \
        ${update_loader_flag} ${update_baseparam_flag} ${update_cache_flag} \
        ${update_data_flag} ${STRICT_UPGRADE_FLAG} ${telecom_ca_flag} ${update_router_flag} \
        ${update_fastplay_flag} ${update_qbdata_flag} ${update_pqparam_flag} \
        ${update_apploader_flag} ${update_system_img_flag} ${vmx_ca_flag} \
        ${set_otp_flag} ${set_rootkey_flag} \
        ${update_trustedcore_flag} ${update_partition_flag} ${update_securestore_flag} \
        ${update_devinfo_full_flag} ${update_devinfo_patch_flag} ${support_unite_flag} ${parameters_backup_flag}\
        "
    ###=================================================
    ### Everything Already Ok , Then Ziping All For Create OTA Full Package
    ###=================================================
    # 从 BUILD_ID_MK 指定的文件中读取 REPRODUCT_VERSION 的值，并赋给 reproduct_version
    reproduct_version=$(Read_Value ${BUILD_ID_MK} REPRODUCT_VERSION)
    # 如果 reproduct_version 的值为 y，则执行 DoSomething_before_makeUpdatezip 函数
    if [[ ${reproduct_version} == "y" ]]
    then
    	# 在小系统中未找定义该函数的地方，这个应该是留给公司自己实现的吧。
    	# 在 build_id.mk 文件中也没有找到 REPRODUCT_VERSION 的定义
        DoSomething_before_makeUpdatezip
    fi
    magenta "---------------------"
    red "Copy target All Files Into target-xxoo.zip"
    # 下面主要是拷贝文件到 OTA/bin 目录中
    mkdir -p ${zip_root}/OTA/bin
    echo "borad=" > ${zip_root}/OTA/android-info.txt
    cp -arf ${TOP}/platform/${RELEASE_DIR}/system/bin/applypatch ${zip_root}/OTA/bin
    cp -arf ${TOP}/platform/${RELEASE_DIR}/system/bin/applypatch_static ${zip_root}/OTA/bin
    cp -arf ${TOP}/platform/${RELEASE_DIR}/system/bin/check_prereq ${zip_root}/OTA/bin
    cp -arf ${TOP}/platform/${RELEASE_DIR}/system/bin/updater ${zip_root}/OTA/bin

    cp -arf ${TOP}/platform/on-project/pub/system/bin/applypatch ${zip_root}/OTA/bin
    cp -arf ${TOP}/platform/on-project/pub/system/bin/applypatch_static ${zip_root}/OTA/bin
    cp -arf ${TOP}/platform/on-project/pub/system/bin/check_prereq ${zip_root}/OTA/bin
    cp -arf ${TOP}/platform/on-project/pub/system/bin/updater ${zip_root}/OTA/bin

	red "Call project_priv_ota.sh "
	# 如果 PROJECT_PRIV_OTA_SH 中指定的脚本文件存在，则执行该脚本文件
	if [ -f ${PROJECT_PRIV_OTA_SH} ]
	then
		. ${PROJECT_PRIV_OTA_SH} ${TOP} ${zip_root}
	fi
	echo

	# 创建 META 目录，并在该目录下创建文件和向文件中写入数据
    mkdir -p ${zip_root}/META
    echo "recovery_api_version=3" > ${zip_root}/META/misc_info.txt
    echo "fs_type=ext4" >> ${zip_root}/META/misc_info.txt
    echo "use_set_metadata=1" >> ${zip_root}/META/misc_info.txt
    echo "update_rename_support=1" >> ${zip_root}/META/misc_info.txt
    # 切换目录到 zip_root
    pushd ${zip_root}
    green "I Am Ziping Everything For ${target_name}.zip "
    # 将目录中的内容压缩成压缩包
    zip -qry ../${target_name}.zip .
    # 拷贝压缩包到 PUBLISH_PATH 目录下
    cp -arf ${zip_root}.zip ${PUBLISH_PATH}

    if [[ ${USE_QBDATA} == "y" ]]
    then
    	# 
    	# zipinfo 命令用于列出压缩包中的文件
    	# -1 表示只列出文件名
    	# FS 指定分隔符
    	# sub(/SYSTEM/, "system") 使用 system 替换掉 SYSTEM
        zipinfo -1 ${zip_root}.zip | awk 'BEGIN { FS="SYSTEM/" } sub(/SYSTEM/,"system") {print $$2} END { FS="QBDATA/" } sub(/QBDATA/,"qbdata") {print $$2}' | ${OUT}/build/tool/linux-x86/bin/fs_config > ${zip_root}/META/filesystem_config.txt
    else
        zipinfo -1 ${zip_root}.zip | awk 'BEGIN { FS="SYSTEM/" } sub(/SYSTEM/,"system") {print $$2}' | ${OUT}/build/tool/linux-x86/bin/fs_config > ${zip_root}/META/filesystem_config.txt
    fi

	# 将 META 目录下的内容添加到压缩包中
    zip -qry ../${target_name}.zip META/
    # 恢复当前目录
    popd
    if [[ ${reproduct_version} == "y" ]]
    then
    	# 该函数不存在，由用户自己实现
        DoSomething_after_makeUpdatezip
    fi
    magenta "---------------------"
    echo

    #=================================================
    ###
    ### OTA Package
    ###
    cyan "### OTA Package ###"
    magenta "----------------------------------"
	# 设置构建标志   
   build_name_flag=${build_number}${BUILD_PROJECT_NAME}${BUILD_CA_TYPE}${build_sign_flag}${USER_FLAG}
   	# 设置OTA包路径
    OTA_Full_Package_zip="${PUBLISH_PATH}/full-${build_id}-${build_name_flag}${WIPEDATA_FLAG}${project_tag}${TIMETAG_FLAG}-cmdc-shandong.zip"
    # 调用 ota_from_target_files 可执行文件生成 OTA 包
    ${OUT}/build/tool/releasetools/ota_from_target_files -v \
        -p ${OUT}/build/tool/linux-x86 \
        -k ${SECURITY_KEY} \
        ${ota_package_flag}  -n \
        ${zip_root}.zip ${OTA_Full_Package_zip}

    #=================================================
    ###
    ### OTA_factory Package
    ###
    cyan "### OTA_factory Package ###"
    magenta "----------------------------------"
    # 构建工厂 OTA 包
    if [[ ${ota_factory} == "y" ]]
    then
        make_ota_factory_package
    fi
    # 构建版本OTA包
    make_ota_pre_package

}

# 编译 images
function make_images()
{
	# 从 BUILD_ID_MK 指定的文件中读取 PARTINFO_ARRAY 的值，并赋给 PARTINFO_ARRAY
    PARTINFO_ARRAY=$(Read_Array_Value ${BUILD_ID_MK} PARTINFO_ARRAY)
    # 如果 PARTINFO_ARRAY 的值为空，则设置其值为 partinfo.conf
    if [[ ${PARTINFO_ARRAY} == '' ]]
    then
        PARTINFO_ARRAY="partinfo.conf"
    fi
    echo "PARTINFO_ARRAY: ${PARTINFO_ARRAY}"
    # 遍历 PARTINFO_ARRAY
    for PARTINFO_TYPE in ${PARTINFO_ARRAY}
    do
        make_num=0
        # 遍历芯片名数组
        for chip_name in ${chip_name_array[*]}
        do
        	# 获取 PARTINFO_CONF 文件路径
            PARTINFO_CONF=$(Get_Project_File ${OUT}/on-project/pub/swproduct/${PARTINFO_TYPE})
            echo "PARTINFO_CONF: ${PARTINFO_CONF}"

            ###===================================================
            cyan " Judge flash type is NAND or EMMC for \"${PARTINFO_CONF}\""
            # 通过 PARTINFO_CONF 文件判断 FLASH 类型是 NAND 还是 EMMC
            # judge_flash_partition 是 small/platform/build/PartitionCreate.sh 脚本
            # 中的函数
            flash=$(judge_flash_partition ${PARTINFO_CONF})

            cyan "### Mkdir images path ###"
            # 获取存放 image 的文件夹路径
            # 例如：/home/qintuanye/workspace/zhaoge_mv300_2020/cmdc/small/platform/out/publish/images-100.462.001-partinfo_nand
            # 该目录会在编译完成后删除
            images_path=${PUBLISH_PATH}/images-${build_name_flag}${WIPEDATA_FLAG}-${PARTINFO_TYPE%.conf*}
            mkdir -p ${images_path}

            cyan "### echo nand.xml/emmc.xml###"
            # 创建 *_nand.xml 或 *_emmc.xml 文件，并向其添加内容
            magenta "----------------------------------"
            if [ "${flash}" == "nand" ];then
                xmlname="-nand.xml"
            elif [ "${flash}" == "emmc" ];then
                xmlname="-emmc.xml"
            fi
            echo '<?xml version="1.0" encoding="GB2312" ?>' >> ${images_path}/${chip_name}${xmlname}
            echo '<Partition_Info>' >> ${images_path}/${chip_name}${xmlname}

            #=====================================================
            ###
            ### make patition image ###
            ###
            cyan "### make patition image ###"
            # 读取 PARTINFO_CONF 文件内容
            while read line
            do
            	# 获取一行中的第一项数据，并将其 Windows 的文件分隔符转换成 unix 的文件分隔符
            	# dos2unix 命令将字符串中的 Windows 文件分隔符转换成 unix 文件分隔符
                part_name=$(echo ${line} | awk '{print $1}' | dos2unix)
                # 如果是文件首行数据，则跳过
                if [ "${part_name}" == "#part" ];then
                    continue
                fi
                # 获取一行中的第2项数据，根据该数据设置 fs_type 变量
                fs_type=$(echo ${line} | awk '{print $2}')
                if [ "${fs_type}" == "raw" ];then
                    fs_type="none"
                elif [ "${fs_type}" == "ubifs" ];then
                    fs_type="ubifs"
                elif [ "${fs_type}" == "ext4" ];then
                    fs_type="ext3/4"
                fi
                # 获取一行中的第3项数据，并将其赋给 offset 变量
                offset=$(echo ${line} | awk '{print $3}')
                # 获取一行中的第4个参数，并将其赋给 length 变量
                length=$(echo ${line} | awk '{print $4}')
                # 获取一行中的第5个参数，并将其赋给 image 变量
                image=$(echo ${line} | awk '{print $5}' | dos2unix)
                # 如果 image 变量的值是 0 或者 1，则将 image 的值设置为一行中的第六个参数
                if [[ "${image}" == "0" || "${image}" == "1" ]];then
                    image=$(echo ${line} | awk '{print $6}' | dos2unix)
                fi

                #=================================================
                ###
                ### create hitools use emmc.xml/nand.xml ###
                ###
                # 根据 image 和 part_name 的值设置 sel 和 image_name 变量
                if [[ "${image}" == "NULL" || "${part_name}" == "misc" ]];then
                    sel="0"
                    image_name=""
                else
                    sel="1"
                    if [[ ${part_name} == "fastboot" && ${chip_name_num} -ne 1 ]];then
                        image_name=$(echo ${image/\.bin/\_${chip_name}\.bin})
                    elif [[ "recovery2 boot2" == *${part_name}* ]] && [ ${chip_name_num} -ne 1 ];then
                        image_name=$(echo ${image/\.img/\_${chip_name}\.img})
                    else
                        image_name=${image}
                    fi
                fi
                # 向 *_nand.xml 或 *_emmc.xml 文件写入如下值
                echo "<Part Sel=\""${sel}"\" PartitionName=\""${part_name}"\" FlashType=\""${flash}"\" FileSystem=\""${fs_type}"\" Start=\""${offset}"M\" Length=\""${length}"M\" SelectFile=\""${image_name}"\"/>" >> ${images_path}/${chip_name}${xmlname}

                #=================================================
                ###
                ### make partition image ###
                ###
                # 根据 part_name 和 make_num 的值确定是否编译 partitionimg
                if [[ ${part_name} == "partition" ]] && [ ${make_num} -eq 0 ]
                then
                    cyan "### Create for partition.img ###"
                    ${TOP}/platform/build/tool/linux-x86/bin/mkpartitionimg ${PARTINFO_CONF} ${PUBLISH_PATH}/${image_name}
                fi

				# 设置 make_mlcverify_flag 标志
                [[ ${part_name} == "mlcverify" ]] && make_mlcverify_flag=y

                #=================================================
                ###
                ### make misc image ###
                ###
                # 编译 misc img
                if [[ ${part_name} == "misc" ||  ! -f ${PUBLISH_PATH}/misc.img ]] && [ ${make_num} -eq 0 ]
                then
                    cyan "### Create for misc.img ###"
                    ${TOP}/platform/build/tool/linux-x86/bin/mkmiscimg ${PUBLISH_PATH}/misc.img
                fi

                if [[ "y" == ${Partition_Flag} ]] && [ ${fs_type} != "none" ] && [ ${make_num} -eq 0 ]
                then
                    if [[ ${part_name} == "backup" ]]
                    then
                        ###===================================================
                        ###
                        ### Create backup.ext4 Partition
                        ###
                        # 创建 backup.ext4 分区
                        cyan "### Create backup.ext4 Partitions ###"
                        magenta "----------------------------------"
                        if [[ -f ${BACKUP_IMG} ]]
                        then
                            echo "### copy ${BACKUP_IMG}"
                            cp -arf ${BACKUP_IMG}  ${PUBLISH_PATH}
                        else
                            sleep 1
                            ### backup.img 348M
                            mkdir -p ${PUBLISH_PATH}/backup

                            #如果小系统定义了BACKUP_FIRMWARE_DIR宏，则将备份升级版本拷贝到/backup/${BACKUP_FIRMWARE_DIR}/目录下
                            backup_firmware_dir=$(Read_Value ${BUILD_ID_MK} BACKUP_FIRMWARE_DIR)
                            if [[ ${backup_firmware_dir} ]]
                            then
                                mkdir -p ${PUBLISH_PATH}/backup/${backup_firmware_dir}
                                cp -arf ${OTA_Full_Package_zip} ${PUBLISH_PATH}/backup/${backup_firmware_dir}/update.zip
                            else
                                cp -arf ${OTA_Full_Package_zip} ${PUBLISH_PATH}/backup/update.zip
                            fi
                            echo "version=${build_number}" > ${PUBLISH_PATH}/backup/backup_version.txt
                            # Create_backup 函数是在 PartitionCreate.sh 中定义的
                            Create_backup "backup" ${PARTINFO_CONF}
                            sleep 1
                            rm -rf ${PUBLISH_PATH}/backup
                        fi
                    else
                        #=================================================
                        ###
                        ### Create ubi or ext4 Partition
                        ###
                        cyan "### Create ${part_name} Partitions ###"
                        magenta "----------------------------------"
                        # Create_partition 函数是在 PartitionCreate.sh 中定义的
                        Create_Partition ${part_name} ${PARTINFO_CONF}
                        sleep 1
                    fi
                fi

                #=================================================
                ###
                ### copy all file to a directory ###
                ###
                # 拷贝所有文件到 images_path 指定的目录中
                if [[ "${image}" == "NULL" || "${image}" == "image_name" ]];then
                    continue
                else
                    if [[ ${part_name} == "misc" ]];then
                        continue
                    fi
                    cyan "### Copy ${part_name}:${image_name} files ###"
                    magenta "----------------------------------"
                    if [[ "fastboot recovery2 boot2" == *${part_name}* ]] && [ ${chip_name_num} -ne 1 ];then
                        cp ${PUBLISH_PATH}/${image_name} ${PUBLISH_PATH}/${image}
                    fi
                    cp ${PUBLISH_PATH}/${image_name} ${images_path}/
                fi

            done < ${PARTINFO_CONF}

            #=================================================
            ###
            ### make mlcverify image ###
            ###
            # 编译 mlcverify images
            if [[ ${make_mlcverify_flag} == y ]]
            then
                cyan "### Create for mlcverify.img ###"
                verify_partition=${OUT}/on-project/pub/image/verify_partinfo.conf
                ${OUT}/build/tool/linux-x86/bin/mkmlcverify \
                    -v ${verify_partition} \
                    -p ${PARTINFO_CONF}\
                    -i ${PUBLISH_PATH} \
                    -o ${PUBLISH_PATH}/mlcverify.img
                cp ${PUBLISH_PATH}/mlcverify.img ${images_path}/
            fi

            #=================================================
            ###
            ### supplement hitools use emmc.xml/nand.xml ###
            ###
            cyan "### supplement nand.xml/emmc.xml###"
            magenta "----------------------------------"
            echo '</Partition_Info>' >> ${images_path}/${chip_name}${xmlname}

            #===================================================
            if [[ "y" == ${Partition_User} ]];then
                cyan "### Create Empty For Partitions ###"
                magenta "----------------------------------"
                # Create_User_partition 函数是
                Create_User_Partition ${PARTINFO_CONF}
                magenta "----------------------------------"
            fi

            #=================================================
            ###
            ### make product image ###
            ###
            if [[ "y" == ${mk_productimage} ]]
            then
                cyan "uimages creatory"
                magenta "---------------------------------"
                uimages_creator ${flash} ${PARTINFO_TYPE}

                if [ "${flash}" == "emmc" ]
                then
                    cyan "### Create product.img ###"
                    magenta "---------------------------------"
                    ${TOP}/platform/build/tool/linux-x86/bin/swmakemmcimg -f ${PUBLISH_PATH} -c ${PARTINFO_CONF} -o ${PUBLISH_PATH}/productimg-${chip_name}-${build_name_flag}${WIPEDATA_FLAG}-${PARTINFO_TYPE%.conf*}.img
                    zip -j ${PUBLISH_PATH}/productimg-${chip_name}-${build_name_flag}${WIPEDATA_FLAG}-${PARTINFO_TYPE%.conf*}.zip ${PUBLISH_PATH}/productimg-${chip_name}-${build_name_flag}${WIPEDATA_FLAG}-${PARTINFO_TYPE%.conf*}.img
                    rm ${PUBLISH_PATH}/productimg-${chip_name}-${build_name_flag}${WIPEDATA_FLAG}-${PARTINFO_TYPE%.conf*}.img
                fi
            fi

            make_num=$[${make_num}+1]
        done
        cyan "### zip images path ###"
        magenta "----------------------------------"
        zip -j ${images_path}-cmdc-shandong.zip ${images_path}/*
        rm -rf ${images_path}
    done
    rm -rf ${zip_root}
}

#=================================================
###
### Main Logic
###
#=================================================
	###
	### target-xxoo.zip
	###
	# 从 BUILD_ID_MK 文件中读取 BUILD_ID 的值并赋给 build_id
    build_id=$(Read_Value ${BUILD_ID_MK} BUILD_ID)
    # 从 BUILD_ID_MK 文件中读取 PROJECT_TAG 的值并赋给 project_tag
	project_tag=$(Read_Value ${BUILD_ID_MK} PROJECT_TAG)
	# 如果 project_tag 的值不为空，则将该值转换成 -${project_tag}
	if [ "${project_tag}" != "" ]
	then
		project_tag="-${project_tag}"
    fi
    # 从 BUILD_ID_MK 文件中读取 BUILD_NUMBER 的值并赋给 build_number
    build_number=$(Read_Value ${BUILD_ID_MK} BUILD_NUMBER)
    # 根据 build_number 的值设置 target_name 变量的值为 target-${build_number}
	target_name="target-${build_number}"
	# 设置压缩包的根目录路径
	zip_root="${OUT}/${OUT_DIR}/${TARGET}/${target_name}"
	echo "zip_root [${zip_root}]"
	# 创建压缩包目录
	mkdir -p ${zip_root}
	echo

    ### Read flags form build_id.mk ###
    # 从 BUILD_ID_MK 文件中读取 BUILD_PRODUCT_IMAGE 的值，并赋给 mk_productimage
    mk_productimage=$(Read_Value ${BUILD_ID_MK} BUILD_PRODUCT_IMAGE)
  	# 将 mk_productimage 的值赋给 MK_PRODUCTIMAGE，并将其导入环境变量中
    export MK_PRODUCTIMAGE=${mk_productimage}
    # 如果 mk_productimage 的值为 y，则设置 mk_productimage_flag 的值为空，
    # 否则设置为 "-s"
	if [[ ${mk_productimage} == "y" ]]
	then
		mk_productimage_flag=""
	else
		mk_productimage_flag="-s"
	fi

	### Read flags form build_id.mk ###
	# 从 BUILD_ID_MK 文件中读取 WIPE_DATA 的值，并将其赋给 wipedata
    wipedata=$(Read_Value ${BUILD_ID_MK} WIPE_DATA)
    # 如果 wipedata 的值为 y，则设置 WIPEDATA_FLAG 为 _erase，否则设置为空
	if [[ ${wipedata} == "y" ]]
	then
		WIPEDATA_FLAG="_erase"
	else
		WIPEDATA_FLAG=""
	fi

	### Read flags form build_id.mk ###
	# 从 BUILD_ID_MK 文件中读取 TIME_TAG 的值，并将其赋给 timetag
    timetag=$(Read_Value ${BUILD_ID_MK} TIME_TAG)
    # 如果 timetag 的值为 y，则设置 TIMETAG_FLAG 的值为 -${Time}，否则设置为空
    # Time 变量已在上面定义
	if [[ ${timetag} == "y" ]]
	then
	    TIMETAG_FLAG="-${Time}"
	else
		TIMETAG_FLAG=""
	fi

	### Read flags form build_id.mk ###
	# 从 BUILD_ID_MK 文件中读取 STRICT_UPGRADE 的值，并将其赋给 strictupgrade
    strictupgrade=$(Read_Value ${BUILD_ID_MK} STRICT_UPGRADE)
    # 如果 strictupgrade 的值为 y，则设置 STRICT_UPGRADE_FLAG 的值为 -q，否则设置为空
	if [[ ${strictupgrade} == "y" ]]
	then
	    STRICT_UPGRADE_FLAG="-q"
	else
		STRICT_UPGRADE_FLAG=""
	fi

	### Read flags form build_id.mk ###
	# 从 BUILD_ID_MK 文件中读取 BUILD_EMPTY_PARTITIONS 和 BUILD_USER_PARTITIONS
	# 的值，并赋给 Partition_Flag 和 Partition_User
    Partition_Flag=$(Read_Value ${BUILD_ID_MK} BUILD_EMPTY_PARTITIONS)
	Partition_User=$(Read_Value ${BUILD_ID_MK} BUILD_USER_PARTITIONS)
	# 如果 Partition_User 的值为 y，则设置 Partition_Flag 的值为 n
	if [ "${Partition_User}" == "y" ];then
		Partition_Flag=n
	fi
	echo "Partition_Flag: ${Partition_Flag}"
	echo "Partition_User: ${Partition_User}"

	### Read flags form build_id.mk ###
	# 从 BUILD_ID_MK 文件中读取 PROJECT_SECURITY 的值，并赋给 project_security_flag
    project_security_flag=$(Read_Value ${BUILD_ID_MK} PROJECT_SECURITY)
    # 根据 project_security_flag 的值设置秘钥的路径
	if [[ ${project_security_flag} == "y" ]]
	then
	    SECURITY_KEY=${OUT}/on-project/build/security/testkey
	else
	    SECURITY_KEY=${OUT}/build/tool/security/testkey
	fi
	# 如果秘钥pk8文件不存在，则打印错误信息，并停止编译
	if [[ ! -f ${SECURITY_KEY}.pk8 ]];then
		echo "No security key file: ${SECURITY_KEY}.pk8"
		exit 1
	fi
	echo "SECURITY_KEY=${SECURITY_KEY}"

#=====================================================
# set envionment variables to OTA
#=====================================================
	# 从 BUILD_ID_MK 文件中读取对应的值，并赋予对应的变量，然后再将变量导入环境变量中
	export PROCESS_TIME_SYSTEM=$(Read_Value ${BUILD_ID_MK} PROCESS_TIME_SYSTEM)
	export UPDATE_RECOVERY=$(Read_Value ${BUILD_ID_MK} UPDATE_RECOVERY)
    export UPDATE_BACKUP=$(Read_Value ${BUILD_ID_MK} UPDATE_BACKUP)
    export WIPE_CACHE=$(Read_Value ${BUILD_ID_MK} WIPE_CACHE)
    export WIPE_SWDB=$(Read_Value ${BUILD_ID_MK} WIPE_SWDB)
    export QTEL_CUSTOM=$(Read_Value ${BUILD_ID_MK} QTEL_CUSTOM)
    telecom_ca=$(Read_Value ${BUILD_ID_MK} TELECOM_CA)
    security_l3=$(Read_Value ${BUILD_ID_MK} SECURITY_L3)

    make_num=0
    # 遍历芯片名，并编译对应芯片的相关镜像文件
    for chip_name in ${chip_name_array[*]}
    do
    	# 根据芯片名的数量，设置编译生成后的镜像文件名称
        if [ ${chip_name_num} -eq 1 ];then
            chip_name=""
            BOOT_FILE=${PUBLISH_PATH}/boot.img
            RECOVERY_FILE=${PUBLISH_PATH}/recovery.img
        else
            BOOT_FILE=${PUBLISH_PATH}/boot_${chip_name}.img
            RECOVERY_FILE=${PUBLISH_PATH}/recovery_${chip_name}.img
        fi
        # 拷贝工程文件
        copy_project_file
        # 编译 bootimg
        make_bootimg
        # 编译 recoveryimg
        make_recoveryimg
        # 如果 telecom_ca 的值为 y，则判断 security_l3 的值；
        # 如果 security_l3 的值为 r，则将 BOOT_FILE 和 RECOVERY_FILE 文件压缩成 ready.zip文件，
        # 否则调用 call_telecom_ca 函数
        if [[ ${telecom_ca} == "y" ]];then
            if [[ ${security_l3} == "r" ]];then
                green "ready don't signature boot.img and recovery.img, stop compile!"
                green "zip ready.zip ..."
                zip -j ${PUBLISH_PATH}/ready.zip ${BOOT_FILE} ${RECOVERY_FILE}/
            else
                call_telecom_ca
            fi
        fi

        make_num=$[${make_num}+1]
    done
    # 如果 telecom_ca 为 y，且security_l3 为 r，则编译完成。
    if [[ ${telecom_ca} == "y" && ${security_l3} == "r" ]];then
        green "zip ready.zip sunccess!!"
        exit 0
    fi
    # 编译 logoimg
    make_logoimg
    # 编译 ota_package
    make_ota_package
    # 编译 images
    make_images
    # 如果 project_later 设置的脚本文件存在，则执行该脚本文件
    if [ -f ${project_later} ]
	then
        magenta "----------------------------------"
		cyan "execution project_later.sh"
		. ${project_later} 
        magenta "----------------------------------"
	fi
    green "Compile the complete"


```

