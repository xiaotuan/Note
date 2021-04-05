### 11.2.4　使用ElectroServer创建聊天程序

作为示例，将要使用ElectroServer的JavaScript API创一个简单的聊天室程序。用户将通过HTML的窗体提交聊天消息，并且将聊天的内容显示在HTML5的Canvas上。还要创建一些从ElectroServer发来的状态信息，并将它们显示出来，这样就可以观察到与服务器的连接状态。

#### 1．与ElectroServer建立连接

首先，在客户端程序需要包含以下代码，这样才能引用ElectroServer的JavaScript API。

```javascript
<script src="ElectroServer-5-Client-JavaScript.js"></script>
```

客户端应用在与服务器端运行的ElectroServer建立连接时，需要指定URL地址、监听端口和所使用的协议。在本示例中，URL使用localhost，端口使用8989，协议使用BinaryHTTP。

在建立从客户端到服务器的连接时，需要用到这些值。为此，首先创建一个ElectroServer对象的实例，然后调用它的方法。第一步，创建一个与ElectroServer服务器的连接实例，将其命名为server。第二步，使用之前介绍的属性创建一个新的配置变量，命名为availableConnection。第三步，通过调用addAvailableConnection()方法将这个变量添加到server变量中。将全部代码都写在canvasApp()函数中。

```javascript
var server = new ElectroServer.Server("server1");
var availableConnection = new ElectroServer.AvailableConnection
　　("localhost", 8989, ElectroServer.TransportType.BinaryHTTP);
server.addAvailableConnection(availableConnection);
```

现在，需要使用已经配置好的server变量建立一个到ElectroServer的连接。为此，设置一个名为es的新变量，它是一个ElectroServer对象的实例。然后，调用它的initialize()方法，再调用ElectroServer服务器对象中engine属性的addServer方法将配置的server对象添加到es对象中。

```javascript
var es = new ElectroServer();
es.initialize();
es.engine.addServer(server);
```

现在已经基本准备好连接ElectroServer服务器了。不过，还需要为ElectroServer的事件创建一些事件处理函数。读者可能还记得本书之前介绍过，与ElectroServer的所有的通信都是通过创建和监听事件完成的。因此，在这个过程开始时，需要监听以下事件：ConnectionResponse、LoginResponse、JoinRoomEvent、JoinZoneEvent、ConnectionAttemptResponse和PublicMesssageEvent。

```javascript
es.engine.addEventListener(MessageType.ConnectionResponse, onConnectionResponse);
es.engine.addEventListener(MessageType.LoginResponse, onLoginResponse);
es.engine.addEventListener(MessageType.JoinRoomEvent, onJoinRoomEvent);
es.engine.addEventListener(MessageType.JoinZoneEvent, onJoinZoneEvent);
es.engine.addEventListener(MessageType.ConnectionAttemptResponse,
　　onConnectionAttemptResponse);
es.engine.addEventListener(MessageType.PublicMessageEvent, onPublicMessageEvent);
```

最后，当所有准备都就绪后，调用ElectroServer对象的connect方法，然后等待创建的事件监听函数处理不同的事件。

```javascript
es.engine.connect();
```

当ElectroServer API的对象试图连接一个ElectroServer服务器时，服务器的ConnectionAttemt Response事件将会触发并将事件发回给客户端。使用名为onConnectionAttemptResponse的事件监听函数处理这个事件。在本程序中，在这个事件中仅创建一个用于显示的状态消息，此外不做其他任何处理。statusMessage是一个消息数组，用于保存应用程序的调试信息（下节将简要介绍相关内容）。

```javascript
function onConnectionAttemptResponse(event){
 statusMessages.push("connection attempt response!!");
}
```

此时，客户端正在等待从ElectroServer服务器发回的ConnectionResponse事件。当客户端收到ConnectionResponse事件时，将使用onConnectionResponse函数进行处理。在连接建立起来之后，客户端将尝试登录到服务器。在进行登录时，需要一个用户名。创建一个随机的用户名，也可以使用来自网络服务器上的一个账户，来自窗体的字段或cookie，来自Facebook的账户，或者所找到的任何可用的位置或服务。

有了用户名之后，创建一个LoginReques()对象，设置它的userName属性，然后调用es.engine对象的send()方法。从此之后，向ElectroServer发送的所有消息都会使用send()方法。

```javascript
function onConnectionResponse(event){
　 statusMessages.push("Connect Successful?: "+event.successful);
　 var r = new LoginRequest();
　 r.userName = "CanvasUser_" + Math.floor(Math.random()* 1000);
　 es.engine.send(r);
 }
```

当ElectroServer响应了来自LoginRequest的登录请求之后，应该加入一个区域以及一个房间。回忆一下，任何用户与ElectroServer的连接都需要从属于一个房间，而且每一个房间都从属于一个区域。因此，需要使用CreateRoomRequest()对象让用户从属于一个房间和区域。将zoneName属性设置为TestZoneChat，roomName属性设置为TestRoomChat。如果该名称的区域或房间不存在，服务器将会自动创建；如果已经存在，用户将直接加入。然后将信息发送给服务器。

```javascript
function onLoginResponse(event){
　 statusMessages.push("Login Successful?: "+event.successful);
　 username = event.userName;
　 var crr = new CreateRoomRequest();
　 crr.zoneName = "TestZoneChat";
　 crr.roomName = "TestRoomChat";
　 es.engine.send(crr);
}
```

还需要等待两个服务器的响应事件，这两个事件将通过API从8989端口发送到客户端。在得知加入一个区域之后，使用onJoinZoneEvent()函数进行处理，不需要做任何事情。

```javascript
function onJoinZoneEvent(event){
　 statusMessages.push("joined a zone");
}
```

需要处理的最重要的事件是JoinRoomEvent。如果收到这个事件，就得知已经加入了一个区域以及一个房间，此时应用程序准备运行。对于聊天程序来说，这意味着用户可以开始输入并发送消息。首先，将_room变量赋值为Room对象，该对象是从ElectroServer的事件中返回的。在与ElectroServer之后的通信中使用这个变量。在这个函数中还需要做一些其他事情。要引用一个id等于inputForm的HTML的<div>元素，修改它的样式将它设置为可见。因为在与ElectroServer建立连接之前，不想让用户输入聊天信息。现在，所有准备都已就绪，将显示名为inputForm的<div>标签，此时用户可以开始聊天。

```javascript
function onJoinRoomEvent(event){
　　　　　　statusMessages.push("joined a room");
　　　　　　_room = es.managerHelper.zoneManager.zoneById
　　　　　　　　(event.zoneId).roomById(event.roomId);
　　　　　　var formElement = document.getElementById("inputForm");
　　　　　　formElement.setAttribute("style", "display:true");
　　　　 }
```

#### 2．创建聊天功能

在与ElectroServer建立了连接并且加入了一个区域和一个房间后，聊天程序就可以启动了。

首先介绍一下在canvasApp()函数中新增加的一些变量，它们的作用域覆盖了聊天程序的其余部分。statusMessage数组将保存与ElectroServer连接相关的消息。将这些消息显示在画布右边的一个方框中。chatMessage数组保存用户发送到聊天室的所有消息。username变量保存运行聊天程序的用户的名字。_room变量保存了用户所加入房间的room对象的引用。

```javascript
var statusMessages = new Array();
var chatMessages = new Array();
var username;
var _room;
```

在HTML页面中的<form>表单将收集用户输入的聊天消息。表单中包含了一个id等于textbox的文本框，用户将在其中进行输入。还有一个id等于sendChat的按钮。在接收到JoinRoomEvent事件之前这个表单是不可见的。

```javascript
<form>
<input id="textBox" placeholder="your text" />
<input type="button" id ="sendChat" value="Send"/>
</form>
```

在canvasApp()函数中，要监听用户单击sendChat按钮的事件，并设置一个监听器。当单击事件出发时，sendMessage函数将处理这个事件。

```javascript
var formElement = document.getElementById("sendChat");
formElement.addEventListener('click', sendMessage, false);
```

sendMessage()函数是这个程序中最重要的函数之一。为了与ElectroServer进行通信，在这个函数中创建了两个非常关键的对象。第一个对象是PublicMessageRequest，这是可以向ElectroServer套接字服务器发送的若干类型中的一个。其他的类型有PrivateMessageRequest和PluginMessageRequest。PublicMessageRequest是会被发给房间中每一个人的消息。将使用EsObject发送这个数据，EsObject是一个ElectroServer API的本地对象。不论向同一房间的其他用户发送何种类型的数据，都可以使用这个对象创建对等网（Ad Hoc）数据元素，并用它来访问数据。

提示

> 关于EsObject和ElectroServer的完整描述，读者可以参考ElectroServer的文档。读者可以在服务器本地的安装目录中找到以下文件“[安装文件夹]/documentation/html/index.html”。

对于这个简单的聊天程序示例，要发送的数据是用户输入和提交的聊天信息。为此，要使用EsObject的setString()方法。这个方法有两个参数：要发送的文本和用来访问文本的标识符。用户还需要设置另一个名为type的元素，这个元素可以告诉用户发送的是哪种类型的消息。之所以这样做，是因为在比较复杂的程序中可能会发送各种类型的消息，因此需要一种方法来标识消息的类型，这样才能进行处理。

接下来，使用roomId、zoneId和EsObject对PublicMessageEvent进行配置，之后调用es.engine.send(pmr)方法将消息发送给房间中的其他用户。

```javascript
function sendMessage(event){
　 var formElement = document.getElementById("textBox");
　 var pmr = new PublicMessageRequest();
　 pmr.message = "";
　 pmr.roomId = _room.id;
　 pmr.zoneId = _room.zoneId;
　 var esob = new ElectroServer.EsObject();
　 esob.setString("message", formElement.value);
　 esob.setString("type","chatmessage");
　 pmr.esObject = esob;
　 es.engine.send(pmr);
　 statusMessages.push("message sent")
}
```

请注意，在用户提交聊天消息之后，没有将消息打印在画布上。相反，等待ElectroServer返回PublicMessageEvent事件，然后向其他聊天消息那样进行处理。这样可以保持接口整洁，可以在整个程序中保持一个创建事件和处理事件的过程模型。

在套接字服务器处理聊天消息之后，服务器会将消息通过广播发送给房间中的所有用户。所有的用户都必须为PublicMessageEvent事件创建一个事件处理函数，这样才能接收并处理消息。为此，创建了onPublicMessageEvent事件处理函数。这个函数非常简单。它检查为EsObject变量设置的类型是否为chatMessage。如果是，函数会将一个字符串放入chatMessages数组，这个字符串中包含了发送消息的用户名和消息本身，并使这些消息显示在画布上。

```javascript
function onPublicMessageEvent(event){
　 var esob = event.esObject;
　 statusMessages.push("message received")
　 if (esob.getString("type")== "chatmessage"){
　　　chatMessages.push(event.userName + ":" + esob.getString("message"));
　　　}
}
```

现在，剩下的工作是将收集的信息显示出来。在drawScreen()函数中完成此功能。对于statusMessages数组中的状态消息和chatMessages数组中的聊天消息，都只显示最新的22条消息（如果有22条）。这些消息的显示位置都从y轴的15像素开始。只显示最后22条消息。这样，当更多聊天消息和状态信息产生的时候，它们看起来将会在屏幕上向上滚动。

```javascript
var starty = 15;
var maxMessages = 22;
```

如果数组的长度大于maxMessages，只显示最新的22条。为了找到这些消息，设置一个名为starti的新变量，它的值等于statusMessages数组的长度减去maxMessages的数值。这样就可以得到数组中要显示的第一条的索引。对于chatMessages数组也进行同样的操作。

```javascript
//状态消息框
　 context.strokeStyle = '#000000';
　　 context.strokeRect(345, 10, 145, 285);
　　　　 var starti = 0;
　　　　 if (statusMessages.length > maxMessages){
　　　　　　 starti = (statusMessages.length)- maxMessages;
　　　　 }
　　　　 for (var i = starti;i< statusMessages.length;i++){
　　　　　　context.fillText (statusMessages[i], 350, starty );
　　　　　　starty+=12;
//聊天消息框
　　　　 context.strokeStyle = '#000000';
　　　　 context.strokeRect(10, 10, 335, 285);
　　　　 starti = 0;
　　　　 lastMessage = chatMessages.length-1;
　　　　 if (chatMessages.length > maxMessages){
　　　　　　 starti = (chatMessages.length)- maxMessages;
　　　　 }
　　　　 starty = 15;
　　　　 for (var i = starti;i< chatMessages.length;i++){
　　　　　　context.fillText (chatMessages[i], 10, starty );
　　　　　　starty+=12;
　　　　 }
　　　}
```

至此，就完成了多用户聊天程序的开发。

