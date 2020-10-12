[toc]

### 1. 文本控件

#### 1.1 TextView

如果知道 TextView 的内容将包含一个 URL 或一个 E-mail 地址，则可以将 autoLink 属性设置为 "email|web"，该控件将找到并突出显示这些电子邮件地址和URL。而且，当用户点击这些突出显示的项时，系统将启动电子邮件应用程序向该地址发送邮件或启动浏览器来访问该 URL。在 XML 中，此特性将位于 TextView 标记内，类似于：

```xml
<TextView
	android:layout_width="match_parent"
	android:layout_height="wrap_content"
	android:autoLink="email|web"
	android:minLines="5"
	android:typeface="serif"
	android:text="Please visit www.androidbook.com for more help on using Android." />
```

 autoLink 可以设置如下属性："web"、"email"、"phone"、"map"、"none"（默认值）或"all"。如果希望在代码中而不是使用 XML 设置 autoLink 行为，相应的方法调用为 setAutoLinkMask()。

**代码清单6-6** 在 TextView 中的文本上使用 Linkify

```java
TextView tv = findViewById(R.id.tv);
tv.setAutoLinkMask(Linkify.All);
tv.setText("Please visit my website, http://www.androidbook.com or email me at davemac327@gmail.com");
```

> 请注意，必须在 TextView 设置文本之前设置自动链接选项。因为在设置文本后设置自动链接选项不会影响现有文本。

可以调用 Linkify 类的静态 addLinks() 方法，根据需要查找任何 TextView 或任何 Spannable 的内容并添加链接。无需使用 setAutoLinkMask()，我们可以在设置文本后执行以下代码：

```java
Linkify.addLinks(tv, Linkify.ALL);
```

TextView 还有许多功能需要探讨，从字体特性到 minLines 和 maxLines， 等等。

#### 1.2 EditText

EditText 最重要的特性之一是 inputType。可以将 inputType 属性设置为 textAutoCorrect 来让该控件更正常见的拼写错误。可以将它设置为 textCapWords，让控件将单词转换为大写。还有其他一些选项仅需要电话号码或密码。

通过将 singleLine 属性设置为 true，可以强制用户输入一行内容。使用 inputType，如果不知道 textMultiLine，EditText将默认为单行。

在 XML 中，可以使用 android:hint="your hint text here" 或 android:hint="@string/your_hint_name" 指定 EditText 的提示文本。

#### 1.3 AutoCompleteTextView

AutoCompleteTextView 控件是一个具有自动完成功能的 TextView。

**代码清单6-7** 使用 AutoCompleteTextView 控件

```xml
<AutoCompleteTextView
	android:id="@+id/actv"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

```java
AutoCompleteTextView actv = findViewById(R.id.actv);

ArrayAdapter<String> aa = new ArrayAdapter<>(this, 
                android.R.layout.simple_dropdown_item_1line, 
                new String[] {"English", "Hebrew", "Hindi", 
                              "Spanish", "German", "Greek"});
actv.setAdapter(aa);
```

#### 1.4 MultiAutoCompleteTextView

如果使用过 AutoCompleteTextView 控件，就会知道该控件仅为文本视图的完整文本提供建议。换句话说，如果键入一个句子，不会获得每个单词的建议。MultiAutoCompleteTextView 解决了这一问题。

使用 MultiAutoCompleteTextView 与使用 AutoCompleteTextView 类似。区别在于，使用 MutiAutoCompleteTextView 时必须告诉控件在何处再次开始建议。

**代码清单6-8** 使用 MultiAutoCompleteTextView 控件

```xml
<MultiAutoCompleteTextView
	android:id="@+id/mactv"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

```java
MultiAutoCompleteTextView mactv = findViewById(R.id.mactv);
ArrayAdapter<String> aa2 = new ArrayAdapter<String>(this,
             android.R.layout.simple_dropdown_item_1line,
             new String[] {"English", "Hebrew", "Hindi", 
                           "Spanish", "German", "Greek"});

mactv.setAdapter(aa2);

mactv.setTokenizer(new MultiAutoCompleteTextView.CommaTokenizer());
```

因为在本例中使用了 CommaTokenizer，所以在将逗号 （,）键入到 EditText 字段中之后，该字段将使用字符串数组再次给出建议。

### 2. 按钮控件

#### 2.1 Button

**代码清单6-9** 处理按钮上的单击事件

```xml
<Button
	android:id="@+id/ccbtn1"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="@string/basicBtnLabel" />
```

```java
Button btn = findViewById(R.id.ccbtn1);
btn.setOnClickListener(new OnClickListener() {
    @Override
    public void onClick(View v) {
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://www.androidbook.com"));
        startActivity(intent);
    }
});
```

**代码清单6-10** 设置按钮的单击处理程序

```xml
<Button ... android:onClick="myClickHandler" ... />
```

```java
public void myClickHandler(View target) {
    switch (target.getId()) {
        case R.id.ccbtn1:
            ...
            break;
    }
}
```

#### 2.2 ImageButton

**代码清单6-11** 使用 ImageButton

```xml
<ImageButton
	android:id="@+id/imageBtn"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:onClick="myClickHandler"
    android:src="@drawable/icon" />
```

```java
ImageButton btn = findViewById(R.id.imageBtn);
btn.setImageResource(R.drawable.icon);
```

**代码清单6-12** 为ImageButton 使用选择器

```xml
<?xml version="1.0" encoding="utf-8" ?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
	<item android:state_pressed="true"
          android:drawable="@drawable/button_pressed" /> <!-- pressed -->
    <item android:state_focused="true"
          android:drawable="@drawable/button_focused" /> <!-- focused -->
    <item android:drawable="@drawable/icon" /> <!-- default -->
</selector>
```

关于选择器文件需要注意的是按钮图像的顺序很重要。Android 将测试选择器中的每一项，查看它是否匹配。如果普通图像放在最前面，它将始终匹配并被选择，即使按钮被按下或获得焦点也是如此。当然，引用的图形对象必须位于 /res/drawables 文件夹中。最后，在布局 XML 文件中按钮的定义中，可以将 android:src 属性设置为选择器 XML 文件：

```xml
<Button ... android:src="@drawable/imagebuttonselector" ... />
```

#### 2.3 ToggleButton

ToggleButton 是一种具有两种状态的按钮。此按钮既可以处于 On（打开）状态，也可以处于 Off（关闭）状态。

**代码清单6-13** Android ToggleButton

```xml
<ToggleButton
	android:id="@+id/cctglBtn"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
  	android:text="Toggle Button"
    android:textOn="Stop"
    android:textOff="Run" />
```

因为 ToggleButton 的打开和关闭文本是独立的特性，所以不会真的使用 ToggleButton 的 Android:text 特性。

#### 2.4 CheckBox

**代码清单6-14** 创建复选框

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <CheckBox
        android:id="@+id/chickenCB"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Chicken"
        android:checked="true" />

    <CheckBox
        android:id="@+id/fishCB"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Fish" />

    <CheckBox
        android:id="@+id/steakCB"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Steak"
        android:checked="true"
        android:onClick="doClick" />

</LinearLayout>
```

可以调用 setChecked() 或 toggle() 来管理复选框的状态。可以调用isChecked() 来获取它的状态。

如果需要在选择或取消选中复选框时实现特定的逻辑，可以调用 setOnCheckedChangeListener() 并实现 onCheckedChangeListener 接口。

**代码清单6-15** 在代码中使用复选框

```java
public class CheckBoxActivity extends Activity {

    /** Called when the activity is first created. */
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.checkbox);

        CheckBox fishCB = findViewById(R.id.fishCB);

        if (fishCB.isChecked()) {
            fishCB.toggle();    // flips the checkbox to unchecked if it was checked
        }

        fishCB.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                Log.v("CheckBoxActivity", "The fish checkbox is now " + (isChecked ? "checked" : "not checked"));
            }
        });
    }

    public void doClick(View view) {
        Log.v("CheckBoxActivity", "The steak checkbox is now "
                + (((CheckBox) view).isChecked() ? "checked" : "not checked"));
    }
}
```

设置 OnCheckedChangeListener 的一个好处是它会向你传递 CheckBox 按钮的新状态。也可以使用我们对普通按钮所用的 OnClickListener 技术。

**代码清单6-16** 在代码中结合使用复选框和 android:onClick

```java
public void myClickHandler(View view) {
    switch (view.getId()) {
        case R.id.steakCB:
            ...
            break;
    }
}
```

#### 2.5 RadioButton

要在 Android 中创建一组单选按钮，首先创建 RadioGroup，然后向组中填充单选按钮。

**代码清单6-17** 使用 Android 单选按钮部件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <RadioGroup
        android:id="@+id/radGrp"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content">

        <RadioButton
            android:id="@+id/chRBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Chicken" />

        <RadioButton
            android:id="@+id/fishRBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Fish" />

        <RadioButton
            android:id="@+id/stkRBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Steak" />
        
    </RadioGroup>

</LinearLayout>
```

默认情况下，单选组内的单选按钮最初未被选中，但可以在 XML 定义中使用 android:checked 属性将其设置为选中。可以在代码中调用 setChecked() 方法设置其选中状态：

```java
RadioButton rbtn = findViewById(R.id.stkRBtn);
rbtn.setChecked(true);
```

也可以使用 toggle() 方法来切换单选按钮的状态。如果实现 onCheckedChangeListener 接口并调用 setOnCheckedChangeListener()，你将得到选中和取消选中时间的通知。

请注意，除了单选按钮以外，RadioGroup 还可以包含视图。

**代码清单6-18** 不只包含单选按钮的单选组

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <RadioButton
        android:id="@+id/anotherRadBtn"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Outside"/>

    <RadioGroup
        android:id="@+id/radGrp"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content">

        <RadioButton
            android:id="@+id/chRBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Chicken" />

        <RadioButton
            android:id="@+id/fishRBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Fish" />

        <RadioButton
            android:id="@+id/stkRBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Steak" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="My Favorite" />
    </RadioGroup>

</LinearLayout>
```

可以以编程方式操作 RadioGroup。

**代码清单6-19** 通过代码将 RadioButton 添加到 RadioGroup 中

```java
RadioGroup radGrp = findViewById(R.id.radGrp);
RadioButton newRadioBtn = new RadioButton(this);
newRadioBtn.setText("Pork");
radGrp.addView(newRadioBtn);
```

用户在单选组中选择一个单选按钮之后，无法通过再次单击来取消选择它。取消对单选组中所有单选按钮的选择的唯一方式是，以编程方式 RadioGroup 调用 clearCheck() 方法。

**代码清单6-20** 利用编程方法使用 RadioGroup

```java
public class RadioGroupActivity extends Activity {

    protected static final String TAG = "RadioGroupActivity";

    /** Called when the activity is first created. */
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.radiogroup);

        RadioGroup radGrp = findViewById(R.id.radGrp);

        int checkedRadioButtonID = radGrp.getCheckedRadioButtonId();

        radGrp.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                switch (checkedId) {
                    case -1:
                        Log.v(TAG, "Choices cleared!");
                        break;

                    case R.id.chRBtn:
                        Log.v(TAG, "Chose Chicken");
                        break;

                    case R.id.fishRBtn:
                        Log.v(TAG, "Chose Fish");
                        break;

                    case R.id.stkRBtn:
                        Log.v(TAG, "Chose Steak");
                        break;

                    default:
                        Log.v(TAG, "Huh?");
                        break;
                }
            }
        });
    }
}
```

我们始终可以使用 getCheckedRadioButtonId() 获取当前选择的 RadioButton，它返回所选项的资源 ID， 或者如果未选择任何项（可能没有默认项并且用户还未选择），返回 -1。

### 3. ImageView 控件

**代码清单6-21** XML和代码中的 ImageView

```xml
<ImageView
           android:id="@+id/image1"
           android:layout_width="wrap_content"
           android:layout_height="wrap_content"
           android:src="@drawable/icon" />

<ImageView
           android:id="@+id/image2"
           android:layout_width="125dp"
           android:layout_height="25dp"
           android:src="#555555" />

<ImageView
           android:id="@+id/image3"
           android:layout_width="wrap_content"
           android:layout_height="wrap_content" />

<ImageView
           android:id="@+id/image4"
           android:layout_width="wrap_content"
           android:layout_height="wrap_content"
           android:src="@drawable/manatee02"
           android:scaleType="centerInside"
           android:maxWidth="35dp"
           android:maxHeight="50dp" />
```

```java
ImageView imgView = findViewById(R.id.image3);

imgView.setImageResource(R.drawable.icon);

imgView.setImageBitmap(BitmapFactory.decodeResource(getResources(),
                                                    R.drawable.manatee14));

imgView.setImageDrawable(Drawable.createFromPath("/mnt/sdcard/dave2.jpg"));

imgView.setImageURI(Uri.parse("file://mnt/sdcard/dave2.jpg"));
```

### 4. 日期和时间控件

#### 4.1 DatePicker 和 TimePicker 控件

**代码清单6-22** XML中的 DatePicker 和 TimePicker 控件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/dateDefault"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

    <DatePicker
        android:id="@+id/datePicker"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

    <TextView
        android:id="@+id/timeDefault"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />

    <TimePicker
        android:id="@+id/timePicker"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

</LinearLayout>
```

**代码清单6-23** 分别使用日期和时间初始化 DatePicker 和 TimePicker

```java
@Override
protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.datetimepicker);

    TextView dateDefault = findViewById(R.id.dateDefault);
    TextView timeDefault =findViewById(R.id.timeDefault);

    DatePicker dp = findViewById(R.id.datePicker);
    // The month, and just the month, is zero-based. Add 1 for display.
    dateDefault.setText("Date defaulted to " + (dp.getMonth() + 1) + "/"
                        + dp.getDayOfMonth() + "/" + dp.getYear());
    // And here, subtract 1 from December (12) to set it to December
    dp.init(2008, 11, 10, null);

    TimePicker tp = findViewById(R.id.timePicker);

    Formatter timeF = new Formatter();
    timeF.format("Time defaulted to %d:%02d", tp.getCurrentHour(),
                 tp.getCurrentMinute());
    timeDefault.setText(timeF.toString());

    tp.setIs24HourView(true);
    tp.setCurrentHour(new Integer(10));
    tp.setCurrentMinute(new Integer(10));
}
```

#### 4.2 AnalogClock 和 DigitalClock 控件

**代码清单6-24** 在 XML 中添加 DigitalClock 和 AnalogClock

```xml
<DigitalClock
              android:layout_width="wrap_content"
              android:layout_height="wrap_content" />

<AnalogClock
             android:layout_width="match_parent"
             android:layout_height="wrap_content" />
```

这两个控件只能显示当前时间，因为它们不支持修改日期或时间。也就是说，在 DigitalClock 中显示的时间会不停地变化，在 AnalogClock 中指针会不停地转动，无需我们提供任何额外的信息。

### 5. MapView 控件

**代码清单6-25** 通过 XML 布局创建 MapView 控件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">
    
    <com.google.android.maps.MapView
    	android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:enabled="true"
        android:clickable="true"
        android:apiKey="myAPIKey" />

</LinearLayout>
```

