```shell

#Read_Value build_id.mk BUILD_ID
# 该函数的功能如下：
# -F:= 设置分隔符为 :=
# -v val="${val_name} " 设置变量 val 的值为 "${val_name} "
# awk -F:= -v val="${val_name} " '$1==val {print val $2}' "${input_file}":
# 从 ${input_file} 文件中读取数据，如果 $1 的值等于 val 的值，那么打印 $2 的值
function Read_Value
{
	input_file=$1
	val_name=$2

	value=$(awk -F:= -v val="${val_name} " '$1==val {print val $2}' "${input_file}" | awk '{print $2}')
	echo ${value}
}

# 该函数功能是：
# 获取读取变量值为数组的值
function Read_Array_Value
{
	local input_file=$1
	local val_name=$2
	local value=""
	
	# 比如在 build_id.mk 文件中存在一个数据：PRE_BUILD_NUMBER_ARRAY := [002.460.056 002.460.057 002.460.071]
	# val_name 的值为 PRE_BUILD_NUMBER_ARRAY
	# 执行下面语句后得到的数据是：
	# "[002.460.056 002.460.057 002.460.071]"
	value=$(awk -F:= -v val="${val_name} " '$1==val {print $2}' "${input_file}")
	value=$(echo ${value})
	# ${value:0:1} 获取 value 的第一个字符，${value:0-1:1} 获取 value 的最后一个字符
	if [[ "${value:0:1}" == "[" && "${value:0-1:1}" == "]" ]];then
		# 执行下面命令后可以得到: 002.460.056 002.460.057 002.460.071
		value=${value:1}
		value=${value:0:-1}
	fi
	echo ${value}
}

# 该函数未使用
function Read_Build_Number
{
	build_number=$(awk -F:= '$1=="BUILD_NUMBER " {print "BUILD_NUMBER "$2}' "${1}" | awk '{print $2}')
	echo ${build_number}
}

# 该函数未使用
function Read_Build_Id
{
	build_id=$(awk -F:= '$1=="BUILD_ID " {print "BUILD_ID "$2}' "${1}" | awk '{print $2}')
	echo ${build_id}
}

# 该函数的功能是：
# 将传递过来的参数使用 on-project\/${PROJECT_NAME} 替换
# 掉参数中的 on-project，然后再检查该参数对应的文件是否存在，
# 如果存在，则返回修改过的参数，否则返回原始参数
function Get_Project_File()
{
	local project_file=${1/on-project/on-project\/${PROJECT_NAME}}
	if [ -f $project_file ];then
		echo $project_file
	else
		echo $1
	fi
}

```

