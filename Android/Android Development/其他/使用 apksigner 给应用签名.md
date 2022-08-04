[toc]

> 注意：
>
> 1. `apksigner` 工具在 Android SDK 构建工具的修订banb 24.0.3 及更高版本中可用。
> 2. 如果你在使用 `apksigner` 为 APK 签名后又对 APK 做了更改，则 APK 的签名将会失效。因此，要使用 `zipalign` 等工具，您必须在为 APK 签名之前使用。

> 摘要：可以参阅 <https://developer.android.google.cn/studio/command-line/apksigner?hl=zh_cn>。

### 1. 用法

使用 `apksigner` 工具为 APK 签名的语法如下：

```shell
apksigner sign --ks keystore.jks |
	--key key.pk8 --cert cert.x509.pem
	[signer_options] app-name.apk
```

你可以通过两种不同的方式添加此信息：

+ 使用 `--ks` 选项指定秘钥库文件。
+ 使用 `--key` 和 `--cert` 选项分别指定私钥文件和证书文件。私钥文件必须使用 `PKCS #8` 格式，证书文件必须使用 `X.509` 格式。

通常情况下，你只会使用一个签名者为 APK 签名。如果您需要使用多个签名者为 APK 签名，请使用 `--next-signer` 选项将要应用于每个签名者的常规选项集分隔开：

```shell
apksigner sign [signer_1_options] --next-signer [signer_2_options] app-name.apk
```

#### 1.1 验证 APK 签名

确保签名能在支持的平台上成功通过验证的语法如下：

```shell
apksigner verify [options] app-name.apk
```

#### 1.2 轮替签名秘钥

轮替签名证书世系或新签名序列的语法如下：

```shell
$ apksigner rotate --in /path/to/existing/lineage \
	--out /path/to/new/file \
	--old-signer --ks old-signer-jks \
	--new-signer --ks new-signer-jks
```

### 2. 选项

以下列表包含 `apksigner` 工具支持的每个命令的选项集。

#### 2.1 签名命令

##### 2.1.1 常规选项

以下选项指定要应用于签名者的基本设置：

- `--out <apk-filename>`

  您将要保存已签名 APK 的位置。如果未明确提供此选项，则 APK 软件包将就地签名，并替换输入的 APK 文件。

- `--min-sdk-version <integer>`

  `apksigner` 用来确认 APK 签名将通过验证的最低 Android 框架 API 级别。该级别值越高，表示该工具在为应用签名时可使用的安全参数越强，但这会限制 APK 只能用于搭载更新版本 Android 的设备。默认情况下，`apksigner` 会使用应用清单文件中的 `minSdkVersion` 属性的值。

- `--max-sdk-version <integer>`

  `apksigner` 用来确认 APK 签名将通过验证的最高 Android 框架 API 级别。默认情况下，该工具会使用尽可能高的 API 级别。

- `--v1-signing-enabled <true | false>`

  确定 `apksigner` 是否会使用基于 JAR 的传统签名方案为给定的 APK 软件包签名。默认情况下，该工具会使用 `--min-sdk-version` 和 `--max-sdk-version` 的值来决定何时采用此签名方案。

- `--v2-signing-enabled <true | false>`

  确定 `apksigner` 是否会使用 [APK 签名方案 v2](https://developer.android.google.cn/about/versions/nougat/android-7.0?hl=zh-cn#apk_signature_v2) 为给定的 APK 软件包签名。默认情况下，该工具会使用 `--min-sdk-version` 和 `--max-sdk-version` 的值来决定何时采用此签名方案。

- `--v3-signing-enabled <true | false>`

  确定 `apksigner` 是否会使用 [APK 签名方案 v3](https://source.android.google.cn/security/apksigning/v3?hl=zh-cn) 为给定的 APK 软件包签名。默认情况下，该工具会使用 `--min-sdk-version` 和 `--max-sdk-version` 的值来决定何时采用此签名方案。

- `--v4-signing-enabled <true | false | only>`

  确定 `apksigner` 是否会使用 [APK 签名方案 v4](https://developer.android.google.cn/about/versions/11/features?hl=zh-cn#signature-scheme-v4) 为给定的 APK 软件包签名。此方案会在单独的文件 (`apk-name.apk.idsig`) 中生成签名。如果为 `true` 并且 APK 未签名，则系统会根据 `--min-sdk-version` 和 `--max-sdk-version` 的值生成 v2 或 v3 签名。然后，该命令会根据已签名的 APK 的内容生成 `.idsig` 文件。使用 `only` 仅生成 v4 签名，而不会修改 APK 及其在调用前具有的任何签名；如果 APK 没有 v2 或 v3 签名，或者签名使用的密钥不同于为当前调用提供的密钥，则 `only` 会失败。默认情况下，该工具会使用 `--min-sdk-version` 和 `--max-sdk-version` 的值来决定何时采用此签名方案。

- `-v`，`--verbose`

  使用详细输出模式。

#### 2.2 每个签名者的选项

以下选项用于指定特定签名者的配置。如果您仅使用一个签名者为应用签名，就不需要使用这些选项。

- `--next-signer <signer-options>`

  用于为每个签名者指定不同的[常规选项](https://developer.android.google.cn/studio/command-line/apksigner?hl=zh_cn#options-sign-general)。

- `--v1-signer-name <basename>`

  相关文件的基名，此类文件构成当前签名者的 JAR 签名。默认情况下，对于该签名者，`apksigner` 会使用密钥库的密钥别名或密钥文件的基名。

#### 2.3 密钥和证书选项

以下选项用于指定签名者的私钥和证书：

- `--ks <filename>`

  签名者的私钥和证书链包含在给定的基于 Java 的密钥库文件中。如果文件名设为 `"NONE"`，则包含密钥和证书的密钥库不需要指定文件，某些 PKCS＃11 密钥库就是这种情况。

- `--ks-key-alias <alias>`

  表示签名者在密钥库中的私钥和证书数据的别名的名称。如果与签名者关联的密钥库包含多个密钥，则必须指定此选项。

- `--ks-pass <input-format>`

  包含签名者私钥和证书的密钥库的密码。您必须提供密码才能打开密钥库。`apksigner` 工具支持以下格式：`pass:<password>`- 密码与 `apksigner sign` 命令的其余部分一起提供（内嵌在其中）。`env:<name>` - 密码存储在给定的环境变量中。`file:<filename>` - 密码存储在给定文件中的某一行。`stdin` - 密码作为标准输入流中的某一行提供。这是 `--ks-pass` 的默认行为。**注意**：如果一个文件中包含多个密码，请分别在不同的行中指定这些密码。`apksigner` 工具会根据您指定 APK 签名者的顺序将密码与签名者相关联。如果您为签名者提供了两个密码，`apksigner` 会将第一个密码视为密钥库密码，将第二个密码视为密钥密码。

- `--pass-encoding <charset>`

  在尝试处理包含非 ASCII 字符的密码时，请添加指定的字符编码（例如，`ibm437` 或 `utf-8`）。密钥工具通常使用控制台的默认字符集转换密码，以加密密钥库。默认情况下，`apksigner` 会尝试使用多种形式的密码进行解密：Unicode 编码形式、使用 JVM 默认字符集编码的形式，以及使用控制台的默认字符集编码的形式（在 Java 8 及更早版本上）。在 Java 9 上，`apksigner` 无法检测控制台的字符集。因此，当使用非 ASCII 密码时，您可能需要指定 `--pass-encoding`。对于密钥工具在不同操作系统或不同语言区域中创建的密钥库，您可能也需要指定此选项。

- `--key-pass <input-format>`

  签名者私钥的密码。如果私钥受密码保护，则需要该密码。`apksigner` 工具支持以下格式：`pass:<password>`- 密码与 `apksigner sign` 命令的其余部分一起提供（内嵌在其中）。`env:<name>` - 密码存储在给定的环境变量中。`file:<filename>` - 密码存储在给定文件中的某一行。`stdin` - 密码作为标准输入流中的某一行提供。这是 `--key-pass` 的默认行为。**注意**：如果一个文件中包含多个密码，请分别在不同的行中指定这些密码。`apksigner` 工具会根据您指定 APK 签名者的顺序将密码与签名者相关联。如果您为签名者提供了两个密码，`apksigner` 会将第一个密码视为密钥库密码，将第二个密码视为密钥密码。

- `--ks-type <algorithm>`

  与包含签名者的私钥和证书的密钥库关联的类型或算法。默认情况下，`apksigner` 会使用在安全属性文件中定义为 `keystore.type` 常量的类型。

- `--ks-provider-name <name>`

  请求签名者的密钥库实现时使用的 JCA 提供程序的名称。默认情况下，`apksigner` 会使用优先级最高的提供程序。

- `--ks-provider-class <class-name>`

  请求签名者的密钥库实现时使用的 JCA 提供程序的完全限定类名。此选项可作为 `--ks-provider-name` 的替代选项。默认情况下，`apksigner` 会使用由 `--ks-provider-name` 选项指定的提供程序。

- `--ks-provider-arg <value>`

  要作为 JCA 提供程序类的构造函数的参数传入的字符串值；该类本身由 `--ks-provider-class` 选项定义。默认情况下，`apksigner` 会使用该类的 0 参数构造函数。

- `--key <filename>`

  包含签名者私钥的文件的名称。该文件必须使用 PKCS #8 DER 格式。如果密钥受密码保护，则除非您使用 `--key-pass` 选项指定其他类型的输入格式，否则 `apksigner` 会提示您使用标准输入格式输入密码。

- `--cert <filename>`

  包含签名者证书链的文件的名称。此文件必须使用 X.509 PEM 或 DER 格式。

### 3. 验证命令

- `--print-certs`

  显示有关 APK 签名证书的信息。

- `--min-sdk-version <integer>`

  `apksigner` 用来确认 APK 签名将通过验证的最低 Android 框架 API 级别。该级别值越高，表示该工具在为应用签名时可使用的安全参数越强，但这会限制 APK 只能用于搭载更新版本 Android 的设备。默认情况下，`apksigner` 会使用应用清单文件中的 `minSdkVersion` 属性的值。

- `--max-sdk-version <integer>`

  `apksigner` 用来确认 APK 签名将通过验证的最高 Android 框架 API 级别。默认情况下，该工具会使用尽可能高的 API 级别。

- `-v`、`--verbose`

  使用详细输出模式。

- `-Werr`

  将警告视为错误。

### 4. 示例

#### 4.1 为 APK 签名

使用 `release.jks`（密钥库中唯一的密钥）为 APK 签名：

```
$ apksigner sign --ks release.jks app.apk
```

使用私钥和证书（存储为不同的文件）为 APK 签名：

```
$ apksigner sign --key release.pk8 --cert release.x509.pem app.apk
```

使用两个密钥为 APK 签名：

```
$ apksigner sign --ks first-release-key.jks --next-signer --ks second-release-key.jks app.apk
```

#### 4.2 验证 APK 签名

检查 APK 的签名是否可在 APK 支持的所有 Android 平台上被确认为有效：

```
$ apksigner verify app.apk
```

检查 APK 的签名是否可在 Android 4.0.3（API 级别 15）及更高版本上被确认为有效：

```
$ apksigner verify --min-sdk-version 15 app.apk
```

#### 4.3 轮替签名密钥

启用支持密钥轮替的签名证书沿袭：

```
$ apksigner rotate --out /path/to/new/file --old-signer \
    --ks release.jks --new-signer --ks release2.jks
```

再次轮替您的签名密钥：

```
$ apksigner rotate --in /path/to/existing/lineage \
  --out /path/to/new/file --old-signer --ks release2.jks \
  --new-signer --ks release3.jks
```