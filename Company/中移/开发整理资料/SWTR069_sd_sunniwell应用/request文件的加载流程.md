下面讲解 assets/templates/inform/request.xml 文件加载流程。

该文件在 src/net/sunniwell/tms/CWMPEventHandler.java 文件中的 sendInform() 方法使用到：

```java
private void sendInform(final String[] codes, final ArrayList object) throws IOException, InterruptedException {
    log.i("========sendInform=======codes=" + codes.toString() + " object=" + (object == null ? "null" : object.toString()));
    // Auto-generated method stub
    ACSSession session = new ACSSession(mContext);
    InputStream input;
    try {
        input = CWMPService.getInstance().getTemplateInputStream("Inform");
        Envelope request = Inform.getInstance().buildRequest(codes, input, object);
        input.close();
        session.setRequest(mPreferences, request);
        session.start();
        session.join();
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

从上面的代码中，我们可以看到它通过 src/net/sunniwell/tms/CWMPService.java 类中的 getTemplateInputStream() 方法将其转换成流：

```java
public InputStream getTemplateInputStream(String name) throws IOException {
    Context context = getApplicationContext();
    String template = config.getTemplate(name);
    if (template == null)
        return null;
    log.d("===getTemplateInputStream=======" + template);
    return context.getAssets().open(template);
}
```

在 getTemplateInputStream() 方法中通过 src/net/sunniwell/tms/config/Config.java 类中的 getTemplate() 方法来获取 request.xml 的真实路径的。

```java
public String getTemplate(String name) {
    for (Template template : templates) {
        if (template._name.equalsIgnoreCase(name))
            return template._xml;
    }
    return null;
}
```

从上面的方法中，我们可以看到，它是通过查询 templates 集合中是否存在一个名字叫做 "Inform" 的 Template 变量。如果存在 ，则返回该变量的 _xml 属性，否则返回 null。Config 类是在 src/net/sunniwell/tms/CWMPService.java 类中初始化的。

```java
private void initConfig() throws IOException {
    Context context = getApplicationContext();
    AssetManager assets = context.getAssets();
    InputStream input = assets.open("config.xml");
    config = (Config) XMLBinding.getInstance().load(Config.class, input);
    if (config == null) {
        log.d("parsing config.xml failed");
        assert false;
    }
    input.close();
    log.d("loading config.xml success");
}
```

initConfig() 方法通过读取 assets/config.xml 文件，并通过 XMLBinding 类将其转换成 Config 类。我们可以在 config.xml 文件中看到 Inform 的定义为 “templates/inform/request.xml”：

```xml
<cwmpservice>
  <template name="Inform" xml="templates/inform/request.xml"/>
  <template name="GetRPCMethodsResponse" xml="templates/getrpcmethods/response.xml"/>
  <template name="GetParameterNamesResponse" xml="templates/getparameternames/response.xml"/>
  <template name="GetParameterValuesResponse" xml="templates/getparametervalues/response.xml"/>
  ......
</cwmpservice>
```

上面就是 request.xml 的加载过程。下面我们来看下它是如何转换成对象的。具体转换是通过 sendInform() 方法中的 `Envelope request = Inform.getInstance().buildRequest(codes, input, object);` 语句进行的。那我们来看下 src/net/sunniwell/tms/methods/Inform.java 的 buildRequest() 方法：

```java
public Envelope buildRequest(String[] codes, InputStream template, ArrayList object) {
    Envelope result = (Envelope) XMLBinding.getInstance().load(Envelope.class, template);
    result.body.informRequest.events.list.clear();
    for (String code : codes) {
        EventStruct ev = new EventStruct();
        ev.CommandKey = "";
        if (CWMPEvent.EVENT_CODE_STRING_M_REBOOT.equals(code) || CWMPEvent.EVENT_CODE_STRING_M_DOWNLOAD.equals(code)) {
            String key = new DataPreferences(CWMPService.getInstance().getApplicationContext()).getPreferences(DataPreferences.CommandKey);
            ev.CommandKey = key;
        }
        android.util.Log.d("Inform", "buildRequest=>ev commandKey: " + ev.CommandKey);
        ev.EventCode = code;
        result.body.informRequest.events.list.add(ev);
        result.body.informRequest.events.type = EventList.buildTypeString(codes.length);
        if (code.compareToIgnoreCase(CWMPEvent.EVENT_CODE_STRING_BOOT) == 0 
            || code.compareToIgnoreCase(CWMPEvent.EVENT_CODE_STRING_BOOTSTARP) == 0 || code
            .compareToIgnoreCase(CWMPEvent.EVENT_CODE_STRING_CONNECTION_REQUEST) == 0) {
            result.body.informRequest.currentTime = Utility.getCurrentTime();
            result.body.informRequest.values.type = ParameterValueList.buildTypeString(result.body.informRequest.values.list.size());
        }
        log.d("empty=" + empty);
        // empty = true;
        if (code.compareToIgnoreCase(CWMPEvent.EVENT_CODE_STRING_TRANSFER_COMPLETE) == 0) {
            empty = false;
            if (object instanceof ArrayList) {
                ArrayList<Object> list = (ArrayList<Object>) object;
                log.d("list size=" + list.size());
                commandKey = new DataPreferences(CWMPService.getInstance().getApplicationContext()).getPreferences(DataPreferences.CommandKey);
                for (Object obj : list) {
                    if (obj instanceof FaultStruct) {
                        fault = (FaultStruct) obj;
                    } else if (obj instanceof String) {
                        commandKey = (String) obj;// 默认从datapreference获取，若list存在则覆盖
                    }
                }
                log.d("fault=" + fault + " key=" + commandKey);
            }
        }
        android.util.Log.d("Inform", "buildRequest=>commandKey: " + commandKey);
        if (code.compareToIgnoreCase(CWMPEvent.EVENT_CODE_STRING_BOOT) == 0 || code.compareToIgnoreCase(CWMPEvent.EVENT_CODE_STRING_BOOTSTARP) == 0 || code
            .compareToIgnoreCase(CWMPEvent.EVENT_CODE_STRING_VALUE_CHANGE) == 0) {
            result.body.informRequest.values.list = getAddParameter(result.body.informRequest.values.list, object);
        }
        result.body.informRequest.values.type = ParameterValueList.buildTypeString(result.body.informRequest.values.list.size());
    }
    return result;
}
```

从上面的代码可以看到，它是通过 XMLBinding 类直接将文件转换成 Envelope 类的。我们先来看下 request.xml 的文件结构：

```xml
<soap:Envelope encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:cwmp="urn:dslforum-org:cwmp-1-0">
	<soap:Header>
		<cwmp:ID soap:mustUnderstand="1"></cwmp:ID>
	</soap:Header>
	<soap:Body>
		<cwmp:Inform>
			<DeviceId>
				<Manufacturer>${Device.DeviceInfo.Manufacturer}</Manufacturer> 
				<OUI>${Device.DeviceInfo.OUI}</OUI>
				<ProductClass>${Device.DeviceInfo.ProductClass}</ProductClass>
				<SerialNumber>${Device.DeviceInfo.SerialNumber}</SerialNumber>
			</DeviceId>
			<Event soapenc:arrayType="cwmp:EventStruct[1]">
				<EventStruct>
					<EventCode></EventCode>
					<CommandKey></CommandKey>
				</EventStruct>
			</Event>
			<MaxEnvelopes>1</MaxEnvelopes>
			<CurrentTime></CurrentTime>
			<RetryCount>0</RetryCount>
			<ParameterList soapenc:arrayType="cwmp:ParameterValueStruct[15]">
			    <ParameterValueStruct>
					<Name>Device.DeviceType</Name>
					<Value xsi:type="xsd:string">${Device.DeviceType}</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>Device.DeviceSummary</Name>
					<Value xsi:type="xsd:string">${Device.DeviceSummary}</Value>
				</ParameterValueStruct>
				......
			</ParameterList>
		</cwmp:Inform>
	</soap:Body>
</soap:Envelope>
```

我们再来看下 src/net/sunniwell/tms/methods/beans/Envelope.java 的定义：

```java
public class Envelope {
	public static final String envprefix = "soap";
	public static final String env = "http://schemas.xmlsoap.org/soap/envelope/";
	public static final String encprefix = "soapenc";
	public static final String enc = "http://schemas.xmlsoap.org/soap/encoding/";
	public static final String xsdprefix = "xsd";
	public static final String xsd = "http://www.w3.org/2001/XMLSchema";
	public static final String xsiprefix = "xsi";
	public static final String xsi = "http://www.w3.org/2001/XMLSchema-instance";
	public static final String cwmpprefix = "cwmp";
	public static final String cwmp = "urn:dslforum-org:cwmp-1-0";
	
	@Attribute(name = "encodingStyle", required = false)
	public static final String encoding = "http://schemas.xmlsoap.org/soap/encoding/";

	@Element(name = "Header")
	@Namespace(reference = Envelope.env)
	public static Header head = new Header();

	@Element(name = "Body")
	@Namespace(reference = Envelope.env)
	public Body body = new Body();
	
	public int eventcode = CWMPEvent.EVENT_CWMP_BASE;
}
```

从中我们可以看到 Evelope 类的 head 成员对应着 request.xml 文件的 `<soap:Header>` 节点，body 成员对应着 `<soap:Body>` 节点，它们存储着节点中的相关信息。

下面先来看下 src/net/sunniwell/tms/methods/beans/Header.java 类的定义：

```java 
public class Header {
	@Element(name = "ID")
	@Namespace(reference = Envelope.cwmp)
	public ID id = new ID();
}
```

可以看到类中的成员变量对应这个 request.xml 文件中 header 节点下的值。

再来看下 src/net/sunniwell/tms/methods/beans/Body.java 类的定义：

```java
package net.sunniwell.tms.methods.beans;

import java.lang.reflect.Field;

import net.sunniwell.common.log.SWLogger;

import org.simpleframework.xml.Element;
import org.simpleframework.xml.Namespace;
import org.simpleframework.xml.Root;
import org.simpleframework.xml.core.Validate;


@Root(strict = false)
public class Body {
	......

	/**
	 * ACS Methods
	 */

	@Element(name = "Inform", required = false)
	@Namespace(reference = Envelope.cwmp)
	public InformRequest informRequest;

	...
}
```

