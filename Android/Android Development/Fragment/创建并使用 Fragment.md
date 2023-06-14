[toc]

### 1. 创建并使用 Fragment  的步骤

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

   