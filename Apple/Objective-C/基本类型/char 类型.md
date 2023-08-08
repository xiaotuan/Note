在 `Objective-C` 程序中，`char` 类型变量的功能是存储单个字符，只要将字符放到一对单引号中就是字符常量。例如 `'a'`。

在 `NSLog`调用中，可以使用格式字符 `%c` 来显示 `char` 变量的值。

```objc
int main(int argc, const char * argv[]) {
    @autoreleasepool {
        char charVar = 'W';
        NSLog(@"charVar = %c", charVar);
    }
    return 0;
}
```

另外，使用 `char` 也可以表示字符变量，例如：

```objc
char a, b;
```

每个字符变量被分配一个字节的内存空间，因此只能存放一个字符。字符值是以 `ASCII` 码的形式存放在变量的内存单元之中的。例如：

```objc
a = 'x';
b = 'y';
```

`Objective-C` 语言允许对整型变量赋予字符值，也允许对字符变量赋予整型值。在输出时，允许把字符变量按整型变量输出，也允许把整型量按字符量输出。当整型量按字符型量处理时，只对低 8 位进行处理。

### 1. 字符常量

在 `Objective-C` 程序中，字符常量是用单引号括起来的一个字符，例如：

```
'a'
'='
'?'
```

在 `NSLog` 中显示字符变量时，当格式符为 `%c` 时，对应输出的变量值为字符，当格式符为 `%i` 时，对于输出的变量值为整数，例如：

```objc
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        char charVar = 'W';
        NSLog(@"charVar = %c", charVar);
        NSLog(@"charVar = %i", charVar);
    }
    return 0;
}
```

运行结果如下：

```
charVar = W
charVar = 87
```

