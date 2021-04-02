### 5.5.3　基于QSpinBox的自定义代理类

#### 1．自定义代理类的基本结构

下面设计一个基于QSpinBox类的自定义代理类，用于“测深”数据列的编辑。

在Qt Creator里单击“File”→“New File or Project”菜单项，在出现的“New File or Project”对话框里选择新建一个C++class文件，在出现的对话框里，输入自定义类的名称为QWIntSpinDelegate，设置基类为QStyledItemDelegate，单击下一步后结束向导，系统会自动生成头文件和源文件，并添加到项目里。

在头文件qwintspindelegate.h中包含对自定义类QWIntSpinDelegate的定义，在其中添加4个需要重定义的函数的定义，qwintspindelegate.h的内容如下：

```css
#include   <QStyledItemDelegate>
class QWIntSpinDelegate : public QStyledItemDelegate
{
   Q_OBJECT
public:
   QWIntSpinDelegate(QObject *parent=0);
//自定义代理组件必须继承以下4个函数
  QWidget *createEditor(QWidget *parent, const QStyleOptionViewItem &option,
        const QModelIndex &index) const Q_DECL_OVERRIDE;
  void setEditorData(QWidget *editor, 
               const QModelIndex &index)const Q_DECL_OVERRIDE;
   void setModelData(QWidget *editor, QAbstractItemModel *model,
                const QModelIndex &index) const Q_DECL_OVERRIDE;
   void updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem
       &option, const QModelIndex &index) const Q_DECL_OVERRIDE;
};
```

自定义代理组件必须重新实现这4个函数，函数的原型都是固定的。

#### 2．createEditor()函数的实现

createEditor()函数用于创建需要的编辑组件，QWIntSpinDelegate类希望创建一个QSpinBox作为编辑组件，函数的实现如下：

```css
QWidget *QWIntSpinDelegate::createEditor(QWidget *parent,
   const QStyleOptionViewItem &option, const QModelIndex &index) const
{ //创建代理编辑组件
   QSpinBox *editor = new QSpinBox(parent); 
   editor->setFrame(false); //设置为无边框
   editor->setMinimum(0); 
   editor->setMaximum(10000);
   return editor;  //返回此编辑器
}
```

这段代码创建了一个QSpinBox类型的编辑器editor，parent指向视图组件；然后对创建的editor做一些设置，将editor作为函数的返回值。

#### 3．setEditorData()函数

setEditorData()函数用于从数据模型获取数值，设置为编辑器的显示值。当双击一个单元格进入编辑状态时，就会自动调用此函数，其实现代码如下：

```css
void QWIntSpinDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const
{//从数据模型获取数据，显示到代理组件中
   int value = index.model()->data(index, Qt::EditRole).toInt();
   QSpinBox *spinBox = static_cast<QSpinBox*>(editor);  
   spinBox->setValue(value); 
}
```

函数传递来的参数editor指向代理编辑组件，index是关联的数据单元的模型索引。

通过强制类型转换将editor转换为QSpinBox类型组件spinBox，然后将获取的数值设置为spinBox的值。

#### 4．setModelData()函数

setModelData()函数用于将代理编辑器上的值更新给数据模型，当用户在界面上完成编辑时会自动调用此函数，将界面上的数据更新到数据模型。其代码如下：

```css
void QWIntSpinDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const
{ //将代理组件的数据保存到数据模型中
   QSpinBox *spinBox = static_cast<QSpinBox*>(editor); 
   spinBox->interpretText();
   int value = spinBox->value();
   model->setData(index, value, Qt::EditRole);
}
```

程序先获取代理组件编辑器里的数值，然后利用传递来的数据模型model和模型索引参数index将编辑器的最新值更新到数据模型里。

#### 5．updateEditorGeometry()函数

updateEditorGeometry()函数用于为代理组件设置一个合适的大小，函数传递的参数option的rect变量定义了单元格适合显示代理组件的大小，直接设置为此值即可。代码如下。

```css
void QWIntSpinDelegate::updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const
{ //设置组件大小
   editor->setGeometry(option.rect);
}
```

