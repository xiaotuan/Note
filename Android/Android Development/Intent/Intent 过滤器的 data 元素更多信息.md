可以通过 <https://developer.android.google.cn/guide/topics/manifest/data-element.html>，查看 `Intent` 过滤器的 `data` 元素的 XML 定义。Intent 过滤器节点 data XML 子节点的子元素或特性包括：

+   `android:host`

    URI 授权方的主机部分。除非也为过滤器指定了 `scheme` 属性，否则此属性没有意义。要匹配多个子网域，请使用星号 (`*`) 匹配主机中的零个或多个字符。例如，主机 `*.google.com` 匹配 `www.google.com`、`.google.com` 和 `developer.google.com`。

    星号必须是主机属性的第一个字符。例如，主机 `google.co.*` 无效，因为星号通配符不是第一个字符。

    >   **注意**：Android 框架中的主机名匹配区分大小写，这一点与正式的 RFC 不同。因此，您应始终使用小写字母指定主机名。

+   `android:mimeType`

    MIME 媒体类型，如 image/jpeg 或 audio/mpeg4-generic。子类型可以是星号通配符 (*)，以指示任何子类型都匹配。
    Intent 过滤器经常会声明仅包含 android:mimeType 属性的 \<data>。

    >   **注意**：Android 框架中的 MIME 类型匹配区分大小写，这一点与正式的 RFC MIME 类型不同。因此，您应始终使用小写字母指定 MIME 类型。

+   `android:port`

    URI 授权方的端口部分。仅当同时为过滤器指定了 `scheme` 和 `host` 属性时，此属性才有意义。

+   `android:path`

+   `android:pathPattern`

+   `android:pathPrefix`

    URI 的路径部分，必须以 / 开头。`path` 属性指定与 Intent 对象中的完整路径匹配的完整路径。`pathPrefix` 属性指定只与 Intent 对象中的路径的初始部分匹配的部分路径。`pathPattern` 属性指定与 Intent 对象中的完整路径匹配的完整路径，但它可以包含以下通配符：

    -   星号（“`*`”）匹配出现零次到多次的紧邻前面的字符的一个序列。
    -   句点后跟星号（“`.*`”）匹配零个到多个字符的任意序列。

    由于在从 XML 读取字符串时（在将其解析为模式之前）将“`\`”用作转义字符，因此您需要进行双重转义。例如，字面量“`*`”将编写为“`\\*`”，字面量“”将编写为“`\\\\`”。这基本上与采用 Java 代码构造字符串时需要编写的内容一样。

    如需详细了解这三种类型的模式，请参阅 `PatternMatcher` 类中的 `PATTERN_LITERAL`、`PATTERN_PREFIX` 和 `PATTERN_SIMPLE_GLOB` 的说明。

    仅当同时为过滤器指定了 `scheme` 和 `host` 属性时，这些属性才有意义。

+   `android:scheme`

    URI 授权方的主机部分。除非也为过滤器指定了 `scheme` 属性，否则此属性没有意义。要匹配多个子网域，请使用星号 (`*`) 匹配主机中的零个或多个字符。例如，主机 `*.google.com` 匹配 `www.google.com`、`.google.com` 和 `developer.google.com`。

    星号必须是主机属性的第一个字符。例如，主机 `google.co.*` 无效，因为星号通配符不是第一个字符。

    >   **注意**：Android 框架中的主机名匹配区分大小写，这一点与正式的 RFC 不同。因此，您应始终使用小写字母指定主机名。