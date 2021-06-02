下面使用一个对 `ContentProvider` 进行查询，插入、删除、更新操作的示例代码：

**Kotlin 版本**

```kotlin
package com.qty.bookprovider

import android.content.ContentValues
import android.content.Context
import android.net.Uri
import android.util.Log

open class ProviderTester(
    private val mContext: Context,
    private val mReportTo: IReportBack
) {

    open fun addBook() {
        Log.d(TAG, "Adding a book")
        val cv = ContentValues()
        with(cv) {
            put(BookProviderMetaData.BookTableMetaData.BOOK_NAME, "book1")
            put(BookProviderMetaData.BookTableMetaData.BOOK_ISBN, "isbn-1")
            put(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR, "author-1")
        }

        val uri = BookProviderMetaData.BookTableMetaData.CONTENT_URI
        Log.d(TAG, "book insert uri: $uri")
        val insertedUri = mContext.contentResolver.insert(uri, cv)
        Log.d(TAG, "inserted uri: $insertedUri")
        reportString("Inserted Uri: $insertedUri")
    }

    open fun updateBook() {
        Log.d(TAG, "Update a book")
        val c = mContext.contentResolver.query(BookProviderMetaData.BookTableMetaData.CONTENT_URI,
            null,
            null,
            null,
            null)
        val count = c?.count ?: 0
        if (count > 0) {
            c?.moveToFirst()
            val updateId = c!!.getInt(c!!.getColumnIndex(BookProviderMetaData.BookTableMetaData._ID))
            val cv = ContentValues()
            with(cv) {
                put(BookProviderMetaData.BookTableMetaData.BOOK_NAME, "book2")
                put(BookProviderMetaData.BookTableMetaData.BOOK_ISBN, "isbn-2")
                put(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR, "author-2")
            }
            mContext.contentResolver.update(BookProviderMetaData.BookTableMetaData.CONTENT_URI, cv,
                "${BookProviderMetaData.BookTableMetaData._ID} = ?", arrayOf(updateId.toString()))
        } else {
            reportString("No data to update.")
            Log.d(TAG, "ContentProvider no data.")
        }
        c?.close()
    }

    open fun removeBook() {
        val i = getCount()
        val uri = BookProviderMetaData.BookTableMetaData.CONTENT_URI
        val delUri = Uri.withAppendedPath(uri, i.toString())
        reportString("Del Uri: $delUri")
        mContext.contentResolver.delete(delUri, null, null)

        reportString("Newcount: ${getCount()}")
    }

    open fun showBooks() {
        val uri = BookProviderMetaData.BookTableMetaData.CONTENT_URI
        val c = mContext.contentResolver.query(uri,
            null,
            null,
            null,
            null
        )
        if (c != null) {
            val iname = c!!.getColumnIndex(BookProviderMetaData.BookTableMetaData.BOOK_NAME)
            val iisbn = c!!.getColumnIndex(BookProviderMetaData.BookTableMetaData.BOOK_ISBN)
            val iauthor = c!!.getColumnIndex(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR)

            // Report your indexes
            reportString("name, isbn, author: $iname, $iisbn, $iauthor")

            // walk through the rows based on indexes
            while (c!!.moveToNext()) {
                // Gather values
                val id = c.getString(1)
                val name = c.getString(iname)
                val isbn = c.getString(iisbn)
                val auther = c.getString(iauthor)

                // Report or log the row
                val cbuf = StringBuffer(id)
                with(cbuf) {
                    append(",").append(name)
                    append(",").append(isbn)
                    append(",").append(auther)
                }
                reportString(cbuf.toString())
            }
        }

        // Report how many rows have been read
        val numberOfRecords = c?.count ?: 0
        reportString("Num of Records: $numberOfRecords")

        // Close the cursor
        // ideally this should be done in
        // a finally block.
        c?.close()
    }

    private fun getCount(): Int {
        val uri = BookProviderMetaData.BookTableMetaData.CONTENT_URI
        val c = mContext.contentResolver.query(uri,
            null,   // projection
            null,  // selection string
            null,   // selection args array of strings
            null,   // sort order
        )
        val count = c?.count ?: 0
        c?.close()
        return count
    }

    private fun report(stringId: Int) {
        mReportTo.reportBack(TAG, mContext.getString(stringId))
    }

    private fun reportString(s: String) {
        mReportTo.reportBack(TAG, s)
    }

    private fun reportString(s: String, stringId: Int) {
        mReportTo.reportBack(TAG, s)
        report(stringId)
    }

    companion object {
        const val TAG = "ProviderTester"
    }
}
```

**Java 版本**

```java
package com.qty.bookprovider;

import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.net.Uri;
import android.util.Log;

public class ProviderTester {

    private static final String TAG = "Provider Tester";
    private final Context mContext;
    private final IReportBack mReportTo;

    ProviderTester(Context ctx, IReportBack target) {
        mContext = ctx;
        mReportTo = target;
    }

    public void addBook() {
        Log.d(TAG, "Adding a book");
        ContentValues cv = new ContentValues();
        cv.put(BookProviderMetaData.BookTableMetaData.BOOK_NAME, "book1");
        cv.put(BookProviderMetaData.BookTableMetaData.BOOK_ISBN, "isbn-1");
        cv.put(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR, "author-1");

        ContentResolver cr = this.mContext.getContentResolver();
        Uri uri = BookProviderMetaData.BookTableMetaData.CONTENT_URI;
        Log.d(TAG, "book insert uri:" + uri);
        Uri insertedUri = cr.insert(uri, cv);
        Log.d(TAG, "inserted uri:" + insertedUri);
        this.reportString("Inserted Uri:" + insertedUri);
    }

    public void updateBook() {
        Cursor c = mContext.getContentResolver().query(BookProviderMetaData.BookTableMetaData.CONTENT_URI,
                null,
                null,
                null,
                null);
        if (c.getCount() > 0) {
            c.moveToFirst();
            int id = c.getInt(c.getColumnIndex(BookProviderMetaData.BookTableMetaData._ID));
            ContentValues cv = new ContentValues();
            cv.put(BookProviderMetaData.BookTableMetaData.BOOK_NAME, "book2");
            cv.put(BookProviderMetaData.BookTableMetaData.BOOK_ISBN, "isbn-2");
            cv.put(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR, "author-2");
            int count = mContext.getContentResolver().update(BookProviderMetaData.BookTableMetaData.CONTENT_URI,
                    cv,
                    BookProviderMetaData.BookTableMetaData._ID + " = ?",
                    new String[]{String.valueOf(id)});
            reportString("Update count: " + count);
            Log.w(TAG, "Update count: " + count);
        } else {
            reportString("No data to update.");
            Log.w(TAG, "ContentProvider no data.");
        }
        c.close();
    }

    public void removeBook() {
        int i = getCount();
        ContentResolver cr = this.mContext.getContentResolver();
        Uri uri = BookProviderMetaData.BookTableMetaData.CONTENT_URI;
        Uri delUri = Uri.withAppendedPath(uri, Integer.toString(i));
        reportString("Del Uri:" + delUri);
        cr.delete(delUri, null, null);
        this.reportString("Newcount:" + getCount());
    }

    public void showBooks() {
        Uri uri = BookProviderMetaData.BookTableMetaData.CONTENT_URI;
        Cursor c = mContext.getContentResolver().query(uri,
                null, //projection
                null, //selection string
                null, //selection args array of strings
                null); //sort order
        int iname = c.getColumnIndex(BookProviderMetaData.BookTableMetaData.BOOK_NAME);
        int iisbn = c.getColumnIndex(BookProviderMetaData.BookTableMetaData.BOOK_ISBN);
        int iauthor = c.getColumnIndex(BookProviderMetaData.BookTableMetaData.BOOK_AUTHOR);

        //Report your indexes
        reportString("name,isbn,author:" + iname + iisbn + iauthor);

        //walk through the rows based on indexes
        for (c.moveToFirst(); !c.isAfterLast(); c.moveToNext()) {
            //Gather values
            String id = c.getString(1);
            String name = c.getString(iname);
            String isbn = c.getString(iisbn);
            String author = c.getString(iauthor);

            //Report or log the row
            String cbuf = id + "," + name +
                    "," + isbn +
                    "," + author;
            reportString(cbuf);
        }

        //Report how many rows have been read
        int numberOfRecords = c.getCount();
        reportString("Num of Records:" + numberOfRecords);

        //Close the cursor
        //ideally this should be done in
        //a finally block.
        c.close();
    }

    private int getCount() {
        Uri uri = BookProviderMetaData.BookTableMetaData.CONTENT_URI;
        Cursor c = mContext.getContentResolver().query(uri,
                null, //projection
                null, //selection string
                null, //selection args array of strings
                null); //sort order
        int numberOfRecords = c.getCount();
        c.close();
        return numberOfRecords;
    }

    private void reportString(String s) {
        this.mReportTo.reportBack(TAG, s);
    }

}
```

