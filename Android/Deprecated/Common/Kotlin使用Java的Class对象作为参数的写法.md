**Java的写法**

```java
private static void showDialog(Activity activity, Class clazz, String tag) {
    FragmentManager fm = activity.getFragmentManager();
    FragmentTransaction ft = fm.beginTransaction();
    Fragment prev = fm.findFragmentByTag(tag);
    if (prev != null) {
        ft.remove(prev);
    }
    ft.addToBackStack(null);

    try {
        ((DialogFragment) clazz.newInstance()).show(ft, tag);
    } catch (InstantiationException | IllegalAccessException e) {
        e.printStackTrace();
    }
}
```

**Kotlin的写法**

```kotlin
fun showDialog(activity: FragmentActivity, clazz: Class<*>, tag: String) {
    val fm = activity.supportFragmentManager
    val ft = fm.beginTransaction()
    val prev = fm.findFragmentByTag(tag)
    if (prev != null) {
        ft.remove(prev)
    }
    ft.addToBackStack(null)
    try {
        (clazz.newInstance() as androidx.fragment.app.DialogFragment).show(ft, tag)
    } catch (e: InstantiationException) {
        e.printStackTrace()
    } catch (e: IllegalAccessException) {
        e.printStackTrace()
    }
}
```

