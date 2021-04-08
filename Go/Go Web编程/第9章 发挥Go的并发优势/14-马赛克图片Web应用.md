### 9.4.2　马赛克图片Web应用

在实现了马赛克生成函数之后，我们接下来就可以实现与之相对应的Web应用了。代码清单9-16展示了这个应用的具体代码，这些代码放在了 `main.go` 文件中。

代码清单9-16　马赛克图片Web应用

```go
package main
import (
　"bytes"
　"encoding/base64"
　"fmt"
　"html/template"
　"image"
　"image/draw"
　"image/jpeg"
　"net/http"
　"os"
　"strconv"
　"sync"
　"time"
)
func main() {
　mux := http.NewServeMux()
　files := http.FileServer(http.Dir("public"))
　mux.Handle("/static/", http.StripPrefix("/static/", files))
　mux.HandleFunc("/", upload)
　mux.HandleFunc("/mosaic", mosaic)
　server := &http.Server{
　　Addr:　　"127.0.0.1:8080",
　　Handler: mux,
　}
　TILESDB = tilesDB()
　fmt.Println("Mosaic server started.")
　server.ListenAndServe()
}
func upload(w http.ResponseWriter, r *http.Request) {
　t, _ := template.ParseFiles("upload.html")
　t.Execute(w, nil)
}
func mosaic(w http.ResponseWriter, r *http.Request) {
　t0 := time.Now()
    r.ParseMultipartForm(10485760) 
　file, _, _ := r.FormFile("image") ❶
　defer file.Close()
    tileSize, _ := strconv.Atoi(r.FormValue("tile_size"))
　original, _, _ := image.Decode(file)  ❷
　bounds := original.Bounds()
　newimage := image.NewNRGBA(image.Rect(bounds.Min.X, bounds.Min.X,
　bounds.Max.X, bounds.Max.Y))
　db := cloneTilesDB() ❸
　sp := image.Point{0, 0} ❹
　for y := bounds.Min.Y; y < bounds.Max.Y; y = y + tileSize { ❺
　　for x := bounds.Min.X; x < bounds.Max.X; x = x + tileSize {
　　　r, g, b, _ := original.At(x, y).RGBA()
　　　color := [3]float64{float64(r), float64(g), float64(b)}
　　　nearest := nearest(color, &db)
　　　file, err := os.Open(nearest)
　　　if err == nil {
　　　　img, _, err := image.Decode(file)
　　　　if err == nil {
　　　　　t := resize(img, tileSize)
　　　　　tile := t.SubImage(t.Bounds())
　　　　　tileBounds := image.Rect(x, y, x+tileSize, y+tileSize)
　　　　　draw.Draw(newimage, tileBounds, tile, sp, draw.Src)
　　　　} else {
　　　　　fmt.Println("error:", err, nearest)
　　　　}
　　　} else {
　　　　fmt.Println("error:", nearest)
　　　}
　　　file.Close()
　　}
　}
　buf1 := new(bytes.Buffer)
　jpeg.Encode(buf1, original, nil) ❻
　originalStr := base64.StdEncoding.EncodeToString(buf1.Bytes())
　buf2 := new(bytes.Buffer)
　jpeg.Encode(buf2, newimage, nil)
　mosaic := base64.StdEncoding.EncodeToString(buf2.Bytes())
　t1 := time.Now()
　images := map[string]string{
　　"original": originalStr,
　　"mosaic": mosaic,
　　"duration": fmt.Sprintf("%v ", t1.Sub(t0)),
　}
　t, _ := template.ParseFiles("results.html")
　t.Execute(w, images)
}
```

❶ 获取用户上传的目标图片，以及瓷砖图片的尺寸

❷ 对用户上传的目标图片进行解码

❸ 复制瓷砖图数据库

❹ 为每张瓷砖图片设置起始点

❺ 对目标图片分割出的每张子图进行迭代

❻ 将图片编码为JPEG 格式，然后通过base64字符串将其传输至浏览器

`mosaic` 函数是一个处理器函数，在这个函数里包含了用于生成马赛克图片的主要逻辑：首先，程序会获取用户上传的目标图片，并从表单中获取瓷砖图片的尺寸；接着，程序会对目标图片进行解码，并创建出一张全新的、空白的马赛克图片；之后，程序会复制一份瓷砖图片数据库，并为每张瓷砖图片设置起始点（source point），而这一起始点将在稍后的代码中被 `image/draw` 包所使用。在完成了上述的准备工作之后，程序就可以开始对目标图片分割出的各张瓷砖图片尺寸的子图片进行迭代了。

对于每张被分割的子图片，程序都会把它左上角的第一个像素设置为该图片的平均颜色，然后在瓷砖图片数据库中查找与该颜色最为接近的瓷砖图片。在找到匹配的瓷砖图片之后，被调用的函数就会向程序返回该图片的文件名，然后程序就可以打开这张瓷砖图片并将其缩放至指定的瓷砖图片尺寸了。在缩放操作执行完毕之后，程序就会把最终得到的瓷砖图片绘制到之前创建的马赛克图片上。

在使用上述方法生成出整张马赛克图片之后，程序首先会将其编码为JPEG格式的图片，然后再将图片编码为base64格式的字符串。

之后，程序会将用户上传的目标图片以及新鲜出炉的马赛克图片都发送到代码清单9-17中展示的 `results.html` 模板中。正如代码清单中加粗部分的代码所示，这个模板会通过数据URL以及嵌入Web页面中的base64字符串来显示被传入的两张图片。注意，这里使用的数据URL跟一般URL的作用并不相同，前者用于包含给定的数据，而后者则用于指向其他资源。

代码清单9-17　用于展示马赛克图片生成结果的模板

```go
< !DOCTYPE html>
< html>
　< head>
　　< meta http-equiv="Content-Type" content="text/html; charset=utf-8">
　　< title>Mosaic< /title>
　　...
　< /head>
　< body>
　　< div class='container'>
　　　　< div class="col-md-6">
　　　　　< img src="data:image/jpg;base64,{{ .original }}" width="100%">
　　　　　< div class="lead">Original< /div>
　　　　< /div>
　　　　< div class="col-md-6">
　　　　　< img src="data:image/jpg;base64,{{ .mosaic }}" width="100%">
　　　　　< div class="lead">Mosaic – {{ .duration }} < /div>
　　　　< /div>
　　　　< div class="col-md-12 center">
　　　　　< a class="btn btn-lg btn-info" href="/">Go Back< /a>
　　　　< /div>
　　< /div>
　　< br>
　< /body>
< /html>
```

假设上述程序位于 `mosaic` 目录当中，那么我们可以在构建该程序之后，通过执行以下命令，以只使用一个CPU的方式去运行它，并得到图9-5所示的结果：

```go
GOMAXPROCS=1 ./mosaic
```

![56.png](../images/56.png)
<center class="my_markdown"><b class="my_markdown">图9-5　基本的马赛克图片生成Web应用</b></center>

在完成了基本的马赛克图片生成Web应用之后，我们接下来要考虑的就是如何把这个应用改造成相应的并发版本了。

