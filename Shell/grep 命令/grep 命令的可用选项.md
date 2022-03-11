| 选项 | 含义                                             |
| ---- | ------------------------------------------------ |
| -c   | 输出匹配行的数目，而不是输出匹配的行             |
| -E   | 启用扩展表达式                                   |
| -h   | 取消每个输出行的普通前缀，即匹配查询模式的文件名 |
| -i   | 忽略大小写                                       |
| -l   | 只列出包含匹配行的文件名，而不输出真正的匹配行   |
| -v   | 对匹配模式取反，即搜索不匹配行而不是匹配行       |

例如：

```shell
$ grep in words.txt
When shall we three meet again. In thunder, lightning, or in rain?
I come, Graymalkin!
$ grep -c in words.txt words2.txt
words.txt:2
words2.txt:14
$ grep -c -v in words.txt words2.txt
words.txt:9
words2.txt:16
$
```

