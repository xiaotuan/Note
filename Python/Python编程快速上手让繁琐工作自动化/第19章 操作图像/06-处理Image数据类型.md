### 19.2.1　处理Image数据类型

`Image` 对象有一些有用的属性，提供了加载的图像文件的基本信息：它的宽度和高度、文件名和图像格式（如JPEG、GIF或PNG）。

例如，在交互式环境中输入以下代码：

```javascript
   >>> from PIL import Image
   >>> catIm = Image.open('zophie.png')
   >>> catIm.size
❶  (816, 1088)
❷  >>> width, height = catIm.size
❸  >>> width
   816
❹  >>> height
   1088
   >>> catIm.filename
   'zophie.png'
   >>>  catIm.format
   'PNG'
   >>> catIm.format_description
   'Portable network graphics'
❺  >>> catIm.save('zophie.jpg')
```

从zophie.png得到一个 `Image` 对象并将其保存在 `catIm` 中后，我们可以看到该对象的 `size` 属性是一个元组，包含该图像的宽度和高度的像素数❶。我们可以将元组中的值赋给 `width` 和 `height` 变量❷，以便分别访问宽度❸和高度❹。 `filename` 属性描述了原始文件的名称。 `format` 和 `format_description` 属性是字符串，描述了原始文件的图像格式（ `format_description` 比较详细）。

最后，调用 `save()` 方法，传入 `'zophie.jpg'` ，将新图像以文件名zophie.jpg保存到硬盘上❺。 `pillow` 看到文件扩展名是.jpg，就自动使用JPEG图像格式来保存图像。现在硬盘上应该有两个图像：zophie.png和zophie.jpg。虽然这些文件都基于相同的图像，但它们不一样，因为格式不同。

`pillow` 还提供了 `Image.new()` 函数，它返回一个 `Image` 对象。这很像 `Image.open()` ，不过 `Image.new()` 返回的对象表示空白的图像。 `Image.new()` 的参数如下。

+ 字符串 `'RGBA'` ，将颜色模式设置为RGBA（还有其他模式，但本书没有涉及）。
+ 大小，是两个整数元组，作为新图像的宽度和高度。
+ 图像开始采用的背景颜色，是一个表示RGBA值的 4 整数元组。你可以用 `ImageColor. getcolor()` 函数的返回值作为这个参数。另外， `Image.new()` 也支持传入标准颜色名称的字符串。

例如，在交互式环境中输入以下代码：

```javascript
   >>> from PIL import Image
❶  >>> im = Image.new('RGBA', (100, 200), 'purple')
   >>> im.save('purpleImage.png')
❷  >>> im2 = Image.new('RGBA', (20, 20))
   >>> im2.save('transparentImage.png')
```

这里，我们创建了一个 `Image` 对象，它有100像素宽、200像素高，带有紫色背景❶。然后，该图像存入文件purpleImage.png中。我们再次调用 `Image.new()` ，创建另一个 `Image` 对象，这次传入（ `20, 20` ）作为大小，没有指定背景色❷。如果未指定颜色参数，默认的颜色是不可见的黑色（0, 0, 0, 0），因此第二个图像具有透明背景，我们将这个20像素×20像素的透明正方形存入transparentImage.png。

