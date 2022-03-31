下面是需要实现 AppWidgetProvider 类的方法：

```java
import android.appwidget.AppWidgetManager;
import android.appwidget.AppWidgetProvider;
import android.content.Context;

public class BDayWidgetProvider extends AppWidgetProvider {

    @Override
    public void onUpdate(Context context, AppWidgetManager appWidgetManager, int[] appWidgetIds) {
        super.onUpdate(context, appWidgetManager, appWidgetIds);
    }

    @Override
    public void onDeleted(Context context, int[] appWidgetIds) {
        super.onDeleted(context, appWidgetIds);
    }

    @Override
    public void onEnabled(Context context) {
        super.onEnabled(context);
    }

    @Override
    public void onDisabled(Context context) {
        super.onDisabled(context);
    }
}

```

+ `onEnabled()` ：该回调方法表明至少有一个部件实例在主屏幕上运行。
+ `onDeleted()`：当用户将部件实例视图拖到回收站时，将调用该回调方法。
+ `onUpdate()`：当计时器过期时会调用 `onUpdate()` 回调方法。如果没有配置器活动，那么在首次创建部件实例时，也会调用此方法。
+ `onDisabled()`：从主屏幕上删除了最后一个部件实例之后，将调用该回调方法。