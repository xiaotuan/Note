[toc]

`RadioGroup` 控件是与 `RadioButton` 一起使用的，放在 `RadioGroup` 中的 `RadioButton` 一次只能选中其中一个 `RadioButton`。

### 1. 在 xml 中定义 RadioGroup

```xml
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
```

### 2. 在代码中使用 RadioGroup

#### 2.1 Kotlin

```Kotlin
import android.widget.RadioGroup

val radGrp = findViewById<RadioGroup>(R.id.radGrp)

val checkedRadioButtonID = radGrp.checkedRadioButtonId

radGrp.setOnCheckedChangeListener {_, id ->
    when (id) {
        -1 -> Log.v(TAG, "Choices cleared!")
        R.id.chRBtn -> Log.v(TAG, "Chose Chicken")
        R.id.fishRBtn -> Log.v(TAG, "Chose Fish")
        R.id.stkRBtn -> Log.v(TAG, "Chose Steak")
        else -> Log.v(TAG, "Huh?")
    }
}
```

#### 2.2 Java

```java
import android.widget.RadioGroup;

RadioGroup radGrp = findViewById(R.id.radGrp);

int checkedRadioButtonID = radGrp.getCheckedRadioButtonId();

radGrp.setOnCheckedChangeListener((radioGroup, id) -> {
    switch (id) {
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
});
```

