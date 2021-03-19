实现代码如下所示：

```java
import java.io.*;
import java.util.zip.CRC32;
import java.util.zip.CheckedInputStream;

public class CRC32Utils {

    /**
     * 通过 BufferedInputStream 方式获取文件的 CRC32 值
     * @param filePath  文件路径
     * @return  文件的 CRC32 值
     * @throws IOException 当文件不存在或者打开失败时，抛出异常
     */
    public static long getCRC32ByBis(String filePath) throws IOException {
        InputStream is = new BufferedInputStream(new FileInputStream(filePath));
        CRC32 crc32 = new CRC32();
        byte[] bytes = new byte[1024];
        int cnt;
        while ((cnt = is.read(bytes)) != -1) {
            crc32.update(bytes, 0, cnt);
        }
        is.close();
        return crc32.getValue();
    }

    /**
     * 通过 CheckedInputStream 方式获取文件的 CRC32 值
     * @param filePath 文件路径
     * @return 文件的 CRC32 值
     * @throws IOException 当文件不存在或者打开失败时，抛出异常
     */
    public static long getCRC32ByCis(String filePath) throws IOException {
        CRC32 crc32 = new CRC32();
        FileInputStream fis = new FileInputStream(new File(filePath));
        CheckedInputStream cis = new CheckedInputStream(fis, crc32);
        byte[] buffer = new byte[1024];
        while (cis.read(buffer) != -1) {

        }
        cis.close();
        return crc32.getValue();
    }
}
```

> 提示：
>
> 上面两个方法都可以计算文件的 CRC32 值，但是 getCRC32ByBis() 方法比 getCRC32ByCis() 快，推荐使用 getCRC32ByBis() 方法，下面是使用两个方法计算文件 CRC32 值的结果：
>
> ```console
> # 使用 getCRC32ByBis() 方法的耗时
> CRC32: 33C35FBF, 用时：381 ms
> # 使用 getCRC32ByCis() 方法的耗时
> CRC32: 33C35FBF, 用时：1339 ms
> ```