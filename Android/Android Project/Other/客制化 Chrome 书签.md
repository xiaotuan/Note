[toc]

### 1. Chrome Immutable Partner Bookmarks  

#### 1.1 Purpose
Starting in build M35, Chrome for Android offers the ability for partners to disable Partner Bookmarks editing when the ChromeCustomizations.apk when the enabled Immutable Partner Bookmarks setting is active on the device.

#### 1.2 References
See the [Chrome Customization APK Instructions](https://drive.google.com/a/google.com/file/d/0B373dspH0jyNYk4tTE1BUHpOek0/edit?usp=sharing) for general implementation instructions and a sample APK.
See the [Chrome Browser ­ Customizations](https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fa%2Fgoogle.com%2Fgms_distribution%2Fintegration-instructions%23TOC-Customizations&sa=D&sntz=1&usg=AFQjCNGvI45K8sKVmyQFRJgTeVuojMx_jA) section of the GMS integration instructions for other customizations available.

#### 1.3 Behavior
If the Immutable Partner Bookmarks setting is active:

+ Partner bookmarks are shown “as is” without any previously made user
  renames/removals.

+ Menu options “Rename” and “Delete” are no longer shown for the partner bookmarks.

#### 1.4 Specifications
On startup:

1. By default, partner bookmarks editing is enabled. This mode can modified by a customization APK. Please refer to the [Chrome Customization APK Instructions](https://docs.google.com/a/google.com/document/d/1ZxS0I9Qps_0k7uMNTQSsdb919JzXeVur0Fid68AxwhE/edit#) documentation for details.

2. Chrome queries:

   ```
   content://com.android.partnerbrowsercustomizations/disablebookmarksediting
   ```

   + If the provider returns the integer 1 as the first and only element in the returned cursor, partner bookmarks editing will be disabled. The “Rename” and “Remove” options will be removed from the bookmark menu.

   + If there are existing user edits (renames/removals) to the partner bookmarks, the edits will not be applied if the provider signals to Chrome that partner bookmarks editing should be disabled.

   + If the provider returns any other value, partner bookmarks editing will not be disabled.

### 2. 修改书签

#### 2.1 修改书签文件夹名称

修改 `PartnerBookmarksProvider/res/values/strings.xml` 文件中如下代码：

```xml
<string name="bookmarks_folder_name" translatable="false">Partner Bookmarks</string>
```

#### 2.2 修改书签名称

修改 `PartnerBookmarksProvider/res/values/strings.xml` 文件中如下代码：

```xml
<string-array name="bookmarks" />
```

例如：

```xml
<string-array name="bookmarks">
	<item>百度</item>
    <item>https://www.baidu.com</item>
    <item>谷歌</item>
    <item>https://www.google.com</item>
</string-array>
```



#### 2.3 修改书签图标

修改 `PartnerBookmarksProvider/res/values/bookmarks_icons.xml` 文件中如下代码：

```xml
<array name="bookmark_preloads" />
```

例如：

```xml
<array name="bookmark_preloads">
	<item>@raw/ic_baidu_favicon</item>
    <item>@raw/ic_baidu_touchicon</item>
    <item>@raw/ic_google_favicon</item>
    <item>@raw/ic_google_touchicon</item>
</array>
```

### 3. PartnerBookmarksProvider 源代码

#### 3.1 PartnerBookmarksProvider 目录结构

```
PartnerBookmarksProvider
|__ src
|	|__ com
|		|__ android
|			|__ providers
|				|__ partnerbookmarks
|					|__ PartnerBookmarksContract.java
|					|__ PartnerBookmarksProvider.java
|__ res
|	|__ values
|	|	|__ bookmarks_icons.xml
|	|	|__ strings.xml
|	|__ raw
|		|__ ic_baidu_favicon.png
|		|__ ic_baidu_touchicon.png
|		|__ ic_google_favicon.png
|   	|__ ic_google_touchicon.png
|__ Android.mk
|__ AndroidManifest.xml
```

#### 3.2  源代码

##### 3.2.1 PartnerBookmarksContract.java

```java
/*
 * Copyright (C) 2012 The Android Open Source Project
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

package com.android.providers.partnerbookmarks;

import android.content.ContentUris;
import android.net.Uri;

/**
 * <p>
 * The contract between the partner bookmarks provider and applications.
 * Contains the definition for the supported URIs and columns.
 * </p>
 * <p>
 * Authority URI: content://com.android.partnerbookmarks
 * </p>
 * <p>
 * Partner bookmarks URI: content://com.android.partnerbookmarks/bookmarks
 * </p>
 * <p>
 * If the provider is found, and the set of bookmarks is non-empty, exactly one
 * top-level folder with “parent” set to {@link #BOOKMARK_PARENT_ROOT_ID}
 * shall be provided; more than one bookmark with “parent” set to
 * {@link #BOOKMARK_PARENT_ROOT_ID} will cause the import to fail.
 * </p>
 */
public class PartnerBookmarksContract {
    /** The authority for the partner bookmarks provider */
    public static final String AUTHORITY = "com.android.partnerbookmarks";

    /** A content:// style uri to the authority for the partner bookmarks provider */
    public static final Uri AUTHORITY_URI = Uri.parse("content://" + AUTHORITY);

    /**
     * A parameter for use when querying any table that allows specifying
     * a limit on the number of rows returned.
     */
    public static final String PARAM_LIMIT = "limit";

    /**
     * A parameter for use when querying any table that allows specifying
     * grouping of the rows returned.
     */
    public static final String PARAM_GROUP_BY = "groupBy";

    /**
     * The bookmarks table, which holds the partner bookmarks.
     */
    public static final class Bookmarks {
        /**
         * This utility class cannot be instantiated.
         */
        private Bookmarks() {}

        /**
         * The content:// style URI for this table
         */
        public static final Uri CONTENT_URI = Uri.withAppendedPath(AUTHORITY_URI, "bookmarks");

        /**
         * The content:// style URI for the root partner bookmarks folder
         */
        public static final Uri CONTENT_URI_PARTNER_BOOKMARKS_FOLDER =
                Uri.withAppendedPath(CONTENT_URI, "folder");

        /**
         * Builds a URI that points to a specific folder.
         * @param folderId the ID of the folder to point to
         */
        public static final Uri buildFolderUri(long folderId) {
            return ContentUris.withAppendedId(CONTENT_URI_PARTNER_BOOKMARKS_FOLDER, folderId);
        }

        /**
         * The MIME type of {@link #CONTENT_URI} providing a directory of bookmarks.
         */
        public static final String CONTENT_TYPE = "vnd.android.cursor.dir/partnerbookmark";

        /**
         * The MIME type of a {@link #CONTENT_URI} of a single bookmark.
         */
        public static final String CONTENT_ITEM_TYPE = "vnd.android.cursor.item/partnerbookmark";

        /**
         * Used in {@link #TYPE} column and indicates the row is a bookmark.
         */
        public static final int BOOKMARK_TYPE_BOOKMARK = 1;

        /**
         * Used in {@link #TYPE} column and indicates the row is a folder.
         */
        public static final int BOOKMARK_TYPE_FOLDER = 2;

        /**
         * Used in {@link #PARENT} column and indicates the row doesn't have a parent.
         */
        public static final int BOOKMARK_PARENT_ROOT_ID = 0;

        /**
         * The type of the item.
         * <p>Type: INTEGER</p>
         * <p>Allowed values are:</p>
         * <p>
         * <ul>
         * <li>{@link #BOOKMARK_TYPE_BOOKMARK}</li>
         * <li>{@link #BOOKMARK_TYPE_FOLDER}</li>
         * </ul>
         * </p>
         */
        public static final String TYPE = "type";

        /**
         * The unique ID for a row.  Cannot be BOOKMARK_PARENT_ROOT_ID.
         * <p>Type: INTEGER (long)</p>
         */
        public static final String ID = "_id";

        /**
         * This column is valid when the row is not a folder.
         * <p>Type: TEXT (URL)</p>
         */
        public static final String URL = "url";

        /**
         * The user visible title.
         * <p>Type: TEXT</p>
         */
        public static final String TITLE = "title";

        /**
         * The favicon of the bookmark, may be NULL.
         * Must decode via {@link BitmapFactory#decodeByteArray}.
         * <p>Type: BLOB (image)</p>
         */
        public static final String FAVICON = "favicon";

        /**
         * The touch icon for the web page, may be NULL.
         * Must decode via {@link BitmapFactory#decodeByteArray}.
         * <p>Type: BLOB (image)</p>
         */
        public static final String TOUCHICON = "touchicon";

        /**
         * The ID of the parent folder. BOOKMARK_PARENT_ROOT_ID is the root folder.
         * <p>Type: INTEGER (long) (reference to item in the same table)</p>
         */
        public static final String PARENT = "parent";
    }
}
```

##### 3.2.2 PartnerBookmarksProvider.java

```java
/*
 * Copyright (C) 2012 The Android Open Source Project
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

package com.android.providers.partnerbookmarks;

import android.content.ContentProvider;
import android.content.ContentUris;
import android.content.ContentValues;
import android.content.Context;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.content.UriMatcher;
import android.content.res.Configuration;
import android.content.res.Resources;
import android.content.res.TypedArray;
import android.database.Cursor;
import android.database.DatabaseUtils;
import android.database.MatrixCursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.database.sqlite.SQLiteQueryBuilder;
import android.net.Uri;
import android.text.TextUtils;
import android.util.Log;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

/**
 * Default partner bookmarks provider implementation of {@link PartnerBookmarksContract} API.
 * It reads the flat list of bookmarks and the name of the root partner
 * bookmarks folder using getResources() API.
 *
 * Sample resources structure:
 *     res/
 *         values/
 *             strings.xml
 *                  string name="bookmarks_folder_name"
 *                  string-array name="bookmarks"
 *                      item TITLE1
 *                      item URL1
 *                      item TITLE2
 *                      item URL2...
 *             bookmarks_icons.xml
 *                  array name="bookmark_preloads"
 *                      item @raw/favicon1
 *                      item @raw/touchicon1
 *                      item @raw/favicon2
 *                      item @raw/touchicon2
 *                      ...
 */
public class PartnerBookmarksProvider extends ContentProvider {
    private static final String TAG = "PartnerBookmarksProvider";

    // URI matcher
    private static final int URI_MATCH_BOOKMARKS = 1000;
    private static final int URI_MATCH_BOOKMARKS_ID = 1001;
    private static final int URI_MATCH_BOOKMARKS_FOLDER = 1002;
    private static final int URI_MATCH_BOOKMARKS_FOLDER_ID = 1003;
    private static final int URI_MATCH_BOOKMARKS_PARTNER_BOOKMARKS_FOLDER_ID = 1004;

    private static final UriMatcher URI_MATCHER = new UriMatcher(UriMatcher.NO_MATCH);
    private static final Map<String, String> BOOKMARKS_PROJECTION_MAP
            = new HashMap<String, String>();

    // Default sort order for unsync'd bookmarks
    private static final String DEFAULT_BOOKMARKS_SORT_ORDER =
            PartnerBookmarksContract.Bookmarks.ID + " DESC, "
                    + PartnerBookmarksContract.Bookmarks.ID + " ASC";

    // Initial bookmark id when for getResources() importing
    // Make sure to fix tests if you are changing this
    private static final long FIXED_ID_PARTNER_BOOKMARKS_ROOT =
            PartnerBookmarksContract.Bookmarks.BOOKMARK_PARENT_ROOT_ID + 1;

    // DB table name
    private static final String TABLE_BOOKMARKS = "bookmarks";

    static {
        final UriMatcher matcher = URI_MATCHER;
        final String authority = PartnerBookmarksContract.AUTHORITY;
        matcher.addURI(authority, "bookmarks", URI_MATCH_BOOKMARKS);
        matcher.addURI(authority, "bookmarks/#", URI_MATCH_BOOKMARKS_ID);
        matcher.addURI(authority, "bookmarks/folder", URI_MATCH_BOOKMARKS_FOLDER);
        matcher.addURI(authority, "bookmarks/folder/#", URI_MATCH_BOOKMARKS_FOLDER_ID);
        matcher.addURI(authority, "bookmarks/folder/id",
                URI_MATCH_BOOKMARKS_PARTNER_BOOKMARKS_FOLDER_ID);
        // Projection maps
        Map<String, String> map = BOOKMARKS_PROJECTION_MAP;
        map.put(PartnerBookmarksContract.Bookmarks.ID,
                PartnerBookmarksContract.Bookmarks.ID);
        map.put(PartnerBookmarksContract.Bookmarks.TITLE,
                PartnerBookmarksContract.Bookmarks.TITLE);
        map.put(PartnerBookmarksContract.Bookmarks.URL,
                PartnerBookmarksContract.Bookmarks.URL);
        map.put(PartnerBookmarksContract.Bookmarks.TYPE,
                PartnerBookmarksContract.Bookmarks.TYPE);
        map.put(PartnerBookmarksContract.Bookmarks.PARENT,
                PartnerBookmarksContract.Bookmarks.PARENT);
        map.put(PartnerBookmarksContract.Bookmarks.FAVICON,
                PartnerBookmarksContract.Bookmarks.FAVICON);
        map.put(PartnerBookmarksContract.Bookmarks.TOUCHICON,
                PartnerBookmarksContract.Bookmarks.TOUCHICON);
    }

    private final class DatabaseHelper extends SQLiteOpenHelper {
        private static final String DATABASE_FILENAME = "partnerBookmarks.db";
        private static final int DATABASE_VERSION = 1;
        private static final String PREFERENCES_FILENAME = "pbppref";
        private static final String ACTIVE_CONFIGURATION_PREFNAME = "config";
        private final SharedPreferences sharedPreferences;

        public DatabaseHelper(Context context) {
            super(context, DATABASE_FILENAME, null, DATABASE_VERSION);
            sharedPreferences = context.getSharedPreferences(
                    PREFERENCES_FILENAME, Context.MODE_PRIVATE);
        }

        private String getConfigSignature(Configuration config) {
            return "mmc=" + Integer.toString(config.mcc)
                    + "-mnc=" + Integer.toString(config.mnc)
                    + "-loc=" + config.locale.toString();
        }

        public synchronized void prepareForConfiguration(Configuration config) {
            final SQLiteDatabase db = mOpenHelper.getWritableDatabase();
            String newSignature = getConfigSignature(config);
            String activeSignature =
                    sharedPreferences.getString(ACTIVE_CONFIGURATION_PREFNAME, null);
            if (activeSignature == null || !activeSignature.equals(newSignature)) {
                db.delete(TABLE_BOOKMARKS, null, null);
                if (!createDefaultBookmarks(db)) {
                    // Failure to read/insert bookmarks should be treated as "no bookmarks"
                    db.delete(TABLE_BOOKMARKS, null, null);
                }
            }
        }

        private void setActiveConfiguration(Configuration config) {
            Editor editor = sharedPreferences.edit();
            editor.putString(ACTIVE_CONFIGURATION_PREFNAME, getConfigSignature(config));
            editor.apply();
        }

        private void createTable(SQLiteDatabase db) {
            db.execSQL("CREATE TABLE " + TABLE_BOOKMARKS + "(" +
                    PartnerBookmarksContract.Bookmarks.ID +
                    " INTEGER NOT NULL DEFAULT 0," +
                    PartnerBookmarksContract.Bookmarks.TITLE +
                    " TEXT," +
                    PartnerBookmarksContract.Bookmarks.URL +
                    " TEXT," +
                    PartnerBookmarksContract.Bookmarks.TYPE +
                    " INTEGER NOT NULL DEFAULT 0," +
                    PartnerBookmarksContract.Bookmarks.PARENT +
                    " INTEGER," +
                    PartnerBookmarksContract.Bookmarks.FAVICON +
                    " BLOB," +
                    PartnerBookmarksContract.Bookmarks.TOUCHICON +
                    " BLOB" + ");");
        }

        private void dropTable(SQLiteDatabase db) {
            db.execSQL("DROP TABLE IF EXISTS " + TABLE_BOOKMARKS);
        }

        @Override
        public void onCreate(SQLiteDatabase db) {
            synchronized (this) {
                createTable(db);
                if (!createDefaultBookmarks(db)) {
                    // Failure to read/insert bookmarks should be treated as "no bookmarks"
                    dropTable(db);
                    createTable(db);
                }
            }
        }

        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
            dropTable(db);
            onCreate(db);
        }

        @Override
        public void onDowngrade(SQLiteDatabase db, int oldVersion, int newVersion) {
            dropTable(db);
            onCreate(db);
        }

        private boolean createDefaultBookmarks(SQLiteDatabase db) {
            Resources res = getContext().getResources();
            try {
                CharSequence bookmarksFolderName = res.getText(R.string.bookmarks_folder_name);
                final CharSequence[] bookmarks = res.getTextArray(R.array.bookmarks);
                if (bookmarks.length >= 1) {
                    if (bookmarksFolderName.length() < 1) {
                        Log.i(TAG, "bookmarks_folder_name was not specified; bailing out");
                        return false;
                    }
                    if (!addRootFolder(db,
                            FIXED_ID_PARTNER_BOOKMARKS_ROOT, bookmarksFolderName.toString())) {
                        Log.i(TAG, "failed to insert root folder; bailing out");
                        return false;
                    }
                    if (!addDefaultBookmarks(db,
                            FIXED_ID_PARTNER_BOOKMARKS_ROOT, FIXED_ID_PARTNER_BOOKMARKS_ROOT + 1)) {
                        Log.i(TAG, "failed to insert bookmarks; bailing out");
                        return false;
                    }
                }
                setActiveConfiguration(res.getConfiguration());
            } catch (android.content.res.Resources.NotFoundException e) {
                Log.i(TAG, "failed to fetch resources; bailing out");
                return false;
            }
            return true;
        }

        private boolean addRootFolder(SQLiteDatabase db, long id, String bookmarksFolderName) {
            ContentValues values = new ContentValues();
            values.put(PartnerBookmarksContract.Bookmarks.ID, id);
            values.put(PartnerBookmarksContract.Bookmarks.TITLE,
                    bookmarksFolderName);
            values.put(PartnerBookmarksContract.Bookmarks.PARENT,
                    PartnerBookmarksContract.Bookmarks.BOOKMARK_PARENT_ROOT_ID);
            values.put(PartnerBookmarksContract.Bookmarks.TYPE,
                    PartnerBookmarksContract.Bookmarks.BOOKMARK_TYPE_FOLDER);
            return db.insertOrThrow(TABLE_BOOKMARKS, null, values) != -1;
        }

        private boolean addDefaultBookmarks(SQLiteDatabase db, long parentId, long firstBookmarkId) {
            long bookmarkId = firstBookmarkId;
            Resources res = getContext().getResources();
            final CharSequence[] bookmarks = res.getTextArray(R.array.bookmarks);
            int size = bookmarks.length;
            TypedArray preloads = res.obtainTypedArray(R.array.bookmark_preloads);
            DatabaseUtils.InsertHelper insertHelper = null;
            try {
                insertHelper = new DatabaseUtils.InsertHelper(db, TABLE_BOOKMARKS);
                final int idColumn = insertHelper.getColumnIndex(
                        PartnerBookmarksContract.Bookmarks.ID);
                final int titleColumn = insertHelper.getColumnIndex(
                        PartnerBookmarksContract.Bookmarks.TITLE);
                final int urlColumn = insertHelper.getColumnIndex(
                        PartnerBookmarksContract.Bookmarks.URL);
                final int typeColumn = insertHelper.getColumnIndex(
                        PartnerBookmarksContract.Bookmarks.TYPE);
                final int parentColumn = insertHelper.getColumnIndex(
                        PartnerBookmarksContract.Bookmarks.PARENT);
                final int faviconColumn = insertHelper.getColumnIndex(
                        PartnerBookmarksContract.Bookmarks.FAVICON);
                final int touchiconColumn = insertHelper.getColumnIndex(
                        PartnerBookmarksContract.Bookmarks.TOUCHICON);

                for (int i = 0; i + 1 < size; i = i + 2) {
                    CharSequence bookmarkDestination = bookmarks[i + 1];

                    String bookmarkTitle = bookmarks[i].toString();
                    String bookmarkUrl = bookmarkDestination.toString();
                    byte[] favicon = null;
                    if (i < preloads.length()) {
                        int faviconId = preloads.getResourceId(i, 0);
                        try {
                            favicon = readRaw(res, faviconId);
                        } catch (IOException e) {
                            Log.i(TAG, "Failed to read favicon for " + bookmarkTitle, e);
                        }
                    }
                    byte[] touchicon = null;
                    if (i + 1 < preloads.length()) {
                        int touchiconId = preloads.getResourceId(i + 1, 0);
                        try {
                            touchicon = readRaw(res, touchiconId);
                        } catch (IOException e) {
                            Log.i(TAG, "Failed to read touchicon for " + bookmarkTitle, e);
                        }
                    }
                    insertHelper.prepareForInsert();
                    insertHelper.bind(idColumn, bookmarkId);
                    insertHelper.bind(titleColumn, bookmarkTitle);
                    insertHelper.bind(urlColumn, bookmarkUrl);
                    insertHelper.bind(typeColumn,
                            PartnerBookmarksContract.Bookmarks.BOOKMARK_TYPE_BOOKMARK);
                    insertHelper.bind(parentColumn, parentId);
                    if (favicon != null) {
                        insertHelper.bind(faviconColumn, favicon);
                    }
                    if (touchicon != null) {
                        insertHelper.bind(touchiconColumn, touchicon);
                    }
                    bookmarkId++;
                    if (insertHelper.execute() == -1) {
                        Log.i(TAG, "Failed to insert bookmark " + bookmarkTitle);
                        return false;
                    }
                }
            } finally {
                preloads.recycle();
                insertHelper.close();
            }
            return true;
        }

        private byte[] readRaw(Resources res, int id) throws IOException {
            if (id == 0) return null;
            InputStream is = res.openRawResource(id);
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            try {
                byte[] buf = new byte[4096];
                int read;
                while ((read = is.read(buf)) > 0) {
                    bos.write(buf, 0, read);
                }
                bos.flush();
                return bos.toByteArray();
            } finally {
                is.close();
                bos.close();
            }
        }
    }

    private DatabaseHelper mOpenHelper;

    @Override
    public boolean onCreate() {
        mOpenHelper = new DatabaseHelper(getContext());
        return true;
    }

    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        mOpenHelper.prepareForConfiguration(getContext().getResources().getConfiguration());
    }

    @Override
    public Cursor query(Uri uri, String[] projection,
            String selection, String[] selectionArgs, String sortOrder) {
        final int match = URI_MATCHER.match(uri);
        mOpenHelper.prepareForConfiguration(getContext().getResources().getConfiguration());
        final SQLiteDatabase db = mOpenHelper.getReadableDatabase();
        SQLiteQueryBuilder qb = new SQLiteQueryBuilder();
        String limit = uri.getQueryParameter(PartnerBookmarksContract.PARAM_LIMIT);
        String groupBy = uri.getQueryParameter(PartnerBookmarksContract.PARAM_GROUP_BY);
        switch (match) {
            case URI_MATCH_BOOKMARKS_FOLDER_ID:
            case URI_MATCH_BOOKMARKS_ID:
            case URI_MATCH_BOOKMARKS: {
                if (match == URI_MATCH_BOOKMARKS_ID) {
                    // Tack on the ID of the specific bookmark requested
                    selection = DatabaseUtils.concatenateWhere(selection,
                            TABLE_BOOKMARKS + "." +
                                    PartnerBookmarksContract.Bookmarks.ID + "=?");
                    selectionArgs = DatabaseUtils.appendSelectionArgs(selectionArgs,
                            new String[] { Long.toString(ContentUris.parseId(uri)) });
                } else if (match == URI_MATCH_BOOKMARKS_FOLDER_ID) {
                    // Tack on the ID of the specific folder requested
                    selection = DatabaseUtils.concatenateWhere(selection,
                            TABLE_BOOKMARKS + "." +
                                    PartnerBookmarksContract.Bookmarks.PARENT + "=?");
                    selectionArgs = DatabaseUtils.appendSelectionArgs(selectionArgs,
                            new String[] { Long.toString(ContentUris.parseId(uri)) });
                }
                // Set a default sort order if one isn't specified
                if (TextUtils.isEmpty(sortOrder)) {
                    sortOrder = DEFAULT_BOOKMARKS_SORT_ORDER;
                }
                qb.setProjectionMap(BOOKMARKS_PROJECTION_MAP);
                qb.setTables(TABLE_BOOKMARKS);
                break;
            }

            case URI_MATCH_BOOKMARKS_FOLDER: {
                qb.setTables(TABLE_BOOKMARKS);
                String[] args;
                String query;
                // Set a default sort order if one isn't specified
                if (TextUtils.isEmpty(sortOrder)) {
                    sortOrder = DEFAULT_BOOKMARKS_SORT_ORDER;
                }
                qb.setProjectionMap(BOOKMARKS_PROJECTION_MAP);
                String where = PartnerBookmarksContract.Bookmarks.PARENT + "=?";
                where = DatabaseUtils.concatenateWhere(where, selection);
                args = new String[] { Long.toString(FIXED_ID_PARTNER_BOOKMARKS_ROOT) };
                if (selectionArgs != null) {
                    args = DatabaseUtils.appendSelectionArgs(args, selectionArgs);
                }
                query = qb.buildQuery(projection, where, null, null, sortOrder, null);
                Cursor cursor = db.rawQuery(query, args);
                return cursor;
            }

            case URI_MATCH_BOOKMARKS_PARTNER_BOOKMARKS_FOLDER_ID: {
                MatrixCursor c = new MatrixCursor(
                        new String[] {PartnerBookmarksContract.Bookmarks.ID});
                c.newRow().add(FIXED_ID_PARTNER_BOOKMARKS_ROOT);
                return c;
            }

            default: {
                throw new UnsupportedOperationException("Unknown URL " + uri.toString());
            }
        }

        return qb.query(db, projection, selection, selectionArgs, groupBy, null, sortOrder, limit);
    }

    @Override
    public String getType(Uri uri) {
        final int match = URI_MATCHER.match(uri);
        if (match == UriMatcher.NO_MATCH) return null;
        return PartnerBookmarksContract.Bookmarks.CONTENT_ITEM_TYPE;
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

##### 3.2.3 bookmarks_icons.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- Copyright (C) 2012 The Android Open Source Project

     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.
-->

<resources>
    <array name="bookmark_preloads" />
</resources>
```

##### 3.2.4 strings.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- Copyright (C) 2012 The Android Open Source Project

     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.
-->

<resources xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2">
    <string name="bookmarks_folder_name" translatable="false">Partner Bookmarks</string>
    <string-array name="bookmarks" />
</resources>
```

##### 3.2.5 Android.mk

```makefile
#
# Copyright (C) 2012 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)

LOCAL_MODULE_TAGS := optional

LOCAL_STATIC_JAVA_LIBRARIES := android-common

LOCAL_SRC_FILES := $(call all-java-files-under, src)

LOCAL_PACKAGE_NAME := PartnerBookmarksProvider

include $(BUILD_PACKAGE)

# additionally, build tests in sub-folders in a separate .apk
include $(call all-makefiles-under,$(LOCAL_PATH))
```

##### 3.2.6 AndroidManifest.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
 Copyright (C) 2012 The Android Open Source Project

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.android.providers.partnerbookmarks">

    <!-- We add an application tag here just to indicate the authorities -->
    <application>
        <provider android:name="PartnerBookmarksProvider"
            android:authorities="com.android.partnerbookmarks"
                  android:exported="true" />
    </application>
    <uses-sdk android:minSdkVersion="14" android:targetSdkVersion="14" />
</manifest>
```

