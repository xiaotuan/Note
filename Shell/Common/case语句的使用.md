case 的语法格式如下所示：

```shell
case 值 in
	模式1)
		command1
		command2
		;;
		
	模式2)
		command3
		command4
		;;
	*)
		command5
		command6
		;;
esac
```

例如：

```shell
function main() {
    # 上一个参数
    lastArg=""
    # 遍历脚本参数
    for arg in $@
    do
        # 解析脚本参数
        case $arg in
            # 适配所有以 --开头的字符串
            --*)
                if [[ $arg = "--help" ]];then
                    showHelper
                    lastArg="-h"
                else 
                    echo "Error: unknown command $arg"
                    return -1
                fi
                ;;

            # 适配所有以 - 开头的字符串
            -*)
                if [[ $arg = "-h" ]];then
                    showHelper
                fi
                lastArg=$arg
                ;;

            # 适配所有不以 - 或 -- 开头的字符串
            *)
                echo $arg
                ;;
        esac
    done

}
```

可以使用匹配模式 `|` 和 `*`，`|` 表示或，`*` 表示匹配任何字符。

例如：

```shell
function main() {
    # 上一个参数
    lastArg=""
    # 遍历脚本参数
    for arg in $@
    do
        # 解析脚本参数
        case $arg in
            --help | -h)
                showHelper
                ;;

            # 适配所有不以 - 或 -- 开头的字符串
            *)
                echo $arg
                ;;
        esac
    done

}
```

