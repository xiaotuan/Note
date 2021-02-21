[toc]

### 1. Audio 元素

当前，audio 元素支持三种音频格式，即 ACC、MP3 和 Wav，可以通过 `<source>` 元素来为同一个音频指定多个源，供不同的浏览器来选择适合自己的播放源。

### 2. Video 元素

当前，video 元素支持三种视频格式，即 Ogg、MPEG4、WebM。可以通过 `<source>` 元素来为同一个视频指定多个源，供不同的浏览器来选择适合自己的播放源。

### 3. Audio 和 Video 的属性

#### 3.1 src

src 属性用来指定媒体数据的 URL 地址，即播放的视频或者音频文件的 URL 地址。

#### 3.2 preload

该属性表明视频或音频文件是否需要进行预加载。如果需要预加载，浏览器将会预先将视频或者音频进行缓冲，这样可以加快播放的速度。

Preload 属性值有以下三种形式。

+ none：表示不进行预加载。
+ metadata：表示只预先加载媒体的元数组，主要包括媒体字节数、第一帧、播放列表、持续时间等信息。
+ auto：表示预加载全部视频或音频，该值是默认值。

```html
<video src="example.mp4" preload="auto"></video>
```

#### 3.3 poster

该属性为 video 元素的独有属性，用于视频不可用时，向用户展示一张替代图片，从而避免视频不可用时，页面出行一片空白。

```html
<video src="example.mp4" poster="poster.png"></video>
```

#### 3.4 loop

该属性指定是否循环播放视频或音频。

```html
<vide src="example.mp4" loop="loop"></vide>
```

#### 3.5 controls

该属性指定是否为视频或音频添加浏览器自带的播放控制条。开发人员也可以通过写脚本的方式自定义控制条，而不使用浏览器默认的控制条。

```html
<video src="example.mp4" controls="controls"></video>
```

#### 3.6 width 和 height

该属性为 video 元素的独有属性，用来指定视频的宽度和高度。

```html
<video src="example.mp4" width="400" height="300"></video>
```

#### 3.7 error

在读取、使用媒体数据的过程中，正常情况下，video 和 audio 元素的 error 属性为 null。当出现错误时，error 属性将返回一个 MediaError 对象，该对象通过 code 的方式将错误状态提供出来。错误状态值为只读属性，且有4 个可能值。

+ 1（MEDIA_ERR_ABORTED）：数据在下载中因为用户操作的原因而被中止。
+ 2（MEDIA_ERR_NETWORK）：确认媒体资源可用，但是在下载时出现网络错误，媒体数据的下载过程被中止。
+ 3（MEDIA_ERR_DECODE）：确认媒体资源可用，但是解码时发生错误。
+ 4（MEDIA_ERR_SRC_NOT_SUPPORTED）：媒体格式不被支持。

**案例：示例 6-02：读取错误状态**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta keywords="HTML5 Video Audio Error">
		<meta content="读取视频文件的错误状态">
		<title>读取错误状态</title>
	</head>

	<body>
		<!--视频播放器 begin-->
		<video id="showVideo" src="medias/WoWeiZiJiDaiYan-AD.avi" controls></video>
		<!--视频播放器 end-->
		<!--JS 执行-->
		<script>
			var videoerror = document.getElementById("showVideo");
			videoerror.addEventListener("error", function () {
				var errorinfo = videoerror.error;
				switch (errorinfo.code) {
					case 1:
						alert("用户取消了视频的载入。");
						break;
					case 2:
						alert("网络故障，造成数据载入失败。");
						break;
					case 3:
						alert("解码错误，请重新访问。");
						break;
					case 4:
						alert("浏览器不支持获得的视频格式。");
						break;
				}
			}, false);
		</script>
	</body>
</html>
```

#### 3.8 networkState

媒体数据在加载过程中可以使用 video 元素或 audio 元素的 networkState 属性读取当前网络状态，其可能值有 4 个，该属性值为只读属性。

+ 0（NETWORK_EMPTY）：初始状态。
+ 1（NETWORK_IDLE）：浏览器已经选择好用什么编码格式来播放媒体，但尚未建立网络连接。
+ 2（NETWORK_LOADING）：媒体数据加载中。
+ 3（NETWORK_NO_SOURCE）：没有支持的编码格式，不进行加载。

#### 3.9 currentSrc

currentSrc 属性用来读取 video 元素和 audio 元素中正在播放的媒体数据的 URL 地址。

#### 3.10 buffered

buffered 属性用来返回一个对象，该对象实现 TimeRange 接口，以确认浏览器是否已缓存媒体数据。buffered 属性值为只读属性。

#### 3.11 readyState

该属性返回 video 或 audio 元素中媒体当期播放位置的就绪状态，readyState 属性值为只读属性，其有 5 个可能值。

+ 0（HAVE_NOTHING）：没有获得任何媒体的信息，当期播放位置没有播放数据。
+ 1（HAVE_METADATA）：已经获得到足够的媒体信息，但是当前播放位置没有有效的媒体数据，暂时不能够播放。
+ 2（HAVE_CURRENT_DATA）：当期播放位置已经有数据可以播放，但没有获取到可以让播放器前进的数据。如果是视频，就是说当前帧数据已经获得，下一帧数据没有获得。
+ 3（HAVE_FUTURE_DATA）：当前播放位置已经有数据可以播放，而且也获取到了可以让播放器前进的数据。当媒体为视频时，意思是当期帧的数据已经获得，且下一帧的数据也已经获得。
+ 4（HAVE_ENOUGH_DATA）：当前播放位置已经有数据可以播放，下一帧数据已经获得，且浏览器确认媒体数据以某一种速度进行加载，可以保证有足够的后续数据进行播放。

#### 3.12 seeking 和 seekable

seeking 属性返回一个布尔值，表示浏览器是否正在请求某一特定播放位置的数据，true 表示浏览器正在请求数据，false 表示浏览器已经停止请求。

seekable 属性返回一个 TimeRange 对象，该对象表示请求到的数据的时间范围。

seeking 和 seekable 均为只读属性。

#### 3.13 currentTime、startTime 和 duration

currentTime 属性用来读取媒体的当前播放位置，通过修改该属性值可以修改当前播放位置。如果修改的位置上没有可用的媒体数据，将产生 INVALID_STATE_ERR 异常，如果修改的位置上的数据浏览器上没有获得，将产生 INDEX_SIZE_ERR 异常。

startTime 属性用来读取媒体播放的开始时间，通常为 0。

duration 属性用来读取媒体文件总的播放时间。

currentTime、startTime 、duration 属性的值均为秒。currentTime 的属性值为读写属性，startTime、duration 属性值为只读属性。

#### 3.14 played、paused 和 ended

played 属性可以返回一个 TimeRange 对象，该对象中可以读取媒体文件已经播放部分的时间段。该时间段的开始时间为已播放部分的开始时间，结束时间为已播放部分的结束时间。

paused 属性可以返回一个布尔值，表示十分处于暂停播放状态。true 表示目前已经暂停播放，false 表示媒体正在播放。

ended 属性可以返回一个布尔值，表示是否已经播放完毕。true 表示媒体播放完毕，false 表示媒体没有播放完毕。

played、pause、ended 属性值均为只读属性。

#### 3.15 defaultPlaybackRate 和 playbackRate

defaultPlaybackRate 属性读取或修改媒体默认的播放速率。

playbackRate 属性读取或修改媒体当前的播放速率。

#### 3.16 volume 和 muted

volume 属性读取或修改媒体播放的音量，范围为 0 到 1，0 为静音，1 为最大音量。

muted 属性读取或修改媒体的静音状态，该属性值为布尔值，true 表示处于静音状态，false 表示处于非静音状态。

#### 3.17 autoplay

autoplay 属性设置或返回音视频是否在加载后立即开始播放。属性值有两个 true 和 false，true 指示音视频在加载完成后立即播放：false 为默认值，指示音视频不应在加载后立即播放。

```html
<video src="example.mp4" autoplay="true"></video>
```

### 4. Audio 和 Video 的方法

video 元素和 audio 元素具有四种方法。

#### 4.1 play

使用 play 方法来播放媒体，自动将元素的 paused 值变为 false。

#### 4.2 pause

使用 pause 方法来暂停播放，自动将元素的 paused 值变为 true。

#### 4.3 load

使用 load 方法来重新载入媒体进行播放，自动将元素的 playbackRate 属性设置变为 defaultPlaybackRate 属性的值，自动将元素的 error 的值变为 null。

#### 4.4 canPlayType

使用 canPlayType 方法来测试浏览器是否支持指定的媒体类型，该方法的定义如下：

```js
var supportTypeInfo = videoElement.canPlayType(type);
```

其中参数 type 的指定方法是使用播放文件的 MIME 类型来指定，可以在指定的字符串中加上表示媒体编码格式的 code 参数。

该方法返回 3 个可能值，具体值如下所示：

+ 空字符串：表示浏览器不支持此中媒体类型。
+ maybe：表示浏览器可能支持此种媒体类型。
+ probably：表示浏览器确定支持此种媒体类型。

### 5. Audio 和 Video 的事件

#### 5.1 事件处理方法

对事件的捕捉，有以下两种方式。

方式一：监听。

使用 video 或 audio 元素的 addEventListener 方法来对事件的发生进行监听，该方法定义如下：

```js
videoElement.addEventListener(type, listener, userCapture);
```

userCapture 是一个布尔值，表示该事件的响应顺序，该值如果为 true，浏览器采用 Capture 响应方式，如果为 false，浏览器采用 bubbing 响应方式，一般采用 false，默认情况下也为 false。

方法二：使用 JavaScript 脚本中的获取事件句柄。

```html
<video id="videodemo" src="medias/video.webm" onplay="begin_playing();"></video>
<script>
	function begin_playing() {
        ......
    }
</script>
```

#### 5.2 事件

<center><b>表 6-3 HTML5 中的 Audio/Video 事件</b></center>

| 事件           | 描述                                         |
| -------------- | -------------------------------------------- |
| abort          | 当音频/视频的加载已放弃时                    |
| canplay        | 当浏览器可以播放音频/视频时                  |
| canplaythrough | 当浏览器可在不因缓冲而停顿的情况下进行播放时 |
| durationchange | 当音频/视频的时长已更改时                    |
| emptied        | 当目前的播放列表为空时                       |
| ended          | 当目前的播放列表已结束时                     |
| error          | 当在音频/视频加载期间发生错误时              |
| loadeddata     | 当浏览器已加载音频/视频的当前帧时            |
| loadedmetadata | 当浏览器已加载音频/视频的元数据时            |
| loadstart      | 当浏览器开始查找音频/视频时                  |
| pause          | 当音频/视频已暂停时                          |
| paly           | 当音频/视频已开始或不再暂停时                |
| playing        | 当音频/视频在因缓冲而暂停或停止后已就绪时    |
| progress       | 当浏览器正在下载音频/视频时                  |
| ratechange     | 当音频/视频的播放速度已更改时                |
| seeked         | 当用户已移动/跳跃到音频/视频中的新位置时     |
| seeking        | 当用户开始移动/跳跃到音频/视频中的新位置时   |
| stalled        | 当浏览器尝试获取媒体数据，但数据不可用时     |
| suspend        | 当浏览器刻意不获取媒体数据时                 |
| timeupdate     | 当目前的播放位置已更改时                     |
| volumechange   | 当音量已更改时                               |

### 6.案例：在网页上使用背景音乐

**案例：示例 6-03：在网页上使用背景音乐**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8" />
		<meta keywords="HTML5 Audio" />
		<meta content="HTMl5实现视频播放" />
		<title>在网页上使用背景音乐</title>
		<!--CSS 引入-->
		<link rel="stylesheet" type="text/css" href="" />
		<!--JS 引入-->
		<script type="text/javascript" src=""></script>
		<style type="text/css">
			audio {
				/*播放器大小设置*/
				width: 480px;
				height: 80px;
			}
		</style>
	</head>

	<body>
		<!--音乐播放器 begin-->
		<audio src="medias/DaiWoDaoShanDing.mp3" controls autoplay="autoplay" loop></audio>
		<!--音乐播放器 end-->
	</body>
</html>
```

### 7. 案例：在网页上播放视频

**案例：示例 6-04：在网页上播放视频**

```html
<!doctype html>
<html>
	<head>
		<meta charset="utf-8" />
		<meta keywords="HTML5 Audio" />
		<meta content="HTMl5实现视频播放" />
		<title>在网页上使用背景音乐</title>
		<!--CSS 引入-->
		<link rel="stylesheet" type="text/css" href="" />
		<!--JS 引入-->
		<script type="text/javascript" src=""></script>
		<style type="text/css">
			audio {
				/*播放器大小设置*/
				width: 480px;
				height: 80px;
			}
		</style>
	</head>

	<body>
		<!--音乐播放器 begin-->
		<audio src="medias/DaiWoDaoShanDing.mp3" controls autoplay="autoplay" loop></audio>
		<!--音乐播放器 end-->
	</body>
</html>
```

