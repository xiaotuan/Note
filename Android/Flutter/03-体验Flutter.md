[toc]

# 起步: 体验

本页介绍如何 “试驾” Flutter: 从我们的模板创建一个新的Flutter应用程序，运行它，并学习如何使用Hot Reload进行更新重载

Flutter是一个灵活的工具包，所以请首先选择您的开发工具来编写、构建和运行您的Flutter应用程序。

## Android Studio

  - *Android Studio:* 为Flutter提供完整的IDE体验.

  - **创建新应用**

  - 1. 选择 **File>New Flutter Project**
    2. 选择 **Flutter application** 作为 project 类型, 然后点击 Next
    3. 输入项目名称 (如 `myapp`), 然后点击 Next
    4. 点击 **Finish**
    5. 等待Android Studio安装SDK并创建项目.

  - 上述命令创建一个Flutter项目，项目名为myapp，其中包含一个使用[Material 组件](https://material.io/guidelines/)的简单演示应用程序。

  - 在项目目录中，您应用程序的代码位于 `lib/main.dart`.

  - **运行应用程序**
- 1. 定位到Android Studio 工具栏:
     ![Main IntelliJ toolbar](./images/main-toolbar.png)
    - 2. 在 **target selector** 中, 选择一个运行该应用的Android设备. 如果没有列出可用，请选择 **Tools>Android>AVD Manager** 并在那里创建一个
    - 3. 在工具栏中点击 **Run图标**, 或者调用菜单项 **Run > Run**.
    - 4. 如果一切正常, 您应该在您的设备或模拟器上会看到启动的应用程序:
     ![Starter App on Android](./images/flutter-starter-app-android.png)
    
  - **体验热重载**

    - Flutter 可以通过 *热重载（hot reload）* 实现快速的开发周期，热重载就是无需重启应用程序就能实时加载修改后的代码，并且不会丢失状态（译者语:如果是一个web开发者，那么可以认为这和webpack的热重载是一样的）。简单的对代码进行更改，然后告诉IDE或命令行工具你需要重新加载（点击reload按钮），你就会在你的设备或模拟器上看到更改。

    - 1. 将字符串
     `'You have pushed the button this many times:'` 更改为
     `'You have clicked the button this many times:'`
    - 2. 不要按“Stop”按钮; 让您的应用继续运行。
    - 3. 要查看您的更改, 只需调用 **Save All** (`cmd-s` / `ctrl-s`), 或点击 **热重载按钮** (带有闪电⚡️图标的按钮).

  - 你就会立即看到更新后的字符串。

## VS Code

*VS Code:* 轻量级编辑器，支持Flutter运行和调试.

- 创建新的应用

  1. 启动 VS Code
  2. 调用 **View>Command Palette…**
  3. 输入 ‘flutter’, 然后选择 **‘Flutter: New Project’** action
  4. 输入 Project 名称 (如`myapp`), 然后按回车键
  5. 指定放置项目的位置，然后按蓝色的确定按钮
  6. 等待项目创建继续，并显示main.dart文件

上述命令创建一个Flutter项目，项目名为myapp，其中包含一个使用[Material 组件](https://material.io/guidelines/)的简单的演示应用程序。

在项目目录中，您的应用程序的代码位于 `lib/main.dart`.

- 运行应用程序

  1. 确保在VS Code的右下角选择了目标设备
  2. 按 F5 键或调用**Debug>Start Debugging**
  3. 等待应用程序启动
  4. 如果一切正常，在应用程序建成功后，您应该在您的设备或模拟器上看到应用程序:
   ![Starter App on Android](./images/flutter-starter-app-android.png)

- 体验热重载

Flutter 可以通过 *热重载（hot reload）* 实现快速的开发周期，热重载就是无需重启应用程序就能实时加载修改后的代码，并且不会丢失状态（译者语:如果是一个web开发者，那么可以认为这和webpack的热重载是一样的）。简单的对代码进行更改，然后告诉IDE或命令行工具你需要重新加载（点击reload按钮），你就会在你的设备或模拟器上看到更改。

  1. 用你喜欢的编辑器打开文件`lib/main.dart`
  2. 将字符串
      `'You have pushed the button this many times:'` 更改为
      `'You have clicked the button this many times:'`
  3. 不要按“停止”按钮; 让您的应用继续运行.
  4. 要查看您的更改，请调用 **Save** (`cmd-s` / `ctrl-s`), 或者点击 **热重载按钮** (绿色圆形箭头按钮).

你会立即在运行的应用程序中看到更新的字符串

## Terminal + 编辑器

*Terminal + 编辑器:* 您的编辑选择与Flutter的终端工具结合运行和构建

-  创建新的应用

  1. 使用 `flutter create` 命令创建一个project:

  ```
  $ flutter create myapp
  $ cd myapp
  ```

  上述命令创建一个Flutte让项目，项目名为`myapp`，其中包含一个使用[Material 组件](https://material.io/guidelines/)的简单演示应用程序。

  在项目目录中，您的应用程序的代码位于 `lib/main.dart`.

  - 运行应用程序

  - 检查Android设备是否在运行。如果没有显示, 请参照 [设置](https://flutterchina.club/get-started/install/).

  ```
  $ flutter devices
  ```

  - 运行 `flutter run` 命令来运行应用程序:

  ```
  $ flutter run
  ```

  如果一切正常，在应用程序建成功后，您应该在您的设备或模拟器上看到应用程序:
  ![Starter App on Android](./images/flutter-starter-app-android.png)

- 体验热重载

Flutter 可以通过 *热重载（hot reload）* 实现快速的开发周期，热重载就是无需重启应用程序就能实时加载修改后的代码，并且不会丢失状态（译者语:如果是一个web开发者，那么可以认为这和webpack的热重载是一样的）。简单的对代码进行更改，然后告诉IDE或命令行工具你需要重新加载（点击reload按钮），你就会在你的设备或模拟器上看到更改。

  1. 打开文件`lib/main.dart`
  2. 将字符串
      `'You have pushed the button this many times:'` 更改为
      `'You have clicked the button this many times:'`
  3. 不要按“停止”按钮; 让您的应用继续运行.
  4. 要查看您的更改，请调用 **Save** (`cmd-s` / `ctrl-s`), 或者点击 **热重载按钮** (带有闪电图标的按钮).

你会立即在运行的应用程序中看到更新的字符串