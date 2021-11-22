<center><b>活动类别及其说明</b></center>

| 类别名称                      | 说明                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| CATEGORY_DEFAULT              | 此类活动可以将自身声明为 DEFAULT 活动，以供隐式 Intent 调用，如果未为活动定义此类别，那么每次都需要通过该活动的类名显示调用它。这就是会看到通过一般操作或其他操作名称来调用的活动使用默认类别规范的原因 |
| CATEGORY_BROWSABLE            | 此类活动可以将自身声明为 BROWSABLE，方法是向浏览器承诺它启动后不会影响浏览器安全 |
| CATEGORY_TAB                  | 此类活动可以嵌入在带选项卡的父活动中                         |
| CATEGORY_ALTERNATIVE          | 对于正在查看的某些数据类型，此类活动可以将自身声明为 ALTERNATIVE 活动。在查看文档时，这些项目通常显示为选项菜单的一部分。例如，打印视图被视为常规视图的替代视图 |
| CATEGORY_SELECTED_ALTERNATIVE | 对于某些数据类型，此类活动可以将自身声明为 ALTERNATIVE 活动。这类似于为文本文档或 HTML 文档列出一系列可用的编辑器 |
| CATEGORY_LAUNCHER             | 如果将此类别分配给一个活动，可以在启动屏幕上列出该活动       |
| CATEGORY_HOME                 | 此类活动表示主屏幕。通常，应该只有一个这种类型的活动。如果有多个，系统将提示挑选一个 |
| CATEGORY_PREFERENCE           | 此活动将一个活动标识为首选活动，这样该活动就会显示在首选项屏幕上 |
| CATEGORY_GADGET               | 此类活动可以嵌入到父活动中                                   |
| CATEGORY_TEST                 | 测试活动                                                     |
| CATEGORY_EMBED                | 此类别已由 GADGET 类别取代，但为了实现向后兼容性，它仍然保留了下来 |

要了解这些活动类别的详细信息，可以访问 <https://developer.android.google.cn/android/reference/android/content/Intent.html#CATEGORY_ALTERNATIVE>。