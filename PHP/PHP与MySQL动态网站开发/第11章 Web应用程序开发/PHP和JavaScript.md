虽然 PHP 不能做 JavaScript 所能够做的某些事情，但是 PHP 可用于创建 JavaScript （就像 PHP 可以创建 HTML 那样）。换句话说，网络浏览器中包含了 JavaScript 并用于与 HTML 进行交互，但是 PHP 可以动态生成 JavaScript 代码，就像使用 PHP 来动态生成 HTML 一样。

可以通过 `scandir()` 函数来实现检索上传目录的内容，此函数返回一个数组，列出给定目录中的文件。

在 PHP 中，脚本将使用 `getimagesize()` 函数查找后面的两个值。它返回给定图片的信息数组。

**表11-3 getimagesize()数组**

| 元素 | 值 | 示例 |
| :- | :- | :- |
| 0 | 图像的宽度（以像素为单位） | 423 |
| 1 | 图像的高度（以像素为单位） | 368 |
| 2 | 图像的类型 | 2 （表示 JPG） |
| 3 | 适合的 HTML img 标签数据 | height="368" width="423" |
| mime | 图像的 MIME 类型 | image/png |

```php
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>Images</title>
	<script type="text/javascript" charset="utf-8" src="js/function.js"></script>
</head>
<body>
<p>Click on an image to view it in a separate window.</p>
<ul>
<?php # Script 11.6 - images.php
// This script lists the images in the uploads directory.
// This version now shows each image's file size and uploaded date and time.

// Set the default timezone:
date_default_timezone_set ('America/New_York');

$dir = '../uploads'; // Define the directory to view.

$files = scandir($dir); // Read all the images into an array.

// Display each image caption as a link to the JavaScript function:
foreach ($files as $image) {

	if (substr($image, 0, 1) != '.') { // Ignore anything starting with a period.
	
		// Get the image's size in pixels:
		$image_size = getimagesize ("$dir/$image");
		
		// Calculate the image's size in kilobytes:
		$file_size = round ( (filesize ("$dir/$image")) / 1024) . "kb";
		
		// Determine the image's upload date and time:
		$image_date = date("F d, Y H:i:s", filemtime("$dir/$image"));
		
		// Make the image's name URL-safe:
		$image_name = urlencode($image);
		
		// Print the information:
		echo "<li><a href=\"javascript:createWindow('$image_name',$image_size[0],$image_size[1])\">$image</a> $file_size ($image_date)</li>\n";
	
	} // End of the IF.
    
} // End of the foreach loop.

?>
</ul>
</body>
</html>
```
