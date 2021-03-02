#!/bin/bash

# 显示帮助文档
function showHelper() {
    echo "usage: push [--auto][--help][--retry=<times>]"
    echo "The following is a description of these named functions:"
    echo "    --auto, -a        automatic code submission"
    echo "    --help, -h        output help information"
    echo "    --retry=<times>   set the number of retries for failed submissions"
    echo ""
}

# 手动提交代码
function submitManually() {
    git st 2>&1
    read -p ":" var
    return 1
}

function main() {
    # 脚本执行状态
    status=0
    # 是否自动提交仓库
    auto=0
    # 是否是打印帮助信息
    isHelp=0
    # 失败重试次数
    retryTimes=0
    # 处理脚本参数
    for arg in $@; do
        case $arg in
            '--auto' | '-a')
                auto=1
                ;;
            "--retry="*)
                retryTimes=`echo $arg | tr -cd "[0-9]"`
                ;;
            '--help' | '-h')
                showHelper
                isHelp=1
                ;;
        esac
    done
    # 如果是打印帮助信息则直接退出
    if [ $isHelp -eq 1 ];then
        return 0
    fi
    # 执行 git st 命令，并将命令的输出内容保存到 statusResult 变量中
    statusResult=`git status 2>&1`
    # 仓库没有任何修改时，git st 命令输出会包含的内容
    noChange='nothing to commit, working tree clean'
    # 如果在不是仓库的目录下执行 git st 命令，输出会包含的内容
    notRepository='not a git repository'
    # 判断仓库是否有修改
    if [[ $statusResult == *$noChange* ]]; 
    then
        echo -e "\e[1;32m仓库没有文件改变，不需要操作\e[0m"
        status=0
    elif [[ $statusResult == *$notRepository* ]]; 
    then
        echo -e "\e[1;31m当前目录不是一个仓库\e[0m"
    else
        echo -e "\e[1;33m仓库文件有修改\e[0m"
        if [ $auto -eq 1 ];then
            echo -e "\e[1;32m开始自动提交代码\e[0m"
        else
            echo -e "\e[1;33m没有设置自动提交代码，需要手动执行提交，请按提示操作\e[0m"
            submitManually
            status=$?
        fi
    fi

    # 输出执行结果
    if [ $status -eq 0 ];then
        echo -e "\n\e[1;32m================ 仓库提交成功 ================\e[0m"
    else
        echo -e "\n\e[1;31m================仓库提交失败 ================\e[0m"
    fi

    # git add -A
    # git commit -m "添加笔记"
    # echo "开始更新仓库...."
    # git pull --rebase
    # pullStatus = $?
    # echo "开始上传代码至Gitee远程仓库...."
    # git push origin
    # echo "开始上传代码至Github远程仓库...."
    # git push Github
    # echo "开始上传代码至Gitlab远程仓库...."
    # git push GitLab
}

# 执行脚本
main $@;
