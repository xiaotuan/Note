![01](./images/01.png)

首先，`Fragment.onCreate(Bundle?)` 是公共函数，而 `Activity.onCreate(Bundle?)` 是受 保护函数。`Fragment.onCreate(Bundle?)` 函数及其他 `Fragment` 生命周期函数必须是公共函数，因为托管 `fragment` 的 `activity` 要调用它们。

其次，类似于 `activity`，`fragment` 同样具有保护及获取状态的 `bundle`。如同使用 `Activity.onSaveInstanceState(Bundle)` 函数那样，你也可以根据需要覆盖 `Fragment.onSaveInstanceState(Bundle)` 函数。

最后，`fragment` 的视图并没有在 `Fragment.onCreate(Bundle?)` 函数中生成。虽然我们在该函数中配置了 `fragment` 实例，但创建和配置 `fragment` 视图是另一个 `Fragment` 生命周期函数完成的：`onCreateView(LayoutInflater, ViewGroup?, Bundle?)`。该函数会实例化 `fragment` 视图的布局，然后将实例化的 `View` 返回给托管 `activity`。`LayoutInflater` 及 `ViewGroup` 是实例化布局的必要参数。`Bundle` 用来存储恢复数据，可供该函数从保存状态下重建视图。