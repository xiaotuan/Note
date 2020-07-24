[toc]

#### 1. 报 UNIQUE constraint failed: AUTH.\_id (code 1555) 错误的解决办法

1. 类的实现代码

```java
@Entity
public class AuthData {

    @Id(autoincrement = true)
    @Property(nameInDb = "id")
    public long dbId;
    @Property(nameInDb = "authId")
    public int id;
    public String ts;

}
```

2. 报错信息

```console
05-09 10:02:51.372 18762-18762/com.wise.gate E/WiseGate: [UpdateAuthDataHelper]onRequestAuthResponse=>error: 
    android.database.sqlite.SQLiteConstraintException: UNIQUE constraint failed: AUTH._id (code 1555)
        at android.database.sqlite.SQLiteConnection.nativeExecuteForLastInsertedRowId(Native Method)
        at android.database.sqlite.SQLiteConnection.executeForLastInsertedRowId(SQLiteConnection.java:780)
        at android.database.sqlite.SQLiteSession.executeForLastInsertedRowId(SQLiteSession.java:788)
        at android.database.sqlite.SQLiteStatement.executeInsert(SQLiteStatement.java:86)
        at org.greenrobot.greendao.AbstractDao.insertInsideTx(AbstractDao.java:368)
        at org.greenrobot.greendao.AbstractDao.executeInsert(AbstractDao.java:351)
        at org.greenrobot.greendao.AbstractDao.insert(AbstractDao.java:319)
        at com.wise.gate.helper.UpdateAuthDataHelper$2$1.run(UpdateAuthDataHelper.java:167)
        at android.os.Handler.handleCallback(Handler.java:743)
        at android.os.Handler.dispatchMessage(Handler.java:95)
        at android.os.Looper.loop(Looper.java:148)
        at android.app.ActivityThread.main(ActivityThread.java:5417)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:772)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:662)
```

3. 解决办法

将 `dbId` 属性的类型修改为 `Long` 即可。