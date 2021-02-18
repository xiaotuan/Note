#!/bin/bash

git st

git add -A

git commit -m "添加笔记"

git pull --rebase

git push origin

git push GitHub

git push Gitlab
