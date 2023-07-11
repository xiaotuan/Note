`Locale` 由多达 5 个部分构成：

1）一种语言，由 2 个或 3 个小写字母表示，例如 `en` （英语）、`de`（德语）和 `zh`（中文）。

<center><b>常见的 ISO-639-1语言代码</b></center>

| 语言      | 代码 | 语言         | 代码 |
| --------- | ---- | ------------ | ---- |
| `Chinese` | `zh` | `Italian`    | `it` |
| `Danish`  | `da` | `Japanese`   | `ja` |
| `Dutch`   | `nl` | `Korean`     | `ko` |
| `English` | `en` | `Norwegian`  | `no` |
| `French`  | `fr` | `Portuguese` | `pt` |
| `Finnish` | `fi` | `Spanish`    | `es` |
| `German`  | `de` | `Swedish`    | `sv` |
| `Greek`   | `el` | `Turkish`    | `tr` |

2）可选的一段脚本，由首字母大写的四个字母表示，例如 `Latn`（拉丁文）、`Cyrl`（西里尔文）和 `Hant`（繁体中文字符）。

3）可选的一个国家或地区，由 2 个大写字母或 3 个数字表示，例如 `US`（美国）和 `CH`（瑞士）。

4）可选的一个变体，用于指定各种杂项特性，例如方言和拼写规则。

5）可选的一个扩展。扩展描述了日历（例如日本历）和数字（替代西方数字的泰语数字）等内容的本地偏好。`Unicode` 标准规范了其中的某些扩展，这些扩展应该以 `u-` 和两个字母代码开头，这两个字母的代码指定了该扩展处理的是日历（`ca`）还是数字（`nu`），或者其他内容。

<center><b>常见的 ISO-3166-1 国家代码</b></center>

| 语言            | 代码 | 语言              | 代码 |
| --------------- | ---- | ----------------- | ---- |
| `Austria`       | `AT` | `Japan`           | `JP` |
| `Belgium`       | `BE` | `Korea`           | `KR` |
| `Canada`        | `CA` | `The Netherlands` | `NL` |
| `China`         | `CN` | `Norway`          | `NO` |
| `Denmark`       | `DK` | `Portugal`        | `PT` |
| `Finland`       | `FI` | `Spain`           | `ES` |
| `Germany`       | `DE` | `Sweden`          | `SE` |
| `Great Britain` | `GB` | `Switzerland`     | `CH` |
| `Greece`        | `GR` | `Taiwan`          | `TW` |
| `Ireland`       | `IE` | `Turkey`          | `TR` |
| `Italy`         | `IT` | `United States`   | `US` |

`locale` 的规则在 `Internet Engineering Task Force` 的 `Best Current Practices` 备忘录 `BCP47`（<https://www.rfc-editor.org/info/bcp47>）进行了明确阐述。你可以在 <https://www.w3.org/International/articles/language-tags/> 处找到更容易理解的总结。

`locale` 是用标签描述的，标签是由 `locale` 的各个元素通过连字符连接起来的字符串，例如 `en-US`。

如果只指定了语言，例如 `de`，那么该 `locale` 就不能用于与国家相关的场景，例如货币。

我们可以像下面这样用标签字符串来构建 `Locale` 对象：

```java
Locale usEnglish = Locale.forLanguageTag("en-US");
```

`toLanguageTag` 方法可以生成给定 `Locale` 的语言标签。例如，`Local.US.toLanguageTag()` 生成的字符串是 `en-US`。

为了方便起见，`Java SE` 为各个国家预定了 `Locale` 对象：

```
Locale.CANADA
Locale.CANADA_FRENCH
```

`Java SE` 还预定义了大量的语言 `Locale`，它们只设定了语言而没有设定位置：

```
Locale.CHINESS
Locale.ENGLISH
```

最后，静态的 `getAvailableLocale` 方法会返回由 `Java` 虚拟机所能够识别的所有 `Locale` 构成的数组。

`Locale` 类的静态 `getDefault` 方法可以获得作为本地操作系统的一部分而存在的默认 `Locale`。可以调用 `setDefault` 来改变默认的 `Java Locale`；但是，这种改变只对你的程序有效，不会对操作系统产生影响。

对于所有与 `Locale` 相关的工具类，可以返回一个它们所支持的 `Locale` 数组。比如，

```java
java -Duser.language=de -Duser.region=CH MyProgram
```

`Locale` 类中唯一有用的是那些识别语言和国家代码的方法，其中最重要的一个是 `getDisplayName`，它返回一个描述 `Locale` 的字符串。这个字符串并不包含前面所说的由两个字母组成的代码，而是以一种面向用户的形式来表现，比如：

```
German (Switzerland)
```

事实上，这里有一个问题，显示的名字是以默认的 `Locale` 来表示的，这可能不太恰当。如果你的用户已经选择了德语作为首选的语言，那么你可能希望将字符串显示成德语。通过将 `German Locale` 作为参数传递就可以做到这一点：

```java
Locale loc = new Locale("de", "CH");
System.out.println(loc.getDisplayName(Locale.GERMAN));
```

将打印出:

```
Deutsch (Schweiz)
```



