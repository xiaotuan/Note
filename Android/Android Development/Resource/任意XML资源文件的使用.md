[toc]

### 1. 创建任意 XML 资源

`Android` 允许将任意 `XML` 文件用作资源。任意 `XML` 文件需要放在 `res/xml` 目录下。

```xml
<rooteleml>
    <subeleml name="hello">
        Hello World from an xml sub element
    </subeleml>
</rooteleml>
```

### 2. 在代码中使用任意 XML 资源

**Java 版本**

```java
private String getEventsFromAnXMLFile(Activity activity)
	throws XmlPullParserException, IOException {
    StringBuffer sb = new StringBuffer();
    Resources res = activity.getResources();
    XmlResourceParser xpp = res.getXml(R.xml.test);

    xpp.next();
    int eventType = xpp.getEventType();
    while (eventType != XmlPullParser.END_DOCUMENT) {
        if (eventType == XmlPullParser.START_DOCUMENT) {
            sb.append("**********Start document");
        } else if (eventType == XmlPullParser.START_TAG) {
            sb.append("\nStart tag " + xpp.getName());
            for (int i = 0; i < xpp.getAttributeCount(); i++) {
                sb.append("\nAttribute name: " + xpp.getAttributeName(i)
                          + ", value: " + xpp.getAttributeValue(i));
            }
        } else if (eventType == XmlPullParser.END_TAG) {
            sb.append("\nEnd tag " + xpp.getName());
        } else if (eventType == XmlPullParser.TEXT) {
            sb.append("\nText " + xpp.getText());
        }
        eventType = xpp.next();
    }
    sb.append("\n*************End document");
    Log.d("example", "xml content: \n" + sb.toString());
    return sb.toString();
}
```

**Kotlin 版本**

```kotlin
private fun getEventsFromAnXMLFile(activity: Activity): String {
    val sb = StringBuffer()
    val xpp = activity.resources.getXml(R.xml.test)

    xpp.next()
    while (xpp.eventType != XmlPullParser.END_DOCUMENT) {
        when (xpp.eventType) {
            XmlPullParser.START_DOCUMENT -> sb.append("**********Start document")
            XmlPullParser.START_TAG -> {
                sb.append("\nStart tag " + xpp.getName());
                for (i in 0 until xpp.attributeCount) {
                    sb.append(
                        "\nAttribute name: " + xpp.getAttributeName(i)
                        + ", value: " + xpp.getAttributeValue(i)
                    );
                }
            }
            XmlPullParser.END_TAG -> sb.append("\nEnd tag " + xpp.name)
            XmlPullParser.TEXT -> sb.append("\nText " + xpp.text)

        }
        xpp.next()
    }
    sb.append("\n*************End document");
    Log.d("example", "xml content: \n$sb");
    return sb.toString()
}
```

