[toc]

### 1. 使用 opencv-python 转换

#### 1. 安装 opencv-python

```shell
pip install opencv-python
```

#### 2. 转换代码

```python
import cv2

path = "C:\\Users\\xiaotuan\\Desktop\\Image00001.png"
# 开始读取
img = cv2.imread(path,cv2.IMREAD_UNCHANGED)
bmp = "C:\\Users\\xiaotuan\\Desktop\\Image00001.bmp"
cv2.imwrite(bmp,img) #写入
```

### 2. 使用 PIL 转换

#### 2.1 安装 PIL

```shell
pip install pillow
```

#### 2.2 转换代码

```python
from PIL import Image
path = "C:\\Users\\xiaotuan\\Desktop\\Image00001.png"
bmp = "C:\\Users\\xiaotuan\\Desktop\\Image00001.bmp"
img = Image.open(path)
img.save(bmp)
```

### 3. 使用 Aspose.Words 转换

#### 3.1 安装 Aspose.Words

```shell
pip install Aspose.Words
```

#### 3.2 转换代码

```shell
import aspose.words as aw

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

shape = builder.insert_image("C:\\Users\\xiaotuan\\Desktop\\Image00001.png")
shape.image_data.save("C:\\Users\\xiaotuan\\Desktop\\Image00001.bmp")
```

> 提示：使用 Aspose.Words 转换后的 bmp 文件最小。