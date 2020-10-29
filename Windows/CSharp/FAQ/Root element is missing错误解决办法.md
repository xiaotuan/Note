**错误类型：** System.Xml

**产生错误的代码片段：**

```c#
XDocument doc = XDocument.Load("data.xml");
var filtered = from p in doc.Descendants("Product")
    join s in doc.Descendants("Supplier")
    on (int)p.Attribute("SupplierID")
    equals (int)s.Attribute("SupplierID")
    where (decimal)p.Attribute("Price") > 10
    orderby (string)p.Attribute("Name"), (string)p.Attribute("Name")
    select new
{
    SupplierName = (string)s.Attribute("Name"),
    ProductName = (string)p.Attribute("Name")
};
```

**错误信息：**

```shell
System.Xml.XmlException
  HResult=0x80131940
  Message=Root element is missing.
  Source=System.Private.Xml
  StackTrace:
   at System.Xml.XmlTextReaderImpl.Throw(Exception e)
   at System.Xml.XmlTextReaderImpl.ParseDocumentContent()
   at System.Xml.XmlTextReaderImpl.Read()
   at System.Xml.Linq.XDocument.Load(XmlReader reader, LoadOptions options)
   at System.Xml.Linq.XDocument.Load(String uri, LoadOptions options)
   at System.Xml.Linq.XDocument.Load(String uri)
   at Simple06.Program.Main(String[] args) in C:\Workspace\GitSpace\Github\GitResources\CSharpInDepthThirdEdition\Chapter01\Simple06\Program.cs:line 34
```

**错误产生原因：**

经查看发现，生成目录中的 data.xml 内容为空导致的。

**解决办法：**

修改 data.xml 文件使其符合 XML 格式规范即可。

