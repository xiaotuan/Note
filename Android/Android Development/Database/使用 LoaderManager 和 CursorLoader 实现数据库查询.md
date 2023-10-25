Loader 的优点：

+ 如果你直接在 Activity 或 Fragment 获取数据，造成用户在UI 线程中执行可能耗时的查询而缺乏响应能力，也有可能引起 ANR。
+  如果创建一个异步任务（比如 AysncTask ）来获取数据，一般场景可以满足要求，但是有个缺点：当组件 Activity 或 Fragment 因屏幕旋转等因素被销毁重建后，AysncTask 又会重新执行务。

+ Loader 在单独的线程上运行，以防止 UI 出现卡顿或无响应。
+ Loader 通过在事件发生时提供回调方法来简化线程管理。
+ Loader 在配置更改中持久保存和缓存结果，以防止重复查询。
+ Loader 可以实现一个观察者来监控底层数据源的变化。例如，CursorLoader 自动注册一个ContentObserver 以在数据更改时触发重新加载。

使用 `LoaderManager` 和 `CursorLoader` 处理数据库操作的步骤如下：

1. 获取 `LoaderManager` 实例

   **Kotlin**

   ```kotlin
   import androidx.loader.app.LoaderManager
   
   val loaderManager = LoaderManager.getInstance(this)
   ```

   **Java**

   ```java
   import androidx.loader.app.LoaderManager;
   
   LoaderManager loaderManager = LoaderManager.getInstance(this)
   ```

2. 创建 `LoaderManager.LoaderCallbacks<Cursor>` 回调实现

   可以通过让 `Activity` 或 `Fragment` 实现改回调方法：

   **Kotlin**

   ```kotlin
   import android.content.ContentValues
   import android.database.Cursor
   import android.net.Uri
   import androidx.appcompat.app.AppCompatActivity
   import android.os.Bundle
   import android.util.Log
   import androidx.loader.app.LoaderManager
   import androidx.loader.content.CursorLoader
   import androidx.loader.content.Loader
   
   private const val TAG = "MainActivity"
   
   class MainActivity : AppCompatActivity(), LoaderManager.LoaderCallbacks<Cursor> {
   
       override fun onCreate(savedInstanceState: Bundle?) {
           super.onCreate(savedInstanceState)
           setContentView(R.layout.activity_main)
           
           val loaderManager = LoaderManager.getInstance(this)
           loaderManager.initLoader(0, null, this)
       }
       
       override fun onCreateLoader(id: Int, args: Bundle?): Loader<Cursor> {
           TODO("Not yet implemented")
       }
   
       override fun onLoaderReset(loader: Loader<Cursor>) {
           TODO("Not yet implemented")
       }
   
       override fun onLoadFinished(loader: Loader<Cursor>, data: Cursor?) {
           TODO("Not yet implemented")
       }
   }
   ```

   **Java**

   ```java
   import android.content.ContentValues;
   import android.database.Cursor;
   import android.net.Uri;
   import androidx.appcompat.app.AppCompatActivity;
   import android.os.Bundle;
   import android.util.Log;
   import androidx.loader.app.LoaderManager;
   import androidx.loader.content.CursorLoader;
   import androidx.loader.content.Loader;
   
   private const val TAG = "MainActivity"
   
   class MainActivity extends AppCompatActivity implements LoaderManager.LoaderCallbacks<Cursor> {
   
       @override
       public void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           setContentView(R.layout.activity_main);
           
           LoaderManager loaderManager = LoaderManager.getInstance(this);
           loaderManager.initLoader(0, null, this);
       }
       
       @override
       public Loader<Cursor> onCreateLoader(Int id, Bundle args) {
           // TODO: "Not yet implemented"
       }
   
       @override
       public void onLoaderReset(Loader<Cursor> loader) {
           // TODO: "Not yet implemented"
       }
   
       @override
       public void onLoadFinished(Loader<Cursor> loader, Cursor data) {
           // TODO: "Not yet implemented"
       }
   }
   ```

   也可以使用下面方法：

   **kotlin**

   ```kotlin
   val loaderManager = LoaderManager.getInstance(this)
   loaderManager.initLoader(0, null, object: LoaderManager.LoaderCallbacks<Cursor> {
   
       override fun onCreateLoader(id: Int, args: Bundle?): Loader<Cursor> {
           TODO("Not yet implemented")
       }
   
       override fun onLoaderReset(loader: Loader<Cursor>) {
           TODO("Not yet implemented")
       }
   
       override fun onLoadFinished(loader: Loader<Cursor>, data: Cursor?) {
           TODO("Not yet implemented")
       }
   })
   ```

   **Java**

   ```java
   LoaderManager loaderManager = LoaderManager.getInstance(this);
   loaderManager.initLoader(0, null, new LoaderManager.LoaderCallbacks<Cursor>() {
       @override
       public Loader<Cursor> onCreateLoader(Int id, Bundle args) {
           // TODO: "Not yet implemented"
       }
   
       @override
       public void onLoaderReset(Loader<Cursor> loader) {
           // TODO: "Not yet implemented"
       }
   
       @override
       public void onLoadFinished(Loader<Cursor> loader, Cursor data) {
           // TODO: "Not yet implemented"
       }
   });
   ```

3. 执行数据库查询

   调用 `LoaderManager` 的 `initLoader(int id, @Nullable Bundle args,
               @NonNull LoaderManager.LoaderCallbacks<D> callback)` 方法将会触发 `LoaderManager.LoaderCallbacks<T>` 回调。

   `initLoader()` 方法参数说明：

   + `id` ：用于区别不同的查询。
   + `args`：传递给 `LoaderManager.LoaderCallbacks<T>` 回调中 `onCreateLoader(Int id, Bundle args)` 方法中的 `args` 参数。
   + `callback`：`LoaderManager.LoaderCallbacks<D>` 回调接口。

   例如：

   **kotlin**

   ```kotlin
   val loaderManager = LoaderManager.getInstance(this)
   loaderManager.initLoader(1, null, this)
   ```

   **Java**

   ```java
   LoaderManager loaderManager = LoaderManager.getInstance(this);
   loaderManager.initLoader(0, null, this);
   ```

   当调用 `initLoader()` 时，如果 `id` 对应的 `Loader` 已经存在，则直接使用该 `Loader`。如果不存在，就创建一个。但是有时需要丢掉过时的数据并重新开始，可以调用 `restartLoader()` 方法。例如：

   **Kotlin**

   ```kotlin
   loaderManager.restartLoader(1, null, this)
   ```

   **Java**

   ```Java
   loaderManager.restartLoader(0, null, this);
   ```

4. `LoaderManager.LoaderCallbacks` 接口方法说明

   `CursorLoader` 在 `Loader` 结束后将保留其数据。允许应用保持 `activity` 或 `Fragment` 的 `onStop()` 和 `onStart()` 方法相关的数据，当用户返回程序时他们不必等待数据重载。

   + **onCreateLoader** 方法

     当你试图访问一个 `Loader` （例如通过 `initLoader()` ）时，它会检查该 `ID` 指定的 `Loader` 是否存在。如果没有，则触发 `LoaderManager.LoaderCallbacks` 的 `onCreateLoader` 方法。这是你创建一个新的 `Loader` 的地方。例如：

     **Kotlin**

     ```kotlin
     override fun onCreateLoader(id: Int, args: Bundle?): Loader<Cursor> {
         if (id == 0) {
             return CursorLoader(
                 this,
                 CitizenTable.CONTENT_URI,
                 null,
                 null,
                 null,
                 "${CitizenTable.INCOME} ASC"
             )
         } else if (id == 1) {
             val myC = Uri.withAppendedPath(CitizenTable.CONTENT_URI, "2")
             return CursorLoader(
                 this,
                 myC,
                 null,
                 null,
                 null,
                 null
             )
         } else {
             return CursorLoader(
                 this,
                 CitizenTable.CONTENT_URI,
                 null,
                 null,
                 null,
                 null
             )
         }
     }
     ```

     **Java**

     ```java
     @override
     public Loader<Cursor> onCreateLoader(Int id, Bundle args) {
         if (id == 0) {
             return new CursorLoader(
                 this,
                 CitizenTable.CONTENT_URI,
                 null,
                 null,
                 null,
                 "${CitizenTable.INCOME} ASC"
             );
         } else if (id == 1) {
             Uri myC = Uri.withAppendedPath(CitizenTable.CONTENT_URI, "2");
             return new CursorLoader(
                 this,
                 myC,
                 null,
                 null,
                 null,
                 null
             );
         } else {
             return new CursorLoader(
                 this,
                 CitizenTable.CONTENT_URI,
                 null,
                 null,
                 null,
                 null
             );
         }
     }
     ```

   + `onLoaderReset` 方法

     当调用 `LoaderManager` 的 `destroyLoader()` 方法后，将触发该方法。这个回调让你找出数据何时被释放，这样你就可以移除它的引用。例如：

     **kotlin**

     ```kotlin
     override fun onLoaderReset(loader: Loader<Cursor>) {
         adapter.swapCursor(null)
     }
     ```

     **Java**

     ```java
     public void onLoaderReset(Loader<Cursor> loader) {
         // This is called when the last Cursor provided to onLoadFinished()
         // above is about to be closed.  We need to make sure we are no
         // longer using it.
         adapter.swapCursor(null);
     }
     ```

   + `onLoadFinished` 方法
   
     查询结束后会回调该方法。可以通过 `loader` 参数的 `id` 属性获取当前查询结果属于那个加载项的，`data` 参数为查询结果的 `Cursor` 对象。例如：
   
     **Kotlin**
   
     ```kotlin
     override fun onLoadFinished(loader: Loader<Cursor>, data: Cursor?) {
         Log.d(TAG, "onLoadFinished=>id: ${loader.id}")
         data?.apply {
             val idCol = getColumnIndex(CitizenTable.ID)
             val nameCol = getColumnIndex(CitizenTable.NAME)
             val stateCol = getColumnIndex(CitizenTable.STATE)
             val incomeCol = getColumnIndex(CitizenTable.INCOME)
             while (moveToNext()) {
                 val id = getInt(idCol)
                 val name = getString(nameCol)
                 val state = getString(stateCol)
                 val income = getInt(incomeCol)
                 Log.d(TAG, "Retrieved || $id || $name || $state || $income")
             }
             Log.d(TAG, "----------------------------------------------------")
         }
     }
     ```
   
     **Java**
   
     ```java
     @override
     public void onLoadFinished(Loader<Cursor> loader, Cursor data) {
         Log.d(TAG, "onLoadFinished=>id: " + loader.getId());
         if (data != null) {
             int idCol = data.getColumnIndex(CitizenTable.ID);
             int nameCol = data.getColumnIndex(CitizenTable.NAME);
             int stateCol = data.getColumnIndex(CitizenTable.STATE);
             int incomeCol = data.getColumnIndex(CitizenTable.INCOME);
             while (data.moveToNext()) {
                 int id = data.getInt(idCol)
                 String name = data.getString(nameCol)
                 String state = data.getString(stateCol)
                 int income = data.getInt(incomeCol)
                 Log.d(TAG, "Retrieved || $id || $name || $state || $income")
             }
     		Log.d(TAG, "----------------------------------------------------");
         }
     }
     ```
   
     