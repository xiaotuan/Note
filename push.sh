#!/bin/bash
git st
git add -A
git commit -m "添加笔记"
echo "开始更新仓库...."
git pull --rebase
pullStatus = $?
echo "开始上传代码至Gitee远程仓库...."
git push origin
echo "开始上传代码至Github远程仓库...."
git push Github
echo "开始上传代码至Gitlab远程仓库...."
git push GitLab
