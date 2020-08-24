```shell

###
### Define Function
###
function Print
{
	echo " Create Partition [ ${1} ] [ size  $2 ]..."
}

function get_size
{
	part_name=$1
	conf_file=$2
	part_size=$(awk -v name="${part_name}" '$0 ~ "^" name {print $4}' ${conf_file})
	part_size=$(( ${part_size} * 1024 * 1024 ))
	echo $part_size
}

function get_type
{
	part_name=$1
	conf_file=$2
	part_type=$(awk -v name="${part_name}" '$0 ~ "^" name {print $2}' ${conf_file})
	echo $part_type
}

function judge_flash_partition
{
  part_conf=$1
  while read line
	do
		fs_type=$(echo ${line} | awk '{print $2}')
		if [ "${fs_type}" == "ubifs" ]
		then
			flash="nand"
			break
		elif [ "${fs_type}" == "ext4" ]
		then
			flash="emmc"
			break
		else
			continue
			fi
	done < ${PARTINFO_CONF}
	echo $flash

}
function Create_Normal_Partition
{
	size=$(get_size $1 $2)
	if [ "${size}" == "" ];then
		echo "Create Partition [ $1 ], get size failed! [ $2 ]"
		return 1
	fi

	mk_productimage=${MK_PRODUCTIMAGE}
	Print ${PUBLISH_PATH}/${1} ${size}
	mkdir -p ${PUBLISH_PATH}/${1}

	${OUT}/build/tool/linux-x86/bin/make_ext4fs ${mk_productimage_flag} \
		-l ${size} -a ${PUBLISH_PATH}/${1} \
		${PUBLISH_PATH}/${1}.img ${PUBLISH_PATH}/${1} 
	sleep 1 
	mv ${PUBLISH_PATH}/${1}.img ${PUBLISH_PATH}/${1}.ext4
    rm ${PUBLISH_PATH}/${1} -rf
}

function Create_backup
{
	backup_name=$1
	backup_size=$(get_size $1 $2)
	${OUT}/build/tool/linux-x86/bin/make_ext4fs \
		${mk_productimage_flag} -l ${backup_size} \
		-a ${backup_name} ${OUT}/${OUT_DIR}/obj/${backup_name}.img \
		${PUBLISH_PATH}/${backup_name}
	if [ "$?" != "0" ];then
		echo "make_ext4fs backup failed, make again with 16384 blocks per group"
		${OUT}/build/tool/linux-x86/bin/make_ext4fs \
			-b 2k \
			-l ${backup_size} \
			${OUT}/${OUT_DIR}/obj/${backup_name}.img \
			${PUBLISH_PATH}/${backup_name}
	fi
	sleep 1
	mv ${OUT}/${OUT_DIR}/obj/${backup_name}.img ${PUBLISH_PATH}/${backup_name}.ext4
	sleep 1
}
function Create_Partition
{
    part_name=$1
    part_conf=$2
    Nand_Block=$(Read_Value ${BUILD_ID_MK} NAND_BLOCK)
    Nand_Page=$(Read_Value ${BUILD_ID_MK} NAND_PAGE)
   	part_size=$(get_size ${part_name} ${part_conf})
	if [ "${part_size}" == "" ];then
		echo "Create Partition [ $1 ], get size failed! [ $2 ]"
		return 1
	fi

    if [ ${PROJECT_NAME} ];then
        ON_PROJECT_PATH=${TOP}/platform/on-project/${PROJECT_NAME}
    else
        ON_PROJECT_PATH=${TOP}/platform/on-project
    fi
	mk_productimage=${MK_PRODUCTIMAGE}
	Print ${PUBLISH_PATH}/${part_name} ${part_size}
    mkdir -p ${PUBLISH_PATH}/${part_name}
	if [ "${part_name}" == "qbdata" ];then
        cp -arlf ${OUT}/${OUT_DIR}/${TARGET}/${target_name}/QBDATA/* ${PUBLISH_PATH}/${part_name}
    elif [ "${part_name}" == "backup" ];then
        cp -arlf ${OTA_Full_Package_zip} ${PUBLISH_PATH}/backup/update.zip
    elif [ "${part_name}" == "system" ];then
        cp -arlf ${OUT}/${OUT_DIR}/${TARGET}/${target_name}/SYSTEM/* ${PUBLISH_PATH}/${part_name}
    elif [ "${part_name}" == "ctc" ];then
        cp -arlf ${OUT}/${OUT_DIR}/${TARGET}/${target_name}/CTC/* ${PUBLISH_PATH}/${part_name}
    elif [ "${part_name}" == "cache" ];then
        if [[ ${mk_productimage} == "y" ]]; then
            echo "copying files for product_version into cache"
            cp -arf ${zip_root}/CACHE/* ${PUBLISH_PATH}/cache/
            cp ${ON_PROJECT_PATH}/pub/swproduct/executeproducttest.txt ${PUBLISH_PATH}/${part_name}
            cp ${ON_PROJECT_PATH}/pub/swproduct/8192EU.txt ${PUBLISH_PATH}/${part_name}
            cp ${ON_PROJECT_PATH}/pub/swproduct/destEfuse.txt ${PUBLISH_PATH}/${part_name}
            if [[ ${vmx_ca} == "y" ]];then
                cp -rfp ${ON_PROJECT_PATH}/pub/swproduct/recovery/ ${PUBLISH_PATH}/${part_name}
            fi
        fi
    elif [ "${part_name}" == "swdb" ];then
        appver=$(Read_Build_Number ${BUILD_ID_MK})
        cp -arlf ${ON_PROJECT_PATH}/pub/swproduct/swdb/*  ${PUBLISH_PATH}/${part_name}
        echo "AppVersion=${appver}"  >> ${PUBLISH_PATH}/${part_name}/swproduct.inf
        if [[ ${CA_MARKET_ID} ]];then
            echo "MarketId=${CA_MARKET_ID}" >> ${PUBLISH_PATH}/${part_name}/swproduct.inf
        fi
    elif [ "${part_name}" == "userdata" ];then
        cp -arlf ${zip_root}/DATA/* ${PUBLISH_PATH}/${part_name}
    else
        if [ -f ${ON_PROJECT_PATH}/pub/${part_name} ];then
            cp -arlf ${ON_PROJECT_PATH}/pub/${part_name}/* ${PUBLISH_PATH}/${part_name}
        fi
    fi

    fs_type_flash=$(get_type $1 $2)
    if [ "${fs_type_flash}" == "ubifs" ]
    then 
        bash  ${TOP}/platform/build/tool/linux-x86/bin/mkubiimg.sh \
            ${TOP}/platform/build/tool/linux-x86/bin/  \
            ${PUBLISH_PATH}/${part_name} \
            ${Nand_Page} \
            ${Nand_Block}
	elif [ "${fs_type_flash}" == "ext4" ]
    then
        ${OUT}/build/tool/linux-x86/bin/make_ext4fs \
            ${mk_productimage_flag} -l ${part_size} \
            -a ${part_name} ${PUBLISH_PATH}/${part_name}.img \
            ${PUBLISH_PATH}/${part_name}
        sleep 1 
        mv ${PUBLISH_PATH}/${part_name}.img ${PUBLISH_PATH}/${part_name}.ext4
    else
        echo "ERROR: get fs type failed!"
	fi
    #rm -rf ${PUBLISH_PATH}/${part_name}
}

function Create_User_Partition
{
	part_conf=$1
	while read line
	do
        fs_type=$(echo ${line} | awk '{print $2}')
        if [ "${fs_type}" == "ext4" ] || [ "${fs_type}" == "ubifs" ];then
            part_name=$(echo ${line} | awk '{print $1}')
            Create_Partition ${part_name} ${part_conf}
        fi
	done < ${part_conf}
}

function Create_User_ubi_Partition
{
	part_conf=$1
    Nand_Page=$2
    Nand_Block=$3

	while read line
	do
		fs_type=$(echo ${line} | awk '{print $2}')
		if [ "${fs_type}" == "ubifs" ];then
			part_name=$(echo ${line} | awk '{print $1}')
            Create_Partition ${part_name} ${part_conf}
		fi
	done < ${part_conf}
}


###
### Main Logic
###

### FLASH Total Size 3728M

#Create "cache" "224"
#Create "userdata" "384"
#Create "data_dalvik" "256"
#Create "user_app" "1024"
#Create "swdb" "48"
#Create "backup" "248"

### SDCARD Size :  3728M - 2600M = 1128M

#Create "sdcard" "1024"





```

