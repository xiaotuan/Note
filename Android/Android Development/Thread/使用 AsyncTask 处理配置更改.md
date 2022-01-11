[toc]

> 注意
> `onRetainCustomNonConfigurationInstance()` 方法已被标志为过时方法。

如果启动 `AsyncTask` 的活动被销毁并重新创建，该 `AsyncTask` 将不会生效，但是 `AsyncTask` 还存在。因为 `AsyncTask` 在应用程序内一个独立线程中运行，所以在创建新活动时它仍然存在。我们要做的就是重新连接二者，使用 `AsyncTask` 能够找到新活动上的视图。`Activity` 上有一个回调和一个方法来完成此工作，它们分别是 `onRetainCustomNonConfigurationInstance()` 和 `getLastNonConfigurationInstance()` 。

### 1. Kotlin

```kotlin
import android.os.AsyncTask
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    
    private var mTask: MyTask? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        mTask = lastNonConfigurationInstance as? MyTask
        if (mTask == null) {
            mTask = MyTask()
            mTask?.execute("params")
        }
    }

    override fun onRetainCustomNonConfigurationInstance(): Any? {
        return mTask;
    }

    companion object {
        const val TAG = "qty"
    }

    private class MyTask: AsyncTask<String, Int, Boolean>() {

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

    }
}
```

### 2. Java

```java
import androidx.appcompat.app.AppCompatActivity;
import android.os.AsyncTask;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "qty";

    private MyTask mTask;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mTask = (MyTask) getLastNonConfigurationInstance();
        if (mTask == null) {
            mTask = new MyTask();
            mTask.execute("params");
        }
    }

    @Override
    public Object onRetainCustomNonConfigurationInstance() {
        return mTask;
    }

    private class MyTask extends AsyncTask<String, Integer, Boolean> {

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
            return null;
        }

        @Override
        protected void onPostExecute(Boolean aBoolean) {
            super.onPostExecute(aBoolean);
        }

    }

}
```

