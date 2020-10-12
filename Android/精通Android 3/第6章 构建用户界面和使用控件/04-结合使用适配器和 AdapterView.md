[toc]

### 1. 基本的列表控件：ListView

通常编译一个扩展 android.app.ListActivity 的新活动来使用 ListView。ListActivity 包含一个 ListView，可以调用 setListAdapter() 方法来为 ListView 设置数据。

#### 1.1 在 ListView 中显示值

**代码清单6-27** 向 ListView 添加项

```java
public class ListViewActivity extends ListActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Cursor c = managedQuery(Contacts.People.CONTENT_URI, null, null, null, Contacts.People.NAME);

        String[] cols = new String[] {Contacts.People.NAME};
        int[] views = new int[] {android.R.id.text1};

        SimpleCursorAdapter adapter = new SimpleCursorAdapter(this, android.R.layout.simple_list_item_1, c, cols, views);
        setListAdapter(adapter);
    }
}
```

要运行上面的代码需要在 AndroidManifest.xml 文件中添加 android.permission.READ_CONTACTS 权限。

#### 1.2 ListView 中的可单击项

**代码清单6-28** 接受 ListView 上的用户输入

```java
public class ListViewActivity2 extends ListActivity implements AdapterView.OnItemClickListener {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        ListView lv = getListView();

        Cursor c = managedQuery(Contacts.People.CONTENT_URI, null, null, null, Contacts.People.NAME);

        String[] cols = new String[] {Contacts.People.NAME};
        int[] views = new int[] {android.R.id.text1};

        SimpleCursorAdapter adapter = new SimpleCursorAdapter(this, android.R.layout.simple_list_item_1, c, cols, views);
        setListAdapter(adapter);
        lv.setOnItemClickListener(this);
    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        Log.v("ListViewActivity", "in onItemClick with " + ((TextView) view).getText() + ". Position = " + position + ". Id = " + id);
        Uri selectedPerson = ContentUris.withAppendedId(Contacts.People.CONTENT_URI, id);
        Intent intent = new Intent(Intent.ACTION_VIEW, selectedPerson);
        startActivity(intent);
    }
}
```

#### 1.3 使用 ListView 添加其他控件

**代码清单6-29** 改写 ListActivity 引用的 ListView

```xml
<?xml version="1.0" encoding="utf-8"?><!-- This file is at /res/layout/list.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <ListView
        android:id="@android:id/list"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1" />

    <Button
        android:id="@+id/btn"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Submit Selection"
        android:onClick="doClick" />

</LinearLayout>
```

请注意 ListView ID 的规范。必须使用 "@android:id/list"，因为 ListActivity 需要在布局中找到一个具有此名称的 ListView。

**代码清单6-30** 从 ListActivity 读取用户输入

```java
public class ListViewActivity3 extends ListActivity {

    private static final String TAG = "ListViewActivity3";
    private ListView lv = null;
    private Cursor cursor = null;
    private int idCol = -1;
    private int nameCol = -1;
    private int notesCol = -1;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.list);

        lv = getListView();

        cursor = managedQuery(Contacts.People.CONTENT_URI, null, null, null, Contacts.People.NAME);

        String[] cols = new String[] {Contacts.People.NAME};
        idCol = cursor.getColumnIndex(Contacts.People._ID);
        nameCol = cursor.getColumnIndex(Contacts.People.NAME);
        notesCol = cursor.getColumnIndex(Contacts.People.NOTES);

        int[] views = new int[] {android.R.id.text1};

        SimpleCursorAdapter adapter = new SimpleCursorAdapter(this, android.R.layout.simple_list_item_multiple_choice, cursor, cols, views);

        setListAdapter(adapter);

        lv.setChoiceMode(ListView.CHOICE_MODE_MULTIPLE);


    }

    public void doClick(View view) {
        int count = lv.getCount();
        SparseBooleanArray viewItems = lv.getCheckedItemPositions();
        for (int i = 0; i < count; i++) {
            if (viewItems.get(i)) {
                // CursorWrapper cw = (CursorWrapper) lv.getItemAtPosition(i);
                cursor.moveToPosition(i);
                long id = cursor.getLong(idCol);
                String name = cursor.getString(nameCol);
                String notes = cursor.getString(notesCol);
                Log.v(TAG, name + " is checked. Notes: " + notes + ". Position = " + i +". Id = " + id);
            }
        }
    }
}
```

#### 1.4 从 ListView 读取选择的另一种方式

Android 1.6 引入了另一个方法来从 ListView 获取所选行的列表：getCheckItemIds()。

**代码清单6-31** 从 ListActivity 读取用户输入的另一种方式

```java
public class ListViewActivity4 extends ListActivity {

    private static final String TAG = "ListViewActivity4";
    private static final Uri CONTACTS_URI = ContactsContract.Contacts.CONTENT_URI;
    private SimpleCursorAdapter adapter = null;
    private ListView lv = null;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.list);

        lv = getListView();

        String[] projection = new String[] {ContactsContract.Contacts._ID, ContactsContract.Contacts.DISPLAY_NAME};
        Cursor c = managedQuery(CONTACTS_URI, projection, null, null, ContactsContract.Contacts.DISPLAY_NAME);

        String[] cols = new String[] {ContactsContract.Contacts.DISPLAY_NAME};
        int[] views = new int[] {android.R.id.text1};

        adapter = new SimpleCursorAdapter(this, android.R.layout.simple_list_item_multiple_choice, c, cols, views);

        setListAdapter(adapter);

        lv.setChoiceMode(ListView.CHOICE_MODE_MULTIPLE);
    }

    public void doClick(View view) {
        if (!adapter.hasStableIds()) {
            Log.v(TAG, "Data is not stable");
            return;
        }
        long[] viewItems = lv.getCheckedItemIds();
        for (int i = 0; i < viewItems.length; i++) {
            Uri selectedPerson = ContentUris.withAppendedId(CONTACTS_URI, viewItems[i]);

            Log.v(TAG, selectedPerson.toString() + " is checked.");
        }
    }
}
```

对于此示例，要指出的最后一点是，方法 getCheckedItemIds() 要求适配器中的基础数据保持稳定。因此，强烈建议在调用 ListView 的 getCheckedItemIds() 之前，先调用适配器的 hasStableIds()。

### 2. GridView 控件

**代码清单6-32** XML 布局中的 GridView 定义和关联的 Java 代码

```xml
<?xml version="1.0" encoding="utf-8"?>
<GridView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/gridview"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="10px"
    android:verticalSpacing="10px"
    android:horizontalSpacing="10px"
    android:numColumns="auto_fit"
    android:columnWidth="100px"
    android:stretchMode="columnWidth"
    android:gravity="center"/>
```

```java
public class GridViewActivity extends Activity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.gridview);

        GridView gv = findViewById(R.id.gridview);

        Cursor c = managedQuery(Contacts.People.CONTENT_URI, null, null, null, Contacts.People.NAME);

        String[] cols = new String[] {Contacts.People.NAME};
        int[] views = new int[] {android.R.id.text1};

        SimpleCursorAdapter adapter = new SimpleCursorAdapter(this, android.R.layout.simple_list_item_1, c, cols, views);
        gv.setAdapter(adapter);
    }
}
```

### 3. Spinner 控件

可通过 XML 布局简单地实例化 Spinner：

```xml
<Spinner
	android:id="@+id/spinner"
	android:layout_width="wrap_content"
	android:layout_height="wrap_content"
	android:prompt="@string/spinnerprompt"/>
```

请注意，新特性 android:prompt 用于在要进行选择的列表顶部设置一个提示。

**代码清单6-33** 通过资源文件创建微调框的代码

```java
public class SpinnerActivity extends Activity {

    /** Called when the activity is first created. */
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.spinner);

        Spinner spinner = findViewById(R.id.spinner);

        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.planets, android.R.layout.simple_spinner_item);

        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        spinner.setAdapter(adapter);
    }
}
```

### 4. Gallery 控件

Gallery 控件是一种可水平滚动的列表控件，焦点始终位于列表中央。即可以通过 XML 布局也可以通过代码实例化 Gallery。

```xml
<Gallery xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/gallery"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

### 5. 创建自定义适配器

Android 提供了一个名为 BaseAdapter 的抽象类，如果需要自定义适配器，可以扩展它。

**代码清单6-34** 自定义适配器：ManateeAdapter

```xml
<?xml version="1.0" encoding="utf-8"?>
<GridView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/gridview"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="10px"
    android:verticalSpacing="10px"
    android:horizontalSpacing="10px"
    android:numColumns="auto_fit"
    android:columnWidth="100px"
    android:stretchMode="columnWidth"
    android:gravity="center"/>
```

```java
public class GridViewCustomAdapter extends Activity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.gridviewcustom);

        GridView gv = findViewById(R.id.gridview);

        ManateeAdapter adapter = new ManateeAdapter(this);

        gv.setAdapter(adapter);
    }

    private static class ManateeAdapter extends BaseAdapter {

        private static final String TAG = "ManateeAdapter";
        private static int convertViewCounter= 0;
        private Context mContext;
        private LayoutInflater mInflater;

        static class ViewHolder {
            ImageView image;
        }

        private int[] manatees = {
                R.drawable.manatee00, R.drawable.manatee01, R.drawable.manatee02,
                R.drawable.manatee03, R.drawable.manatee04, R.drawable.manatee05,
                R.drawable.manatee06, R.drawable.manatee07, R.drawable.manatee08,
                R.drawable.manatee09, R.drawable.manatee10, R.drawable.manatee11,
                R.drawable.manatee12, R.drawable.manatee13, R.drawable.manatee14,
                R.drawable.manatee15, R.drawable.manatee16, R.drawable.manatee17,
                R.drawable.manatee18, R.drawable.manatee19, R.drawable.manatee20,
                R.drawable.manatee21, R.drawable.manatee22, R.drawable.manatee23,
                R.drawable.manatee24, R.drawable.manatee25, R.drawable.manatee26,
                R.drawable.manatee27, R.drawable.manatee28, R.drawable.manatee29,
                R.drawable.manatee30, R.drawable.manatee31, R.drawable.manatee32,
                R.drawable.manatee33 };

        private Bitmap[] manateeImages = new Bitmap[manatees.length];
        private Bitmap[] manateeThumbs = new Bitmap[manatees.length];

        public ManateeAdapter(Context context) {
            Log.v(TAG, "Constructing ManateeAdapter");
            this.mContext = context;
            mInflater = LayoutInflater.from(context);

            for (int i = 0; i < manatees.length; i++) {
                manateeImages[i]= BitmapFactory.decodeResource(context.getResources(), manatees[i]);
                manateeThumbs[i] = Bitmap.createScaledBitmap(manateeImages[i], 100, 100, false);
            }
        }

        @Override
        public int getCount() {
            Log.v(TAG,"in getCount()");
            return manatees.length;
        }

        @Override
        public int getViewTypeCount() {
            Log.v(TAG, "in getViewTypeCount()");
            return 1;
        }

        @Override
        public int getItemViewType(int position) {
            Log.v(TAG, "in getItemViewType() for position " + position);
            return 0;
        }

        @Override
        public Object getItem(int position) {
            Log.v(TAG, "in getItem() for position " + position);
            return manateeImages[position];
        }

        @Override
        public long getItemId(int position) {
            Log.v(TAG, "in getItemId() for position " + position);
            return position;
        }

        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            ViewHolder holder;

            Log.v(TAG, "in getView for position " + position + ", convertView is " + ((convertView == null) ? "null" : "being recycled"));

            if (convertView == null) {
                convertView = mInflater.inflate(R.layout.gridimage, null);
                convertViewCounter++;
                Log.v(TAG, convertViewCounter + " convertViews have been created");

                holder = new ViewHolder();
                holder.image = convertView.findViewById(R.id.gridImageView);

                convertView.setTag(holder);
            } else {
                holder = (ViewHolder) convertView.getTag();
            }

            holder.image.setImageBitmap(manateeImages[position]);

            return convertView;
        }
    }
}
```

如果有一个 ListView 并希望在常规数据行之间放置分隔符，则可能有两种类型的视图并需要从 getViewTypeCount() 返回 2。可以拥有任意多种不同的视图类型，只要从此方法恰当地返回正确的计数，getItemViewType() 与此方法相关联。

如果使用分隔符，应该做的另一件事是实现 isEnabled() 方法。对于列表项，此方法应该返回 true；对于分隔符，应该返回 false，因为分隔符不能选择或单击。

### 6. Android 中的其他控件

ScrollView 是设置带有垂直滚动条的 View 容器的控件。

ProgressBar 和 RatingBar 控件类似于滑块，第一个用于直观地显示某项操作的进度，第二个用于显示评价的星级。

Chronometer 控件是一个累积的计时器。如果希望显示一个倒计时器，可以使用 CountDownTimer 类，但它不是 View 类。

WebView 是一种显示 HTML 的特殊视图。