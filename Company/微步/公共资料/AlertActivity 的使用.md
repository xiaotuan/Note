[toc]

### 1. ShowVersionActivity.java

```java
/*
 * Copyright (C) 2011 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.sprd.validationtools.secretcode;

import android.os.Build;
import android.os.Bundle;
import android.content.DialogInterface;


import com.android.internal.app.AlertActivity;
import com.android.internal.app.AlertController;
import com.sprd.validationtools.R;

public class ShowVersionActivity extends AlertActivity
        implements DialogInterface.OnClickListener {

    @Override
    public void onCreate(Bundle icicle) {
        super.onCreate(icicle);

        final AlertController.AlertParams ap = mAlertParams;
        ap.mTitle = getString(R.string.software_version_title);
        ap.mMessage = Build.DISPLAY;
        ap.mPositiveButtonText = getString(android.R.string.ok);
        ap.mNegativeButtonText = getString(android.R.string.cancel);
        ap.mPositiveButtonListener = this;
        ap.mNegativeButtonListener = this;
        setupAlert();
    }

    public void onClick(DialogInterface dialog, int which) {
        finish();
    }
}
```

> 提示：
>
> 如果需要自定视图可以使用如下方法：
>
> ```java
> LayoutInflater inflater = (LayoutInflater) getSystemService(
>                     Context.LAYOUT_INFLATER_SERVICE);
>             ap.mView = inflater.inflate(com.android.internal.R.layout.always_use_checkbox, null);
> ```

### 2. styles.xml

```xml
<style name="Theme.Dialog.Alert" parent="@*android:style/Theme.DeviceDefault.Light.Dialog.Alert" />
```

### 3. AndroidManifest.xml

```xml
<!-- show software version dialog -->
<activity android:name=".secretcode.ShowVersionActivity"
          android:exported="true"
          android:theme="@style/Theme.Dialog.Alert"
          android:finishOnCloseSystemDialogs="true"
          android:excludeFromRecents="false">
</activity>
```

