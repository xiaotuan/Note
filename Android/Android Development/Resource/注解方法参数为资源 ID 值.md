可以使用 `@StringRes` 、`@IdRes` 等注解，将方法参数设置为只接收指定资源 ID  值。例如：

**Kotlin**

```kotlin
package com.bignerdranch.android.geoquiz

import androidx.annotation.StringRes

data class Question(@StringRes val textResId: Int, val answer: Boolean)
```

**Java**

```java
package com.bignerdranch.android.geoquiz;

import androidx.annotation.StringRes;

public class Question {

    private int textResId;
    private boolean answer;

    public Question(@StringRes int resId, boolean answer) {
        this.textResId = resId;
        this.answer = answer;
    }

    public void setTextResId(@StringRes int resId) {
        this.textResId = resId;
    }

    public int getTextResId() {
        return textResId;
    }

    public void setAnswer(boolean answer) {
        this.answer = answer;
    }

    public boolean isAnswer() {
        return answer;
    }
}
```

