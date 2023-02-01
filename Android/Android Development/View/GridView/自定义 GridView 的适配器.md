[toc]

### 1. 在  xml 中定义 GridView

```xml
<?xml version="1.0" encoding="utf-8"?><!-- This file is at /res/layout/gridviewcustom.xml -->
<GridView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/gridview"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:horizontalSpacing="10dp"
    android:numColumns="auto_fit"
    android:padding="10dp"
    android:verticalSpacing="10dp" />
```

### 2. 在代码中使用 GridView

#### 2.1 Kotlin

```kotlin
import android.widget.GridView

val gv = findViewById<GridView>(R.id.gridview)

val adapter = ManateeAdapter(this)

gv.adapter = adapter
```

#### 2.2 Java

```java
import android.widget.GridView;

GridView gv = findViewById(R.id.gridview);

ManateeAdapter adapter = new ManateeAdapter(this);

gv.setAdapter(adapter);
```

### 3. 创建自定义适配器

#### 3.1 Kotlin

```kotlin
import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.ImageView

companion object {

    class ManateeAdapter(private val context: Context): BaseAdapter() {

        private val mInflater = LayoutInflater.from(context)

        private val manatees = intArrayOf(
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
            R.drawable.manatee33
        )

        private var manateeImages = ArrayList<Bitmap>()
        private var manateeThumbs = ArrayList<Bitmap>()

        init {
            for (i in manatees.indices) {
                manateeImages.add(BitmapFactory.decodeResource(context.resources, manatees[i]))
                manateeThumbs.add(Bitmap.createScaledBitmap(manateeImages[i],
                    100, 100, false))
            }
        }

        override fun getCount(): Int {
            return manatees.size
        }

        override fun getItem(position: Int): Bitmap {
            return manateeImages[position]
        }

        override fun getItemId(position: Int): Long {
            return position.toLong()
        }

        override fun getViewTypeCount(): Int {
            Log.v(TAG, "in getViewTypeCount()")
            return 1
        }

        override fun getItemViewType(position: Int): Int {
            Log.v(TAG, "in getItemViewType() for position $position")
            return 0
        }

        override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
            var holder: ViewHolder? = null
            var view: View?

            Log.v(TAG, "in getView for position $position, covertView is ${if (convertView == null)  "null" else "being recycled"}")

            if (convertView == null) {
                view = mInflater.inflate(R.layout.gridimage, null)
                convertViewCounter++
                Log.v(TAG, "$convertViewCounter convertViews have been created")

                holder = ViewHolder()
                holder.image = view.findViewById(R.id.gridImageView)

                view.tag = holder
            } else {
                holder = convertView.tag as ViewHolder
                view = convertView
            }

            holder.image.setImageBitmap(manateeImages[position])

            return view!!
        }

        companion object {
            const val TAG = "ManateeAdapter"
            var convertViewCounter = 0

            class ViewHolder {
                lateinit var image: ImageView
            }
        }
    }
}
```

#### 3.2 Java

```java
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;

public static class ManateeAdapter extends BaseAdapter {
    private static final String TAG = "ManateeAdapter";
    private static int convertViewCounter = 0;
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
            R.drawable.manatee33};

    private Bitmap[] manateeImages = new Bitmap[manatees.length];
    private Bitmap[] manateeThumbs = new Bitmap[manatees.length];

    public ManateeAdapter(Context context) {
        Log.v(TAG, "Constructing ManateeAdapter");
        this.mContext = context;
        mInflater = LayoutInflater.from(context);

        for (int i = 0; i < manatees.length; i++) {
            manateeImages[i] = BitmapFactory.decodeResource(
                    context.getResources(), manatees[i]);
            manateeThumbs[i] = Bitmap.createScaledBitmap(manateeImages[i],
                    100, 100, false);
        }
    }

    public int getCount() {
        Log.v(TAG, "in getCount()");
        return manatees.length;
    }

    public int getViewTypeCount() {
        Log.v(TAG, "in getViewTypeCount()");
        return 1;
    }

    public int getItemViewType(int position) {
        Log.v(TAG, "in getItemViewType() for position " + position);
        return 0;
    }

    public View getView(int position, View convertView, ViewGroup parent) {
        ViewHolder holder;

        Log.v(TAG, "in getView for position " + position +
                ", convertView is " +
                ((convertView == null) ? "null" : "being recycled"));

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

    public Object getItem(int position) {
        Log.v(TAG, "in getItem() for position " + position);
        return manateeImages[position];
    }

    public long getItemId(int position) {
        Log.v(TAG, "in getItemId() for position " + position);
        return position;
    }
}
```

