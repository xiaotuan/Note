```shell
# 文件位置：cmdc/small/platform/build/color
# tput setaf 命令设置终端文本前景色
# tput sgr0 命令清除所有该命令的设置
BLACK=$(tput setaf 0)
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
BLUE=$(tput setaf 4)
MAGENTA=$(tput setaf 5)
CYAN=$(tput setaf 6)
WHITE=$(tput setaf 7)
NORMAL=$(tput sgr0)

###
### Funcitons Define
###
# 以红色前景色打印参数
function red()
{
	echo -e "${RED} ${1} ${NORMAL}"
}
# 以绿色前景色打印参数
function green()
{
	echo -e "${GREEN} ${1} ${NORMAL}"
}
# 以黄色前景色打印参数
function yellow()
{
	echo -e "${YELLOW} ${1} ${NORMAL}"
}
# 以蓝色前景色打印参数
function blue()
{
	echo -e "${BLUE} ${1} ${NORMAL}"
}
# 以品红前景色打印参数
function magenta()
{
	echo -e "${MAGENTA} ${1} ${NORMAL}"
}
# 以青色前景色打印参数
function cyan()
{
	echo -e "${CYAN} ${1} ${NORMAL}"
}
# 输出帮助文档
function help()
{
	cat <<XXOO
		Usage: ${0} ${1}
XXOO
}

###
### Main Logic
###
#blue "blue font"
#red "red font"
#green "green font"
#yellow "yellow font"
#magenta "magenta font"
#cyan "cyan font"


```

