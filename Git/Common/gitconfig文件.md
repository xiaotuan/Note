**Ubuntu 的 .gitconfig 文件**

```
[user]
	name = qintuanye
	email = qin_ty@chinaxuhu.com
[core]
	editor = gedit
	filemode = false
[color]
	status = auto
	branch = auto
	diff = auto
	ui = true
	pager = true
[color "branch"]
	current = yellow reverse
	local = yellow
	remote = green
[color "diff"]
	meta = yellow bold
	frag = magenta bold
	old = red bold
	new = green bold
[color "status"]
	added = yellow
	changed = green
	untracked = cyan
[diff]   
    tool = bc3
[difftool "bc3"]   
    cmd = /usr/bin/bcompare \"$LOCAL\" \"$REMOTE\"   
[difftool]   
    prompt = false   
[merge]
    tool = bc3

[mergetool "bc3"]
    cmd = bcompare \
    "$PWD/$LOCAL" \
    "$PWD/$REMOTE" \
    "$PWD/$BASE" \
    "$PWD/$MERGED"
    keepBackup = false
    trustExitCode = false

[alias]
	lg = log --color --graph --date=short --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen (%ci) %C(bold blue)<%an>%Creset' --abbrev-commit
	st = status
	df = difftool
	lgfile = log --color --graph --date=short --name-status --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen (%ci) %C(bold blue)<%an>%Creset' --abbrev-commit
	lgme = log --color --graph --date=short --author=swpub92 --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen (%ci) %C(bold blue)<%an>%Creset' --abbrev-commit 
	lgfileme = log --color --graph --date=short --name-status --author=swpub92 --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen (%ci) %C(bold blue)<%an>%Creset' --abbrev-commit 
	shfile = show --graph --date=short --name-only  --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen (%ci) %C(bold blue)<%an>%Creset' --abbrev-commit 

[gui]
	recentrepo = /media/F/lpingsheng_share/S980_Debug

[receive]
	denyCurrentBranch = ignore
[push]
	default = simple

```

**Windows 的 .gitconfig 文件**

```shell
[user]
	name = xiaotuan
	email = 583168425@qq.com
	
[color]
	status = auto
	branch = auto
	diff = auto 
	ui = true
	pager = true
	
[color "branch"]
	current = yellow reverse
	local = yellow
	remote = green
	
[color "diff"]
	meta = yellow bold
	frag = magenta bold
	old = red bold
	new = green bold
	
[color "status"]
	added = yellow
	changed = green
	untracked = cyan
	
[gui]
encoding = utf-8
[i18n]
commitencoding = utf-8
[svn]
pathnameencoding = utf-8

#使用beyond compare来查看文件差异
[diff]
#对比工具名称,必须与difftool项里的名称保持一致
tool = bc4
[difftool "bc4"]
#beyond compare路径和调用命令
#$REMOTE 表示commit之后的文件
#LOCAL 表示commit到git的文件
cmd = "\"C:/program files/Beyond Compare 4/BComp.exe\" \"$LOCAL\" \"$REMOTE\""
#合并分支
[merge]
#对比工具名称,必须与mergetool项里的名称保持一致
tool = bc4
[mergetool]
prompt = false
[mergetool "bc4"]
#beyond compare路径和调用命令
cmd = "\"C:/program files/Beyond Compare 4/BComp.exe\" \"$LOCAL\" \"$REMOTE\" \"$BASE\" \"$MERGED\""

[alias]
	lg = log --color --graph --date=short --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen (%ci) %C(bold blue)<%an>%Creset' --abbrev-commit
	st = status
	df = difftool
	lgfile = log --color --graph --date=short --name-status --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen (%ci) %C(bold blue)<%an>%Creset' --abbrev-commit
	lgme = log --color --graph --date=short --author=swpub92 --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen (%ci) %C(bold blue)<%an>%Creset' --abbrev-commit 
	lgfileme = log --color --graph --date=short --name-status --author=swpub92 --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen (%ci) %C(bold blue)<%an>%Creset' --abbrev-commit 
	shfile = show --graph --date=short --name-only  --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen (%ci) %C(bold blue)<%an>%Creset' --abbrev-commit 
	
[receive]
	denyCurrentBranch = ignore
[push]
	default = simple
```
