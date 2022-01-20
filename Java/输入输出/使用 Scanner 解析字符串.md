可以构造一个带有字符串参数的 `Scanner`，但这个 `Scanner` 将字符串解释为数据而不是文件名：

```java
import java.util.Scanner;

Scanner in = new Scanner("myfile.txt");
```

这个 `Scanner` 会将参数作为包含 10 个字符的数据：'m'，'y'，'f' 等。