PHP 的内置函数 `header()` 可用于利用 HTTP 头协议。函数 `header()` 的语法如下：

```php
header(header string);
```

要使用 `header()` 重定向 Web 浏览器，可输入：

```php
header('Location: http://www.example.com/page.php');
```

`Content-Type` 指示 Web 浏览器其后将接着什么类型的数据。`Content-Type` 值与数据的 MIME 类型匹配。

```php
header("Content-Type:application/pdf\n");
```

可以使用 `Content-Disposition`，它告诉浏览器如何处理数据：

```php
header("Content-Disposition: attachment; filename=\"somefile.pdf"\n");
```

attachment 值提示浏览器下载文件。一种替代方法是使用 inline，它告诉浏览器显示数据。filename 属性告诉浏览器与数据关联的名称。

用于下载文件的第三个头部是 Content-Length。这个值对应于要发送的数据量。

```php
header("Content-Length: 4096\n");
```

> 如果一个脚本使用多个 `header()` 调用，应该用换行符（\n）终止每个 `hearder()` 调用。更重要的是，必须在把**任何**内容发送给 Web 浏览器之前调用它。这包括 HTML，或者甚至是空白。如果你的代码在调用 header() 之前具有任何 echo 或 print 语句，把空白行保持在 PHP 标签外面，或者包含做任何事情的文件，则会看到一条出错消息。
> ```
> Warning: Cannot modify header information - headers already sent by (output started at /Users/larryullman/Sites/phpmysql4/proxy.php:2)in /Users/larryullman/Sites/phpmysql4/proxy.php on line 3
> ```

**提示**

+ 有一点无论怎样强调也不过分，即在使用 `header()` 函数之前，不能把**任何内容**发送到 Web 浏览器。即使包含文件在 PHP 结束标签后面有一个空白行，这也会使得 `header()` 函数不可用。
+ 在使用 `header()` 时为了避免出现问题，可以先调用 `headers_sent()` 函数。它返回一个布尔值，指示是否已经把某些内容发送给了 Web 浏览器：

```php
if (!headers_sent()) {
    // Use the header() function.
} else {
    // Do something else.
}
```
输出缓冲技术也可以阻止在使用 `header()` 时出现问题。
+ 可使用用于 Firefox 的 Live HTTP Headers 插件来调试这样的脚本。
+ 你还可以使用 PHP 和 header() 函数来制定网络浏览器的页面编码：

```php
<?php header('Content-Type: text/html; charset=UTF-8');
?>
```

这比使用 META 标签更加有效，但是它需要页面是一个 PHP 脚本。如果使用这个方法，它必须在页面的第一行，所有 HTML 代码的前面。

例如：

```php
<?php # Script 11.5 - show_image.php
// This page displays an image.

$name = FALSE; // Flag variable:

// Check for an image name in the URL:
if (isset($_GET['image'])) {

	// Make sure it has an image's extension:
	$ext = strtolower ( substr ($_GET['image'], -4));
	
	if (($ext == '.jpg') OR ($ext == 'jpeg') OR ($ext == '.png')) {

		// Full image path:
		$image = "../uploads/{$_GET['image']}";

		// Check that the image exists and is a file:
		if (file_exists ($image) && (is_file($image))) {
			
			// Set the name as this image:
			$name = $_GET['image'];	

		} // End of file_exists() IF.

	} // End of $ext IF.
	
} // End of isset($_GET['image']) IF.

// If there was a problem, use the default image:
if (!$name) {
	$image = 'images/unavailable.png';	
	$name = 'unavailable.png';
}

// Get the image information:
$info = getimagesize($image);
$fs = filesize($image);

// Send the content information:
header ("Content-Type: {$info['mime']}\n");
header ("Content-Disposition: inline; filename=\"$name\"\n");
header ("Content-Length: $fs\n");

// Send the file:
readfile ($image);
```