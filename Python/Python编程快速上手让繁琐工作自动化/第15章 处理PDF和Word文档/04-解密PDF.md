### 15.1.2　解密PDF

某些PDF文档有加密功能，以防止别人阅读，只有在打开文档时提供口令才能阅读。在交互式环境中输入以下代码，处理下载的PDF，它已经用口令rosebud加密：

```javascript
 >>> import PyPDF2
 >>> pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
❶ >>> pdfReader.isEncrypted
  True
 >>> pdfReader.getPage(0)
❷ Traceback (most recent call last):
     File "<pyshell#173>", line 1, in <module> 
        pdfReader.getPage()
     --snip--
     File "C:\Python34\lib\site-packages\PyPDF2\pdf.py", line 1173, in getObject
       raise utils.PdfReadError("file has not been decrypted")
     PyPDF2.utils.PdfReadError: file has not been decrypted
 >>> pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
❸ >>> pdfReader.decrypt('rosebud')
  1
 >>> pageObj = pdfReader.getPage(0)
```

所有 `PdfFileReader` 对象都有一个 `isEncrypted` 属性，如果PDF是加密的，它就是 `True` ；如果不是，它就是 `False` ❶。在文件用正确的口令解密之前，尝试调用函数来读取文件将会导致错误❷。



**注意：**
由于PyPDF2版本1.26.0中的一个bug，所以在打开加密的PDF之前调用 `getPage()` 会导致未来的 `getPage()` 调用失败，并出现以下错误： `IndexError: list index out of range` 。这就是我们的例子用一个新的 `PdfFileReader` 对象重新打开文件的原因。



要读取加密的PDF，就调用 `decrypt()` 函数，以传入口令字符串❸。在用正确的口令调用 `decrypt()` 后，你会看到调用 `getPage()` 不再导致错误。如果提供了错误的口令，那么 `decrypt()` 函数将返回0，并且 `getPage()` 会继续失败。请注意， `decrypt()` 函数只解密了 `PdfFileReader` 对象，而不是实际的PDF文档。在程序中止后，硬盘上的文件仍然是加密的。在程序下次运行时，仍然需要再次调用 `decrypt()` 。

