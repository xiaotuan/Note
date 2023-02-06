[toc]

# ViewModel 概览  **[Android Jetpack](https://developer.android.google.cn/jetpack?hl=zh-cn) 的一部分。**



[`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel?hl=zh-cn) 类是一种[业务逻辑或屏幕级状态容器](https://developer.android.google.cn/topic/architecture/ui-layer/stateholders?hl=zh-cn)。它用于将状态公开给界面，以及封装相关的业务逻辑。 它的主要优点是，它可以缓存状态，并可在配置更改后持久保留相应状态。这意味着在 activity 之间导航时或进行配置更改后（例如旋转屏幕时），界面将无需重新提取数据。

**目标**：本指南介绍了 ViewModel 的基础知识、如何将其融入 [Modern Android Development](https://developer.android.google.cn/modern-android-development?hl=zh-cn) 以及如何在应用中实现 ViewModel。

如需详细了解状态容器，请参阅[状态容器](https://developer.android.google.cn/topic/architecture/ui-layer/stateholders?hl=zh-cn)指南。 同样，如需详细了解有关界面层的一般信息，请参阅[界面层](https://developer.android.google.cn/topic/architecture/ui-layer?hl=zh-cn)指南。

## ViewModel 的优势

ViewModel 的替代方案是保存要在界面中显示的数据的普通类。在 activity 或 Navigation 目的地之间导航时，这可能会造成问题。此时，如果您不利用[保存实例状态机制](https://developer.android.google.cn/topic/libraries/architecture/saving-states?hl=zh-cn#onsaveinstancestate)存储相应数据，系统便会销毁相应数据。ViewModel 提供了一个便捷的数据持久性 API，可以解决此问题。

ViewModel 类的主要优势实际上有两个方面：

- 它允许您持久保留界面状态。
- 它可以提供对业务逻辑的访问权限。

**注意**：ViewModel 完全支持与主要的 Jetpack 库集成，例如 [Hilt](https://developer.android.google.cn/training/dependency-injection/hilt-android?hl=zh-cn)、[Navigation](https://developer.android.google.cn/guide/navigation?hl=zh-cn) 和 [Compose](https://developer.android.google.cn/jetpack/compose?hl=zh-cn)。

### 持久性

ViewModel 允许数据在 ViewModel 持有的状态和 ViewModel 触发的操作结束后继续存在。这种缓存意味着在常见的配置更改（例如屏幕旋转）完成后，您无需重新提取数据。

#### 作用域

实例化 ViewModel 时，您会向其传递实现 [`ViewModelStoreOwner`](https://developer.android.google.cn/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner?hl=zh-cn) 接口的对象。它可能是 Navigation 目的地、Navigation 图表、activity、fragment 或实现接口的任何其他类型。然后，ViewModel 的作用域将限定为 `ViewModelStoreOwner` 的 [Lifecycle](https://developer.android.google.cn/reference/androidx/lifecycle/Lifecycle?hl=zh-cn)。它会一直保留在内存中，直到其 `ViewModelStoreOwner` 永久消失。

有一系列类是 `ViewModelStoreOwner` 接口的直接或间接子类。直接子类为 [`ComponentActivity`](https://developer.android.google.cn/reference/androidx/activity/ComponentActivity?hl=zh-cn)、[`Fragment`](https://developer.android.google.cn/reference/androidx/fragment/app/Fragment?hl=zh-cn) 和 [`NavBackStackEntry`](https://developer.android.google.cn/reference/androidx/navigation/NavBackStackEntry?hl=zh-cn)。如需查看间接子类的完整列表，请参阅 [`ViewModelStoreOwner` 参考文档](https://developer.android.google.cn/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner?hl=zh-cn)。

当 ViewModel 的作用域 fragment 或 activity 被销毁时，异步工作会在作用域限定到该 fragment 或 activity 的 ViewModel 中继续进行。这是持久性的关键。

如需了解详情，请参阅下文有关 [ViewModel 生命周期](https://developer.android.google.cn/topic/libraries/architecture/viewmodel?hl=zh_cn#lifecycle)的部分。

#### SavedStateHandle

借助 [SaveStateHandle](https://developer.android.google.cn/topic/libraries/architecture/viewmodel/viewmodel-savedstate?hl=zh-cn)，您不仅可以在更改配置后持久保留数据，还可以在进程重新创建过程中持久保留数据。也就是说，即使用户关闭应用，稍后又将其打开，您的界面状态也可以保持不变。

### 对业务逻辑的访问权限

尽管绝大多数[业务逻辑](https://developer.android.google.cn/topic/architecture/ui-layer/stateholders?hl=zh-cn#business-logic)都存在于数据层中，但界面层也可以包含业务逻辑。当您合并多个代码库中的数据以创建屏幕界面状态时，或特定类型的数据不需要数据层时，情况就是如此。

ViewModel 是在界面层处理业务逻辑的正确位置。当需要应用业务逻辑来修改应用数据时，ViewModel 还负责处理事件并将其委托给层次结构中的其他层。

## Jetpack Compose

使用 Jetpack Compose 时，ViewModel 是向可组合项公开屏幕界面状态的主要方式。在混合应用中，activity 和 fragment 仅用于托管可组合函数。这与以往的方法不同；过去，创建包含 activity 和 fragment 且可重复使用的界面部分没有这么简单和直观，因此这类部分在作为界面控制器时会更加活跃。

将 ViewModel 与 Compose 一起使用时，最重要的注意事项是，您无法将 ViewModel 的作用域限定为可组合项。这是因为可组合项不属于 `ViewModelStoreOwner`。组合中同一可组合项的两个实例，或者在同一 `ViewModelStoreOwner` 下访问同一 ViewModel 类型的两个不同的可组合项，将会收到相同的 ViewModel 实例，而这通常并不是预期的行为。

如需在 Compose 中利用 ViewModel 的[优势](https://developer.android.google.cn/topic/libraries/architecture/viewmodel?hl=zh_cn#viewmodel-benefits)，请在 fragment 或 activity 中托管每个屏幕，或者使用 Compose Navigation，并在尽可能靠近 Navigation 目的地的可组合函数中使用 ViewModel。这是因为，您可以将 ViewModel 的作用域限定为 Navigation 目的地、Navigation 图表、activity 和 fragment。

如需了解详情，请参阅有关[状态和 Jetpack Compose](https://developer.android.google.cn/jetpack/compose/state?hl=zh-cn#viewmodels-source-of-truth) 的指南。

## 实现 ViewModel

以下是 ViewModel 的一个实现示例：该用例是显示用户列表。

**重要提示**：在此示例中，获取和保存用户列表的责任在于 ViewModel，而不直接在于 activity 或 fragment。

[Kotlin](https://developer.android.google.cn/topic/libraries/architecture/viewmodel?hl=zh_cn#kotlin)[Java](https://developer.android.google.cn/topic/libraries/architecture/viewmodel?hl=zh_cn#java)

```kotlin
data class DiceUiState(
    val firstDieValue: Int? = null,
    val secondDieValue: Int? = null,
    val numberOfRolls: Int = 0,
)

class DiceRollViewModel : ViewModel() {

    // Expose screen UI state
    private val _uiState = MutableStateFlow(DiceUiState())
    val uiState: StateFlow<DiceUiState> = _uiState.asStateFlow()

    // Handle business logic
    fun rollDice() {
        _uiState.update { currentState ->
            currentState.copy(
                firstDieValue = Random.nextInt(from = 1, until = 7),
                secondDieValue = Random.nextInt(from = 1, until = 7),
                numberOfRolls = currentState.numberOfRolls + 1,
            )
        }
    }
}
```

然后，您可以从 Activity 访问该列表，如下所示：

[Kotlin](https://developer.android.google.cn/topic/libraries/architecture/viewmodel?hl=zh_cn#kotlin)[Java](https://developer.android.google.cn/topic/libraries/architecture/viewmodel?hl=zh_cn#java)[Jetpack Compose](https://developer.android.google.cn/topic/libraries/architecture/viewmodel?hl=zh_cn#jetpack-compose)

```kotlin
import androidx.activity.viewModels

class DiceRollActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        // Create a ViewModel the first time the system calls an activity's onCreate() method.
        // Re-created activities receive the same DiceRollViewModel instance created by the first activity.

        // Use the 'by viewModels()' Kotlin property delegate
        // from the activity-ktx artifact
        val viewModel: DiceRollViewModel by viewModels()
        lifecycleScope.launch {
            repeatOnLifecycle(Lifecycle.State.STARTED) {
                viewModel.uiState.collect {
                    // Update UI elements
                }
            }
        }
    }
}
```

**注意**：[`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel?hl=zh-cn) 通常不应引用视图、[`Lifecycle`](https://developer.android.google.cn/reference/androidx/lifecycle/Lifecycle?hl=zh-cn) 或可能存储对 activity 上下文的引用的任何类。由于 ViewModel 的生命周期大于界面的生命周期，因此在 ViewModel 中保留与生命周期相关的 API 可能会导致内存泄漏。

**注意**：如需将 [`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel?hl=zh-cn) 导入 Android 项目，请参阅 [Lifecycle 版本说明](https://developer.android.google.cn/jetpack/androidx/releases/lifecycle?hl=zh-cn#declaring_dependencies)中关于声明依赖项的说明。

### 将协程与 ViewModel 一起使用

`ViewModel` 支持 Kotlin 协程。它能够像持久保留界面状态一样持久保留异步工作。

如需了解详情，请参阅[将 Kotlin 协程与 Android 架构组件一起使用](https://developer.android.google.cn/topic/libraries/architecture/coroutines?hl=zh-cn)。

## ViewModel 的生命周期

[`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel?hl=zh-cn) 的生命周期与其作用域直接关联。`ViewModel` 会一直保留在内存中，直到其作用域 [`ViewModelStoreOwner`](https://developer.android.google.cn/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner?hl=zh-cn) 消失。以下上下文中可能会发生这种情况：

- 对于 activity，是在 activity 完成时。
- 对于 fragment，是在 fragment 分离时。
- 对于 Navigation 条目，是在 Navigation 条目从返回堆栈中移除时。

这使得 ViewModels 成为了存储在配置更改后仍然存在的数据的绝佳解决方案。

图 1 说明了 activity 经历屏幕旋转而后结束时所处的各种生命周期状态。该图还在关联的 activity 生命周期的旁边显示了 [`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel?hl=zh-cn) 的生命周期。此图表说明了 activity 的各种状态。这些基本状态同样适用于 fragment 的生命周期。

![说明 ViewModel 随着 activity 状态的改变而经历的生命周期。](https://developer.android.google.cn/static/images/topic/libraries/architecture/viewmodel-lifecycle.png?hl=zh-cn)

您通常在系统首次调用 activity 对象的 [`onCreate()`](https://developer.android.google.cn/reference/android/app/Activity?hl=zh-cn#onCreate(android.os.Bundle)) 方法时请求 [`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel?hl=zh-cn)。系统可能会在 activity 的整个生命周期内多次调用 [`onCreate()`](https://developer.android.google.cn/reference/android/app/Activity?hl=zh-cn#onCreate(android.os.Bundle))，如在旋转设备屏幕时。[`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel?hl=zh-cn) 存在的时间范围是从您首次请求 [`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel?hl=zh-cn) 直到 activity 完成并销毁。

### 清除 ViewModel 依赖项

当 `ViewModelStoreOwner` 在 ViewModel 的生命周期内销毁 ViewModel 时，ViewModel 会调用 [`onCleared`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel?hl=zh-cn#onCleared()) 方法。这样，您就可以清理遵循 ViewModel 生命周期的任何工作或依赖项。

以下示例展示了 [`viewModelScope`](https://developer.android.google.cn/topic/libraries/architecture/coroutines?hl=zh-cn#viewmodelscope) 的替代方法。 `viewModelScope` 是一个内置 [`CoroutineScope`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/)，会自动遵循 ViewModel 的生命周期。ViewModel 使用 viewModelScope 触发与业务相关的操作。如果您想使用自定义作用域（而不是 `viewModelScope`）使[测试更简单](https://developer.android.google.cn/kotlin/coroutines/test?hl=zh-cn)，ViewModel 可以在其构造函数中接收 `CoroutineScope` 作为依赖项。如果 `ViewModelStoreOwner` 在 ViewModel 的生命周期结束时清除 ViewModel，ViewModel 也会取消 `CoroutineScope`。

```kotlin
class MyViewModel(
    private val coroutineScope: CoroutineScope =
        CoroutineScope(SupervisorJob() + Dispatchers.Main.immediate)
) : ViewModel() {

    // Other ViewModel logic ...

    override fun onCleared() {
        coroutineScope.cancel()
    }
}
```

从 Lifecycle [版本 2.5](https://developer.android.google.cn/jetpack/androidx/releases/lifecycle?hl=zh-cn#version_25_2) 及更高版本开始，您可以将一个或多个 `Closeable` 对象传递给在清除 ViewModel 实例时自动关闭的 ViewModel 构造函数。

```kotlin
class CloseableCoroutineScope(
    context: CoroutineContext = SupervisorJob() + Dispatchers.Main.immediate
) : Closeable, CoroutineScope {
    override val coroutineContext: CoroutineContext = context
    override fun close() {
        coroutineContext.cancel()
   }
}

class MyViewModel(
    private val coroutineScope: CoroutineScope = CloseableCoroutineScope()
) : ViewModel(coroutineScope) {
    // Other ViewModel logic ...
}
```

## 最佳实践

以下是实现 ViewModel 时应遵循的一些重要的最佳实践：

- 由于 [ViewModel 的作用域](https://developer.android.google.cn/topic/libraries/architecture/viewmodel?hl=zh-cn#lifecycle)，请使用 ViewModel 作为屏幕级状态容器的实现细节。请勿将它们用作芯片组或表单等可重复使用的界面组件的状态容器。否则，当您在同一 ViewModelStoreOwner 下将同一界面组件用于不同用途时，您会获取相同的 ViewModel 实例。
- ViewModel 不应该知道界面实现细节。请尽可能对 ViewModel API 公开的方法和界面状态字段使用通用名称。这样一来，ViewModel 便可以适应任何类型的界面：手机、可折叠设备、平板电脑甚至 Chromebook！
- 由于 ViewModel 的生命周期可能比 `ViewModelStoreOwner` 更长，因此 ViewModel 不应保留任何对与生命周期相关的 API（例如 `Context` 或 `Resources`）的引用，以免发生内存泄漏。
- 请勿将 ViewModel 传递给其他类、函数或其他界面组件。由于平台会管理它们，因此您应该使其尽可能靠近平台。应该靠近您的 activity、fragment 或屏幕级可组合函数。这样可以防止较低级别的组件访问超出其需求的数据和逻辑。

## 更多信息

随着数据变得越来越复杂，您可能会选择使用单独的类加载数据。[`ViewModel`](https://developer.android.google.cn/reference/androidx/lifecycle/ViewModel?hl=zh-cn) 的用途是封装界面控制器的数据，以使数据在配置更改后仍然存在。如需了解如何在配置更改后加载、保留和管理数据，请参阅[保存的界面状态](https://developer.android.google.cn/topic/libraries/architecture/saving-states?hl=zh-cn)。

[Android 应用架构指南](https://developer.android.google.cn/topic/libraries/architecture/guide?hl=zh-cn#fetching_data)建议构建存储区类来处理这些功能。

## 其他资源

如需详细了解 `ViewModel` 类，请参阅以下资源。

### 文档

- [界面层](https://developer.android.google.cn/topic/architecture/ui-layer?hl=zh-cn)
- [用户界面事件](https://developer.android.google.cn/topic/architecture/ui-layer/events?hl=zh-cn)
- [状态容器和界面状态](https://developer.android.google.cn/topic/architecture/ui-layer/stateholders?hl=zh-cn)
- [状态生成](https://developer.android.google.cn/topic/architecture/ui-layer/state-production?hl=zh-cn)
- [数据层](https://developer.android.google.cn/topic/architecture/data-layer?hl=zh-cn)