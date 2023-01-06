[toc]

### 1. Chrome Customization APK Instructions  

#### 1.1 Purpose
This generic document complements the specific customization steps found in the [Chrome Browser](https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fa%2Fgoogle.com%2Fgms_distribution%2Fintegration-instructions%23TOC-Chrome-Browser&sa=D&sntz=1&usg=AFQjCNHmFqQjt1flTnNRtLoNuirI2vR6YA) section of the GMS integration instructions. Use the steps below to implement and test your customizations.

#### 1.2 Implementation
At launch, Chrome checks if a vendor customization APK exists for Chrome and reads the information provided by the APK.
In detail, on startup:

1. Chrome checks if the content provider
   com.android.partnerbrowsercustomizations exists and is from a system
   package, that is, having the ApplicationInfo.FLAG_SYSTEM flag.
   For example, apps installed under /system/app or /vendor/app will have this flag.

2. If it exists, Chrome queries several content URLs to read the customization information.
   For example:

   ```
   content://com.android.partnerbrowsercustomizations/homepage 
   ```

See the Content Providers documentation for background:
http://developer.android.com/guide/topics/providers/content­providers.html
Note:

+ In general, installing an APK under `/vendor/app` requires this patch to function
  correctly:
  <https://android­review.googlesource.com/#/c/80435/>

+ Before M34, the APK path should be exactly either:
  `/vendor/app/ChromeCustomizations.apk`
  or:
  `/system/app/ChromeCustomizations.apk`

+ Starting in M34, this restriction is removed as long as the APK is installed as a system package.

> **Important: **The package can have any name as long as AUTHORITY is
> `com.android.partnerbrowsercustomizations`. (For instance, you can include your organization’s name in the package to better identify it later.) It has no specific signing requirements.

#### 1.3 Example
1. Remount `/system/` as read­write.

   ```shell
   adb root && adb wait-for-device
   adb shell mount -o rw,remount /system
   ```

2. Build an example customizations content provider APK from the
   [PartnerCustomizationsProviderExample.zip](https://drive.google.com/a/google.com/file/d/0B373dspH0jyNWVg0NjhnUWhDaTQ/edit?usp=sharing):

   ```shell
   android update project --path . --name PartnerCustomizationProviderExample --target 1
   ant debug
   ```

3. Install the compiled APK:

   ```shell
   adb shell mkdir -p /system/app
   adb push bin/PartnerCustomizationProviderExample-debug.apk
   /system/app/ChromeCustomizations.apk
   ```

4. Restart Java services to ensure dex caching:

   ```shell
   adb shell stop && adb shell start
   ```

5. Start Chrome:

   ```shell
   adb shell am start -S -n com.android.chrome/.Main
   ```

6. If it worked correctly, Chrome should enable the homepage button, disable incognito mode and partner bookmark editing mode.

#### 1.4 Considerations
Because the customizations query timeout (initial minimum 500ms, max 10s) is quite generous, it is possible to perform time­consuming tasks in the provider, such as reading something on the web. However, we encourage partners to avoid placing blocking tasks in the customizations provider. If a blocking task is needed, please contact us.
­

- The Android team  

### 2. 修改 PartnerCustomizationsProvider 应用

修改 `sys/packages/providers/PartnerCustomizationsProvider/src/com/android/partnerbrowsercustomizations/PartnerBrowserCustomizationsProvider.java` 文件的如下代码：

```diff
@@ -17,7 +17,7 @@ import android.net.Uri;
 public class PartnerBrowserCustomizationsProvider extends ContentProvider {
     // "http://www.android.com/" is just an example. Please replace this to actual homepage.
     // Other strings in this class must remain as it is.
-    private static String HOMEPAGE_URI = "http://www.android.com/";
+    private static String HOMEPAGE_URI = "http://www.vortexcellular.com/";
     private static final int URI_MATCH_HOMEPAGE = 0;
     private static final int URI_MATCH_DISABLE_INCOGNITO_MODE = 1;
     private static final int URI_MATCH_DISABLE_BOOKMARKS_EDITING = 2;
```

### 3. PartnerCustomizationsProvider 应用源代码

#### 3.1 PartnerCustomizationsProvider 应用目录结构

```
PartnerCustomizationsProvider 
|__ src
|	|__ com
|		|__ android
|			|__ partnerbrowsercustomizations
|				|__ PartnerBrowserCustomizationsProvider.java
|__ Android.bp
|__ AndroidManifest.xml
|__ LICENSE
|__ proguard.flags
|__ README
```

#### 3.2 源代码

##### 3.2.1 PartnerBrowserCustomizationsProvider.java

```java
// Copyright 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Package path can be changed, but should match <manifest package="..."> in AndroidManifest.xml.
package com.android.partnerbrowsercustomizations;

import android.content.ContentProvider;
import android.content.ContentValues;
import android.content.UriMatcher;
import android.database.Cursor;
import android.database.MatrixCursor;
import android.net.Uri;

// Class name can be changed, but should match <provider android:name="..."> in
// AndroidManifest.xml.
public class PartnerBrowserCustomizationsProvider extends ContentProvider {
    // "http://www.android.com/" is just an example. Please replace this to actual homepage.
    // Other strings in this class must remain as it is.
    private static String HOMEPAGE_URI = "http://www.android.com/";
    private static final int URI_MATCH_HOMEPAGE = 0;
    private static final int URI_MATCH_DISABLE_INCOGNITO_MODE = 1;
    private static final int URI_MATCH_DISABLE_BOOKMARKS_EDITING = 2;
    private static final UriMatcher URI_MATCHER = new UriMatcher(UriMatcher.NO_MATCH);
    static {
        URI_MATCHER.addURI("com.android.partnerbrowsercustomizations", "homepage",
                URI_MATCH_HOMEPAGE);
        URI_MATCHER.addURI("com.android.partnerbrowsercustomizations", "disableincognitomode",
                URI_MATCH_DISABLE_INCOGNITO_MODE);
        URI_MATCHER.addURI("com.android.partnerbrowsercustomizations", "disablebookmarksediting",
                URI_MATCH_DISABLE_BOOKMARKS_EDITING);
    }

    @Override
    public boolean onCreate() {
        return true;
    }

    @Override
    public String getType(Uri uri) {
        // In fact, Chrome does not call this.
        // Just a recommaned ContentProvider practice in general.
        switch (URI_MATCHER.match(uri)) {
            case URI_MATCH_HOMEPAGE:
                return "vnd.android.cursor.item/partnerhomepage";
            case URI_MATCH_DISABLE_INCOGNITO_MODE:
                return "vnd.android.cursor.item/partnerdisableincognitomode";
            case URI_MATCH_DISABLE_BOOKMARKS_EDITING:
                return "vnd.android.cursor.item/partnerdisablebookmarksediting";
            default:
                return null;
        }
    }

    @Override
    public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs,
            String sortOrder) {
        switch (URI_MATCHER.match(uri)) {
            case URI_MATCH_HOMEPAGE:
            {
                MatrixCursor cursor = new MatrixCursor(new String[] { "homepage" }, 1);
                cursor.addRow(new Object[] { HOMEPAGE_URI });
                return cursor;
            }
            case URI_MATCH_DISABLE_INCOGNITO_MODE:
            {
                MatrixCursor cursor = new MatrixCursor(new String[] { "disableincognitomode" }, 1);
                cursor.addRow(new Object[] { 1 });
                return cursor;
            }
            case URI_MATCH_DISABLE_BOOKMARKS_EDITING:
            {
                MatrixCursor cursor = new MatrixCursor(
                        new String[] { "disablebookmarksediting" }, 1);
                cursor.addRow(new Object[] { 1 });
                return cursor;
            }
            default:
                return null;
        }
    }

    @Override
    public Uri insert(Uri uri, ContentValues values) {
        throw new UnsupportedOperationException();
    }

    @Override
    public int delete(Uri uri, String selection, String[] selectionArgs) {
        throw new UnsupportedOperationException();
    }

    @Override
    public int update(Uri uri, ContentValues values, String selection, String[] selectionArgs) {
        throw new UnsupportedOperationException();
    }

}
```

##### 3.2.2 AndroidManifest.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- Copyright 2013 The Chromium Authors. All rights reserved.
     Use of this source code is governed by a BSD-style license that can be
     found in the LICENSE file.
-->

<manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.android.partnerbrowsercustomizations">
    <application>
        <!--android:authorities must remain as it is. -->
        <provider android:name="PartnerBrowserCustomizationsProvider"
                android:authorities="com.android.partnerbrowsercustomizations"
				android:exported="true"
				/>
    </application>
</manifest>
```

##### 3.2.3 Android.bp

```bp
//
// Copyright (C) 2012 The Android Open Source Project
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//

android_app {
    name: "PartnerCustomizationsProvider",
    srcs: ["src/**/*.java"],
    sdk_version: "current",
    optimize: {
        proguard_flags_files: ["proguard.flags"],
    },
}
```

##### 3.2.4 LICENSE

```
// Copyright 2013 The Chromium Authors. All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are
// met:
//
//    * Redistributions of source code must retain the above copyright
// notice, this list of conditions and the following disclaimer.
//    * Redistributions in binary form must reproduce the above
// copyright notice, this list of conditions and the following disclaimer
// in the documentation and/or other materials provided with the
// distribution.
//    * Neither the name of Google Inc. nor the names of its
// contributors may be used to endorse or promote products derived from
// this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

##### 3.2.5 proguard.flags

```flags
# Needed for tests
-keep class com.android.providers.partnerbookmarks.PartnerBookmarksContract$Bookmarks {
  *;
}
```

##### 3.2.6 README

```md
# Remount /system/ as read-write.
adb root && adb wait-for-device
adb shell mount -o rw,remount /system

# Build an example customizations content provider APK.
android update project --path . --name PartnerCustomizationProviderExample --target 1
ant debug

# Install the compiled APK.
adb shell mkdir -p /system/app
adb push bin/PartnerCustomizationProviderExample-debug.apk /system/app/ChromeCustomizations.apk

# Restart Java services to ensure dex caching.
adb shell stop && adb shell start

# Start Chrome.
adb shell am start -S -n com.android.chrome/.Main

# If it worked correctly, Chrome should enable homepage button, disable incognito mode and partner bookmark editing mode.

```

