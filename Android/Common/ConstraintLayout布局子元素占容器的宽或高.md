如果希望在 `ConstraintLayout` 布局中设置子元素占满容器的宽或高可以设子元素的宽或高为0dp。例如：

```xml
 <androidx.constraintlayout.widget.ConstraintLayout
     android:layout_width="match_parent"
     android:layout_height="match_parent" >

    <LinearLayout
        android:id="@+id/status_bar"
        android:layout_width="0dp"
        android:layout_height="32dp"
        android:orientation="horizontal"
        android:gravity="center_vertical"
        android:background="@drawable/status_bar_bg"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintLeft_toLeftOf="parent">
    
    </LinearLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
```