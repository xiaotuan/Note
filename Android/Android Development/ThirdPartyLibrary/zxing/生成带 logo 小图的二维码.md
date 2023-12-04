[toc]

### 1. Kotlin

```kotlin
object QrCodeUtil {
    /**
     * 创建二维码位图 (支持自定义配置和自定义样式)
     * @param content 字符串内容
     * @param width 位图宽度,要求>=0(单位:px)
     * @param height 位图高度,要求>=0(单位:px)
     * @param character_set 字符集/字符转码格式 (支持格式:{@link CharacterSetECI })。传null时,zxing源码默认使用 "ISO-8859-1"
     * @param error_correction 容错级别 (支持级别:{@link ErrorCorrectionLevel })。传null时,zxing源码默认使用 "L"
     * @param margin 空白边距 (可修改,要求:整型且>=0), 传null时,zxing源码默认使用"4"。
     * @param color_black 黑色色块的自定义颜色值
     * @param color_white 白色色块的自定义颜色值
     * @param logoBitmap logo小图片
     * @return
     */
    fun createQRCodeBitmap(
        content: String,
        width: Int,
        height: Int,
        character_set: String = "UTF-8",
        error_correction: String = "H",
        margin: String = "1",
        @ColorInt color_black: Int = Color.BLACK,
        @ColorInt color_white: Int = Color.WHITE,
        logoBitmap: Bitmap? = null
    ): Bitmap? {
        /** 1.参数合法性判断  */
        if (width < 0 || height < 0) { // 宽和高都需要>=0
            return null
        }
        try {
            /** 2.设置二维码相关配置,生成BitMatrix(位矩阵)对象  */
            val hints: Hashtable<EncodeHintType, String> = Hashtable()
            if (character_set.isNotEmpty()) {
                hints[EncodeHintType.CHARACTER_SET] = character_set // 字符转码格式设置
            }
            if (error_correction.isNotEmpty()) {
                hints[EncodeHintType.ERROR_CORRECTION] = error_correction // 容错级别设置
            }
            if (margin.isNotEmpty()) {
                hints[EncodeHintType.MARGIN] = margin // 空白边距设置
            }
            val bitMatrix =
                QRCodeWriter().encode(content, BarcodeFormat.QR_CODE, width, height, hints)

            /** 3.创建像素数组,并根据BitMatrix(位矩阵)对象为数组元素赋颜色值  */
            val pixels = IntArray(width * height)
            for (y in 0 until height) {
                for (x in 0 until width) {
                    if (bitMatrix[x, y]) {
                        pixels[y * width + x] = color_black // 黑色色块像素设置
                    } else {
                        pixels[y * width + x] = color_white // 白色色块像素设置
                    }
                }
            }
            /** 4.创建Bitmap对象,根据像素数组设置Bitmap每个像素点的颜色值,之后返回Bitmap对象  */
            val bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
            bitmap.setPixels(pixels, 0, width, 0, 0, width, height)
            /** 5.为二维码添加logo小图标 */
            if (logoBitmap != null) {
                return addLogo(bitmap, logoBitmap, logoPercent)
            }
            return bitmap
        } catch (e: WriterException) {
            e.printStackTrace()
        }
        return null
    }
    
    private static Bitmap addLogo(Bitmap qrBitmap, Bitmap logoBitmap) {
        int qrCodeWidth = qrBitmap.getWidth();
        int qrCodeHeight = qrBitmap.getHeight();
        int logoWidth = logoBitmap.getWidth();
        int logoHeight = logoBitmap.getHeight();

        Bitmap combinedBitmap = Bitmap.createBitmap(qrCodeWidth, qrCodeHeight, qrBitmap.getConfig());
        Canvas canvas = new Canvas(combinedBitmap);

        canvas.drawBitmap(qrBitmap, 0, 0, null);

        float centerX = (qrCodeWidth - logoWidth) / 2f;
        float centerY = (qrCodeHeight - logoHeight) / 2f;

        canvas.drawBitmap(logoBitmap, centerX, centerY, null);

        return combinedBitmap;
    }

    private fun addLogo(srcBitmap: Bitmap?, logoBitmap: Bitmap?, logoPercent: Float): Bitmap? {
        /** 1.参数合法性判断  */
        if (srcBitmap == null || logoBitmap == null) {
            return null
        }
        /** 2. 获取原图片和Logo图片各自的宽、高值 */
        val srcWidth = srcBitmap.width
        val srcHeight = srcBitmap.height
        val logoWidth = logoBitmap.width
        val logoHeight = logoBitmap.height

        /** 3. 使用Canvas绘制,合成图片 */
        val bitmap = Bitmap.createBitmap(srcWidth, srcHeight, srcBitmap.config)
        val canvas = Canvas(bitmap)
        
        canvas.drawBitmap(srcBitmap, 0f, 0f, null)
        
        val centerX = (srcWidth - logoWidth) / 2f;
        val centerY = (srcHeight - logoHeight) / 2f;
        
        canvas.drawBitmap(logoBitmap, centerX, centerY, null)
        
        return bitmap
    }
}
```

### 2. Java

```java
package com.android.androidtest;

import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.text.TextUtils;
import android.util.Log;

import androidx.annotation.ColorInt;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.EncodeHintType;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.QRCodeWriter;

import java.util.Hashtable;

public class QRCodeUtil {

    private static final String TAG = "QRCodeUtil";

    /**
     * 生成二维码图像
     * @param content 二维码内容
     * @param width 图像宽度
     * @param height 图像高度
     * @param charset 二维码内容字符编码
     * @param errorCorrection 纠错级别
     * @param margin 二维码边距
     * @param blackColor 黑色块的颜色
     * @param whiteColor 白色块的颜色
     * @param logoBitmap logo 图片
     * @return 返回二维码图像
     */
    public static Bitmap createQRCodeBitmap(String content, int width, int height, String charset,
                                      String errorCorrection, String margin, @ColorInt int blackColor,
                                            @ColorInt int whiteColor, Bitmap logoBitmap) {
        if (width < 0 || height < 0) {
            Log.e(TAG, "createQRCodeBitmap=>width and height must great 0.");
            return null;
        }
        try {
            Hashtable<EncodeHintType, String> hints = new Hashtable<>();
            if (!TextUtils.isEmpty(charset)) {
                hints.put(EncodeHintType.CHARACTER_SET, charset);
            }
            if (!TextUtils.isEmpty(errorCorrection)) {
                hints.put(EncodeHintType.ERROR_CORRECTION, errorCorrection);
            }
            if (!TextUtils.isEmpty(margin)) {
                hints.put(EncodeHintType.MARGIN, margin);
            }
            BitMatrix bitMatrix = new QRCodeWriter().encode(content, BarcodeFormat.QR_CODE, width, height, hints);
            int[] pixels = new int[width * height];
            for (int y = 0; y < height; y++) {
                for (int x = 0; x < width; x++) {
                    if (bitMatrix.get(x, y)) {
                        pixels[y * width + x] = blackColor;
                    } else {
                        pixels[y * width + x] = whiteColor;
                    }
                }
            }
            Bitmap bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888);
            bitmap.setPixels(pixels, 0, width, 0, 0, width, height);
            if (logoBitmap != null)  {
                return addLogo(bitmap, logoBitmap);
            }
            return bitmap;
        } catch (WriterException e) {
            Log.e(TAG, "createQRCodeBitmap=>error: ", e);
        }
        return null;
    }

    private static Bitmap addLogo(Bitmap qrBitmap, Bitmap logoBitmap) {
        int qrCodeWidth = qrBitmap.getWidth();
        int qrCodeHeight = qrBitmap.getHeight();
        int logoWidth = logoBitmap.getWidth();
        int logoHeight = logoBitmap.getHeight();

        Bitmap combinedBitmap = Bitmap.createBitmap(qrCodeWidth, qrCodeHeight, qrBitmap.getConfig());
        Canvas canvas = new Canvas(combinedBitmap);

        canvas.drawBitmap(qrBitmap, 0, 0, null);

        float centerX = (qrCodeWidth - logoWidth) / 2f;
        float centerY = (qrCodeHeight - logoHeight) / 2f;

        canvas.drawBitmap(logoBitmap, centerX, centerY, null);

        return combinedBitmap;
    }
}
```

