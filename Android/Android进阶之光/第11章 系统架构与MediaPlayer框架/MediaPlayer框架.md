[toc]

### 1. Java Framework 层的 MediaPlayer 分析

我们来查看 MediaPlayer 的 prepare 方法, 如下所示：

**frameworks/base/media/java/android/media/MediaPlayer.java**

```java
public void prepare() throws IOException, IllegalStateException {
    _prepare();
    scanInternalSubtitleTracks();

    // DrmInfo, if any, has been resolved by now.
    synchronized (mDrmLock) {
        mDrmInfoResolved = true;
    }
}
```

### 2. JNI 层的 MediaPlayer 分析

要使用 JNI 需要先加载 JNI 库，在 MediaPlayer.java 中有如下代码：

**frameworks/base/media/java/android/media/MediaPlayer.java**

```java
static {
    System.loadLibrary("media_jni");
    native_init();
}
```

MediaPlayer 的 JNI 层的代码在 frameworks/base/media/jni/android_media_MediaPlayer.cpp 中，代码如下所示：

**frameworks/base/media/jni/android_medai_MediaPlayer.cpp**

```cpp
static const JNINativeMethod gMethods[] = {
    ...
    {"_setDataSource",      "(Ljava/io/FileDescriptor;JJ)V",    (void *)android_media_MediaPlayer_setDataSourceFD},
    {"_setDataSource",      "(Landroid/media/MediaDataSource;)V",(void *)android_media_MediaPlayer_setDataSourceCallback },
    {"_setVideoSurface",    "(Landroid/view/Surface;)V",        (void *)android_media_MediaPlayer_setVideoSurface},
    ...
    {"_prepare",            "()V",                              (void *)android_media_MediaPlayer_prepare},
    ...
};
```

从上面来看，JNINativeMethod 数组有 3 个参数。

+ 第一个参数，比如 "_prepare"，它是 Java 层 Native 方法的名称。在 Java 层调用 Native 方法，交由 JNI 层来实现。
+ 第二个参数是 Java 层 Native 方法的参数和返回值。其中 () 中的字符代表参数，后面的字母则代表返回值。
+ 第三个参数是 Java 层 Native 方法对应的 JNI 层的方法，比如 _prepare 方法对应 JNI 层的方法为 android_media_MediaPlayer_prepare。而通过 JNI 层的方法就可以调用 Native 层相应的方法。

前面在 MediaPlayer.java 的静态代码中调用了 native_init 方法，它对应的是 android_media_MediaPlayer_native_init 方法，如下所示:

**frameworks/base/media/jni/android_medai_MediaPlayer.cpp**

```cpp
static void
android_media_MediaPlayer_native_init(JNIEnv *env)
{
    jclass clazz;

    clazz = env->FindClass("android/media/MediaPlayer");	// 1
    if (clazz == NULL) {
        return;
    }

    fields.context = env->GetFieldID(clazz, "mNativeContext", "J");
    if (fields.context == NULL) {
        return;
    }

    fields.post_event = env->GetStaticMethodID(clazz, "postEventFromNative",
                                               "(Ljava/lang/Object;IIILjava/lang/Object;)V");	// 2
    ...
}
```

上面代码注释 1 处的代码是 JNI 层调用 Java 层，获取 MediaPlayer 对象。在注释2 处的代码获取了 Java 层的 postEventFromNative 方法。

_prepare 对应的 JNI 层的方法为 android_media_MediaPlayer_prepare，代码如下所示：

**frameworks/base/media/jni/android_medai_MediaPlayer.cpp**

```cpp
static void
android_media_MediaPlayer_prepare(JNIEnv *env, jobject thiz)
{
    sp<MediaPlayer> mp = getMediaPlayer(env, thiz);	// 1
    if (mp == NULL ) {
        jniThrowException(env, "java/lang/IllegalStateException", NULL);
        return;
    }

    // Handle the case where the display surface was set before the mp was
    // initialized. We try again to make it stick.
    sp<IGraphicBufferProducer> st = getVideoSurfaceTexture(env, thiz);
    mp->setVideoSurfaceTexture(st);

    process_media_player_call( env, thiz, mp->prepare(), "java/io/IOException", "Prepare failed." );	// 2
}
```

在上面代码注释 1 处得到 MediaPlayer 的强指针，接着再注释 2 处的 process_media_player_call 方法中，调用 mp->prepare() 来调用 MediaPlayer 的 prepare 方法。也就是通过 JNI 层的 android_media_MediaPlayer_prepare 方法调用了 Natvie 层的 prepare 方法。因此通过 JNINativeMethod 数组间接实现了 Java 层与 Native 层的关联。

### 3. Native 层的 MediaPlayer 分析

MediaPlayer 的 Native 层整体是一个 C/S（Client/Server）架构，Client 端和 Server 端是运行在两个进程中的，它们之间是通过 Binder 机制来进行通信的。Client 端 MediaPlayer 对应的动态库是 libmedia.so，Server 端 MediaPlayerService 对应的动态库为 libmediaservice.so。首先我们分析 Client 端的实现。

#### 3.1 Client 端分析

MediaPlayer Client 端的功能实现定义的头文件为 mediaplayer.h，相应的源文件为 mediaplayer.cpp。我们接着来看 mediaplayer.cpp 的 prepare 方法，如下所示：

**frameworks/av/media/libmedia/mediaplayer.cpp**

```cpp
status_t MediaPlayer::prepare()
{
    ...
    status_t ret = prepareAsync_l();
    ...
}
```

prepare 方法会调用 prepareAsync_l 方法：

**frameworks/av/media/libmedia/mediaplayer.cpp**

```cpp
status_t MediaPlayer::prepareAsync_l()
{
    if ( (mPlayer != 0) && ( mCurrentState & (MEDIA_PLAYER_INITIALIZED | MEDIA_PLAYER_STOPPED) ) ) {
        if (mAudioAttributesParcel != NULL) {
            mPlayer->setParameter(KEY_PARAMETER_AUDIO_ATTRIBUTES, *mAudioAttributesParcel);
        } else {
            mPlayer->setAudioStreamType(mStreamType);
        }
        mCurrentState = MEDIA_PLAYER_PREPARING;
        return mPlayer->prepareAsync();	// 1
    }
    ALOGE("prepareAsync called in state %d, mPlayer(%p)", mCurrentState, mPlayer.get());
    return INVALID_OPERATION;
}
```

在上面的代码注释 1 处调用了 mPlayer 的 prepareAsync 方法，那么 mPlayer 指 的是什么呢？我们带着这个问题来查看 mediaplayer.cpp 的 setDataSource 方法， 如下所示：

**frameworks/av/media/libmedia/mediaplayer.cpp**

```cpp
status_t MediaPlayer::setDataSource(const sp<IDataSource> &source)
{
    ALOGV("setDataSource(IDataSource)");
    status_t err = UNKNOWN_ERROR;
    const sp<IMediaPlayerService> service(getMediaPlayerService());	// 1
    if (service != 0) {
        sp<IMediaPlayer> player(service->create(this, mAudioSessionId));	// 2
        if ((NO_ERROR != doSetRetransmitEndpoint(player)) ||
            (NO_ERROR != player->setDataSource(source))) {
            player.clear();
        }
        err = attachNewPlayer(player);	// 3
    }
    return err;
}
```

在上面代码注释 1 处通过 getMediaPlayerService方法得到 IMediaPlayerService 指针。IMediaPlayerService 指针指向的就是 MediaPlayer 的 Service 端：MediaPlayerService。又在注释 2        处通过 IMediaPlayerService 的 create 方法得到 IMediaPlayer 指针。通过 IMediaPlayer 指针就可以调用 MediaPlayerService 所提供的各种功能，接下来看注释 3 处的 attachNewPlayer 方法：

**frameworks/av/media/libmedia/mediaplayer.cpp**

```cpp
status_t MediaPlayer::attachNewPlayer(const sp<IMediaPlayer>& player)
{
    ...
        mPlayer = player;
    ...
}
```

attachNewPlayer 方法将 player 赋值给 mPlayer。mPlayer 指的就是 IMediaPlayer 指针，调用 mPlayer 的 prepareAsync 方法其实就是调用 MediaPlayerService 的 prepareAsync 方法。

#### 3.2 Server 端分析

Android 的多媒体服务是由一个叫作 MediaServer 的服务进程提供的，它是一个可执行程序，在 Android 系统启动时，MediaServer 也会被启动。它的入口函数如下所示：

**frameworks/av/media/mediaserver/main_mediaserver.cpp**

```cpp

```

