[toc]

### 1. 消息对话框

```shell
dialog --title "Questionnaire" --msgbox "Welcome to my simple survey" 9 18
```

### 2. 复选框对话框

```shell
dialog --title "Check me" --checklist "Pick Numbers" 15 25 3 1 "one" "off" 2 "two" "on" 3 "three" "off"
```

获取对话框选择结果：

```shell
#!/bin/sh
dialog --title "Check me" --checklist "Pick Numbers" 15 25 3 1 "one" "off" 2 "two" "on" 3 "three" "off" 2> result.txt
dialog --clear
selects=$(cat result.txt)
echo $selects
```

### 3. 是/否对话框

```shell
#!/bin/sh
dialog --title "Confirm" --yesno "Are you willing to take part?" 9 18
if [ $? != 0 ]; then
	dialog --infobox "Thank you anyway" 5 20
	sleep 2
	dialog --clear
	exit 0
fi
```

### 4. 输入对话框

```shell
#!/bin/sh
dialog --title "Questionnaire" --inputbox "Please enter your name" 9 30 2> _1.txt
Q_NAME=$(cat _1.txt)
echo $Q_NAME
```

### 5. 菜单对话框

```shell
#!/bin/sh
dialog --menu "Jone, what music do you like best?" 15 30 4 1 "Classical" 2 "Jazz" 3 "Country" 4 "Other" 2>_1.txt
Q_MUSIC=$(cat _1.txt)
echo $Q_MUSIC
```

