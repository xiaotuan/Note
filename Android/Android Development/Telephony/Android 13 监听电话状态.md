Android 12 后，PhoneStateListener 类已过时，Android 推荐使用 TelephonyCallback 类进行监听电话状态：

```java
package com.android.factorytest.telephony;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.telephony.CellInfo;
import android.telephony.PhoneStateListener;
import android.telephony.ServiceState;
import android.telephony.SignalStrength;
import android.telephony.TelephonyCallback;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.TextView;

import com.android.factorytest.Constaint;
import com.android.factorytest.FactoryTestApp;
import com.android.factorytest.R;
import com.android.factorytest.State;
import com.android.factorytest.TestItem;

import java.util.List;

public class SimTest extends Activity {

    private static final String TAG = "SimTest";

    private TelephonyManager mTelephonyManager;
    private TelephoneListener mCallback;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.sim_test);
        getActionBar().setDisplayHomeAsUpEnabled(true);
		
        mCallback = new TelephoneListener();
        mTelephonyManager = (TelephonyManager) getSystemService(TELEPHONY_SERVICE);
    }

    @Override
    protected void onResume() {
        super.onResume();
        mTelephonyManager.registerTelephonyCallback(getMainExecutor(), mCallback);
    }

    @Override
    protected void onPause() {
        super.onPause();
        mTelephonyManager.unregisterTelephonyCallback(mCallback);
    }

    @Override
    public boolean onMenuItemSelected(int featureId, MenuItem item) {
        if (item.getItemId() == android.R.id.home) {
            finish();
            return true;
        }
        return super.onMenuItemSelected(featureId, item);
    }

    private class TelephoneListener extends TelephonyCallback implements
            TelephonyCallback.SignalStrengthsListener,
            TelephonyCallback.ServiceStateListener,
            TelephonyCallback.DataConnectionStateListener {

        @Override
        public void onServiceStateChanged(ServiceState serviceState) {
            serviceState.get
        }

        @Override
        public void onSignalStrengthsChanged(SignalStrength signalStrength) {

        }

        @Override
        public void onDataConnectionStateChanged(int state, int networkType) {

        }
    };
}
```

