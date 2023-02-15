首先，我们需要创建一个继承 `ViewModel` 的类。在该类中，如果需要在该类销毁时做一些善后清理工作，比如解绑某个数据项，这时我们可以覆写 `onCleared()` 方法，该方法会在该类销毁前调用。

**Kotlin**

```kotlin
package com.bignerdranch.android.geoquiz

import android.util.Log
import androidx.lifecycle.ViewModel

class QuizViewModel: ViewModel() {

    var currentIndex = 0

    private val questionBank = listOf(
        Question(R.string.question_australia, true),
        Question(R.string.question_oceans, true),
        Question(R.string.question_mideast, false),
        Question(R.string.question_africa, false),
        Question(R.string.question_americas, true),
        Question(R.string.question_asia, true)
    )

    val currentQuestionAnswer: Boolean
        get() = questionBank[currentIndex].answer

    val currentQuestionText: Int
        get() = questionBank[currentIndex].textResId

    fun moveToNext() {
        currentIndex = (currentIndex + 1) % questionBank.size
    }

    override fun onCleared() {
        super.onCleared()
        Log.d(TAG, "onCleared=>ViewModel instance about to be destroyed")
    }

    companion object {
        const val TAG = "QuizViewModel"
    }
}
```

**Java**

```java
package com.bignerdranch.android.geoquizj;

import android.util.Log;

import androidx.lifecycle.ViewModel;

public class QuizViewModel extends ViewModel {

    private static final String TAG = "QuizViewModel"

    int currentIndex = 0;

    private Question[] questionBank = new Question[] {
            new Question(R.string.question_australia, true),
            new Question(R.string.question_oceans, true),
            new Question(R.string.question_mideast, false),
            new Question(R.string.question_africa, false),
            new Question(R.string.question_americas, true),
            new Question(R.string.question_asia, true)
    };

    boolean getCurrentQuestionAnswer() {
        return questionBank[currentIndex].getAnswer();
    }

    int getCurrentQuestionText() {
        return questionBank[currentIndex].getTextResId();
    }

    void moveToNext() {
        currentIndex = (currentIndex + 1) % questionBank.length;
    }

    @Override
    protected void onCleared() {
        super.onCleared();
        Log.d(TAG, "onCleared=>ViewModel instance about to be destroyed");
    }
}
```

然后，在 `Activity` 的 `onCreate()` 方法中将 `ViewModel` 和 `Activity` 关联起来：

**Kotlin**

```kotlin
package com.bignerdranch.android.geoquiz

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider

private const val TAG = "MainActivity"

class MainActivity : AppCompatActivity() {

    private lateinit var trueButton: Button
    private lateinit var falseButton: Button
    private lateinit var nextButton: Button
    private lateinit var questionTextView: TextView

    private val quizViewModel: QuizViewModel by lazy {
        ViewModelProvider(this)[QuizViewModel::class.java]
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        trueButton = findViewById(R.id.true_button)
        falseButton = findViewById(R.id.false_button)
        nextButton = findViewById(R.id.next_button)
        questionTextView = findViewById(R.id.question_text_view)

        trueButton.setOnClickListener { view: View ->
            checkAnswer(true)
        }

        falseButton.setOnClickListener { view: View ->
            checkAnswer(false)
        }

        nextButton.setOnClickListener{
            quizViewModel.moveToNext()
            updateQuestion()
        }

        updateQuestion()
    }

    private fun updateQuestion() {
        val questionTextResId = quizViewModel.currentQuestionText
        questionTextView.setText(questionTextResId)
    }

    private fun checkAnswer(userAnswer: Boolean) {
        val correctAnswer = quizViewModel.currentQuestionAnswer
        val messageResId = if (userAnswer == correctAnswer) {
            R.string.correct_toast
        } else {
            R.string.incorrect_toast
        }
        Toast.makeText(this, messageResId, Toast.LENGTH_SHORT).show()
    }
}
```

**Java**

```java
package com.bignerdranch.android.geoquizj;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private Button trueButton;
    private Button falseButton;
    private Button nextButton;
    private TextView questionTextView;

    private QuizViewModel quizViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        quizViewModel = new ViewModelProvider(this).get(QuizViewModel.class);

        trueButton = findViewById(R.id.true_button);
        falseButton = findViewById(R.id.false_button);
        nextButton = findViewById(R.id.next_button);
        questionTextView = findViewById(R.id.question_text_view);

        trueButton.setOnClickListener(v -> {
            checkAnswer(true);
        });

        falseButton.setOnClickListener(v -> {
            checkAnswer(false);
        });

        nextButton.setOnClickListener(v -> {
            quizViewModel.moveToNext();
            updateQuestion();
        });

        updateQuestion();
    }

    private void updateQuestion() {
        int questionTextResId = quizViewModel.getCurrentQuestionText();
        questionTextView.setText(questionTextResId);
    }

    private void checkAnswer(boolean userAnswer) {
        boolean correctAnswer = quizViewModel.getCurrentQuestionAnswer();
        int messageResId = R.string.incorrect_toast;
        if (userAnswer == correctAnswer) {
            messageResId = R.string.correct_toast;
        }
        Toast.makeText(this, messageResId, Toast.LENGTH_SHORT).show();
    }
}
```

