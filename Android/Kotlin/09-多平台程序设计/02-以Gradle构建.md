[toc]

# 使用 Gradle 构建多平台项目

> 多平台项目是 Kotlin 1.2 与 Kotlin 1.3 中的一个实验性特性。本文档中描述的所有语言与工具特性在未来的 Kotlin 版本中都可能会有所变化。

本文档解释了 [Kotlin 多平台项目](https://www.kotlincn.net/docs/reference/multiplatform.html)的结构，并描述了如何使用 Gradle 配置与构建这些项目。

## 目录

- [项目结构](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#项目结构)
- [搭建一个多平台项目](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#搭建一个多平台项目)
- [Gradle 插件](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#gradle-插件)
- 设置目标
  - [已支持平台](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#已支持平台)
  - [配置编译项](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#配置编译项)
- 配置源集
  - [关联源集](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#关联源集)
  - [添加依赖](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#添加依赖)
  - [语言设置](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#语言设置)
- [默认项目布局](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#默认项目布局)
- [运行测试](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#运行测试)
- 发布多平台库
  - [元数据发布](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#元数据发布)
  - [目标消歧义](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#目标消歧义)
- [JVM 目标平台中的 Java 支持](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#jvm-目标平台中的-java-支持)
- Android 支持
  - [发布 Android 库](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#发布-android-库)
- 使用 Kotlin/Native 目标平台
  - [目标快捷方式](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#目标快捷方式)
  - [构建最终原生二进制文件](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#构建最终原生二进制文件)

## 项目结构

Kotlin 多平台项目的布局由以下构建块构成：

- [目标](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#设置目标)是构建的一部分，负责构建、测试及打包其中一个平台的完整软件。因此，多平台项目通常包含多个目标。
- 构建每个目标涉及一到多次编译 Kotlin 源代码。换句话说，一个目标可能有一到多个[编译项](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#配置编译项)。例如，一个编译项用于编译生产代码，另一个用于编译测试代码。
- Kotlin 源代码会放到[源集](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#配置源集)中。除了 Kotlin 源文件与资源外，每个源集都可能有自己的依赖项。源集之间以*“依赖”*关系构成了层次结构。源集本身是平台无关的，但是如果一个源集只面向单一平台编译，那么它可能包含平台相关代码与依赖项。

每个编译项都有一个默认源集，是放置该编译项的源代码与依赖项的地方。默认源集还用于通过“依赖”关系将其他源集引到该编译项中。

以下是一个面向 JVM 与 JS 的项目的图示：

![项目结构](../images/mpp-structure-default-jvm-js.png)

这里有两个目标，即 `jvm` 与 `js`，每个目标都分别编译生产代码、测试代码，其中一些代码是共享的。 这种布局只是通过创建两个目标来实现的，并没有对编译项与源集进行额外配置：都是为相应目标[默认创建](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#默认项目布局)的。

在上述示例中，JVM 目标的生产源代码由其 `main` 编译项编译，其中包括来自 `jvmMain` 与 `commonMain`（由于*依赖*关系）的源代码与依赖项：

![源集与编译项](../images/mpp-one-compilation.png)

这里 `jvmMain` 源集为共享的 `commonMain` 源集中的预期 API 提供了[平台相关实现](https://www.kotlincn.net/docs/reference/platform-specific-declarations.html)。这就是在平台之间灵活共享代码、 按需使用平台相关实现的方式。

在后续部分，会详细描述这些概念以及将其配置到项目中的 DSL。

## 搭建一个多平台项目

可以在 IDE 的 New Project - Kotlin 对话框下选择一个多平台项目模板来创建一个多平台项目。

例如，如果选择了“Kotlin (Multiplatform Library)”，会创建一个包含三个[目标](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#设置目标)的库项目，其中一个用于 JVM，一个用于 JS，还有一个用于您正在使用的原生平台。 这些是在 `build.gradle` 脚本中以下列方式配置的：

```
Groovy``Kotlin
plugins {
    id 'org.jetbrains.kotlin.multiplatform' version '1.3.72'
}

repositories {
    mavenCentral()
}

kotlin {
    jvm() // 使用默认名称 “jvm” 创建一个 JVM 目标
    js()  // 使用名称 “js” 创建一个 JS 目标
    mingwX64("mingw") // 使用名称 “mingw” 创建一个 Windows (MinGW X64) 目标
    
    sourceSets { /* …… */ }
}
plugins {
    kotlin("multiplatform") version "1.3.72"
}

repositories {
    mavenCentral()
}

kotlin {
    jvm() // 使用默认名称 “jvm” 创建一个 JVM 目标
    js()  // 使用名称 “js” 创建一个 JS 目标
    mingwX64("mingw") // 使用名称 “mingw” 创建一个 Windows (MinGW X64) 目标

    sourceSets { /* …… */ }
}
```

这三个目标是通过预设函数 `jvm()`、`js()` 与 `mingwX64()` 创建的，它们提供了一些[默认项目布局](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#默认项目布局)。每个[已支持平台](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#已支持平台)都有预设的函数。

然后配置[源集](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#配置源集)及其[依赖](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#添加依赖)，如下所示：

```
Groovy``Kotlin
plugins { /* …… */ }

kotlin {
    /* 省略目标声明 */

    sourceSets {
        commonMain {
            dependencies {
                implementation kotlin('stdlib-common')
            }
        }
        commonTest {
            dependencies {
                implementation kotlin('test-common')
                implementation kotlin('test-annotations-common')
            }
        }

        // 仅用于 JVM 的源码及其依赖的默认源集
        // 或者使用 jvmMain { …… }
        jvm().compilations.main.defaultSourceSet {
            dependencies {
                implementation kotlin('stdlib-jdk8')
            }
        }
        // 仅用于 JVM 的测试及其依赖
        jvm().compilations.test.defaultSourceSet {
            dependencies {
                implementation kotlin('test-junit')
            }
        }

        js().compilations.main.defaultSourceSet  { /* …… */ }
        js().compilations.test.defaultSourceSet { /* …… */ }

        mingwX64('mingw').compilations.main.defaultSourceSet { /* …… */ }
        mingwX64('mingw').compilations.test.defaultSourceSet { /* …… */ }
    }
}
plugins { /* …… */ }

kotlin {
    /* 省略目标声明 */

    sourceSets {
        val commonMain by getting {
            dependencies {
                implementation(kotlin("stdlib-common"))
            }
        }
        val commonTest by getting {
            dependencies {
                implementation(kotlin("test-common"))
                implementation(kotlin("test-annotations-common"))
            }
        }

        // 仅用于 JVM 的源码及其依赖的默认源集
        jvm().compilations["main"].defaultSourceSet {
            dependencies {
                implementation(kotlin("stdlib-jdk8"))
            }
        }
        // 仅用于 JVM 的测试及其依赖
        jvm().compilations["test"].defaultSourceSet {
            dependencies {
                implementation(kotlin("test-junit"))
            }
        }

        js().compilations["main"].defaultSourceSet  { /* …… */ }
        js().compilations["test"].defaultSourceSet { /* …… */ }

        mingwX64("mingw").compilations["main"].defaultSourceSet { /* …… */ }
        mingwX64("mingw").compilations["test"].defaultSourceSet { /* …… */ }
    }
}
```

这些在上面配置的目标的生产与测试的源码都有各自的[默认源集名称](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#默认项目布局)。源集 `commonMain` 与 `commonTest` 将被分别包含在所有目标的生产与测试编译项中。 需要注意的是，公共源集 `commonMain` 与 `commonTest` 的依赖使用的都是公共构件，而平台库将转到特定目标的源集。

## Gradle 插件

Kotlin 多平台项目需要 Gradle 4.7 及以上版本，不支持旧版本的 Gradle。

如需在 Gradle 项目中从头开始设置多平台项目，首先要将 `kotlin-multiplatform` 插件应用到项目中，即在 `build.gradle` 文件的开头添加以下内容：

```
Groovy``Kotlin
plugins {
    id 'org.jetbrains.kotlin.multiplatform' version '1.3.72'
}
plugins {
    kotlin("multiplatform") version "1.3.72"
}
```

这会在顶层创建 `kotlin` 扩展。然后可以在构建脚本中访问该扩展，来：

- 为多个平台[设置目标](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#设置目标)（默认不会创建目标）；
- [配置源集](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#配置源集)及其[依赖](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#添加依赖)；

## 设置目标

目标是构建的一部分，负责编译，测试与打包针对一个[已支持平台](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#已支持平台)的软件。

所有的目标可能共享一些源代码，也可能拥有平台专用的源代码。

由于平台的不同，目标也以不同的方式构建，并且拥有各个平台专用的设置。Gradle 插件捆绑了一些已支持平台的预设。

要创建一个目标，请使用其中一个预设函数，这些预置函数根据目标平台命名，并可选择接收一个目标名称与一个配置代码块：

```
kotlin {
    jvm() // 用默认名称 “jvm” 创建一个 JVM 目标
    js("nodeJs") // 用自定义名称 “nodeJs” 创建一个 JS 目标
        
    linuxX64("linux") {
        /* 在此处指定 “linux” 的其他设置 */
    }
}
```

如果存在，这些预置函数将返回一个现有的目标。这可以用于配置一个现有的目标：

```
kotlin {
    /* …… */

    // 配置 “jvm6” 目标的属性
    jvm("jvm6").attributes { /* …… */ }
}
```

注意目标平台与命名都很重要：如果一个目标作为 `jvm('jvm6')` 创建，使用 `jvm()` 将会创建一个单独的目标（使用默认名称 `jvm`）。如果用于创建该名称下的预设函数不同，将会报告一个错误。

从预置函数创建的目标将被添加到域对象集合 `kotlin.targets` 中，这可以用于通过名称访问它们或者配置所有目标：

```
kotlin {
    jvm()
    js("nodeJs")

    println(targets.names) // 打印：[jvm, metadata, nodeJs]

    // 配置所有的目标，包括稍后添加的目标
    targets.all {
        compilations["main"].defaultSourceSet { /* …… */ }
    }
}
```

要从动态创建或访问多个预设中的多个目标，你可以使用 `targetFromPreset` 函数， 它接收一个接收预设（那些被包含在 `kotlin.presets` 域对象集合中的），以及可选的目标名称与配置的代码块。

例如，要为每一个 Kotlin/Native 支持的平台（见下文）创建目标，使用以下代码：

```
Groovy``Kotlin
kotlin {
    presets.withType(org.jetbrains.kotlin.gradle.plugin.mpp.KotlinNativeTargetPreset).each {
        targetFromPreset(it) {
            /* 配置每个已创建的目标 */
        }
    }
}
import org.jetbrains.kotlin.gradle.plugin.mpp.KotlinNativeTargetPreset

/* …… */

kotlin {
    presets.withType<KotlinNativeTargetPreset>().forEach {
        targetFromPreset(it) {
            /* 配置每个已创建的目标 */
        }
    }
}
```

### 已支持平台

如上所示，对于以下目标平台，可以使用预设函数应用目标平台预设：

- `jvm` 用于 Kotlin/JVM；

- `js` 用于 Kotlin/JS；

- `android` 用于 Android 应用程序与库。请注意在创建目标之前， 应该应用其中之一的 Android Gradle 插件；

- Kotlin/Native 目标平台预设（参见下文[备注](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#使用-kotlinnative-目标平台)）：

  - `androidNativeArm32` 与 `androidNativeArm64` 用于 Android NDK；
  - `iosArm32`、 `iosArm64`、 `iosX64` 用于 iOS；
  - `watchosArm32`、 `watchosArm64`、 `watchosX86` 用于 watchOS；
  - `tvosArm64`、 `tvosX64` 用于 tvOS；
  - `linuxArm64`、 `linuxArm32Hfp`、 `linuxMips32`、 `linuxMipsel32`、 `linuxX64` 用于 Linux；
  - `macosX64` 用于 MacOS；
  - `mingwX64` 与 `mingwX86` 用于 Windows；
  - `wasm32` 用于 WebAssembly。

  请注意，某些 Kotlin/Native 目标平台需要[适宜的主机](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#使用-kotlinnative-目标平台)来构建。

某些目标平台可能需要附加配置。Android 与 iOS 示例请参见[多平台项目：iOS 与 Android](https://www.kotlincn.net/docs/tutorials/native/mpp-ios-android.html) 教程。

### 配置编译项

构建目标需要一次或多次编译 Kotlin。目标的每次 Kotlin 编译项都可以用于不同的目的（例如生产代码，测试），并包含不同的[源集](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#配置源集)。 可以在 DSL 中访问目标的编译项，例如，配置[Kotlin 编译器选项](https://www.kotlincn.net/docs/reference/using-gradle.html#编译器选项)或者获取依赖项文件和编译项输出用来获取任务。

```
Groovy``Kotlin
kotlin {
    jvm {
        compilations.main.kotlinOptions {
            // 为“main”编译项设置 Kotlin 编译器选项：
            jvmTarget = "1.8"
        }

        compilations.main.compileKotlinTask // 获取 Kotlin 任务“compileKotlinJvm”
        compilations.main.output // 获取 main 编译项输出
        compilations.test.runtimeDependencyFiles // 获取测试运行时路径
    }

    // 配置所有目标的所有编译项：
    targets.all {
        compilations.all {
            kotlinOptions {
                allWarningsAsErrors = true
            }
        }
    }
}
kotlin {
    jvm {
        val main by compilations.getting {
            kotlinOptions {
                // 为“main”编译项设置 Kotlin 编译器选项：
                jvmTarget = "1.8"
            }

            compileKotlinTask // 获取 Kotlin 任务“compileKotlinJvm”
            output // 获取 main 编译项输出
        }

        compilations["test"].runtimeDependencyFiles // 获取测试运行时路径
    }

    // 配置所有目标的所有编译项：
    targets.all {
        compilations.all {
            kotlinOptions {
                allWarningsAsErrors = true
            }
        }
    }
}
```

每个编译项都附带一个[默认源集](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#配置源集)，该默认源集存储特定于该编译项的源和依赖项。目标 `bar` 的编译项 `foo` 的默认源集的名称为 `barFoo`。也可以使用 `defaultSourceSet` 从编译项中访问它：

```
Groovy``Kotlin
kotlin {
    jvm() // 使用默认名称“jvm”创建一个 JVM 目标

    sourceSets {
        // “jvm”目标的“main”编译项的默认源集：
        jvmMain {
            /* …… */
        }
    }

    // 或者，从目标的编译项中访问它：
    jvm().compilations.main.defaultSourceSet {
        /* …… */
    }
}
kotlin {
    jvm() // 使用默认名称“jvm”创建一个 JVM 目标

    sourceSets {
        // “jvm”目标的“main”编译项的默认源集：
        val jvmMain by getting {
            /* …… */
        }
    }

    // 或者，从目标的编译项中访问它：
    jvm().compilations["main"].defaultSourceSet {
        /* …… */
    }
}
```

为了收集参与编译项的所有源集，包括通过依赖关系添加的源集，可以使用属性 `allKotlinSourceSets`。

对于某些特定用例，可能需要创建自定义编译项。这可以在目标的 `compilations` 领域对象集合中完成。请注意，需要为所有自定义编译项手动设置依赖项，并且自定义编译项输出的使用取决于构建所有者。例如，对目标 `jvm()` 的集成测试的自定义编译项：

```kotlin
Groovy``Kotlin
kotlin {
    jvm() {
        compilations.create('integrationTest') {
            defaultSourceSet {
                dependencies {
                    def main = compilations.main
                    // 根据 main 编译项的编译类路径和输出进行编译：
                    implementation(main.compileDependencyFiles + main.output.classesDirs)
                    implementation kotlin('test-junit')
                    /* …… */
                }
            }

            // 创建一个测试任务来运行此编译项产生的测试：
            tasks.create('jvmIntegrationTest', Test) {
                // 使用包含编译依赖项（包括“main”）的类路径运行测试，
                // 运行时依赖项以及此编译项的输出：
                classpath = compileDependencyFiles + runtimeDependencyFiles + output.allOutputs

                // 仅运行此编译项输出中的测试：        
                testClassesDirs = output.classesDirs
            }
        }
    }
}
kotlin {
    jvm() {
        compilations {
            val main by getting

            val integrationTest by compilations.creating {
                defaultSourceSet {
                    dependencies {
                        // 根据 main 编译项的编译类路径和输出进行编译：
                        implementation(main.compileDependencyFiles + main.output.classesDirs)
                        implementation(kotlin("test-junit"))
                        /* …… */
                    }
                }

                // 创建一个测试任务来运行此编译项产生的测试：
                tasks.create<Test>("integrationTest") {
                    // 使用包含编译依赖项（包括“main”）的类路径运行测试，
                    // 运行时依赖项以及此编译项的输出：
                    classpath = compileDependencyFiles + runtimeDependencyFiles + output.allOutputs

                    // 仅运行此编译项输出中的测试：
                    testClassesDirs = output.classesDirs
                }
            }
        }
    }
}
```

还要注意，默认情况下，自定义编译项的默认源集既不依赖于 `commonMain` 也不依赖于 `commonTest`。

## 配置源集

Kotlin 源集是 Kotlin 源代码及其资源、依赖关系以及语言设置的集合， 一个源集可能会参与一个或多个[目标](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#设置目标)的 Kotlin 编译项。

源集不限于平台特定的或“共享的”；允许包含的内容取决于其用法： 添加到多个编译项中的源集仅限于通用语言特性及依赖项，仅由单个目标使用的源集可以具有平台特定的依赖项，并且其代码可能使用目标平台特定的语言特性。

默认情况下会创建并配置一些源集：`commonMain`、`commonTest` 和编译项的默认源集。 请参见[默认项目布局](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#默认项目布局)。

源集在 `kotlin { ... }` 扩展的 `sourceSets { ... }` 块内配置：

```
Groovy``Kotlin
kotlin {
    sourceSets { 
        foo { /* …… */ } // 创建或配置名称为 “foo” 的源集
        bar { /* …… */ }
    }
}
kotlin {
    sourceSets {
        val foo by creating { /* …… */ } // 创建一个名为 “foo” 的新源集
        val bar by getting { /* …… */ } // 使用名称 “bar” 配置现有的源集
    }
}
```

> 注意：创建源集不会将其链接到任何目标。一些源集是[预定义的](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#默认项目布局) 因此默认情况下进行编译。但是，始终需要将自定义源集明确地定向到编译项。 请参见：[关联源集](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#关联源集)。

源集名称区分大小写。在通过名称引用默认源集时，请确保源集的名称前缀与目标名称匹配，例如，目标 `iosX64` 的源集 `iosX64Main`。

源集本身是平台无关的，但是如果仅针对单个平台进行编译，则可以将其视为特定于平台的。因此，源集可以包含平台之间共享的公共代码或平台特定的代码。

每个源集都有 Kotlin 源代码的默认源目录：`src/<源集名称>/kotlin`。要将 Kotlin 源目录以及资源添加到源集中，请使用其 `kotlin` 与 `resources` `SourceDirectorySet`：

默认情况下，源集的文件存储在以下目录中：

- 源文件：`src/<source set name>/kotlin`
- 资源文件：`src/<source set name>/resources`

应该手动创建这些目录。

要将自定义 Kotlin 源目录和资源添加到源集中，请使用其 `kotlin` 与 `resources` `SourceDirectorySet`：

```
Groovy``Kotlin
kotlin { 
    sourceSets { 
        commonMain {
            kotlin.srcDir('src')
            resources.srcDir('res')
        } 
    }
}
kotlin {
    sourceSets {
        val commonMain by getting {
            kotlin.srcDir("src")
            resources.srcDir("res")
        }
    }
}
```

### 关联源集

Kotlin 源集可能与 *“depends on”* 关系有关，因而如果一个源集 `foo` 依赖于一个源集 `bar`，那么：

- 每当为特定目标编译 `foo` 时，`bar` 也参与到编译中，并且还会编译成相同的目标二进制格式，例如 JVM 类文件或者 JS 代码；
- `foo` 源中的代码能 “看到” `bar` 的定义，包括 `internal` 的以及 `bar` 的[依赖](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#添加依赖)，即使是被指定为 `implementation` 的依赖；
- `foo` 可能包含针对 `bar` 的预期定义的[特定平台的实现](https://www.kotlincn.net/docs/reference/platform-specific-declarations.html)；
- `bar` 的资源总是与 `foo` 的资源一起处理与复制；
- `foo` 与 `bar` 的语言应该是一致的；

不允许源集间循环依赖。

源集 DSL 可以用于定义两个源集之间的联系：

```
Groovy``Kotlin
kotlin {
    sourceSets {
        commonMain { /* …… */ }
        allJvm {
            dependsOn commonMain
            /* …… */
        }
    }
}
kotlin {
    sourceSets {
        val commonMain by getting { /* …… */ }
        val allJvm by creating {
            dependsOn(commonMain)
            /* …… */
        }
    }
}
```

除了[默认源集](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#默认项目布局)外，还应将创建的自定义源集显式地包含在依赖关系层次结构中，以便于能够使用其他源集的定义，并且最重要的是能够参与到编译中。 大多数时候，它们需要 `dependsOn(commonMain)` 或 `dependsOn(commonTest)` 声明，并且一些默认的特定平台的源集应该直接或间接地依赖于自定义的源集

```
Groovy``Kotlin
kotlin { 
    mingwX64()
    linuxX64()

    sourceSets {
        // 带有两个目标测试的自定义源集
        desktopTest {
            dependsOn commonTest
            /* …… */
        }
        // 将 “windows” 的默认测试源集设置为依赖于 “desktopTest”
        mingwX64().compilations.test.defaultSourceSet {
            dependsOn desktopTest
            /* …… */
        }
        // 并且为其他目标做同样的工作：
        linuxX64().compilations.test.defaultSourceSet {
            dependsOn desktopTest
            /* …… */
        }
    }
}
kotlin {
    mingwX64()
    linuxX64()

    sourceSets {
        // 带有两个目标测试的自定义源集
        val desktopTest by creating {
            dependsOn(getByName("commonTest"))
            /* …… */
        }
        // 将 “windows” 的默认测试源集设置为依赖于 “desktopTest”
        mingwX64().compilations["test"].defaultSourceSet {
            dependsOn(desktopTest)
            /* …… */
        }
        // 并且为其他目标做同样的工作：
        linuxX64().compilations["test"].defaultSourceSet {
            dependsOn(desktopTest)
            /* …… */
        }
    }
}
```

### 添加依赖

为了添加依赖到源集中，需要在源集 DSL 中使用 `dependencies { …… }` 块，支持以下四种依赖：

- `api` 依赖在编译项与运行时均会使用，并导出到库使用者。如果当前模块的公共 API 中使用了依赖中的任何类型，那么它应该是一个 `api` 依赖；
- `implementation` 依赖在当前模块的编译项与运行时均会使用，但不暴露给其他具有 `implementation` 依赖的模块的编译项。对于那种内部逻辑实现所需要的依赖，应该使用 `implementation` 依赖类型。如果模块是一个未发布的 endpoint 应用，它或许该使用 `implementation` 依赖而不是 `api` 依赖。
- `compileOnly` 依赖仅用于当前模块的编译项，并且在运行时与<!— ->其他模块的编译项均不可用。这些依赖应该用于运行时具有第三方实现 API 中。
- `runtimeOnly` 依赖在运行时可用，但在任何模块的编译项都是不可见的。

每个源集都可以通过以下方式指定依赖：

```
Groovy``Kotlin
kotlin {
    sourceSets {
        commonMain {
            dependencies {
                api 'com.example:foo-metadata:1.0'
            }
        }
        jvm6Main {
            dependencies {
                api 'com.example:foo-jvm6:1.0'
            }
        }
    }
}
kotlin {
    sourceSets {
        val commonMain by getting {
            dependencies {
                api("com.example:foo-metadata:1.0")
            }
        }
        val jvm6Main by getting {
            dependencies {
                api("com.example:foo-jvm6:1.0")
            }
        }
    }
}
```

请注意，为了 IDE 能够正确地识别公共源的依赖，除了特定平台源集构件的依赖外， 公共源集还需要在 Kotlin 元数据包中具有相应的依赖。通常， 在使用一个已发布的库时（除非它与 Gradle 元数据一起发布，如下所述）， 需要有一个后缀为 `-common` （如 `kotlin-stdlib-common`）或 `-metadata` 的构件。

然而，在另一个多平台项目中的 `project('……')` 依赖会被自动处理成一个合适的目标。在源集的依赖中指定单个 `project('……')` 依赖就足够了， 并且包含在源集中的编译将会接收到其项目的合适的特定平台的构件， 鉴于它具有兼容的目标：

```
Groovy``Kotlin
kotlin {
    sourceSets {
        commonMain {
            dependencies {
                // 包含源集 “commonMain” 的所有编译项
                // 会将依赖项解析为兼容的目标（如果有）：
                api project(':foo-lib')
            }
        }
    }
}
kotlin {
    sourceSets {
        val commonMain by getting {
            dependencies {
                // 包含源集 “commonMain” 的所有编译项
                // 会将依赖项解析为兼容的目标（如果有）：
                api(project(":foo-lib"))
            }
        }
    }
}
```

同样的，如果[发布了带有 Gradle 元数据](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#元数据发布)的一个多平台库，那么只需要为公共源集指定一次依赖。 除此以外，应该为每个特定平台的源集提供库的相应平台模块（除了公共模块），如上所示。

指定依赖的另一种方式是在顶层使用 Gradle 内置 DSL，其配置名称遵循模式 `<源集名称><依赖类型>`：

```
Groovy``Kotlin
dependencies {
    commonMainApi 'com.example:foo-common:1.0'
    jvm6MainApi 'com.example:foo-jvm6:1.0'
}
dependencies {
    "commonMainApi"("com.example:foo-common:1.0")
    "jvm6MainApi"("com.example:foo-jvm6:1.0")
}
```

一些 Gradle 内置依赖（例如 `gradleApi()`、`localGroovy()`、或 `gradleTestKit()`）在源集依赖 DSL 中是不可用的。但是，你可以将它们添加到顶级依赖块中，如上所示。

可以使用 `kotlin("stdlib")` 表示法添加对 Kotlin 模块（例如 `kotlin-stdlib` 或 `kotlin-reflect`）的依赖， 这是 `"org.jetbrains.kotlin:kotlin-stdlib"` 的简写。

### 语言设置

源集的语言设置可以通过以下方式指定：

```
Groovy``Kotlin
kotlin {
    sourceSets {
        commonMain {
            languageSettings {
                languageVersion = '1.3' // 可填：“1.0”、“1.1”、“1.2”、“1.3”
                apiVersion = '1.3' // 可填：“1.0”、“1.1”、“1.2”、“1.3”
                enableLanguageFeature('InlineClasses') // 语言特性名称
                useExperimentalAnnotation('kotlin.ExperimentalUnsignedTypes') // 注解的全限定名
                progressiveMode = true // 默认为 false
            }
        }
    }
}
kotlin {
    sourceSets {
        val commonMain by getting {
            languageSettings.apply {
                languageVersion = "1.3" // 可填：“1.0”、“1.1”、“1.2”、“1.3”
                apiVersion = "1.3" // 可填：“1.0”、“1.1”、“1.2”、“1.3”
                enableLanguageFeature("InlineClasses") // 语言特性名称
                useExperimentalAnnotation("kotlin.ExperimentalUnsignedTypes") // 注解的全限定名
                progressiveMode = true // 默认为 false
            }
        }
    }
}
```

可以一次性为所有源集配置语言设置：

```
kotlin.sourceSets.all {
    languageSettings.progressiveMode = true
}
```

源集的语言设置会影响 IDE 识别源代码的方式。由于当前的限制，在 Gradle 构建中，只有构建的默认源集的语言设置会被使用，并且应用于参与编译的所有源代码。

检查语言设置是否相互依赖，以确保源集之间的一致性。即如果 `foo` 依赖于 `bar`：

- `foo` 需设置高于或等于 `bar` 的 `languageVersion`；
- `foo` 需要启用所有 `bar` 启用的非稳定语言特性（对于错误修复特性则没有这种要求）；
- `foo` 需要使用所有 `bar` 使用的实验性注解；
- `apiVersion`、错误修复的语言特性 和 `progressiveMode` 可以被任意设置；

## 默认项目布局

默认情况下，每个项目都包含了两个源集，`commonMain` 与 `commonTest`，在其中可以放置应在所有目标平台之间共享的所有代码。这些源集会被分别添加到每个生产和测试编译项。

之后，当目标被添加时，将为其创建默认编译项：

- 针对 JVM、JS 和原生目标的 `main` 与 `test` 编译项；
- 针对每个 [Android 构建版本](https://developer.android.com/studio/build/build-variants)的编译项；

对于每个编译项，在由 `<目标名称><编译项名称>` 组成的名称下都有一个默认源集。这个默认源集参与编译，因此它应用于特定平台的代码与依赖，并且以依赖的方式将其他源集添加到编译项中。例如，一个有着 `jvm6` （JVM）与 `nodeJs`（JS）目标的项目将拥有源集：`commonMain`、`commonTest`、`jvm6Main`、`jvm6Test`、`nodeJsMain` 以及 `nodeJsTest`。

仅仅是默认源集就涵盖了很多用例，因此不需要自定义源集。

每个源集都默认拥有在 `src/<源集名称>/kotlin` 目录下的 Kotlin 源代码与在 `src/<源集名称>/resources` 目录下的资源。

在 Android 项目中，将为每个 [Android 源集](https://developer.android.com/studio/build/#sourcesets)创建额外的 Kotlin 源集. 如果其 Android 目标的名称为 `foo`，那么其 Android 源集 `bar` 将获得一个对应的 Kotlin 源集 `fooBar`。 然而，Kotlin 编译项能够使用来自所有 `src/bar/java`、`src/bar/kotlin` 以及 `src/fooBar/kotlin` 目录的 Kotlin 源代码。而 Java 源代码则只能从上述第一个目录读取。

## 运行测试

目前默认支持 JVM、Android、Linux、Windows 以及 macOS 在 Gradle 构建中运行测试； JS 与其他 Kotlin/Native 目标需要手动配置以在适当的环境、模拟器或测试框架下运行测试。

将为每个适合测试的目标创建名为 `<目标名称>Test` 的测试任务。运行 `check` 任务以为所有目标运行测试。

由于 `commonTest` [默认源集](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#默认项目布局)被添加到所有测试编译项中，所以会将所有目标平台上所需的测试和测试工具放在此处。

[`kotlin.test` API](https://kotlinlang.org/api/latest/kotlin.test/index.html)对于多平台测试是可用的。 添加 `kotlin-test-common` 与 `kotlin-test-annotations-common` 依赖到 `commonTest` 以在公共测试中使用断言函数（例如 `kotlin.test.assertTrue(……)` 以及 `@Test`/`@Ignore`/`@BeforeTest`/`@AfterTest` 注解）

对于 JVM 目标，将 `kotlin-test-junit` 或 `kotlin-test-testng` 用于相应的断言器实现和注解映射。

对于 Kotlin/JS 目标，把 `kotlin-test-js` 添加为测试依赖。至此，将创建针对 Kotlin/JS 的测试任务，但默认情况下并不会运行测试； 应该手动配置它们以使用 JavaScript 测试框架运行测试。

Kotlin/Native 目标不需要额外测试依赖，并且内置了 `kotlin.test` API 的实现。

## 发布多平台库

> 目标平台集合由多平台库作者定义，并且他们应该为库提供所有特定平台的实现。 不支持为多平台库添加用户端的新目标。

来自多平台项目的库构建可以通过 [`maven-publish` Gradle 插件](https://docs.gradle.org/current/userguide/publishing_maven.html)发布到 Maven 仓库，这个插件可通过以下方式应用：

```
plugins {
    /* …… */
    id("maven-publish")
}
```

一个库也需要在项目中设置 `group` 与 `version` 字段：

```
plugins { /* …… */ }

group = "com.example.my.library"
version = "0.0.1"
```

与发布一个普通的 Kotlin/JVM 或 Java 项目相比，并没有必要通过 `publishing { …… }` DSL 来手动创建一个发布项。将为可在当前主机构建的每个目标自动创建发布项，但 Android 目标除外，Android 目标需要额外的步骤来配置发布，参见[发布 Android 库](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#发布-android-库)。

通过在 `publishing { …… }` DSL 中的 `repositories` 块添加将被发布的库的仓库。 如 [Maven Publish Plugin. Repositories](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven:repositories) 所述。

默认构件 ID 遵循模式 `<项目名称>-<小写的目标名称>`，例如对于项目 `sample-lib` 中名为 `nodeJs` 的目标，为 `sample-lib-nodejs`。

默认情况下，将为每个发布项中添加源代码 JAR（除了它的主构件）。源代码 JAR 包含了目标主编译项所使用的源代码。如果你还需要发布文档构件（例如 Javadoc JAR），则需要手动配置其构建并且将其作为构件添加到相关发布项中，如下所示。

此外，会默认添加名为 `metadata` 的额外发布项，它包含序列化的 Kotlin 定义并且被 IDE 用于分析多平台库。 这个发布项的默认构件 ID 的形式为 `<项目名称>-metadata`。

可以更改 Maven 坐标，并且可以为在 `targets { …… }` 块或 `publishing { …… }` DSL 中的发布项添加额外的构件文件：

```
Groovy``Kotlin
kotlin {
    jvm('jvm6') {
        mavenPublication { // 为目标 “jvm6” 设置发布项
            // 默认的 artifactId 为 “foo-jvm6”，修改它：
            artifactId = 'foo-jvm'
            // 添加 docs JAR 构件（应是一个自定义任务）：
            artifact(jvmDocsJar)
        }
    }
}

// 使用 `publishing { …… }` DSL 来配置发布项是可选的：
publishing {
    publications {
        jvm6 { /* 为目标 “jvm6” 设置发布项 */ }
        metadata { /* 为 Kotlin 元数据设置发布项 */ }
    }
}
kotlin {
    jvm("jvm6") {
        mavenPublication { // 为目标 “jvm6” 设置发布项
            // 默认的 artifactId 为 “foo-jvm6”，修改它：
            artifactId = "foo-jvm"
            // 添加 docs JAR 构件（应是一个自定义任务）：
            artifact(jvmDocsJar)
        }
    }
}

// 使用 `publishing { …… }` DSL 来配置发布项是可选的：
publishing {
    publications.withType<MavenPublication>().apply {
        val jvm6 by getting { /* 为目标 “jvm6” 设置发布项 */ }
        val metadata by getting { /* 为 Kotlin 元数据设置发布项 */ }
    }
}
```

由于 Kotlin/Native 的汇编构件需要多次构建才能在不同的主机平台运行，所以发布包含 Kotlin/Native 目标的多平台库需要使用同一套主机进行。为了避免重复发布能在多个平台 （例如 JVM、JS、Kotlin 元数据以及 WebAssembly）上构建的模块，可以将这些模块的发布任务配置为有条件地运行。

这个简化的例子确保了 JVM、JS 与 Kotlin 元数据的发布仅在命令行中传递 `-PisLinux=true` 到构建时上传：

```
Groovy``Kotlin
kotlin {
    jvm()
    js()
    mingwX64()
    linuxX64()

    // 注意 Kotlin 元数据也在这里。
    // 由于 mingwx64() 目标在 Linux 构建中不兼容而被自动跳过。
    configure([targets["metadata"], jvm(), js()]) {
        mavenPublication { targetPublication ->
            tasks.withType(AbstractPublishToMaven)
                .matching { it.publication == targetPublication }
                .all { onlyIf { findProperty("isLinux") == "true" } }
        }
    }
}
kotlin {
    jvm()
    js()
    mingwX64()
    linuxX64()

    // 注意 Kotlin 元数据也在这里。
    // 由于 mingwx64() 目标在 Linux 构建中不兼容而被自动跳过。
    configure(listOf(metadata(), jvm(), js())) {
        mavenPublication {
            val targetPublication = this@mavenPublication
            tasks.withType<AbstractPublishToMaven>()
                .matching { it.publication == targetPublication }
                .all { onlyIf { findProperty("isLinux") == "true" } }
        }
    }
}
```



### 元数据发布

Gradle 模块元数据提供了丰富的发布与解析依赖项的特性，这些特性用于 Kotlin 多平台项目来为构建作者简化依赖配置。特别是多平台库的发布项包含一个特殊的 “根” 模块，它基于整个库，并且在添加为依赖项时自动解析到适当的特定平台构件中，如下所述。

In Gradle 6.0 and above, the module metadata is always used during dependency resolution and included in publications.

In earlier Gradle versions starting from 5.3，依赖项解析期间使用模块元数据，但在默认情况下，发布项不会包含任何模块元数据。为了启用发布模块元数据，需要添加 `enableFeaturePreview("GRADLE_METADATA")` 到根项目的 `settings.gradle` 文件。

When publications include module metadata，一个额外的名为 `kotlinMultiplatform` 的 “根” 发布项将添加到项目的发布项中。这个发布项的默认构件 ID 与没有任何额外后缀的项目名称相匹配。 为了配置这个发布项，可以通过 `maven-publish` 插件的 `publishing { …… }` DSL 访问：

```
Groovy``Kotlin
kotlin { /* …… */ }

publishing {
    publications {
        kotlinMultiplatform {
            artifactId = "foo"
        }
    }
}
kotlin { /* …… */ }

publishing {
    publications {
        val kotlinMultiplatform by getting {
            artifactId = "foo"
        }
    }
}
```

这个发布项没有包含任何构件并且仅将其他发布项引用为它的变体。然而， 如果仓库需要，则可能需要提供源代码和文档构件。在这种情况下，在发布项的 scope 中通过使用 [`artifact(...)`](https://docs.gradle.org/current/javadoc/org/gradle/api/publish/maven/MavenPublication.html#artifact-java.lang.Object-) 添加那些构件， 如上所示访问。

如果库拥有一个 “根” 发布项，用户可以在公共源集中指定对整个库的单个依赖， 并且将为每个包含这个依赖项的编译项（如果有）选择一个合适的特定平台版本。 考虑一个为 JVM 与 JS 编译并且与 “根” 发布项一起发布的 `sample-lib` 库：

```
Groovy``Kotlin
kotlin {
    jvm('jvm6')
    js('nodeJs')

    sourceSets {
        commonMain {
            dependencies {
                // 这单个依赖将解析到适当的目标模块，
                // 例如，对于 JVM 解析为 `sample-lib-jvm6`，而对于 JS 解析为 `sample-lib-js`：
                api 'com.example:sample-lib:1.0'
            }
        }
    }
}
kotlin {
    jvm("jvm6")
    js("nodeJs")

    sourceSets {
        val commonMain by getting {
            dependencies {
                // 这单个依赖将解析到适当的目标模块，
                // 例如，对于 JVM 解析为 `sample-lib-jvm6`，而对于 JS 解析为 `sample-lib-js`：
                api("com.example:sample-lib:1.0")
            }
        }
    }
}
```

### 目标消歧义

在一个多平台库中，对于单个平台可能拥有多个目标。例如，这些目标可能提供了相同的 API，并且在运行时调用的实现库中有所不同，例如测试框架或日志解决方案。

然而，对这种多平台库的依赖可能存在歧义，并且可能因为没有充足的信息来决定选择哪个目标，从而导致解析的失败。

解决的方法是用自定义属性标记目标, Gradle 会根据它来解析依赖项。 但是，库的作者与用户必须同时给目标加上自定义属性， 并且库作者有责任将属性与可能的值传达给使用者。

添加属性对库作者和用户来说是对称的。例如，考虑一个在两个目标中分别支持了 JUnit 和 TestNG 的测试库。库作者需要为这两个目标添加属性，如下：

```
Groovy``Kotlin
def testFrameworkAttribute = Attribute.of('com.example.testFramework', String)

kotlin {
    jvm('junit') {
        attributes.attribute(testFrameworkAttribute, 'junit')
    }
    jvm('testng') {
        attributes.attribute(testFrameworkAttribute, 'testng')
    }
}
val testFrameworkAttribute = Attribute.of("com.example.testFramework", String::class.java)

kotlin {
    jvm("junit") {
        attributes.attribute(testFrameworkAttribute, "junit")
    }
    jvm("testng") {
        attributes.attribute(testFrameworkAttribute, "testng")
    }
}
```

用户可能只需要给产生歧义的单个目标添加属性。

如果将依赖项被添加到自定义的配置项中（而不是通过插件创建的配置项之一）时出现了相同的歧义，你可以通过相同的方式将属性添加到配置项中：

```
Groovy``Kotlin
def testFrameworkAttribute = Attribute.of('com.example.testFramework', String)

configurations {
    myConfiguration {
        attributes.attribute(testFrameworkAttribute, 'junit')
    }
}
val testFrameworkAttribute = Attribute.of("com.example.testFramework", String::class.java)

configurations {
    val myConfiguration by creating {
        attributes.attribute(testFrameworkAttribute, "junit")
    }
}
```

## JVM 目标平台中的 Java 支持

这个特性自 Kotlin 1.3.40 可用。

默认情况下，JVM 目标将忽略 Java 源代码，并且只编译 Kotlin 源文件。 为了将 Java 源代码包含入 JVM 目标的编译项中，或是为了应用需要 `java` 插件才能工作的 Gradle 插件，你需要为目标显式地启用 Java 支持：

```
kotlin {
    jvm {
        withJava()
    }
}
```

这将会应用 Gradle `java` 插件，并配置目标以与它协作。 注意，在 JVM 目标中仅应用 Java 插件但没有指定 `withJava()`， 将不会对目标有任何影响。

Java 源代码的文件系统位置与 `java` 插件的默认值不同。 Java 源文件需要被放置在 Kotlin 源代码根目录的同级目录中。例如，如果 JVM 目标有一个默认名称 `jvm`，则路径为：

```
src
├── jvmMain
│   ├── java // production Java sources
│   ├── kotlin
│   └── resources
├── jvmTest
│   ├── java // test Java sources
│   ├── kotlin
…   └── resources
```

公共源集不能包含 Java 源代码。

由于当前的限制，一些由 Java 插件配置的任务将被禁用，并且 Kotlin 插件添加了相应的任务来代替它们：

- `jar` 被禁用，取而代之的是目标的 JAR 任务（例如 `jvmJar`）
- `test` 被禁用，并且使用目标的测试任务（例如 `jvmTest`）
- `*ProcessResources` 任务被禁用，并且资源将由编译项的等价任务处理

这个目标的发布项将由 Kotlin 插件处理，并且不需要特定于 Java 插件的步骤，例如手动创建发布项并配置它为 `from(components.java)`。

## Android 支持

Kotlin 多平台项目通过提供 `android` 内置函数支持 Android 平台。 创建 Android 目标需要 Android Gradle 插件之一，例如手动应用`com.android.application` 或 `com.android.library` 到项目中。每个 Gradle 子项目仅可能创建一个 Android 目标：

```
Groovy``Kotlin
plugins {
    id("com.android.library")
    id("org.jetbrains.kotlin.multiplatform").version("1.3.72")
}

android { /* …… */ }

kotlin {
    android { // 创建 Android 目标
        // 提供必要的附加配置
    }
}
plugins {
    id("com.android.library")
    kotlin("multiplatform").version("1.3.72")
}

android { /* …… */ }

kotlin {
    android { // 创建 Android 目标
        // 提供必要的附加配置
    }
}
```

默认创建的 Android 目标编译项与 [Android 构建变体](https://developer.android.com/studio/build/build-variants)相关联： 对于每个构建变体，将会以相同的名称创建 Kotlin 构建项。

然后，对于每个通过变体编译的 [Android 源集](https://developer.android.com/studio/build/build-variants#sourcesets)， 将在目标名称前面的那个源集名称下创建 Kotlin 源集， 例如 Kotlin 源集 `androidDebug` 用于 Android 源集 `debug` 与名为 `android` 的 Kotlin 目标。 这些 Kotlin 源集将相应地添加到变体编译项中。

默认源集 `commonMain` 将添加到每个生产项（应用或库）变体的编译项中。 类似地，`commonTest` 源集也将添加到单元测试的编译项，以及 instrumented 测试变体中。

使用 [kapt](https://www.kotlincn.net/docs/reference/kapt.html) 进行注解处理也是受支持的，但，由于当前的限制， 它要求 Android 目标需要在配置 `kapt` 依赖之前创建，`kapt` 依赖需要在顶级 `dependencies { …… }` 代码块（而不是 Kotlin 源集依赖）中完成。

```
// ...

kotlin {
    android { /* …… */ }
}

dependencies {
    kapt("com.my.annotation:processor:1.0.0")
}
```

### 发布 Android 库

为了将 Android 库发布为多平台库的一部分，需要[为库设定发布项](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#发布多平台库)，并且为 Android 库目标提供额外的配置项。

默认情况下，不会发布 Android 库的构件。为了发布 [Android 变体](https://developer.android.com/studio/build/build-variants)生成的一系列构件，需要在 Android 目标代码块中指定变体名称，如下所示：

```
kotlin {
    android {
        publishLibraryVariants("release", "debug")
    }
}
```

上面的例子将在没有产品类型的 Android 库上工作。对于有产品类型的库，变体名称也要包含产品类型，例如 `fooBarDebug` 或是 `fooBazRelease`。

注意，如果库用户定义了库中缺失的变体，则他们需要提供[备用的匹配](https://developer.android.com/studio/build/dependencies#resolve_matching_errors)。例如，如果库不具有，或者没有发布 `staging` 构建类型，那么有必要为拥有这种构建类型的使用者提供备用的匹配，至少指定库发布项的一个构建类型：

```
Groovy``Kotlin
android {
    buildTypes {
        staging {
            // ...
            matchingFallbacks = ['release', 'debug']
        }
    }
}
android {
    buildTypes {
        val staging by creating {
            // ...
            matchingFallbacks = listOf("release", "debug")
        }
    }
}
```

类似地，如果库发布项中缺失某些备用的匹配，那么库用户也许需要为自定义产品类型提供它们。

你可以选择发布按产品类型分组的变体，以便将不同构建类型的输出放置在单独的模块中，并使构建类型成为构建的分类器（release 构建类型不通过分类器发布）。这个模式默认是禁用的，不过可以通过以下方式启用：

```
kotlin {
    android {
        publishLibraryVariantsGroupedByFlavor = true
    }
}
```

不推荐发布按产品类型分组的变体，以免它们拥有不同的依赖项，因为这些将被合并到一个依赖项列表中。

## 使用 Kotlin/Native 目标平台

重要的是，注意某些 [Kotlin/Native 目标](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#已支持平台)仅能在适当的主机上被编译：

- Linux MIPS 目标（`linuxMips32` 与 `linuxMipsel32`）需要一台 Linux 主机。其他 Linux 目标则可以在任意受支持的主机上编译。
- Windows 目标需要一台 Windows 主机；
- macOS 与 iOS 目标只能在 macOS 主机上编译；
- 64 位的 Android 原生目标需要一台 Linux 或 macOS 主机。32 位的 Android 原生目标则可以在任意受支持的主机上编译。

当前主机不支持的目标在构建期间会被忽略，因此也不会发布。库作者可能希望在目标库平台所需的不同主机上进行构建和发布。

### 目标快捷方式

一些原生目标经常一同创建，并且使用相同的源代码。例如，iOS 设备与模拟器的构建由不同的目标（分别是 `iosArm64` 与 `iosX64`）表示，但它们的源代码通常是相同的。 多平台项目模型中来表示这种共享代码的一个经典方式是创建一个中间源集（`iosMain`），并且在它和平台源集之间配置链接：

```kotlin
Groovy``Kotlin
sourceSets{
    iosMain {
        dependsOn(commonMain)
        iosDeviceMain.dependsOn(it)
        iosSimulatorMain.dependsOn(it)
    }
}
val commonMain by sourceSets.getting
val iosDeviceMain by sourceSets.getting
val iosSimulatorMain by sourceSets.getting

val iosMain by sourceSets.creating {
    dependsOn(commonMain)
    iosDeviceMain.dependsOn(this)
    iosSimulatorMain.dependsOn(this)
}
```

自 1.3.60 起，`kotlin-multiplaform` 插件提供了自动化这些配置的快捷方式：它们使用户可以通过单个 DSL 方法来创建一组目标以及公共源集。

可用快捷方式有这些：

- `ios` 为 `iosArm64` 与 `iosX64` 创建目标。
- `watchos` 为 `watchosArm32`、`watchosArm64` 以及 `watchosX86` 创建目标。
- `tvos` 为 `tvosArm64` 与 `tvosX64` 创建目标。

```
// 为 iOS 创建两个目标。
// 创建公共源集：iosMain 与 iosTest。
ios {
    // 配置目标。
    // 注意：将会为每个目标调用这个 lambda。
}

// 你也可以指定一个名称前缀来创建目标。
// 公共源集也将会有一个前缀：
// anotherIosMain 与 anotherIosTest。
ios("anotherIos")
```

### 构建最终原生二进制文件

默认情况下，Kotlin/Native 目标将被编译为 `*.klib` 库构件，它可以被 Kotlin/Native 自身作为依赖项使用，但并不能被执行，或是用作原生库。为了声明像可执行文件或是链接库的最终原生二进制文件， 需要使用原生目标的 `binaries` 属性。除默认 `*.klib` 构建外， 这个属性还代表一个为这个目标构建的原生二进制文件集合，并且提供了一系列声明和配置它们的方法。

注意，`kotlin-multiplaform` 插件默认不会创建任何生产二进制文件。默认情况下， 唯一可用的二进制文件是调试可执行文件，它允许运行来自 `test` 编译项的测试。

#### 声明二进制文件

`binaries` 集合的元素通过一套工厂方法声明。这些方法允许指定要创建的二进制类型并对其进行配置。以下是受支持的二进制类型（注意， 并不是所有类型都可用于所有原生平台）：

| **工厂方法** | **二进制类型**        | **可用于**                          |
| :----------- | :-------------------- | :---------------------------------- |
| `executable` | 产品可执行文件        | 所有原生目标                        |
| `test`       | 测试可执行文件        | 所有原生目标                        |
| `sharedLib`  | 链接原生库            | 除了 `wasm32` 以外的所有原生目标    |
| `staticLib`  | 静态原生库            | 除了 `wasm32` 以外的所有原生目标    |
| `framework`  | Objective-C framework | 仅 macOS、iOS、watchOS 与 tvOS 目标 |

每个工厂方法都有多个版本。通过 `executable` 方法的示例考虑他们。所有相同的版本对所有其他的工厂方法都是可用的。

最简单的版本不需要任何额外的参数，并且会为每个构建类型都创建二进制文件。 目前有两个可用的构建类型：`DEBUG` （生成带有调试信息的、未优化的二进制文件） 与 `RELEASE` （生成不带有调试信息的、经过优化的二进制文件）。

```
kotlin {
    linuxX64 { // 更改为你所使用的目标。
        binaries {
            executable {
                // 二进制配置。
            }
        }
    }
}
```

在上面例子中的 `executable` 方法接受的 lambda 表达式将应用于创建的每个二进制文件，并且允许配置二进制文件。 （参见[相应部分](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#配置二进制文件)）。注意，如果不需要额外的配置，则可以删除这个 lambda：

```
binaries {
    executable()
}
```

可以指定哪些构建类型将用于创建二进制文件，哪些将不创建。以下的示例仅创建了调试可执行文件。

```
Groovy``Kotlin
binaries {
    executable([DEBUG]) {
        // 二进制配置。
    }
}
binaries {
    executable(listOf(DEBUG)) {
        // 二进制配置。
    }
}
```

最终，最后一个工厂方法版本允许自定义二进制文件名称。

```
Groovy``Kotlin
binaries {
    executable('foo', [DEBUG]) {
        // 二进制配置。
    }

    // 可以删除构建类型的列表（这种情况下，将使用所有可用的构建类型）。
    executable('bar') {
        // 二进制配置。
    }
}
binaries {
    executable("foo", listOf(DEBUG)) {
        // 二进制配置。
    }

    // 可以删除构建类型的列表（这种情况下，将使用所有可用的构建类型）。
    executable("bar") {
        // 二进制配置。
    }
}
```

在这个示例中的第一个参数允许为创建的二进制文件设置名称前缀，该前缀用于在构建脚本中访问它们（参见 [“访问二进制文件”](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#访问二进制文件) 部分）。 这个前缀也用作二进制文件的默认名称。例如在 Windows 平台上，上面的示例将生产出 `foo.exe` 与 `bar.exe` 文件。

#### 访问二进制文件

binaries DSL 不仅允许创建二进制文件，还可以访问已经创建的二进制文件以配置它们或获取它们的属性 （例如输出文件的路径）。`binaries` 集合实现了 [`DomainObjectSet`](https://docs.gradle.org/current/javadoc/org/gradle/api/DomainObjectSet.html) 接口，并提供了类似 `all` 或 `matching` 这些允许配置元素组的方法。

也可以获取集合中的某些元素。有两种方式可以做到。第一种方式，每个库拥有独有的名字。这个名称基于名称的前缀（如果已指定），构建类型和二进制种类根据以下模式： `<可选名称前缀><构建类型><二进制种类>`， 例如 `releaseFramework` 或 `testDebugExecutable`。

> 注意：静态库和共享库分别有 `static` 与 `shared` 后缀，例如 `fooDebugStatic` 或 `barReleaseShared`

这个名称可以用于访问库：

```kotlin
Groovy``Kotlin
// 如果没有这样的库将会导致错误。
binaries['fooDebugExecutable']
binaries.fooDebugExecutable
binaries.getByName('fooDebugExecutable')

 // 如果没有这样的库将返回 null。
binaries.findByName('fooDebugExecutable')
// 如果没有这样的库将会导致错误。
binaries["fooDebugExecutable"]
binaries.getByName("fooDebugExecutable")

 // 如果没有这样的库将返回 null。
binaries.findByName("fooDebugExecutable")
```

第二种方式是使用标记过类型的 getter。这些 getter 允许通过它的名称前缀与构建类型访问某种类型的二进制文件。

```kotlin
Groovy``Kotlin
// 如果没有这样的库将会导致错误。
binaries.getExecutable('foo', DEBUG)
binaries.getExecutable(DEBUG)          // 如果没有设置名称前缀则会跳过第一个参数。
binaries.getExecutable('bar', 'DEBUG') // 你也可以使用字符串作为构建类型。

// 类似的 getter 对其他二进制种类也是可以用的：
// getFramework、getStaticLib 与 getSharedLib。

// 如果没有这样的库将返回 null。
binaries.findExecutable('foo', DEBUG)

// 类似的 getter 对其他二进制种类也是可以用的：
// findFramework、findStaticLib 与 findSharedLib。
// 如果没有这样的库将会导致错误。
binaries.getExecutable("foo", DEBUG)
binaries.getExecutable(DEBUG)          // 如果没有设置名称前缀则会跳过第一个参数。
binaries.getExecutable("bar", "DEBUG") // 你也可以使用字符串作为构建类型。

// 类似的 getter 对其他二进制种类也是可以用的：
// getFramework、getStaticLib 与 getSharedLib。

// 如果没有这样的库将返回 null。
binaries.findExecutable("foo", DEBUG)

// 类似的 getter 对其他二进制种类也是可以用的：
// findFramework、findStaticLib 与 findSharedLib。
```

> 1.3.40 之前，测试和产品可执行文件均由相同的二进制类型表示。因此，要访问通过插件创建的默认测试二进制文件，请使用下行：
>
> ```kotlin
> binaries.getExecutable("test", "DEBUG")
> ```
>
> 自 1.3.40 起，测试可执行文件由单独的二进制类型表示，并且拥有自己的 getter。要访问默认的测试库，请使用：
>
> ```kotlin
> binaries.getTest("DEBUG")
> ```

#### 配置二进制文件

二进制文件具有一套属性，允许配置它们。可用的选项有这些：

- **编译项。** 每个二进制都是基于相同目标中一些可用的编译项构建的。这个参数的默认值依赖于二进制类型：`Test` 二进制文件基于 `test` 编译项，而其他二进制文件基于 `main` 编译项。
- **链接器选项。** 选项将在二进制文件的构建期间被传递到系统链接器中。可以使用这个设置链接到某些原生库。
- **输出文件名称。** 默认情况下，输出文件名称基于二进制文件名称前缀，如果没有指定前缀，则基于项目名称。 但可以使用 `baseName` 属性来单独配置输出文件名称。注意，最终文件名称将通过添加系统相关的前缀与后缀到这个基础名称形成。 例如 Linux 共享库与基础名称 `foo` 将产出 `libfoo.so`。
- **入口点**（仅用于可执行的二进制文件）。默认情况下，Kotlin/Native 程序的入口点是位于根包的 `main` 函数。这个设置允许改变这个默认值，并使用自定义的函数作为入口点。例如它可以用于将 `main` 函数从根包中移出。
- **访问输出文件。**
- **访问链接任务。**
- **访问运行任务**（仅用于可执行的二进制文件）。`kotlin-multiplatform` 插件为主机平台（Windows、Linux 与 macOS）的所有可执行二进制文件创建运行任务。 这些任务的名称基于二进制文件名称，例如 `runReleaseExecutable<目标名称>` 或 `runFooDebugExecutable<目标名称>`。可以使用可执行二进制文件的 `runTask` 属性来访问运行任务。
- **Framework 类型**（仅用于 Objective-C frameworks）。默认情况下，通过 Kotlin/Native 构建的 framework 包含动态库。但可以把它替换为静态库。

下面的例子演示了如何使用这些设置。

```
Groovy``Kotlin
binaries {
    executable('my_executable', [RELEASE]) {
        // 在测试编译项的基础上构建二进制文件。
        compilation = compilations.test

        // 为链接器自定义命令行选项。
        linkerOpts = ['-L/lib/search/path', '-L/another/search/path', '-lmylib']

        // 用于输出文件的基础名称。
        baseName = 'foo'

        // 自定义入口函数。
        entryPoint = 'org.example.main'

        // 访问输出文件。
        println("Executable path: ${outputFile.absolutePath}")

        // 访问链接任务。
        linkTask.dependsOn(additionalPreprocessingTask)

        // 访问运行任务。
        // 注意，对于非本机的平台，runTask 为 null。
        runTask?.dependsOn(prepareForRun)
    }

    framework('my_framework' [RELEASE]) {
        // 在框架中包含静态库，而不是动态库。
        isStatic = true
    }
}
binaries {
    executable("my_executable", listOf(RELEASE)) {
        // 在测试编译项的基础上构建二进制文件。
        compilation = compilations["test"]

        // 为链接器自定义命令行选项。
        linkerOpts = mutableListOf("-L/lib/search/path", "-L/another/search/path", "-lmylib")

        // 用于输出文件的基础名称。
        baseName = "foo"

        // 自定义入口函数。
        entryPoint = "org.example.main"

        // 访问输出文件。
        println("Executable path: ${outputFile.absolutePath}")

        // 访问链接任务。
        linkTask.dependsOn(additionalPreprocessingTask)

        // 访问运行任务。
        // 注意，对于非本机的平台，runTask 为 null。
        runTask?.dependsOn(prepareForRun)
    }

    framework("my_framework" listOf(RELEASE)) {
        // 在框架中包含静态库，而不是动态库。
        isStatic = true
    }
}
```

#### 导出依赖项到二进制文件

当构建 Objective-C framework 或原生库（共享或静态）时，经常不仅要打包当前项目的 class，还需要打包其某些依赖项的 class。binaries DSL 允许使用 `export` 方法指定将哪些依赖项将导出到二进制文件。注意，仅有相应源集的 API 依赖项可以被导出。

```
Groovy``Kotlin
kotlin {
    sourceSets {
        macosMain.dependencies {
            // 将被导出。
            api project(':dependency')
            api 'org.example:exported-library:1.0'

            // 将不被导出。
            api 'org.example:not-exported-library:1.0'
        }
    }

    macosX64("macos").binaries {
        framework {
            export project(':dependency')
            export 'org.example:exported-library:1.0'
        }

        sharedLib {
            // 可以将不同的依赖项集合导出到不同的二进制文件。
            export project(':dependency')
        }
    }
}
kotlin {
    sourceSets {
        macosMain.dependencies {
            // 将被导出。
            api(project(":dependency"))
            api("org.example:exported-library:1.0")

            // 将不被导出。
            api("org.example:not-exported-library:1.0")
        }
    }

    macosX64("macos").binaries {
        framework {
            export(project(":dependency"))
            export("org.example:exported-library:1.0")
        }

        sharedLib {
            // 可以将不同的依赖项集合导出到不同的二进制文件。
            export(project(':dependency'))
        }
    }
}
```

> 如这个示例所展示的，maven 依赖项也可以被导出。但由于 Gradle 元数据的当前限制，这种依赖项应该是平台依赖（例如 `kotlinx-coroutines-core-native_debug_macos_x64` 而不是 `kotlinx-coroutines-core-native`） 或被传递地导出（参见下文）。

默认情况下，导出工作是非传递性的。如果导出了依赖于库 `bar` 的库 `foo`，那么仅有 `foo` 的方法将被添加到输出 framework。这个行为可以通过 `transitiveExport` 标志来改变。

```
Groovy``Kotlin
binaries {
    framework {
        export project(':dependency')
        // 过渡地导出。
        transitiveExport = true
    }
}
binaries {
    framework {
        export(project(":dependency"))
        // 过渡地导出。
        transitiveExport = true
    }
}
```

#### 构建通用 framework

默认情况下，仅支持一个平台通过 Kotlin/Native 产出 Objective-C framework。然而，这种 framework 可以使用 `lipo` 工具将其合并到一个单独的、通用的（fat）二进制文件中。特别的，这种操作对于 32 位与 64 位的 iOS framework 是有意义的。在这种情况下，最终通用 framework 可以在 32 位与 64 位的设备上使用。

Gradle 插件提供了一个单独的任务，该任务从多个常规目标为 iOS 目标创建通用 framework。 下面的示例展示了如何使用这个任务。注意，fat framework 必须具有与初始 framework 相同的基础名称。

```kotlin
Groovy``Kotlin
import org.jetbrains.kotlin.gradle.tasks.FatFrameworkTask

kotlin {
    // 创建并配置目标。 
    targets {
        iosArm32("ios32")
        iosArm64("ios64")

        configure([ios32, ios64]) {
            binaries.framework {
                baseName = "my_framework"
            }
        }
    }

    // 创建一个任务，用于构建 fat framework。
    task debugFatFramework(type: FatFrameworkTask) {
        // fat framework 必须具有与初始 framework 相同的基础名称。
        baseName = "my_framework"

        // 默认目标目录是 “<build 目录>/fat-framework”。
        destinationDir = file("$buildDir/fat-framework/debug")

        // 指定要合并的 framework。
        from(
            targets.ios32.binaries.getFramework("DEBUG"),
            targets.ios64.binaries.getFramework("DEBUG")
        )
    }
}
import org.jetbrains.kotlin.gradle.tasks.FatFrameworkTask

kotlin {
    // 创建并配置目标。 
    val ios32 = iosArm32("ios32")
    val ios64 = iosArm64("ios64")

    configure(listOf(ios32, ios64)) {
        binaries.framework {
            baseName = "my_framework"
        }
    }

    // 创建一个任务，用于构建 fat framework。
    tasks.create("debugFatFramework", FatFrameworkTask::class) {
        // fat framework 必须具有与初始 framework 相同的基础名称。
        baseName = "my_framework"

        // 默认目标目录是 “<build 目录>/fat-framework”。
        destinationDir = buildDir.resolve("fat-framework/debug")

        // 指定要合并的 framework。
        from(
            ios32.binaries.getFramework("DEBUG"),
            ios64.binaries.getFramework("DEBUG")
        )
    }
}
```

### C 互操作支持

自 Kotlin/Native 提供了[与原生语言互操作](https://www.kotlincn.net/docs/reference/native/c_interop.html)， 就有 DSL 允许为特定编译项配置这个特性。

编译项可以与多个原生库交互。它们的互操作性可以在 compilation 的 `cinterops` 块中配置：

```kotlin
Groovy``Kotlin
kotlin {
    linuxX64 { // 替换为你所需要的目标
        compilations.main {
            cinterops {
                myInterop {
                    // Def-file 描述原生 API。
                    // 默认路径是 src/nativeInterop/cinterop/<互操作名称>.def
                    defFile project.file("def-file.def")

                    // 用于放置生成的 Kotlin API 的包。
                    packageName 'org.sample'

                    // 通过 cinterop 工具传递给编译器的选项
                    compilerOpts '-Ipath/to/headers'

                    // 用于头文件搜索的目录（类似于编译器选项 -I<路径>）。
                    includeDirs.allHeaders("path1", "path2")

                    // 搜索在 “headerFilter” def-file 选项中列出的头文件的额外目录。
                    // 类似于命令行参数 -headerFilterAdditionalSearchPrefix。
                    includeDirs.headerFilterOnly("path1", "path2")

                    // includeDirs.allHeaders 的快捷方式。
                    includeDirs("include/directory", "another/directory")
                }

                anotherInterop { /* …… */ }
            }
        }
    }
}
kotlin {
    linuxX64 {  // 替换为你所需要的目标
        compilations.getByName("main") {
            val myInterop by cinterops.creating {
                // Def-file 描述原生 API。
                // 默认路径是 src/nativeInterop/cinterop/<互操作名称>.def
                defFile(project.file("def-file.def"))

                // 用于放置生成的 Kotlin API 的包。
                packageName("org.sample")

                // 通过 cinterop 工具传递给编译器的选项
                compilerOpts("-Ipath/to/headers")

                // 用于寻找头文件的目录。
                includeDirs.apply {
                    // 用于头文件搜索的目录（类似于编译器选项 -I<路径>）。
                    allHeaders("path1", "path2")

                    // 搜索在 “headerFilter” def-file 选项中列出的头文件的额外目录。
                    // 类似于命令行参数 -headerFilterAdditionalSearchPrefix。
                    headerFilterOnly("path1", "path2")
                }
                // includeDirs.allHeaders 的快捷方式。
                includeDirs("include/directory", "another/directory")
            }

            val anotherInterop by cinterops.creating { /* …… */ }
        }
    }
}
```

经常需要为使用了原生库的二进制文件指定特定于目标的链接器选项。可以通过使用二进制文件的 `linkerOpts` 属性来完成。参见[配置二进制文件](https://www.kotlincn.net/docs/reference/building-mpp-with-gradle.html#配置二进制文件)部分获取更多详细内容。