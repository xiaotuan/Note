[toc]

### 1. 使用 opencv-python 转换

```python
import cv2

path = "C:\\Users\\xiaotuan\\Desktop\\Image00001.png"
# 开始读取
img = cv2.imread(path,cv2.IMREAD_UNCHANGED)
bmp = "C:\\Users\\xiaotuan\\Desktop\\Image00001.bmp"
cv2.imwrite(bmp,img) #写入
```

### 2. 使用 PIL 转换

```python
from PIL import Image

path = "C:\\Users\\xiaotuan\\Desktop\\Image00001.png"
bmp = "C:\\Users\\xiaotuan\\Desktop\\Image00001.bmp"

indexed = Image.open(path)

print("mode: " + str(indexed.mode))
# 转换成索引模式
img = indexed.convert("P")
# 设置颜色深度为 24 位
img = img.quantize(colors=24, method=2)

img.save(bmp)

img = Image.open(bmp)
img.show()
print("size: " + str(img.size) + ", widht: " + str(img.width) + ", height: " + str(img.height) + ", format: " + str(img.format))
img.close()
```
