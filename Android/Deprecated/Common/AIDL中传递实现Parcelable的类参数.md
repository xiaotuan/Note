比如有一个类 Person 实现了 Parcelable 接口，它的包名为：

```
com.qty.simple
```

以传递 Person 对象为例：

1. 在 aidl 文件夹中创建与 Person 类的包名相同的包路径：

```
aidl/com/qty/simpe/
```

2. 在上面创建的包路径下新建一个 Person.aidl 文件，文件内容如下：

```
// Person.aidl
package com.qty.simpe;

// Declare any non-default types here with import statements
parcelable Person;
```

3. 在 aidl 文件中使用该 Person 类（假设有一个 IServiceInterface.aidl 文件）：

```
// ISocketServiceInterface.aidl
package com.test.simpe;

import com.qty.simpe.Person;

interface IConnectServiceInterface {

    void setPerson(in Person person);

}
```

> 注意：Person 参数前面需要加 in 修饰符；如果是输入参数，则是 out；如果是输入输出参，则是 inout。