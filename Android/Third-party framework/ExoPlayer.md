<center>
  <font size="5">
  	<b>ExoPlayer框架</b>
  </font>
</center>

[toc]

#### 1. GitHub

<https://github.com/google/ExoPlayer>

#### 2. 最新版本

<kbd>r2.11.3</kbd>

> 该框架最低支持Android版本是21。

#### 3. 简介

ExoPlayer是适用于Android的应用程序级媒体播放器。它提供了Android MediaPlayer API的替代方法，可以在本地和Internet上播放音频和视频 ExoPlayer支持Android MediaPlayer API当前不支持的功能，包括DASH和SmoothStreamin自适应播放。与MediaPlayer API不同，ExoPlayer易于自定义和扩展，可以通过Play商店应用程序更新进行更新。

#### 4. 使用方法

ExoPlayer modules can be obtained from JCenter. It's also possible to clone the repository and depend on the modules locally.

#####4.1 From JCenter

######4.1.1 Add repositories

The easiest way to get started using ExoPlayer is to add it as a gradle dependency. You need to make sure you have the Google and JCenter repositories included in the `build.gradle` file in the root of your project:

```
repositories {
    google()
    jcenter()
}
```

###### 4.1.2 Add ExoPlayer module dependencies

Next add a dependency in the `build.gradle` file of your app module. The following will add a dependency to the full library:

```
implementation 'com.google.android.exoplayer:exoplayer:2.X.X'
```

where `2.X.X` is your preferred version.

As an alternative to the full library, you can depend on only the library modules that you actually need. For example the following will add dependencies on the Core, DASH and UI library modules, as might be required for an app that plays DASH content:

```
implementation 'com.google.android.exoplayer:exoplayer-core:2.X.X'
implementation 'com.google.android.exoplayer:exoplayer-dash:2.X.X'
implementation 'com.google.android.exoplayer:exoplayer-ui:2.X.X'
```

The available library modules are listed below. Adding a dependency to the full library is equivalent to adding dependencies on all of the library modules individually.

- `exoplayer-core`: Core functionality (required).
- `exoplayer-dash`: Support for DASH content.
- `exoplayer-hls`: Support for HLS content.
- `exoplayer-smoothstreaming`: Support for SmoothStreaming content.
- `exoplayer-ui`: UI components and resources for use with ExoPlayer.

In addition to library modules, ExoPlayer has multiple extension modules that depend on external libraries to provide additional functionality. Some extensions are available from JCenter, whereas others must be built manually. Browse the [extensions directory](https://github.com/google/ExoPlayer/tree/release-v2/extensions/) and their individual READMEs for details.

More information on the library and extension modules that are available from JCenter can be found on [Bintray](https://bintray.com/google/exoplayer).

###### 4.1.3 Turn on Java 8 support

If not enabled already, you also need to turn on Java 8 support in all `build.gradle` files depending on ExoPlayer, by adding the following to the `android` section:

```
compileOptions {
  targetCompatibility JavaVersion.VERSION_1_8
}
```

#####4.2 Locally

Cloning the repository and depending on the modules locally is required when using some ExoPlayer extension modules. It's also a suitable approach if you want to make local changes to ExoPlayer, or if you want to use a development branch.

First, clone the repository into a local directory and checkout the desired branch:

```
git clone https://github.com/google/ExoPlayer.git
cd ExoPlayer
git checkout release-v2
```

Next, add the following to your project's `settings.gradle` file, replacing `path/to/exoplayer` with the path to your local copy:

```
gradle.ext.exoplayerRoot = 'path/to/exoplayer'
gradle.ext.exoplayerModulePrefix = 'exoplayer-'
apply from: new File(gradle.ext.exoplayerRoot, 'core_settings.gradle')
```

You should now see the ExoPlayer modules appear as part of your project. You can depend on them as you would on any other local module, for example:

```
implementation project(':exoplayer-library-core')
implementation project(':exoplayer-library-dash')
implementation project(':exoplayer-library-ui')
```

#####4.3 Developing ExoPlayer

######4.3.1 Project branches

- Development work happens on the `dev-v2` branch. Pull requests should normally be made to this branch.
- The `release-v2` branch holds the most recent release.

######4.3.2 Using Android Studio

To develop ExoPlayer using Android Studio, simply open the ExoPlayer project in the root directory of the repository.