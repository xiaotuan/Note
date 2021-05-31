[toc]

### 1. 完全利用代码来构建 UI

**代码清单6-1** 完全通过代码创建简单的用户界面

```java
package com.androidbook.controls;

import android.app.Activity;
import android.os.Bundle;
import android.view.ViewGroup.LayoutParam;
import android.widget.LinearLayout;
import android.widget.TextView;

public class MainActivity extends Activity {
    
    private LinearLayout nameContainer;
    private LinearLayout addressContainer;
    private LinearLayout parentContainer;
    
    /**
     * Called when the activity is first created.
     */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        createNameContainer();
        createAddressContainer();
        createParentContainer();
        
        setContentView(parentContainer);
    }
    
    private void createNameContainer() {
        nameContainer = new LinearLayout(this);
        
        nameContainer.setLayoutParams(new LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.WRAP_CONTENT));
        nameContainer.setOrientation(LinearLayout.HORIZONTAL);
        
        TextView nameLbl = new TextView(this);
        nameLbl.setText("Name: ");
        
        TextView nameValue = new TextView(this);
        nameValue.setText("John Doe");
        
        nameContainer.addView(nameLbl);
        nameContainer.addView(nameValue);
    }
    
    private void createAddressContainer() {
        addressContainer = new LinearLayout(this);
        
        addressContainer.setLayoutParams(new LinearParams(LayoutParams.MATCH_PARENT, LayoutParams.WRAP_CONTENT));
        addressContainer.setOrientation(LinearLayout.VERTICAL);
        
        TextView addrLbl = new TextView(this);
        addrLbl.setText("Address: ");
        
        TextView addrValue = new TextView(this);
        addrValue.setText("911 Hollywood Blvd");
        
        addressContainer.addView(addrLbl);
        addressContainer.addView(addrValue);
    }
    
    private void createParentContainer() {
        parentContainer = new LinearLayout(this);
        
        parentContainer.setLayoutParems(new LayoutParams(LayoutParmas.MATCH_PARENT, LayoutParams.MATCH_PARENT));
        parentContainer.setOrientation(LinearLayout.VERTICAL);
        
        parentContainer.addView(nameContainer);
        parentContainer.addView(addressContainer);
    }
}
```

### 2. 完全使用 XML 构建 UI

**代码清单6-2** 完全在 XML中创建用户界面

```xml
<?xml version="1.0" encoding="utf-8" ?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <!-- NAME CONTAINER -->
    <LinearLayout
    	android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">
    
        <TextView
        	android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Name: " />
        
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="John Doe" />
        
    </LinearLayout>
    
    <!-- ADDRESS CONTAINER -->
    <LinearLayout
    	android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">
    
        <TextView
        	android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Address: " />
        
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:Text="911 Hollwood Blvd." />
        
    </LinearLayout>
</LinearLayout>
```

使用 XML 构建 UI 需要在 Activity 中的 onCreate() 方法中添加如下语句将 XML 设置成 Activity 的界面：

```java
setContentView(R.layout.main);
```

### 3. 使用 XML 结合代码构建 UI

**代码清单6-3** 在 XML 中使用 ID 创建用户界面

```xml
<?xml version="1.0" encoding="utf-8" ?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
	android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <!-- NAME CONTAINER -->
    <LinearLayout
    	android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">
    
        <TextView
        	android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/name_text" />
        
        <TextView
            android:id="@+id/nameValue"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content" />
        
    </LinearLayout>
    
    <!-- ADDRESS CONTAINER -->
    <LinearLayout
    	android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">
    
        <TextView
        	android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/addr_text" />
        
        <TextView
            android:id="@+id/addrValue"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content" />
        
    </LinearLayout>
</LinearLayout>
```

**代码清单6-4** 代码清单6-3的strings.xml文件

```xml
<?xml version="1.0" encoding="utf-8" ?>
<resources>
	<string name="app_name">Common Controls</string>
    <string name="name_text">"Name: "</string>
    <string name="addr_text">"Address: "</string>
</resources>
```

**代码清单6-5** 在运行时引用资源中的控件

```java
setContentView(R.layout.main);

TextView nameValue = findViewById(R.id.nameValue);
nameValue.setText("John Doe");
TextView addrValue = findViewById(R.id.addrValue);
addrValue.setText("911 Hollywood Blvd.");
```

