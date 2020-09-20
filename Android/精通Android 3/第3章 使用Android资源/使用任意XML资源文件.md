需要以此方式读取的 XML 文件存储在 `/res/xml` 子目录下。代码清单3-30是一个名为 `/res/xml/test.xml` 的示例 XML 文件。

**代码清单3-30** 示例 XML 文件

```xml
<rootelem1>
    <subelem1>
        Hello World from an xml sub element
    </subelem1>
</rootelem1>
```

**代码清单3-31** 读取 XML 文件

```java
Resources res = activity.getResources();
XmlResourceParser xpp = res.getXml(R.xml.test);
```

**代码清单3-32** 使用 XmlPullParser

```java
private String getEventsFromAnXMLFile(Activity activity) throws XmlPullParserException, IOException {
    StringBuffer sb = new StringBuffer();
    Resources res = activity.getResources();
    XmlResourceParser xpp = res.getXml(R.xml.test);
    
    xpp.next();
    int eventType = xpp.getEventType();
    while (eventType != XmlPullParser.END_DOCUMENT) {
        if (eventType == XmlPullParser.START_DOCUMENT) {
            sb.append("******Start document");
        } else if (eventType == XmlPullParser.START_TAG) {
            sb.append("\nStart tag " + xpp.getName());
        } else if (eventType == XmlPullParser.END_TAG) {
            sb.append("\nEnd tag " + xpp.getName());
        } else if (eventType == XmlPullParser.TEXT) {
            sb.append("\nText " + xpp.getText());
        }
        eventType = xpp.next();
    } // eof-while
    sb.append("\n******End document");
    return sb.toString();
} // eof-function
```

