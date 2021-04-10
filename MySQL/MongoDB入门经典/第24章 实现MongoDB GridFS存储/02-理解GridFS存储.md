### 24.1　理解GridFS存储

GridFS将大型文件分成块。这些块存储在MongoDB数据库的集合chunks中，而有关文件的元数据存储在集合files中。当您在GridFS中查询文档时，将首先从集合files中读取元数据，再从集合chunks中读取并返回块。

GridFS的一大优点是，无需将整个文件读入内存就能返回请求结果，这降低了内存不足的风险。

在下述情形下，您可能想使用MongoDB GridFS存储而不是标准文件存储：

+ 文件系统限制了一个目录可包含的文件数。您可使用GridFS存储任意数量的文件。
+ 您希望文件和元数据自动同步，并使用MongoDB复制将文件存储到多个系统中。
+ 您要访问大型文件的部分信息，又不想将整个文件都载入内存。您可使用GridFS获取文件的部分内容，而无需将整个文件读入内存。

要实现GridFS，可使用控制台窗口，也可使用MongoDB驱动程序。MongoDB驱动程序都提供了GridFS功能，例如，Node.js MongoDB驱动程序提供了对象Grid和GridStore，让您能够与MongoDB GridFS交互。

