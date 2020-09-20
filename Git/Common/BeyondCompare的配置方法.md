**Windows 系统的配置方法**

```
[alias]
    st = status
    df = difftool
        
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
    keepBackup = false
	trustExitCode = false
```

**Mac OS 系统的配置方法**

```
[alias]
	st = status
	df = difftool

[diff]
	tool = bc4

[difftool "bc4"]
	cmd = "\"/Applications/Beyond Compare.app/Contents/MacOS/bcomp\" \"$REMOTE\" \"$LOCAL\""

[merge]
	tool = bc4
	
[mergetool]
	prompt = false

[mergetool "bc4"]
	cmd = "\"/Applications/Beyond Compare.app/Contents/MacOS/bcomp\" \"$REMOTE\" \"$BASE\" \"$LOCAL\""
	keepBackup = false
	trustExitCode = false
```

