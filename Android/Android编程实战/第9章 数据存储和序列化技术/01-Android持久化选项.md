### 9.1 Android 持久化选项

Android 标准 API 提供了两种现成的方法用来在设备上存储结构化数据，它们分别是偏好文件和 SQLite 数据库。

SharedPreferences 常用来存储设置、选项、用户偏好，以及其他简单的值，一般不用来存储数组、表格或者二进制数据。相反，应该通过 ContentProvider 在 SQLite 数据库中存储那些可以用 Java 表示的列表或者数组数据。

二进制数据不应该直接存储在 SQLite 数据库或者偏好文件中。