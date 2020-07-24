<center><font size="5"><b>stickyheadersrecyclerview框架</b></font></center>

[toc]

> 这个框架要求SDK的最小版本不能低于14；另外，这个框架在2016年4月之后就不再更新维护了。且该框架使用数据的第一个字符作为分组的标题。

#### 1. Github地址

<https://github.com/bxunzhao/StikyHeader>

#### 2. 配置build.gradle

在项目根目录下的 `gradle.properties` 文件中添加如下代码：

```
RECYCLERVIEW_VERSION = 1.0.0
STICKY_HEAD_VERSION = 0.4.3
```

在 `app` 目录下的 `build.gradle` 文件中添加如下代码：

```
implementation "androidx.recyclerview:recyclerview:${RECYCLERVIEW_VERSION}"
implementation "com.timehop.stickyheadersrecyclerview:library:${STICKY_HEAD_VERSION}"
```



#### 3. 使用方法

##### 3.1 布局文件

```XML
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/rv"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

##### 3.2 MainActivity.java中的代码如下：

```Java
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import com.timehop.stickyheadersrecyclerview.StickyRecyclerHeadersAdapter;
import com.timehop.stickyheadersrecyclerview.StickyRecyclerHeadersDecoration;
import com.timehop.stickyheadersrecyclerview.StickyRecyclerHeadersTouchListener;

public class MainActivity extends AppCompatActivity {
    private RecyclerView rv;

    private AnimalsHeadersAdapter adapter;
    private StickyRecyclerHeadersDecoration headersDecor;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        rv = findViewById(R.id.rv);
    }

    @Override
    protected void onResume() {
        super.onResume();
        initView();
        initEvent();
    }

    private void initView() {
        // 为RecyclerView设置适配器
        adapter = new AnimalsHeadersAdapter();
        adapter.addAll(getDummyDataSet());
        rv.setAdapter(adapter);
        // 为RecyclerView添加LayoutManager
        final LinearLayoutManager layoutManager = new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false);
        rv.setLayoutManager(layoutManager);
        // 为RecyclerView添加Decorator装饰器
        // 为RecyclerView中的Item添加Header头部（自动获取头部ID，将相邻的ID相同的聚合到一起形成一个Header）
        headersDecor = new StickyRecyclerHeadersDecoration(adapter);
        rv.addItemDecoration(headersDecor);
        // 为RecyclerView添加Item之间的分隔线
        rv.addItemDecoration(new DividerDecoration(this, DividerDecoration.VERTICAL_LIST));
    }

    private void initEvent() {
        // 为RecyclerView添加普通Item的点击事件（点击Header无效）
        rv.addOnItemTouchListener(new RecyclerItemClickListener(this, new RecyclerItemClickListener.OnItemClickListener() {
            @Override
            public void onItemClick(View view, int position) {
                Toast.makeText(MainActivity.this, adapter.getItem(position) + " Clicked", Toast.LENGTH_SHORT).show();
            }
        }));
        // 为RecyclerView添加Header的点击事件
        StickyRecyclerHeadersTouchListener touchListener = new StickyRecyclerHeadersTouchListener(rv, headersDecor);
        touchListener.setOnHeaderClickListener(new StickyRecyclerHeadersTouchListener.OnHeaderClickListener() {
            @Override
            public void onHeaderClick(View header, int position, final long headerId) {
                Toast.makeText(MainActivity.this, "Header position: " + position + ", id: " + headerId, Toast.LENGTH_SHORT).show();
            }
        });
        rv.addOnItemTouchListener(touchListener);
    }

    // 获取RecyclerView中展示的数据源
    private String[] getDummyDataSet() {
        return getResources().getStringArray(R.array.animals);
    }

    // StickyHeadersRecyclerView的适配器类
    private static class AnimalsHeadersAdapter extends AnimalAdapter<RecyclerView.ViewHolder> implements StickyRecyclerHeadersAdapter<RecyclerView.ViewHolder> {
        @NonNull
        @Override
        public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
            View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.listitem_normal, parent, false);
            return new RecyclerView.ViewHolder(view) {
            };
        }

        @Override
        public void onBindViewHolder(RecyclerView.ViewHolder holder, int position) {
            TextView textView = (TextView) holder.itemView;
            textView.setText(getItem(position));
        }

        // 获取当前Item的首字母，按照首字母将相邻的Item聚集起来并添加统一的头部
        @Override
        public long getHeaderId(int position) {
            return getItem(position).charAt(0);
        }

        // 获取头部布局
        @Override
        public RecyclerView.ViewHolder onCreateHeaderViewHolder(ViewGroup parent) {
            View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.listitem_header, parent, false);
            return new RecyclerView.ViewHolder(view) {
            };
        }

        // 为头部布局中的控件绑定数据
        @Override
        public void onBindHeaderViewHolder(RecyclerView.ViewHolder holder, int position) {
            final TextView textView = (TextView) holder.itemView;
            textView.setText(String.valueOf(getItem(position).charAt(0)));
        }
    }
}
```

##### 3.3 AnimalAdapter.java文件

```Java
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;

/**
 * RecyclerView的适配器
 */
public abstract class AnimalAdapter<VH extends RecyclerView.ViewHolder> extends RecyclerView.Adapter<VH> {
    private ArrayList<String> items = new ArrayList<String>();

    AnimalAdapter() {
        setHasStableIds(true);
    }

    public void add(String object) {
        items.add(object);
        notifyDataSetChanged();
    }

    public void add(int index, String object) {
        items.add(index, object);
        notifyDataSetChanged();
    }

    private void addAll(Collection<? extends String> collection) {
        if (collection != null) {
            items.addAll(collection);
            notifyDataSetChanged();
        }
    }

    void addAll(String... items) {
        addAll(Arrays.asList(items));
    }

    public void clear() {
        items.clear();
        notifyDataSetChanged();
    }

    public void remove(String object) {
        items.remove(object);
        notifyDataSetChanged();
    }

    String getItem(int position) {
        return items.get(position);
    }

    @Override
    public long getItemId(int position) {
        return getItem(position).hashCode();
    }

    @Override
    public int getItemCount() {
        return items.size();
    }
}
```

#####3.4 RecyclerItenClickListener.java文件

```Java
import android.content.Context;
import android.view.GestureDetector;
import android.view.MotionEvent;
import android.view.View;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class RecyclerItemClickListener implements RecyclerView.OnItemTouchListener {
    private OnItemClickListener mListener;
    private GestureDetector mGestureDetector;

    RecyclerItemClickListener(Context context, OnItemClickListener listener) {
        mListener = listener;
        mGestureDetector = new GestureDetector(context, new GestureDetector.SimpleOnGestureListener() {
            @Override
            public boolean onSingleTapUp(MotionEvent e) {
                return true;
            }
        });
    }

    @Override
    public boolean onInterceptTouchEvent(RecyclerView view, MotionEvent e) {
        View childView = view.findChildViewUnder(e.getX(), e.getY());
        if (childView != null && mListener != null && mGestureDetector.onTouchEvent(e)) {
            mListener.onItemClick(childView, view.getChildAdapterPosition(childView));
        }
        return false;
    }

    @Override
    public void onTouchEvent(@NonNull RecyclerView view, @NonNull MotionEvent motionEvent) {
    }

    @Override
    public void onRequestDisallowInterceptTouchEvent(boolean disallowIntercept) {
        // do nothing
    }

    public interface OnItemClickListener {
        void onItemClick(View view, int position);
    }
}
```

##### 3.5 DividerDecoration.java文件

```Java
import android.content.Context;
import android.content.res.TypedArray;
import android.graphics.Canvas;
import android.graphics.Rect;
import android.graphics.drawable.Drawable;
import android.view.View;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

public class DividerDecoration extends RecyclerView.ItemDecoration {

    private static final int[] ATTRS = new int[] {
            android.R.attr.listDivider
    };

    public static final int HORIZONTAL_LIST = LinearLayoutManager.HORIZONTAL;

    public static final int VERTICAL_LIST = LinearLayoutManager.VERTICAL;

    private Drawable mDivider;

    private int mOrientation;

    DividerDecoration(Context context, int orientation) {
        final TypedArray a = context.obtainStyledAttributes(ATTRS);
        mDivider = a.getDrawable(0);
        a.recycle();
        setOrientation(orientation);
    }

    private void setOrientation(int orientation) {
        if (orientation != HORIZONTAL_LIST && orientation != VERTICAL_LIST) {
            throw new IllegalArgumentException("Invalid orientation");
        }
        mOrientation = orientation;
    }

    @Override
    public void onDraw(@NonNull Canvas c, @NonNull RecyclerView parent, @NonNull RecyclerView.State state) {
        if (mOrientation == VERTICAL_LIST) {
            drawVertical(c, parent);
        } else {
            drawHorizontal(c, parent);
        }
    }

    private void drawVertical(Canvas c, RecyclerView parent) {
        final int left = parent.getPaddingLeft();
        final int right = parent.getWidth() - parent.getPaddingRight();

        final int childCount = parent.getChildCount();
        for (int i = 0; i < childCount; i++) {
            final View child = parent.getChildAt(i);
            final RecyclerView.LayoutParams params = (RecyclerView.LayoutParams)child.getLayoutParams();
            final int top = child.getBottom() + params.bottomMargin;
            final int bottom = top + mDivider.getIntrinsicHeight();
            mDivider.setBounds(left, top, right, bottom);
            mDivider.draw(c);
        }
    }

    private void drawHorizontal(Canvas c, RecyclerView parent) {
        final int top = parent.getPaddingTop();
        final int bottom = parent.getHeight() - parent.getPaddingBottom();

        final int childCount = parent.getChildCount();
        for (int i = 0; i < childCount; i++) {
            final View child = parent.getChildAt(i);
            final RecyclerView.LayoutParams params = (RecyclerView.LayoutParams) child.getLayoutParams();
            final int left = child.getRight() + params.rightMargin;
            final int right = left + mDivider.getIntrinsicHeight();
            mDivider.setBounds(left, top, right, bottom);
            mDivider.draw(c);
        }
    }

    @Override
    public void getItemOffsets(@NonNull Rect outRect, @NonNull View view, @NonNull RecyclerView parent, @NonNull RecyclerView.State state) {
        if (mOrientation == VERTICAL_LIST) {
            outRect.set(0, 0, 0, mDivider.getIntrinsicHeight());
        } else {
            outRect.set(0, 0, mDivider.getIntrinsicWidth(), 0);
        }
    }
}
```

##### 3.6 activity_main.xml文件

```Java
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/rv"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

##### 3.7 listitem_header.xml文件

```Java
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="64dp"
    android:paddingLeft="16dp"
    android:textSize="16sp"
    android:textColor="@android:color/white"
    android:gravity="center_vertical"
    android:background="#00326F"
    tools:ignore="RtlHardcoded,RtlSymmetry" />
```

##### 3.8 listitem_normal.xml文件

```Java
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="48dp"
    android:paddingLeft="16dp"
    android:textSize="18sp"
    android:gravity="center_vertical"
    tools:ignore="RtlHardcoded,RtlSymmetry" />
```

##### 3.9 arrays.xml文件

```XML
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string-array name="animals">
        <item>Adlfjdklfgjs</item>
        <item>Adlfjdklfgjs</item>
        <item>Adlfjdklfgjs</item>
        <item>Adlfjdklfgjs</item>
        <item>Adlfjdklfgjs</item>
        <item>Adlfjdklfgjs</item>
        <item>Adlfjdklfgjs</item>
        <item>Adlfjdklfgjs</item>
        <item>Bsdlfjl</item>
        <item>Bsdlfjl</item>
        <item>Bsdlfjl</item>
        <item>Bsdlfjl</item>
        <item>Bsdlfjl</item>
        <item>Bsdlfjl</item>
        <item>Bsdlfjl</item>
        <item>Cdslfksjd</item>
        <item>Cdslfksjd</item>
        <item>Cdslfksjd</item>
        <item>Cdslfksjd</item>
        <item>Cdslfksjd</item>
        <item>Cdslfksjd</item>
        <item>Dsldfkjsdjkl</item>
        <item>Dsldfkjsdjkl</item>
        <item>Dsldfkjsdjkl</item>
        <item>Dsldfkjsdjkl</item>
        <item>Dsldfkjsdjkl</item>
        <item>Dsldfkjsdjkl</item>
    </string-array>

</resources>
```

