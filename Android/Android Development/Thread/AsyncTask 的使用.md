[toc]
> > 注意
>
> `AsyncTask` 已被标注为过时 API。
### 1. 主要方法说明
`AsyncTask` 类的常用方法说明如下：

+ `onPreExecute()`：任务执行前会调用该方法，该方法在主线程上执行。
+ `onProgressUpdate(Integer... values)` ：更新任务处理进度，该方法在主线程上执行
+ `doInBackground(String... strings)` ：后台执行任务，该方法在后台线程上执行
+ `onPostExecute(Boolean aBoolean)` ：任务执行完，将会调用给该方法，该方法在主线程上执行。
+ `onCancelled(Boolean aBoolean)` 或 `onCancelled()`  ： 任务取消将会调用该方法

### 2. 泛型类型说明

`AsyncTask` 三个泛型值含义如下：

`AsyncTask<Params, Progress, Result>`

+ `Params`：`AsyncTask` 执行参数类型，即 `execute()` 方法传递的参数类型
+ `Progress`：进度值的类型，即 `onProgressUpdate()` 方法参数的类型
+ `Result`：任务返回结果类型，即 `onPostExecute()` 方法参数的类型

### 3. 执行任务

通过向 `AsyncTask` 类的 `execute()` 方法传递执行参数来执行任务。

### 4. 更新任务进度

通过调用 `publishProgress()` 方法可以更新任务进度。

### 5. 获取任务执行状态

+ 通过 `getStatus()` 方法来获取当前任务的状态。
+ 通过 `isCancelled()` 方法来查看任务是否已取消。

### 6. 示例代码

#### 6.1 Kotlin

```kotlin
import android.os.AsyncTask

val task = MyTask()
task.execute("params")

class MyTask: AsyncTask<String, Int, Boolean>() {

    override fun onPreExecute() {
        super.onPreExecute()
    }

    override fun onProgressUpdate(vararg values: Int?) {
        super.onProgressUpdate(*values)
    }

    override fun doInBackground(vararg params: String?): Boolean {
        publishProgress(57)
        return false
    }

    override fun onPostExecute(result: Boolean?) {
        super.onPostExecute(result)
    }

    override fun onCancelled(result: Boolean?) {
        super.onCancelled(result)
    }

    override fun onCancelled() {
        super.onCancelled()
    }

}
```

#### 6.2 Java

```java
import android.os.AsyncTask;

MyTask task = new MyTask();
task.execute("params");

class MyTask extends AsyncTask<String, Integer, Boolean> {

    @Override
    protected void onPreExecute() {
        super.onPreExecute();
    }

    @Override
    protected void onProgressUpdate(Integer... values) {
        super.onProgressUpdate(values);
    }

    @Override
    protected Boolean doInBackground(String... strings) {
        publishProgress(57);
        return false;
    }

    @Override
    protected void onPostExecute(Boolean aBoolean) {
        super.onPostExecute(aBoolean);
    }

    @Override
    protected void onCancelled(Boolean aBoolean) {
        super.onCancelled(aBoolean);
    }

    @Override
    protected void onCancelled() {
        super.onCancelled();
    }
}
```

