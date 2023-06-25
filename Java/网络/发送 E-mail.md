过去，编写程序通过创建到 `SMTP` 专用的端口 25 来发送邮件是一件很简单的事。简单邮件传输协议用于描述 `E-mail` 消息的格式。一旦连接到服务器，就可以发送一个邮件报头（采用 `SMTP` 格式）。紧随其后的是邮件消息。

以下是操作的详细过程：

1）打开一个到达主机的套接字：

```java
Socket s = new Socket("mail.yourserver.com", 25);	// 25 is SMTP
PrintWriter out = new PrintWriter(s.getOutputStream(), "utf-8");
```

2）发送以下信息到打印流：

```
HELO sending host
MAIL FROM: sender e-mail address
RCPT TO: recipient e-mail address
DATA
Subject: subject
(blank line)
mail message(any number of lines)
...
QUIT
```

`SMTP` 规范（RFC 821）规定，每一行都要以 `\r` 再紧跟一个 `\n` 来结尾。

`SMTP` 曾经总是例行公事般地路由任何人的 `E-mail`，但是，在蠕虫泛滥的今天，许多服务器都内置了检查功能，并且只接受来自授信用户或授信 `IP` 地址范围的请求。其中，认证通常是通过安全套接字连接来实现的。

我们将展示如何利用 `JavaMail API` 在 `Java` 程序中发送 `E-mail`。可以从 <https://www.oracle.com/technetwork/java/javamail> 或 <[github.com](https://github.com/javaee/javamail/releases/download/JAVAMAIL-1_6_2/javax.mail.jar)>处下载 `JavaMail`，然后将它解压到硬盘上的某处。

如果要使用 `JavaMail`，则需要设置一些和邮件服务器相关的属性。例如，在使用 `Gmail` 时，需要设置：

```
mail.transport.protocol=smtps
mail.smtps.auth=true
mail.smtps.host=smtp.gmail.com
mail.smtps.user=cayhorstmann@gmail.com
```

出于安全的原因，我们没有将密码放在属性文件中，而是要求提示用户需要输入。

首先要读取属性文件，然后像下面这样获取一个邮件会话：

```java
Session mailSession = Session.getDefaultInstance(props);
```

接着，用恰当的发送者、接受者、主题和消息文本来创建消息：

```java
MimeMessage message = new MimeMessage(mailSession);
message.setFrom(new InternetAddress(from));
message.addRecipient(RecipientType.TO, new InternetAddress(to));
message.setSubject(subject);
message.setText(builder.toString());
```

然后将消息发送走：

```java
Transport tr = mailSession.getTransport();
tr.connect(null, password);
tr.sendMessage(message, message.getAllRecipients());
tr.close();
```

要运行该程序，需要键入：

```shell
java -classpath .:path/to/mail.jar path/to/message.txt
```

> 提示：如果你搞不清楚为什么你的邮件连接无法正常工作，那么可以调用：
>
> ```java
> mailSession.setDebug(true);
> ```

**示例程序：MailTest.java**

```java
package com.qty.mailtest;
import java.io.Console;
import java.io.InputStream;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Properties;

import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.Message.RecipientType;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

/**
 * This program shows how to use JavaMail to send mail messages.
 */
public class MailTest {

	public static void main(String[] args) {
		try {
			Properties props = new Properties();
			try (InputStream in = Files.newInputStream(Paths.get("mail", "mail.properties"))) {
				props.load(in);
			}
			List<String> lines = Files.readAllLines(Paths.get(args[0]), Charset.forName("utf-8"));

			String from = lines.get(0);
			String to = lines.get(1);
			String subject = lines.get(2);

			StringBuilder builder = new StringBuilder();
			for (int i = 3; i < lines.size(); i++) {
				builder.append(lines.get(i));
				builder.append("\n");
			}

			Console console = System.console();
			String password = new String(console.readPassword("Password: "));

			Session mailSession = Session.getDefaultInstance(props);
			// mailSession.setDebug(true);
			MimeMessage message = new MimeMessage(mailSession);
			message.setFrom(new InternetAddress(from));
			message.addRecipient(RecipientType.TO, new InternetAddress(to));
			message.setSubject(subject);
			message.setText(builder.toString());
			Transport tr = mailSession.getTransport();
			try {
				tr.connect(null, password);
				tr.sendMessage(message, message.getAllRecipients());
			} finally {
				tr.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
```

