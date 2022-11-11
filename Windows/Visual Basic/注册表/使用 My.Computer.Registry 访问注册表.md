[toc]

访问 Windows 注册表的方式有两种。第一种是使用 Visual Basic 内置的函数 `GetSetting()` 和 `SaveSetting()`。然而，这些函数存在众多局限性，如只能操纵注册表中的键和特定 Visual Basic 键中的值。

`Registry` 对象是 `My.Computer` 的一个对象属性。`My` 对象基本上是其他有用对象的快捷方式，这些对象本身不那么容易理解。`My` 对象的属性之一是 `Computer` 有一个名为 `Registry` 的对象属性，让您能够直接访问 `Windows` 注册表。

### 1. 创建注册表键

`My.Computer.Registry` 对象有很多属性。

<center><b>Registry 对象中常用的顶级节点属性</b></center>

| 属性          | 用于访问            |
| ------------- | ------------------- |
| ClassesRoot   | HKEY_CLASSES_ROOT   |
| CurrentConfig | HKEY_CURRENT_CONFIG |
| CurrentUser   | HKEY_CURRENT_USER   |
| LocalMachine  | HKEY_LOCAL_MACHINE  |
| User          | HKEY_USERS          |

使用 `My.Computer.Registry` 创建注册表键很简单。首先必须确定要在哪个 "蜂窝" 下创建键。知道了 "蜂窝" 后，只需调用对应 "蜂窝" 对象属性的 `CreateSubKey()` 方法，并将要创建的键名传递给它。例如：

```vb
My.Computer.Registry.CurrentUser.CreateSubKey("UserSettings")
```

这条语句在 `HKEY_CURRENT_USER` 下创建键 `UserSettings`。大多数应用程序都在 `\Software` 键下创建一个以公司名称命名的键，然后在公司子健下创建产品键。

`CreateSubKey()` 允许在一次方法调用中指定键的多个层次。要创建上面的键结构，可使用如下所示的语句：

```vb
My.Computer.Registry.CurrentUser.CreateSubKey("Software\CleverSoftware\PictureViewer")
```

> 注意：如果 Visual Basic 找到已存在的子健，将不会覆盖它。

> 说明：为什么是 `HKEY_CURRENT_USER` 而不是 `HKEY_LOCAL_MACHINE` 呢？通常，最好将应用程序的设置存储在 `HKEY_CURRENT_USER` 下，这样使用应用程序的每个用户都将拥有各自的设置。如果将设置存储在 `HKEY_LOCAL_MACHINE` 下，设置对于在此计算机上运行该程序的所有用户来说是全局的。另外，有些管理员限制对 `HKEY_LOCAL_MACHINE` 进行访问，因此应用程序将不能访问受限的键。

### 2. 删除注册表键

可以使用两个方法来删除注册表键：`DeleteSubKey()` 和 `DeleteSubKeyTree()`。`DeleteSubKey()` 删除不包含子健的键及其所有值；`DeleteSubKeyTree()` 不仅删除键及其值，还删除所有的子健，使用这个方法要小心！例如：

```vb
My.Computer.Registry.CurrentUser.DeleteSubKey("Softwore\CleverSoftware\PictureViewer")
```

> 注意：如果指定的键不存在，`DeleteSubKey()` 将引发异常。

### 3. 获取和设置键值

要创建新值或设置已有的值，可使用 `My.Computer.Registry.SetValue()`。`SetValue()` 方法的语法如下所示：

```vb
SetValue(keypath, itemanme, value)
```

必须在 `keypath` 中指定 "蜂窝" 的名称。Visual Basic 将根据传递给方法的值来设置数据类型。例如：

```vb
My.Computer.Registry.SetValue("HKEY_CURRENT_USER\Software\CleverSoftware\PictureViewer\", "RegistrationName", "James Foxall")
```

要从注册表中查询一个值，可使用 `GetValue()`，这个方法也要求完整的 `hive/key` 路径，其格式如下所示：

```vb
GetValue(keypath, itemname, defaultvalue)
```

`defaultvalue` 参数定义了当找不到值时 `GetValue()` 的返回值。这样避免了在找不到值时捕获异常。例如：

```vb
MessageBox.Show(My.Computer.Registry.GetValue("HKEY_CURRENT_USER\Software\CleverSoftWare\PictureViewer\", "RegistrationName", ""))
```

