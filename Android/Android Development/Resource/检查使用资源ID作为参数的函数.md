当函数的参数是资源 ID 时可以通过添加 `@StringRes` 注解，使 `AndroidStudio` 内置的 Lint 代码检查器可以在编译时就知道构造函数是否提供有效的资源 ID，且该注解有助于其他开发人员阅读和理解你的代码。

**1. Kotlin**

```kotlin
import androidx.annotation.StringRes

data class Question(@StringRes val textResId: Int, val answer: Boolean)
```

**2. Java**

```java
import androidx.annotation.StringRes;

public class Question {

    @StringRes
    private int textResId;
    private boolean answer;

    public Question(@StringRes int textResId, boolean answer) {
        this.textResId = textResId;
        this.answer = answer;
    }

    public int getTextResId() {
        return textResId;
    }

    public boolean getAnswer() {
        return answer;
    }
}
```

