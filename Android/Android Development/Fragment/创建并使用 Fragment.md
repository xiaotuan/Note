[toc]

### 1. Kotlin 版本

1. 创建用于显示 `Fragment` 的容器

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <FrameLayout
       xmlns:android="http://schemas.android.com/apk/res/android"
       android:id="@+id/fragment_container"
       android:layout_width="match_parent"
       android:layout_height="match_parent"/>
   ```

2. 创建 `Fragment` 对象

   **Crime.kt**

   ```kotlin
   package com.bignerdranch.android.criminalintent
   
   import java.util.Date
   import java.util.UUID
   
   data class Crime(
       val id: UUID = UUID.randomUUID(),
       var title: String = "",
       var date: Date = Date(),
       var isSolved: Boolean = false
   )
   ```

   **CrimeFragment.kt**

   ```kotlin
   package com.bignerdranch.android.criminalintent
   
   import android.os.Bundle
   import android.text.Editable
   import android.text.TextWatcher
   import android.view.LayoutInflater
   import android.view.View
   import android.view.ViewGroup
   import android.widget.Button
   import android.widget.CheckBox
   import android.widget.EditText
   import androidx.fragment.app.Fragment
   
   class CrimeFragment : Fragment() {
   
       private lateinit var crime: Crime
       private lateinit var titleField: EditText
       private lateinit var dateButton: Button
       private lateinit var solvedCheckBox: CheckBox
   
       override fun onCreate(savedInstanceState: Bundle?) {
           super.onCreate(savedInstanceState)
           crime = Crime()
       }
   
       override fun onCreateView(
           inflater: LayoutInflater,
           container: ViewGroup?,
           savedInstanceState: Bundle?
       ): View? {
           val view = inflater.inflate(R.layout.fragment_crime, container, false)
   
           titleField = view.findViewById(R.id.crime_title) as EditText
           dateButton = view.findViewById(R.id.crime_date) as Button
           solvedCheckBox = view.findViewById(R.id.crime_solved) as CheckBox
   
           dateButton.apply {
               text = crime.date.toString()
               isEnabled = false
           }
   
           return view
       }
   
       override fun onStart() {
           super.onStart()
   
           val titleWatcher = object : TextWatcher {
               override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
                   // TODO("Not yet implemented")
               }
   
               override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
                   crime.title = s.toString()
               }
   
               override fun afterTextChanged(s: Editable?) {
                   // TODO("Not yet implemented")
               }
           }
   
           titleField.addTextChangedListener(titleWatcher)
   
           solvedCheckBox.apply {
               setOnCheckedChangeListener { _, isChecked ->
                   crime.isSolved = isChecked
               }
           }
       }
   }
   ```

3. 在 `Activity` 中显示 `Fragment` 

   **MainActivity.kt**

   ```kotlin
   package com.bignerdranch.android.criminalintent
   
   import androidx.appcompat.app.AppCompatActivity
   import android.os.Bundle
   
   class MainActivity : AppCompatActivity() {
   
       override fun onCreate(savedInstanceState: Bundle?) {
           super.onCreate(savedInstanceState)
           setContentView(R.layout.activity_main)
   
           val currentFragment = supportFragmentManager.findFragmentById(R.id.fragment_container)
   
           if (currentFragment == null) {
               val fragment = CrimeFragment()
               supportFragmentManager
                   .beginTransaction()
                   .add(R.id.fragment_container, fragment)
                   .commit()
           }
       }
   }
   ```


### 2. Java 版本

1. 创建用于显示 `Fragment` 的容器

   ```xml
   <?xml version="1.0" encoding="utf-8"?>
   <FrameLayout
       xmlns:android="http://schemas.android.com/apk/res/android"
       android:id="@+id/fragment_container"
       android:layout_width="match_parent"
       android:layout_height="match_parent"/>
   ```

2. 创建 `Fragment` 对象

   **Crime.java**

   ```java
   package com.bignerdranch.android.criminalintent;
   
   import java.util.Date;
   import java.util.UUID;
   
   public class Crime {
   
       public static final UUID id = UUID.randomUUID();
   
       private String title;
       private Date date;
       private boolean isSolved;
   
       public Crime() {
           this.title = "";
           this.date = new Date();
           this.isSolved = false;
       }
   
       public Crime(String title, Date date, boolean isSolved) {
           this.title = title;
           this.date = date;
           this.isSolved = isSolved;
       }
   
       public String getTitle() {
           return title;
       }
   
       public void setTitle(String title) {
           this.title = title;
       }
   
       public Date getDate() {
           return date;
       }
   
       public void setDate(Date date) {
           this.date = date;
       }
   
       public boolean isSolved() {
           return isSolved;
       }
   
       public void setSolved(boolean solved) {
           isSolved = solved;
       }
   
       @Override
       public String toString() {
           return "Crime{" +
                   "title='" + title + '\'' +
                   ", date=" + date +
                   ", isSolved=" + isSolved +
                   '}';
       }
   }
   ```

   **CrimeFragment.java**

   ```java
   package com.bignerdranch.android.criminalintent;
   
   import android.os.Bundle;
   import android.text.Editable;
   import android.text.TextWatcher;
   import android.view.LayoutInflater;
   import android.view.View;
   import android.view.ViewGroup;
   import android.widget.Button;
   import android.widget.CheckBox;
   import android.widget.EditText;
   
   import androidx.annotation.NonNull;
   import androidx.annotation.Nullable;
   import androidx.fragment.app.Fragment;
   
   public class CrimeFragment extends Fragment {
   
       private Crime crime;
       private EditText titleField;
       private Button dateButton;
       private CheckBox solvedCheckBox;
   
       @Override
       public void onCreate(@Nullable Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           crime = new Crime();
       }
   
       @Nullable
       @Override
       public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
           View view = getLayoutInflater().inflate(R.layout.fragment_crime, container, false);
   
           titleField = view.findViewById(R.id.crime_title);
           dateButton = view.findViewById(R.id.crime_date);
           solvedCheckBox = view.findViewById(R.id.crime_solved);
   
           dateButton.setText(crime.getDate().toString());
           dateButton.setEnabled(false);
   
           return view;
       }
   
       @Override
       public void onStart() {
           super.onStart();
   
           TextWatcher titleWatcher = new TextWatcher() {
               @Override
               public void beforeTextChanged(CharSequence s, int start, int count, int after) {
                   // This space intentionally left blank
               }
   
               @Override
               public void onTextChanged(CharSequence s, int start, int before, int count) {
                   crime.setTitle(s.toString());
               }
   
               @Override
               public void afterTextChanged(Editable s) {
                   // This one too
               }
           };
   
           titleField.addTextChangedListener(titleWatcher);
   
           solvedCheckBox.setOnCheckedChangeListener((cb, isChecked) -> {
               crime.setSolved(isChecked);
           });
       }
   }
   ```

3. 在 `Activity` 中显示 `Fragment` 

   **MainActivity.java**

   ```java
   package com.bignerdranch.android.criminalintent;
   
   import androidx.appcompat.app.AppCompatActivity;
   import androidx.fragment.app.Fragment;
   
   import android.content.ComponentName;
   import android.os.Bundle;
   
   public class MainActivity extends AppCompatActivity {
   
       @Override
       protected void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           setContentView(R.layout.activity_main);
   
           Fragment currentFragment = getSupportFragmentManager().findFragmentById(R.id.fragment_container);
   
           if (currentFragment == null) {
               CrimeFragment fragment = new CrimeFragment();
               getSupportFragmentManager().beginTransaction()
                       .add(R.id.fragment_container, fragment)
                       .commit();
           }
       }
   }
   ```

   