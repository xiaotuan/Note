在 Java 中，可以使用 `ZipInputStream` 来读入 `ZIP` 文档。你可能需要浏览文档中每个单独项，`getNextEntry` 方法就可以返回一个描述这些项的  `ZipEntry` 类型的对象。向 `ZipInputStream` 的 `getInputStream` 方法传递该项可以获取用于读取该项的输入流。然后调用 `closeEntry` 来读入下一项。下面是典型的通读 ZIP 文件的代码序列：

```java
ZipInputStream zin = new ZipInputStream(new FileInputStream(zipname));
ZipEntry entry;
while ((entry = zin.getNextEntry()) != null) {
    InputStream in = zin.getInputStream(entry);
    // read the contents of in
    zin.closeEntry();
}
zin.close();
```

要写出到 ZIP 文件，可以使用 `ZipOutputStream`，而对于你希望放入到 ZIP 文件中的每一项，都应该创建一个 `ZipEntry` 对象，并将文件名传递给 `ZipEntry` 的构造器，它将设置其他诸如文件日期和解压缩方法等参数。如果需要，你可以覆盖这些设置。然后，你需要调用 `ZipOutputStream` 的 `putNextEntry` 方法来开始写出新文件，并将文件数据发送到 ZIP 输出流中。当完成时，需要调用 `closeEntry`。然后，你需要对所有你希望存储的文件都重复这个过程。下面是代码框架：

```java
FileOutputStream fout = new FileOutputStream("test.zip");
ZipOutputStream zout = new ZipOutputStream(fout);
for all files {
    ZipEntry ze = new ZipEntry(filename);
    zout.putNextEntry(ze);
    // send data to zout;
    zout.closeEntry();
}
zout.close();
```

> 注意：JAR 文件只是带有一个特殊项的 ZIP 文件，这个项称作清单。你可以使用 `JarInputStream` 和 `JarOutputStream` 类来读写清单项。