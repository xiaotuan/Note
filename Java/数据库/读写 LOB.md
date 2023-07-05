在 `SQL` 中，二进制大对象称为 `BLOB`，字符型大对象称为 `CLOB`。

要读取 `LOB`，需要执行 `SELECT` 语句，然后在 `ResultSet` 上调用 `getBlob` 或 `getClob` 方法，这样就可以获得 `Blob` 或 `Clob` 类型的对象。要从 `Blob` 中获取二进制数据，可以调用 `getBytes` 或 `getBinaryStream`：

```java
...
stat.set(1, isbn);
try (ResultSet result = stat.executeQuery()) {
    if (result.next()) {
        Blob coverBlob = result.getBlob(1);
        Image coverImage = ImageIO.read(coverBlob.getBinaryStream());
    }
}
```

类似地，如果获取了 `Clob` 对象，那么就可以通过调用 `getSubString()` 或 `getCharacterStream` 方法来获取其中的字符数据。

要将 `LOB` 置于数据库中，需要在 `Connection` 对象上调用 `createBlob` 或 `createClob`，然后获取一个用于该 `LOB` 的输出流或写出器，写出数据，并将该对象存储到数据库中。

```java
Blob coverBlob = connection.createBlob();
int offset = 0;
OutputStream out = coverBlob.setBinaryStream(offset);
ImageIO.write(coverImage, "PNG", out);
PreparedStatement stat = conn.prepareStatement("INSERT INTO Conver VALUES (?,?)");
stat.set(1, isbn);
stat.set(2, coverBlob);
stat.executeUpdate();
```

