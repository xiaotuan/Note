上层执行 `system/bin` 目录下的可执行 bin 文件是通过 `ProcessBuilder` 类实现的，执行方法如下：

```java
ProcessBuilder pb = new ProcessBuilder("memtester", size, totalTimes);
```

其中 `memtester` 为可执行 bin 文件的名称，`size` 和 `totalTimes` 是传递给可执行文件的参数。

然后调用 `ProcessBuilder` 类的 `start()` 方法开始执行该可执行文件。

```java
pb.redirectErrorStream(true);
Process process = pb.start();
```

最后通过 `Process` 类的 `getInputStream()` 方法获取可执行 bin 文件执行时的输出信息：

```java
try (BufferedReader br = new BufferedReader(new InputStreamReader(mTestProcess.getInputStream()))) {
        while(true) {
            String line = br.readLine();
            Log.d(TAG, "doInBackground=>line: " + line);
            if (line == null) {
                break;
            } else {
                publishProgress(line);
                mRamTestManager.collectTestReportLine(line);
            }
        }
    } catch (Exception e) {
        Log.e(TAG, "doInBackground=>error: ", e);
    }
} catch (Exception e) {
    Log.e(TAG, "doInBackground=>error: ", e);
} finally {
    if (mTestProcess != null) {
        mTestProcess.destroy();
    }
}
```

下面是一个完成的示例代码：

```java
package com.weibu.memorytest;

import android.app.Activity;
import android.app.ActivityManager;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Handler;
import android.os.SystemClock;
import android.text.SpannableString;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.view.WindowManager;
import android.view.animation.CycleInterpolator;
import android.view.animation.TranslateAnimation;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.Chronometer;
import android.widget.EditText;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Timer;
import java.util.TimerTask;

public class RamTestActivity extends Activity implements View.OnClickListener, RamTestManager.RamTestResultListener {

    private static final String TAG = "RamTestActivity";

    private SharedPreferences mSp;

    private double mAvailableRamSize = 0.0d;
    private RamTestTask mCurrentTestTask = null;
    private TextView mFinalResult;
    private TextView mFreeRamSizeTextView;
    private boolean mIsFromAgingTest = false;
    private boolean mIsTestOngoing = false;
    private boolean mIsUserTryToEditSize = false;
    private TextView mMaxTestSizeTextView;
    private int mPreserveRamSize = 500;
    private RamTestManager mRamTestManager;
    private TextView mResultTextView;
    private ScrollView mScrollView;
    private Button mStartStopBtn;
    private EditText mTestRamSize;
    private Chronometer mTimeCounter;
    private double mTotalRamSize = 0.0d;
    private EditText mTotalTestTimes;
    private Timer mUpdateFreeRamSizeTimer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mPreserveRamSize = getResources().getInteger(R.integer.default_preserve_ram_size);
        mRamTestManager = new RamTestManager(this);
        mSp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);

        mFreeRamSizeTextView = findViewById(R.id.free_ram_text);
        mMaxTestSizeTextView = findViewById(R.id.max_ram_text_size);
        mResultTextView = findViewById(R.id.result_text_view);
        mScrollView = findViewById(R.id.result_container);
        mTestRamSize = findViewById(R.id.test_ram_size);
        mTotalTestTimes = findViewById(R.id.test_times);
        mStartStopBtn = findViewById(R.id.start_stop_btn);
        mStartStopBtn.setOnClickListener(this);
        mTimeCounter = findViewById(R.id.time_counter);
        mFinalResult = findViewById(R.id.test_state);
        mResultTextView.setText(getString(R.string.test_tips, mPreserveRamSize + ""));
        mTestRamSize.setOnClickListener(v -> mIsUserTryToEditSize = true);

        showLastTestReport();
        handleStartIntent();
    }

    @Override
    protected void onResume() {
        super.onResume();
        updateFreeRamSizeDisplay();
        scheduleUpdateTaskTimer();
        updateUiOnTestStateChange(isTestOnGoing());
    }

    @Override
    protected void onPause() {
        super.onPause();
        cancelUpdateTaskTimer();
        if (mIsTestOngoing) {
            saveResultOnAppExit();
        }
    }

    @Override
    protected void onStop() {
        if (mCurrentTestTask != null && mCurrentTestTask.getStatus() != AsyncTask.Status.FINISHED) {
            mCurrentTestTask.forceCancel();
            mCurrentTestTask.cancel(true);
            mCurrentTestTask = null;
        }
        super.onStop();
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.start_stop_btn:
                if (isTestOnGoing()) {
                    mCurrentTestTask.forceCancel();
                    mCurrentTestTask.cancel(true);
                    mCurrentTestTask = null;
                } else if (validateTestParams()) {
                    mIsTestOngoing = true;
                    if (mRamTestManager != null) {
                        mRamTestManager.registerListener(this);
                        mRamTestManager.onTestStart();
                    }
                    mCurrentTestTask = new RamTestTask();
                    mCurrentTestTask.execute(getTestParams()[0] + "M", String.valueOf(getTestParams()[1]));
                    saveParamsOnTestStart();
                }
                break;
        }
    }

    @Override
    public void onTestFailDetected() {
        if (mCurrentTestTask != null && mCurrentTestTask.getStatus() != AsyncTask.Status.FINISHED) {
            mCurrentTestTask.forceCancel();
        }
    }

    private void showLastTestReport() {
        SpannableString report = mRamTestManager.getLastTestReport();
        if (!TextUtils.isEmpty(report)) {
            mResultTextView.setText(report);
        }
    }

    private void handleStartIntent() {
        mIsFromAgingTest = getIntent().getBooleanExtra("from_auto_aging_test", false);
        if (this.mIsFromAgingTest) {
            new Handler().postDelayed(() -> {
                if (mStartStopBtn != null) {
                    mStartStopBtn.performClick();
                }
            }, 2500);
        }
    }

    private void updateFreeRamSizeDisplay() {
        ActivityManager.MemoryInfo mi = getMemoryInfo();
        double availableMegs = (double) (mi.availMem / 1048576);
        double totalMegs = (double) (mi.totalMem / 1048576);
        double percentAvail = (availableMegs / totalMegs) * 100.0d;
        mAvailableRamSize = availableMegs;
        mTotalRamSize = totalMegs;
        if (mFreeRamSizeTextView != null) {
            mFreeRamSizeTextView.setText(availableMegs + " / " + totalMegs + " (" + String.format("%.2f", Double.valueOf(percentAvail)) + "%)");
        }
        if (mMaxTestSizeTextView != null) {
            mMaxTestSizeTextView.setText("(<" + String.format("%.0f", Double.valueOf(availableMegs - ((double) mPreserveRamSize))) + ")");
        }
        if (!mIsUserTryToEditSize && (!mIsTestOngoing) && mTestRamSize != null) {
            mTestRamSize.setText("" + ((int) ((availableMegs - ((double) mPreserveRamSize)) - 50.0d)));
        }
    }

    private void scheduleUpdateTaskTimer() {
        cancelUpdateTaskTimer();
        final Runnable updateFreeRamRunnable = () -> updateFreeRamSizeDisplay();
        TimerTask timerTask = new TimerTask() {
            public void run() {
                runOnUiThread(updateFreeRamRunnable);
            }
        };
        mUpdateFreeRamSizeTimer = new Timer();
        mUpdateFreeRamSizeTimer.schedule(timerTask, 0, 1000);
    }

    private void updateUiOnTestStateChange(boolean isTestStarted) {
        int i;
        int color;
            if (mTestRamSize != null) {
                mTestRamSize.setEnabled(!isTestStarted);
            }
            if (mTotalTestTimes != null) {
                mTotalTestTimes.setEnabled(!isTestStarted);
            }
            if (mStartStopBtn != null) {
                Button button = mStartStopBtn;
                if (isTestStarted) {
                    i = R.string.btn_text_stop;
                } else {
                    i = R.string.btn_text_start;
                }
                button.setText(i);
                Button button2 = mStartStopBtn;
                if (isTestStarted) {
                    color = getResources().getColor(R.color.btn_bg_red, null);
                } else {
                    color = getResources().getColor(R.color.btn_bg_green, null);
                }
                button2.setBackgroundColor(color);
            }
            if (mTimeCounter != null) {
                if (isTestStarted) {
                    mTimeCounter.setBase(SystemClock.elapsedRealtime());
                    mTimeCounter.start();
                } else {
                    mTimeCounter.stop();
                }
            }
            if (mScrollView != null) {
                mScrollView.fullScroll(130);
            }
    }

    private boolean isTestOnGoing() {
        return mIsTestOngoing;
    }

    private void cancelUpdateTaskTimer() {
        if (mUpdateFreeRamSizeTimer != null) {
            mUpdateFreeRamSizeTimer.cancel();
            mUpdateFreeRamSizeTimer = null;
        }
    }

    private void saveResultOnAppExit() {
        mSp.edit().putString("last_test_duration", mTimeCounter.getText().toString()).commit();
        mRamTestManager.saveTestResultOnAppExit();
    }

    private boolean validateTestParams() {
        int[] params = getTestParams();
        int size = params[0];
        int total = params[1];
        Log.i(TAG, "validateTestParams=>mAvailableRamSize: " + mAvailableRamSize + " , "
                + (mAvailableRamSize - ((double) mPreserveRamSize)));
        if (size <= 0) {
            Toast.makeText(this, (int) R.string.toast_text_params_invalid, Toast.LENGTH_SHORT).show();
            mTestRamSize.startAnimation(getShakeErrorAnimation());
            return false;
        } else if (((double) size) >= mAvailableRamSize - ((double) mPreserveRamSize)) {
            Toast.makeText(this, getString(R.string.toast_text_ram_size_too_large,
                    mPreserveRamSize + ""), Toast.LENGTH_SHORT).show();
            mTestRamSize.startAnimation(getShakeErrorAnimation());
            return false;
        } else if (total > 0) {
            return true;
        } else {
            Toast.makeText(this, R.string.toast_text_params_invalid, Toast.LENGTH_SHORT).show();
            mTotalTestTimes.startAnimation(getShakeErrorAnimation());
            return false;
        }
    }

    private void saveParamsOnTestStart() {
        mSp.edit().putString("last_test_ram_size", "" + getTestParams()[0] + " M")
                .putString("last_test_loop", "" + getTestParams()[1])
                .putString("last_test_free_ram_size", mAvailableRamSize + " M")
                .putString("last_test_total_ram_size", mTotalRamSize + " M")
                .putString("last_test_finish_loop", "")
                .putString("last_test_duration", "")
                .putString("last_test_result", "").commit();
    }

    private int[] getTestParams() {
        int size = 0;
        int total = 0;
        try {
            size = Integer.parseInt(mTestRamSize.getText().toString());
            total = Integer.parseInt(mTotalTestTimes.getText().toString());
        } catch (NumberFormatException e) {
            Log.e(TAG, "getTestParams=>error: ", e);
        }
        return new int[]{size, total};
    }

    private ActivityManager.MemoryInfo getMemoryInfo() {
        ActivityManager.MemoryInfo mi = new ActivityManager.MemoryInfo();
        ((ActivityManager) getSystemService(ACTIVITY_SERVICE)).getMemoryInfo(mi);
        return mi;
    }

    private TranslateAnimation getShakeErrorAnimation() {
        TranslateAnimation shake = new TranslateAnimation(0.0f, 5.0f, 0.0f, 0.0f);
        shake.setDuration(500);
        shake.setInterpolator(new CycleInterpolator(7.0f));
        return shake;
    }

    private void setShowKeyboard(boolean shouldShow) {
        InputMethodManager imm = (InputMethodManager) getSystemService(INPUT_METHOD_SERVICE);
        if (shouldShow) {
            imm.toggleSoftInput(2, 1);
        } else {
            imm.hideSoftInputFromWindow(getWindow().getDecorView().getWindowToken(), 0);
        }
    }

    private void onTestFinish() {
        mRamTestManager.removeListener();
        updateTestFinalResult(mRamTestManager.getTestResult());
        saveResultSummary();
    }

    private void updateTestFinalResult(String result) {
        String resultText;
        Log.i(TAG, "getTestResult: " + result);
        if (result.equals("PASS")) {
            resultText = getString(R.string.test_result_success);
        } else if (result.equals("FAIL")) {
            resultText = getString(R.string.test_result_fail);
        } else if (result.equals("CANCEL")) {
            resultText = getString(R.string.test_result_cancel);
        } else {
            resultText = result;
        }
        if (this.mFinalResult != null) {
            this.mFinalResult.setText(resultText);
            if ("PASS".equals(result)) {
                this.mFinalResult.setBackgroundColor(getResources().getColor(R.color.btn_bg_green, null));
            } else {
                this.mFinalResult.setBackgroundColor(getResources().getColor(R.color.btn_bg_red, null));
            }
        }
    }

    private void saveResultSummary() {
        mSp.edit().putString("last_test_duration", mTimeCounter.getText().toString()).commit();
        mRamTestManager.saveTestResult();
    }

    public class RamTestTask extends AsyncTask<String, String, Boolean> {

        private Process mTestProcess;

        public void onPreExecute() {
            setShowKeyboard(false);
            if (mResultTextView != null) {
                mResultTextView.setText("");
            }
            if (mFinalResult != null) {
                mFinalResult.setText("");
                mFinalResult.setBackgroundColor(0);
            }
            updateUiOnTestStateChange(true);
            mIsTestOngoing = true;
        }

        @Override
        protected Boolean doInBackground(String... strings) {
            String size = strings[0];
            String totalTimes = strings[1];
            Log.d(TAG, "doInBackground=>size: " + size + ", totalTimes: " + totalTimes);
            try {
                ProcessBuilder pb = new ProcessBuilder("memtester", size, totalTimes);
                pb.redirectErrorStream(true);
                mTestProcess = pb.start();
                try (BufferedReader br = new BufferedReader(new InputStreamReader(mTestProcess.getInputStream()))) {
                    while(true) {
                        String line = br.readLine();
                        Log.d(TAG, "doInBackground=>line: " + line);
                        if (line == null) {
                            break;
                        } else {
                            publishProgress(line);
                            mRamTestManager.collectTestReportLine(line);
                        }
                    }
                } catch (Exception e) {
                    Log.e(TAG, "doInBackground=>error: ", e);
                }
            } catch (Exception e) {
                Log.e(TAG, "doInBackground=>error: ", e);
            } finally {
                if (mTestProcess != null) {
                    mTestProcess.destroy();
                }
            }
            return true;
        }

        public void onProgressUpdate(String... values) {
            if (mResultTextView != null) {
                mResultTextView.append(values[0] + "\n");
            }
            if (mScrollView != null) {
                mScrollView.fullScroll(130);
            }
        }

        public void onPostExecute(Boolean result) {
            updateUiOnTestStateChange(false);
            mIsTestOngoing = false;
            if (mRamTestManager != null) {
                mRamTestManager.onTestDone();
                onTestFinish();
            }
        }

        public void onCancelled() {
            updateUiOnTestStateChange(false);
            mIsTestOngoing = false;
            if (mRamTestManager != null) {
                mRamTestManager.onTestCancel();
                onTestFinish();
            }
        }

        public void forceCancel() {
            if (mTestProcess != null) {
                mTestProcess.destroy();
                publishProgress("\n" + getString(R.string.test_cancelled_text));
            }
        }
    }
}
```



