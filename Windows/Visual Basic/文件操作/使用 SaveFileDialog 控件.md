`SaveFileDialog` 控件与 `OpenFileDialog` 控件类似，但它让用户浏览目录并将文件保存而不是要打开文件。`SaveFileDialog` 控件实际上并不保存文件，它只是让用户指定要保存文件的文件名。执行下列步骤来创建 `SaveFileDialog`：

1. 在窗体上创建一个新文本框，并按如下设置它的属性：

   | 属性     | 值             |
   | -------- | -------------- |
   | Name     | txtDestination |
   | Location | 95,34          |
   | Size     | 184,20         |

2. 创建一个