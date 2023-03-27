[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

Android 13 开机动画要求动画图片的颜色空间为 RGBA，可以使用下面脚本将图片的颜色空间转换为 RGBA 模式：

```python
from PIL import Image

import os

def convertColorSpace(filePath):
    image = Image.open(filePath)

    # 设置每个像素点颜色的透明度
    image = image.convert('RGBA')
    img_w, img_h = image.size
    color_white = (255, 255, 255, 255)
    for j in range(img_h):
        for i in range(img_w):
            pos = (i, j)
            color_now = image.getpixel(pos)
            if color_now == color_white:
                # 透明度置为0
                color_now = color_now[:-1] + (0,)
                image.putpixel(pos, color_now)
    
    savePath = os.path.dirname(filePath) + "/rgba"
    if not os.path.exists(savePath):
        os.makedirs(savePath)

    fileName = os.path.splitext(os.path.basename(filePath))[0] + ".png"
    print("convertColorSpace=>fileName: " + fileName)
    savePath = savePath + "/" + fileName
    print("convertColorSpace=>savePath: " + savePath)
    img.save(savePath) # 要保存为.PNG格式的图片才可以

# 图片存储目录
picDirPath = "C:/Users/xiaotuan/Desktop/新建文件夹"
print("Picture directory: " + picDirPath)

# 遍历目录下的图片文件
if os.path.exists(picDirPath) and os.path.isdir(picDirPath):
    for fileName in os.listdir(picDirPath):
        if fileName.lower().endswith(".jpg") or fileName.lower().endswith(".png"):
            print("Convert file: " + fileName)
            convertColorSpace(picDirPath + "/" + fileName)
        else:
            print("File: " + fileName + " is not a picture.")

print("Convert done.")
```

图片的最终样式如下（需要在Windows 图片查看器中查看）：

![01](./images/anim.png)

> 提示：默认情况下，动画背景是黑色的，如果需要显示白色背景，可以修改 `sys/frameworks/base/cmds/bootanimation/BootAnimation.cpp` 文件如下代码：
>
> ```diff
> diff --git a/frameworks/base/cmds/bootanimation/BootAnimation.cpp b/frameworks/base/cmds/bootanimation/BootAnimation.cpp
> index 4b58c9b1049..42577c3b179 100644
> --- a/frameworks/base/cmds/bootanimation/BootAnimation.cpp
> +++ b/frameworks/base/cmds/bootanimation/BootAnimation.cpp
> @@ -1515,11 +1515,13 @@ bool BootAnimation::playAnimation(const Animation& animation) {
>  
>              mCallbacks->playPart(i, part, r);
>  
> -            glClearColor(
> -                    part.backgroundColor[0],
> -                    part.backgroundColor[1],
> -                    part.backgroundColor[2],
> -                    1.0f);
> +            // glClearColor(
> +            //        part.backgroundColor[0],
> +            //        part.backgroundColor[1],
> +            //        part.backgroundColor[2],
> +            //        1.0f);
> +                                       
> +                       glClearColor(255.0f, 255.0f, 255.0f, 1.0f);
>  
>              ALOGD("Playing files = %s/%s, Requested repeat = %d, playUntilComplete = %s",
>                      animation.fileName.string(), part.path.string(), part.count,
> ```

