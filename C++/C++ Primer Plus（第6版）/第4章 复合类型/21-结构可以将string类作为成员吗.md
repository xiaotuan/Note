### 4.4.3　结构可以将string类作为成员吗

可以将成员name指定为string对象而不是字符数组吗？即可以像下面这样声明结构吗？

```css
#include <string>
struct inflatable // structure definition
{
    std::string name;
    float volume;
    double price;
};
```

答案是肯定的，只要您使用的编译器支持对以string对象作为成员的结构进行初始化。

一定要让结构定义能够访问名称空间std。为此，可以将编译指令using移到结构定义之前；也可以像前面那样，将name的类型声明为std::string。

