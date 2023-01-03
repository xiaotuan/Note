通过如下代码建立一个文件系统，它包含 ZIP 文档中的所有文件：

```java
FileSystem fs = FileSystems.newFileSystem(Paths.get(zipname), null);
```

要列出 ZIP 文档中的所有文件，可以遍历文件树：

```java
FileSystem fs = FileSystem.newFileSystem(Paths.get(zipname), null);
Files.walkFileTree(fs.getPath("/"), new SimpleFileVisitor<Path>() {
    @Override
    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
        System.out.println(file);
        return FileVisitResult.CONTINUE;
    }
});
```

