**AIDL 中支持的数据类型**

| 支持类型 | 需要 import? | 备注 |
| :- | :- | :- |
| Java基本类型 | 不需要 import | |
| String | 不需要 import | |
| CharSequence | 不需要 import |  |
| List | 不需要 import | List 内的元素必须是 AIDL 支持的类型；List接收方必须是 ArrayList；|
| Map | 不需要 import | Map 内的元素必须是 AIDL 支持的类型；Map 接收方必须是 HashMap |
| 其他 AIDL 定义的 AIDL 接口 | 需要 import | 传递的是引用 |
| 实现 Parcelable 的类 | 需要 import | 值传递 |

> 注意：
>
> 如果参数是 List、Map 和 实现 Parcelable 的类，则必须在参数前加入 in 、out 或 inout 中的一个修饰符。
>
> **in**：表示该参数是输入型参数。接收方只能读不能写。
>
> **out**：表示该参数是输出型参数，接收方只能写不能读。
>
> **inout**：表示该参数是输入输出型参数，接收方可以读写。