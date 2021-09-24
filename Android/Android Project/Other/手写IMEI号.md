[toc]

### 1. MTK 平台

#### 1.1 mt8766_r

通过调用 `MtkGsmCdmaPhone` 对象的 `invokeOemRilRequestRaw()` 发送写 IMEI 号的 AT 命令，IMEI 写号 AT 命令格式如下：

```
AT+EGMR=1,7,"IMEI号"
```

为了避免应用权限问题，可以将写号界面放置在 `vendor/mediatek/proprietary/packages/apps/CdsInfo` 应用中。

下面是一个写号示例代码：

```java
package com.mediatek.connectivity;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.res.Resources;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.os.AsyncResult;
import android.telephony.SubscriptionManager;
import android.text.TextUtils;
import android.util.Log;
import android.telephony.SubscriptionInfo;
import android.telephony.TelephonyManager;
import android.telephony.TelephonyManager.MultiSimVariants;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.internal.telephony.Phone;
import com.android.internal.telephony.PhoneConstants;
import com.android.internal.telephony.PhoneFactory;
import com.android.internal.util.HexDump;

import com.mediatek.internal.telephony.MtkGsmCdmaPhone;

import java.io.UnsupportedEncodingException;


public class ImeiWriterActivity extends Activity implements View.OnClickListener {

    private static final String TAG = "ImeiWriterActivity";

    private static final int EVENT_AT_CMD_DONE = 1004;

    private static final String INFO_TITLE = "Info.";

    private EditText mImeiEt;
    private Button mWriteBtn;

    private TelephonyManager mTelephonyManager;
    private Phone mGsmPhone = null;
    private Context mContext;

    private int mPhoneId = 0;
    private int mSubId = SubscriptionManager.DEFAULT_SUBSCRIPTION_ID;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_imei_writer);

        mContext = this.getBaseContext();
        mSubId = getSubId(mPhoneId);
        mTelephonyManager = new TelephonyManager(mContext, mSubId);
        mGsmPhone = PhoneFactory.getPhone(mPhoneId);

        mImeiEt = findViewById(R.id.imei);
        mWriteBtn = findViewById(R.id.write);

        mWriteBtn.setOnClickListener(this);
        mImeiEt.setText(getImei());
    }

    @Override
    public void onClick(View v) {
        String atCmdLine = "";

        String imei = mImeiEt.getText().toString().trim();
        if (TextUtils.isEmpty(imei)) {
            Toast.makeText(this, "IMEI不能为空", Toast.LENGTH_SHORT).show();
            return;
        }

        if (imei.equals(getImei())) {
            Toast.makeText(this, "IMEI与原IMEI一致", Toast.LENGTH_SHORT).show();
            return;
        }

        atCmdLine = "AT+EGMR=1,7,\"" + imei + "\"";
        atCmdLine = atCmdLine.replaceAll("\\s+","");

        Log.v(TAG , "Execute AT command:" + atCmdLine);
        sendAtCmd(atCmdLine);
    }

    void sendAtCmd(String atCmdLine) {
        try {
            byte[] rawData = atCmdLine.getBytes();
            byte[] cmdByte = new byte[rawData.length + 1];
            System.arraycopy(rawData, 0, cmdByte, 0, rawData.length);
            cmdByte[cmdByte.length - 1] = 0;
            ((MtkGsmCdmaPhone) mGsmPhone).invokeOemRilRequestRaw(cmdByte,
                    mHandler.obtainMessage(EVENT_AT_CMD_DONE));
        } catch (Exception ee) {
            ee.printStackTrace();
        }
    }

    private String getImei() {
        String imei = "";
        Resources r = getResources();

        Log.i(TAG, "updateProperties:" + mPhoneId + ":" + mSubId);

        imei = mTelephonyManager.getDeviceId(mPhoneId);

        if (imei == null) imei = r.getString(R.string.radioInfo_unknown);
        Log.d(TAG, "getImei=>imei: " + imei);
        return imei;
    }

    private void handleAtCmdResponse(AsyncResult ar) {
        if (ar.exception != null) {
            Log.i(TAG, "The response of command is failed");
            showInfo("Write IMEI failed.");
        } else {
            try {
                byte[] rawData = (byte[]) ar.result;
                Log.i(TAG, "HexDump:" + HexDump.dumpHexString(rawData));
                String txt = new String(rawData, "UTF-8");
                Log.i(TAG, "The resopnse is " + txt);
                showInfo("Write IMEI Success.");
            } catch (NullPointerException e) {
                showInfo("Write IMEI failed.");
                e.printStackTrace();
            } catch (UnsupportedEncodingException ee) {
                ee.printStackTrace();
            }
        }
    }

    private void showInfo(String info) {
        if (isFinishing()) return;
        AlertDialog.Builder infoDialog = new AlertDialog.Builder(this);
        infoDialog.setTitle(INFO_TITLE);
        infoDialog.setMessage(info);
        infoDialog.setIcon(android.R.drawable.ic_dialog_info);
        infoDialog.show();
    }

    private int getSubId(int slotId) {
        SubscriptionInfo result =
                SubscriptionManager.from(mContext).getActiveSubscriptionInfoForSimSlotIndex(slotId);

        if (result != null) {
            Log.i(TAG, "SubscriptionInfo:" + result.getSubscriptionId());
            return result.getSubscriptionId();
        }

        return SubscriptionManager.DEFAULT_SUBSCRIPTION_ID;
    }

    private Handler mHandler = new Handler() {
        public void handleMessage(Message msg) {
            AsyncResult ar;

            switch (msg.what) {
                case EVENT_AT_CMD_DONE:
                    ar = (AsyncResult) msg.obj;
                    handleAtCmdResponse(ar);
                    break;
                default:
                    break;

            }
        }
    };
}
```



