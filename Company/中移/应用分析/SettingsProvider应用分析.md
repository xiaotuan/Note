在 SettingsProvider 应用中的主要修改点有两处，一处是数据库初始化的改动，一处是应用启动时的改动。

数据库初始化的改动主要是用于插入新的数据或者更改默认值。具体修改代码位于 src/com/android/providers/settings/DatabaseHelper.java 文件。它是在 loadSettings() 方法中添加一个自定义的方法来处理该操作：

```java
private void loadSettings(SQLiteDatabase db) {
    loadSystemSettings(db);
    loadSecureSettings(db);
    // The global table only exists for the 'owner' user
    if (mUserHandle == UserHandle.USER_OWNER) {
        loadGlobalSettings(db);
    }
    loadSWSetting(db);
}
```

下面是 loadSettings() 方法的代码：

```java
private void loadSWSetting(SQLiteDatabase db){
    SQLiteStatement systemInsertStmt = null;
    SQLiteStatement secureInsertStmt = null;
    SQLiteStatement globalInsertStmt = null;
    SQLiteStatement systemUpdateStmt = null;
    SQLiteStatement secureUpdateStmt = null;
    SQLiteStatement globalUpdateStmt = null;

    String table = null;
    String line = null;
    BufferedReader br = null;
    FileReader fr = null;
    FileInputStream fis = null;

    try{
        File f = new File("/system/etc/swdefaultparam.txt");
        if(f.exists()){
            fr = new FileReader(f);
            br = new BufferedReader(fr);
            while((line = br.readLine()) != null){
                if(line.startsWith("#")){
                    Log.d(TAG, "the params [" + line + "] is valid!");
                    continue;
                }
                if(line.toLowerCase().trim().equals("[system]")){
                    table = "system";
                    systemInsertStmt = db.compileStatement("INSERT OR IGNORE INTO system(name, value)" + " VALUES(?,?);");
                    systemUpdateStmt = db.compileStatement("UPDATE system SET value = ? where name = ?;");
                    continue;
                }
                if(line.toLowerCase().trim().equals("[secure]")){
                    table = "secure";
                    secureInsertStmt = db.compileStatement("INSERT OR IGNORE INTO secure(name, value)" + " VALUES(?,?);");
                    secureUpdateStmt = db.compileStatement("UPDATE secure SET value = ? where name = ?;");
                    continue;
                }
                if(line.toLowerCase().trim().equals("[global]")){
                    table = "global";
                    globalInsertStmt = db.compileStatement("INSERT OR IGNORE INTO global(name, value)" + " VALUES(?,?);");
                    globalUpdateStmt = db.compileStatement("UPDATE global SET value = ? where name = ?;");
                    continue;
                }
                if(!line.contains("=")){
                    Log.d(TAG, "the params [" +line+ "] is valid !");
                    continue;
                }

                String[] params = line.split("=");
                String name = null;
                String value = null;

                if(params.length >= 2){
                    //这里需要考虑兼容参数值里有"="等号的情况
                    if(params[0].trim().length() == 0){
                        Log.d(TAG, "the params [" + line + "] is wrong !!!!");
                        continue;
                    } else if(params.length == 2) {
                        name = params[0];
                        value = params[1];
                    } else {
                        name = params[0];
                        value = line.substring(params[0].length()+1);
                    }
                }else if(params.length == 1){
                    if(params[0] != null && params[0].trim().length() > 0){
                        name = params[0];
                        value = "";
                    }else{
                        Log.d(TAG, "the params [" + line + "] is wrong !!!!");
                        continue;
                    }
                }else{
                    Log.d(TAG, "the params [" + line +"] is wrong !!!!");
                    continue;
                }

                Log.d(TAG, "the params [" + line + "] is valid!");
                if(table.equals("system")){
                    String dbValue = getStringValueFromTable(db, table, name, null);
                    if(dbValue == null){
                        loadSetting(systemInsertStmt, name, value);
                    }else{
                        loadSetting(systemUpdateStmt, value, name);
                    }
                }

                if(table.equals("secure")){
                    String dbValue = getStringValueFromTable(db, table, name, null);
                    if(dbValue == null){
                        loadSetting(secureInsertStmt, name, value);
                    }else{
                        loadSetting(secureUpdateStmt, value, name);
                    }
                }

                if(table.equals("global")){
                    String dbValue = getStringValueFromTable(db, table, name, null);
                    if(dbValue == null){
                        loadSetting(globalInsertStmt, name, value);
                    }else{
                        loadSetting(globalUpdateStmt, value, name);
                    }
                }
            }
        }else{
            Log.d(TAG, "the system/etc/swdefaultparam.txt does not exit !!!!!!");
        }

    }catch(Exception e){
        e.printStackTrace();
    }finally{
        if(systemInsertStmt != null) systemInsertStmt.close();
        if(secureInsertStmt != null) secureInsertStmt.close();
        if(globalInsertStmt != null) globalInsertStmt.close();
        if(systemUpdateStmt != null) systemUpdateStmt.close();
        if(secureUpdateStmt != null) secureUpdateStmt.close();
        if(globalUpdateStmt != null) globalUpdateStmt.close();
        if(br != null){
            try{
                br.close();
                fr.close();
            }catch(Exception e){
                e.printStackTrace();
            }
        }

    }
}
```

在 loadSettings() 方法中，主要通过 /system/etc/swdefaultparam.txt 文件内容来更新数据库，在该文件中包含了 system、secure 和 global 表中要更新新的数据。如果数据项已经存在，则通过 UpdateStmt 的 SQLiteStatement 对象来更新；如果数据项不存在，则通过 systemInsertStmt 的 SQLiteStatement 对象来插入新数据。

应用启动时进行的改动，主要是根据 /system/etc/swupgradeparam.txt 和 /data/swupgradeparameters.txt 文件内容进行修改的。具体修改代码位于 src/com/android/providers/settings/SettingsProvider.java 文件中。

它是通过在 establishDbTracking() 方法中调用 updateSWParams() 自定义方法来处理的。而 establishDbTracking() 方法又会在 onCreate() 和 getOrEstablishDatabase() 方法中被调用。getOrEstablishDatabase() 方法主要用于获取 DatabaseHelper 对象，当 DatabaseHelper 对象获取失败的时候，会调用 establishDbTracking() 方法来初始化 DatabaseHelper 对象，而在初始化 DatabaseHelper  对象的同时会触发 updateSWParams() 方法的调用。下面是 establishDbTracking() 方法的代码：

```java
private void establishDbTracking(int userHandle) {
    if (LOCAL_LOGV) {
        Slog.i(TAG, "Installing settings db helper and caches for user " + userHandle);
    }

    DatabaseHelper dbhelper;

    while (!mDatabaseLockable) {
        Slog.i(TAG, "establishDbTracking waiting");
        SystemClock.sleep(1000);
    }
    synchronized (this) {
        dbhelper = mOpenHelpers.get(userHandle);
        if (dbhelper == null) {
            dbhelper = new DatabaseHelper(getContext(), userHandle);
            mOpenHelpers.append(userHandle, dbhelper);

            sSystemCaches.append(userHandle, new SettingsCache(TABLE_SYSTEM));
            sSecureCaches.append(userHandle, new SettingsCache(TABLE_SECURE));
            sKnownMutationsInFlight.append(userHandle, new AtomicInteger(0));
        }
    }

    // Initialization of the db *outside* the locks.  It's possible that racing
    // threads might wind up here, the second having read the cache entries
    // written by the first, but that's benign: the SQLite helper implementation
    // manages concurrency itself, and it's important that we not run the db
    // initialization with any of our own locks held, so we're fine.
    SQLiteDatabase db = dbhelper.getWritableDatabase();

    //add by zhanghuagang
    try {
        updateSWParams(db);// android4.0该段代码要放到onCreate方法的return true前
    }catch(Exception e){
        e.printStackTrace();
    }
    //add by zhanghuagang end


    // Watch for external modifications to the database files,
    // keeping our caches in sync.  We synchronize the observer set
    // separately, and of course it has to run after the db file
    // itself was set up by the DatabaseHelper.
    synchronized (sObserverInstances) {
        if (sObserverInstances.get(userHandle) == null) {
            SettingsFileObserver observer = new SettingsFileObserver(userHandle, db.getPath());
            sObserverInstances.append(userHandle, observer);
            Slog.v(TAG, " start observer watching");
            observer.startWatching();
        }
    }

    ensureAndroidIdIsSet(userHandle);

    startAsyncCachePopulation(userHandle);
}
```

updateSWParams() 方法的代码如下：

```java
private void updateSWParams(SQLiteDatabase db) {
    SQLiteStatement systemInsertStmt = null;
    SQLiteStatement secureInsertStmt = null;
    SQLiteStatement globalInsertStmt = null; // android4.0不需要这行
    SQLiteStatement systemUpdateStmt = null;
    SQLiteStatement secureUpdateStmt = null;
    SQLiteStatement globalUpdateStmt = null; // android4.0不需要这行
    String table = null;
    BufferedReader br = null;
    FileReader fr = null;
    BufferedReader omdbr = null;
    boolean isUpgrade = false;
    try {
        File f = new File("/system/etc/swupgradeparam.txt");
        if (f.exists()) {
            SystemProperties.set("persist.sys.report.mdownload", "true");
            fr = new FileReader(f);
            br = new BufferedReader(fr);
            String line = null;
            String versionValue = null;
            while ((line = br.readLine()) != null) {
                if (line.startsWith("#")) {
                    Log.d(TAG, "the params [" + line + " ]is valid!");
                    continue;
                }
                if (line.toLowerCase().trim().equals("[version]")) {
                    table = "version";
                    secureInsertStmt = db.compileStatement("INSERT OR IGNORE INTO secure(name,value)" + " VALUES(?,?);");
                    secureUpdateStmt = db.compileStatement("UPDATE secure SET value = ? where name = ?;");
                    continue;
                }
                if (line.toLowerCase().trim().equals("[system]")) {
                    table = "system";
                    systemInsertStmt = db.compileStatement("INSERT OR IGNORE INTO system(name,value)" + " VALUES(?,?);");
                    systemUpdateStmt = db.compileStatement("UPDATE system SET value = ? where name = ?;");
                    continue;
                }
                if (line.toLowerCase().trim().equals("[secure]")) {
                    table = "secure";
                    secureInsertStmt = db.compileStatement("INSERT OR IGNORE INTO secure(name,value)" + " VALUES(?,?);");
                    secureUpdateStmt = db.compileStatement("UPDATE secure SET value = ? where name = ?;");
                    continue;
                }
                // android4.0不需要下面if语句
                if (line.toLowerCase().trim().equals("[global]")) {
                    table = "global";
                    globalInsertStmt = db.compileStatement("INSERT OR IGNORE INTO global(name,value)" + " VALUES(?,?);");
                    globalUpdateStmt = db.compileStatement("UPDATE global SET value = ? where name = ?;");
                    continue;
                }
                if (!line.contains("=")) {
                    Log.d(TAG, "the params [" + line + " ]is valid!");
                    continue;
                }
                String[] params = line.split("=");
                String name = null;
                String value = null;

                if (params.length >= 2) {
                    //这里需要考虑兼容参数值里有"="等号的情况
                    if (params[0].trim().length() == 0) {
                        Log.d(TAG, "the params [" + line + " ]is wrong!!!!!!!");
                        continue;
                    } else if(params.length == 2) {
                        name = params[0];
                        value = params[1];
                    } else {
                        name = params[0];
                        value = line.substring(params[0].length()+1);
                    }
                } else if (params.length == 1) {
                    if (params[0] != null && params[0].trim().length() > 0) {
                        name = params[0];
                        value = "";
                    } else {
                        Log.d(TAG, "the params [" + line + "] is wrong!!!!!!!");
                        continue;
                    }
                } else {
                    Log.d(TAG, "the params [" + line + "] is wrong!!!!!!!");
                    continue;
                }
                if (table.equals("version")) {
                    String dbVersion = getStringValueFromTable(db, "secure", name, null);
                    Log.d(TAG, "the dbVerion is " + dbVersion + " the swupgradeparam.txt version is " + value);
                    if (dbVersion != null && dbVersion.equals(value)) {
                        Log.d(TAG, "dbVerion=" + dbVersion + " the swupgradeparam.txt  version is " + value + " the version is the same , do nothing!");
                        return;
                    } else {
                        versionValue = value;
                    }
                    isUpgrade = true;
                    continue;
                }
                if (!isUpgrade) {
                    return;
                }
                if (table.equals("system")) {
                    String dbValue = getStringValueFromTable(db, table, name, null);
                    if (dbValue == null) {
                        loadSetting(systemInsertStmt, name, value);
                    } else {
                        loadSetting(systemUpdateStmt, value, name);
                    }
                }
                if (table.equals("secure")) {
                    String dbValue = getStringValueFromTable(db, table, name, null);
                    if (dbValue == null) {
                        loadSetting(secureInsertStmt, name, value);
                    } else {
                        loadSetting(secureUpdateStmt, value, name);
                    }
                }
                // android4.0不需要下面if语句
                if (table.equals("global")) {
                    String dbValue = getStringValueFromTable(db, table, name, null);
                    if (dbValue == null) {
                        loadSetting(globalInsertStmt, name, value);
                    } else {
                        loadSetting(globalUpdateStmt, value, name);
                    }
                }
            }
            if (isUpgrade && versionValue != null) {
                String dbVersion = getStringValueFromTable(db, "secure", "version", null);
                if (dbVersion == null) {
                    loadSetting(secureInsertStmt, "version", versionValue);
                } else {
                    loadSetting(secureUpdateStmt, versionValue, "version");
                }
            }
        } else {
            Log.d(TAG, "the /system/etc/swupgradeparam.txt does not exist!!!!!!");

        }

        File omdFile = new File("/data/swupgradeparameters.txt");
        if(omdFile.exists()){
            FileReader omdfr = new FileReader(omdFile);
            omdbr = new BufferedReader(omdfr);
            String line = null;
            while((line = omdbr.readLine()) != null){
                if(line.startsWith("#")){
                    Log.d(TAG, "the params [" + line + "] is valid!");
                    continue;
                }
                if(line.toLowerCase().trim().equals("[system]")){
                    table = "system";
                    systemInsertStmt = db.compileStatement("INSERT OR IGNORE INTO system(name, value)" + " VALUES(?,?);");
                    systemUpdateStmt = db.compileStatement("UPDATE system SET value = ? where name = ?;");
                    continue;
                }
                if(line.toLowerCase().trim().equals("[secure]")){
                    table = "secure";
                    secureInsertStmt = db.compileStatement("INSERT OR IGNORE INTO secure(name, value)" + " VALUES(?,?);");
                    secureUpdateStmt = db.compileStatement("UPDATE secure SET value = ? where name = ?;");
                    continue;
                }
                if(line.toLowerCase().trim().equals("[global]")){
                    table = "global";
                    globalInsertStmt = db.compileStatement("INSERT OR IGNORE INTO global(name, value)" + " VALUES(?,?);");
                    globalUpdateStmt = db.compileStatement("UPDATE global SET value = ? where name = ?;");
                    continue;
                }
                if(!line.contains("=")){
                    Log.d(TAG, "the params [" +line+ "] is valid !");
                    continue;
                }

                String[] params = line.split("=");
                String name = null;
                String value = null;

                if(params.length >= 2){
                    //这里需要考虑兼容参数值里有"="等号的情况
                    if(params[0].trim().length() == 0){
                        Log.d(TAG, "the params [" + line + "] is wrong !!!!");
                        continue;
                    } else if(params.length == 2) {
                        name = params[0];
                        value = params[1];
                    }
                    else {
                        name = params[0];
                        value = line.substring(params[0].length()+1);
                    }
                }else if(params.length == 1){
                    if(params[0] != null && params[0].trim().length() > 0){
                        name = params[0];
                        value = "";
                    }else{
                        Log.d(TAG,"the params["+line+"] is wrong !!!!");
                        continue;
                    }
                }else{
                    Log.d(TAG, "the params [" + line +"] is wrong !!!!");
                    continue;
                }

                if(table.equals("system")){
                    String dbValue = getStringValueFromTable(db, table, name, null);
                    if(dbValue == null){
                        loadSetting(systemInsertStmt, name, value);
                    }else{
                        loadSetting(systemUpdateStmt,value,name);
                    }
                }

                if(table.equals("secure")){
                    String dbValue = getStringValueFromTable(db, table, name, null);
                    if(dbValue == null){
                        loadSetting(secureInsertStmt,name, value);
                    }else{
                        loadSetting(secureUpdateStmt,value,name);
                    }
                }

                if(table.equals("global")){
                    String dbValue = getStringValueFromTable(db, table, name, null);
                    if(dbValue == null){
                        loadSetting(globalInsertStmt,name,value);
                    }else{
                        loadSetting(globalUpdateStmt,value,name);
                    }
                }
            }

            /**备份长虹的系统属性相关数据
				**	休眠功能设置
				**/
            String mStbManu = SystemProperties.get("ro.stb.manu");
            if("ch".equals(mStbManu)){
                String name = "", value = "";
                String suspend_enable = SystemProperties.get("persist.sys.ch.hdmi.suspend", "unknown");
                if("1".equals(suspend_enable)){
                    value = "1";
                }else {
                    value = "-1";
                }
                name = "standby_by_hdmi";
                String dbValue = getStringValueFromTable(db, "secure", name, null);
                if(dbValue == null){
                    loadSetting(secureInsertStmt, name, value);
                }else{
                    loadSetting(secureUpdateStmt, value, name);
                }

                String suspend_noop = SystemProperties.get("persist.sys.suspend.noop", "unknown");
                if("true".equals(suspend_noop)){
                    value = "1";
                }else {
                    value = "-1";
                }
                name = "standby_by_key";
                dbValue = getStringValueFromTable(db, "secure", name, null);
                if(dbValue == null){
                    loadSetting(secureInsertStmt, name, value);
                }else{
                    loadSetting(secureUpdateStmt, value, name);
                }

            }


        }else{
            Log.d(TAG, "the /data/swupgradeparameters.txt does not exit !!!!!!");

        }
    } catch (Exception e) {
        e.printStackTrace();
    } finally {
        if (systemInsertStmt != null)
            systemInsertStmt.close();
        if (secureInsertStmt != null)
            secureInsertStmt.close();
        if (globalInsertStmt != null)
            globalInsertStmt.close(); // android4.0不需要这行
        if (systemUpdateStmt != null)
            systemUpdateStmt.close();
        if (secureUpdateStmt != null)
            secureUpdateStmt.close();
        if (globalUpdateStmt != null)
            globalUpdateStmt.close();// android4.0不需要这行
        if (br != null) {
            try {
                br.close();
                fr.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        if (omdbr != null) {
            try {
                omdbr.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
```

