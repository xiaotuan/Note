### 10.4.1　配置UBIFS

为了使用UBIFS，你需要在内核中开启对它的支持。为了开启UBIFS功能，必须在内核配置中选择两个不同的内核配置菜单项。首先，开启MTD_UBI。这个内核配置选项的路径为Device Drivers → Memory Technology Device (MTD) support → UBI - Unsorted block images → Enable UBI。选择了这个菜单项之后，我们才可以选择另一个有关文件系统支持的配置选项，路径为File Systems → Miscellaneous filesystem → UBIFS file system support。

