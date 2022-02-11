[toc]

AIDL 对于非原始类型的支持如下：

+ AIDL 支持 String 和 CharSequence。
+ AIDL 支持传递其他 AIDL 接口，但你引用的每个AIDL 接口读需要一个 import 语句（即使引用的 AIDL 接口位于相同包中）。
+ AIDL 支持传递实现 `android.os.Parcelable` 接口的复杂类型。需要在 AIDL 文件中包含针对这些类型的 import 语句。

+ AIDL 支持 `java.util.List` 和 `java.util.Map`，但具有一些限制。集合中项的允许数据类型包括 Java 原始类型、String、CharSequence 或 android.os.parcelable。无需为 List 或 Map 提供 import 语句，但需要为 Parcelable 提供 import 语句。
+ 除字符串以外，非原始类型需要一个方向指示符。方向指示符包括 in、out 和 inout。in 表示值由客户端设置，out 表示值由服务设置，inout 表示客户端和服务都设置了该值。

### 1. 实现 Parcelable 接口

#### 1.1 Kotlin

```kotlin
package com.androidbook.services.stockquoteservice

import android.os.Parcel
import android.os.Parcelable

class Person(
    var age: Int = 0,
    var name: String? = null
): Parcelable {

    private constructor(data: Parcel): this() {
        readFromParcel(data)
    }

    private fun readFromParcel(data: Parcel) {
        age = data.readInt()
        name = data.readString()
    }

    override fun writeToParcel(parcel: Parcel, flags: Int) {
        parcel.writeInt(age)
        parcel.writeString(name)
    }

    override fun describeContents(): Int {
        return 0
    }

    companion object CREATOR : Parcelable.Creator<Person> {
        override fun createFromParcel(parcel: Parcel): Person {
            return Person(parcel)
        }

        override fun newArray(size: Int): Array<Person?> {
            return arrayOfNulls(size)
        }
    }
}
```

#### 1.2 Java

```java
package com.androidbook.services.stockquoteservice;

import android.os.Parcel;
import android.os.Parcelable;

public class Person implements Parcelable {

    private int age;
    private String name;

    public Person() {}

    private Person(Parcel in) {
        readFromParcel(in);
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void readFromParcel(Parcel in) {
        age = in.readInt();
        name = in.readString();
    }

    public static final Parcelable.Creator<Person> CREATOR = new Parcelable.Creator<Person>() {

        @Override
        public Person createFromParcel(Parcel source) {
            return new Person(source);
        }

        @Override
        public Person[] newArray(int size) {
            return new Person[size];
        }
    };

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeInt(age);
        dest.writeString(name);
    }
}
```

### 2. 定义 Parcelable  类的 AIDL 文件

在 aidl 目录中创建 Person.aidl 文件，文件内容如下：

```java
// Person.aidl
package com.androidbook.services.stockquoteservice;

parcelable Person;
```

### 3. 将 Parcelable 传递给服务

#### 3.1 定义 AIDL 接口

**IStockQuoteService.aidl**

```java
// This file is IStockQuoteService.aidl
package com.androidbook.services.stockquoteservice;

import com.androidbook.services.stockquoteservice.Person;

interface IStockQuoteService {
    String getQuote(in String ticker, in Person requester);
}
```

#### 3.2 实现 AIDL 接口

##### 3.2.1 Kotlin

```kotlin
package com.androidbook.services.stockquoteservice

import android.app.Service
import android.content.Intent
import android.os.IBinder
import android.util.Log

class StockQuoteService: Service() {

    override fun onBind(intent: Intent?): IBinder? {
        Log.d(TAG, "onBind() called")
        return StockQuoteServiceImpl()
    }

    override fun onCreate() {
        super.onCreate()
        Log.v(TAG, "onCreate() called")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, "onDestroy() called")
    }

    class StockQuoteServiceImpl: IStockQuoteService.Stub() {

        override fun getQuote(ticker: String?, requester: Person?): String {
            Log.v(TAG, "getQuote() called for $ticker")
            return "Hello ${requester?.name}! Quote for $ticker is 20.0"
        }

    }

    companion object {
        const val TAG = "StockQuoteService"
    }
}
```

##### 3.2.2 Java

```java
package com.androidbook.services.stockquoteservice;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.os.RemoteException;
import android.util.Log;

import androidx.annotation.Nullable;

public class StockQuoteService extends Service {

    private static final String TAG = "StockQuoteService";

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        Log.d(TAG, "onBind() called");
        return new StockQuoteServiceImpl();
    }

    @Override
    public void onCreate() {
        super.onCreate();
        Log.d(TAG, "onCreate() called");
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        Log.d(TAG, "onDestroy() called");
    }

    class StockQuoteServiceImpl extends IStockQuoteService.Stub {

        @Override
        public String getQuote(String ticker, Person requester) throws RemoteException {
            Log.v(TAG, "getQuote() called for " + ticker);
            return "Hello " + requester.name + "! Quote for " + ticker + " is 20.0";
        }

    }
}
```

