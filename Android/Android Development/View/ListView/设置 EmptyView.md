给 `ListView` 设置 `EmptyView` 代码如下：

**Java**

```java
ViewGroup emptyView=(ViewGroup) View.inflate(getActivity(), R.layout.empty_layout, null);
emptyView.setLayoutParams(new LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT));
emptyView.setVisibility(View.GONE);
((ViewGroup)mListView.getParent()).addView(emptyView); 
mListView.setEmptyView(emptyView);
```

**Kotlin**

```kotlin
val emptyView = layoutInflater.inflate(R.layout.empty_list_view, null)
emptyView.layoutParams = ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT)
emptyView.visibility = View.GONE
listView = findViewById(R.id.apk_list)
(listView.parent as ViewGroup).addView(emptyView)
listView.emptyView = emptyView
```



