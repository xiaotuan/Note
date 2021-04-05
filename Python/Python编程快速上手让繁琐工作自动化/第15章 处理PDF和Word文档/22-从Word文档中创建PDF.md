### 15.4　从Word文档中创建PDF

`PyPDF2` 模块不允许你直接创建PDF文档，但如果你在Windows操作系统上安装了Microsoft Word，那么有一种方法可以用Python生成PDF文档。你需要运行 `pip install --user --U pywin32==224` 来安装Pywin32包。有了这个包和docx模块，你可以创建Word文档，然后用下面的脚本将其转换为PDF。

打开一个新的文件编辑器窗口， 输入下面的代码， 然后保存为convertWordToPDF.py：

```javascript
# This script runs on Windows only, and you must have Word installed.
import win32com.client # install with "pip install pywin32==224" 
import docx
wordFilename = 'your_word_document.docx'
pdfFilename = 'your_pdf_filename.pdf'
doc = docx.Document()
# Code to create Word document goes here.
doc.save(wordFilename)
wdFormatPDF = 17 # Word's numeric code for PDFs.
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(wordFilename) 
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF) 
docObj.Close()
wordObj.Quit()
```

要编写一个程序来用自己的内容制作PDF，必须用 `python-docx` 模块创建一个Word文档，然后用Pywin32包的 `win32com.client` 模块将其转换为PDF。将 `# Code to create Word document goes here.` 注释替换为 `docx` 函数调用，来为Word文档中的内容创建PDF文档。

这看起来似乎是一个复杂的制作PDF的方法，但事实表明，专业软件的解决方案往往同样复杂。

