### 第5章　 Model/View结构

Model/View（模型/视图）结构是Qt中用界面组件显示与编辑数据的一种结构，视图（View）是显示和编辑数据的界面组件，模型（Model）是视图与原始数据之间的接口。Model/View结构的典型应用是在数据库应用程序中，例如数据库中的一个数据表可以在一个QTableView组件中显示和编辑。

主要的视图组件有QListView、QTreeView和QTableView，第4章介绍的QListWidget、QTreeWidget和QTableWidget分别是这3个类的便利类，它们不使用数据模型，而是将数据直接存储在组件的每个项里。

本章介绍Model/View结构原理，包括QListView、QTreeView、QTableView视图组件，以及QStringListModel、QStandardItemModel等模型类的用法。

