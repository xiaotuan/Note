下面介绍下如何使用代码实现storyboard的页面跳转:

1. 如果单纯的使用segue进行页面跳转，可以在UIViewController调用下面方法:

```bash
performSegue(withIdentifier: "ShowItem", sender: tableView)
```

如果需要修改跳转的动画效果，可以在init方法中设置modalPresentationStyle的值：

```swift
override init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?) {
        super.init(nibName: nibNameOrNil, bundle: nibBundleOrNil)
        self.modalPresentationStyle = .custom
}
```

然后实现下面的方法进行参数传递：

```swift
override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // If the triggered segue is the "ShowItem" segue
        if segue.identifier == "ShowItem" {
            // Figure out which row was just tapped
            if let row = tableView.indexPathForSelectedRow?.row {
                // Get the item associated with this row and pass it along
                let item = itemStore.allItems[row]
                let detailViewController = segue.destination as! DetailViewController
                detailViewController.item = item
            }
        }
    }
```

1. 如果希望跳转的使用使用系统的样式和动画，可以使用下面的方法：
    a. Show Detail:

```bash
let detailController = DetailViewController()
detailController.item = itemStore.allItems[indexPath.row]
showDetailViewController(detailController, sender: tableView)
```

​		b. Show:

```bash
let detailController = DetailViewController()
detailController.item = itemStore.allItems[indexPath.row]
show(detailController, sender: tableView)
```