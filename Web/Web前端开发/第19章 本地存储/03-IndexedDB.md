[toc]

### 1. 存储原理

#### 1.1 数据库

数据库本身很简单，因为每个数据库都与一台计算机、一个网站或一个应用程序关联，所以不需要考虑用户关联或其他形式的访问限制，只需要指定名称和版本，数据库就处于就绪状态。数据库对象用来管理数据库中的对象，这也是获得数据库事务的唯一方法。

IndexedDB  仅具有在同一个源中执行的程序所共享的空间。在一个源所拥有的空间中可以创建多个数据库，而在一个数据库中又可以创建多个对象存储。

#### 1.2 对象与对象库

IndexedDB 提供的操作对象库的方法如下所示。

① createObjectStore(name, keyPath, autoIncrement)：用于指定属性名称和配置集合来新建一个对象库。name 属性是必须的；keyPath 属性用来声明每个对象的公共索引；autoIncrement 属性是个布尔值，用来指定对象库是否拥有一个键生成器。

② objectStore(name)：要访问对象库中的对象，必须启动一个事务，并为这个事务打开对象库，该方法打开 name 属性名称指定的对象库。

③ deleteObjectStore(name)：这个方法删除 name 属性名称指定的对象库。

只有在创建数据库或者将数据库升级到新版本的时候，才能应用 createObjectStore() 方法、deleteObjectStore() 方法，以及负责数据库配置的其他方法。

IndexedDB 操作对象的方法如下所示。

① add(object)：该方法接受关键字/值组合或包含多个关键字/值组合的对象。用得到的信息向选中的对象库添加对象。如果对象中已经存在与索引相同的对象，则 add() 方法返回错误。

② put(object)：该方法与前一个方法类似，在对象库中已经存在与索引相同的对象时，覆盖索引相同的对象.

③ get(key)：该方法可以从对象库中获取指定对象，key 属性是要获取的对象索引值。

④ delete(key)：要在选中的对象库中删除某个对象，用该对象的索引值作为属性调用该方法。

### 2. 数据操作

IndexedDB 使用异步 API，并不是这条指令执行完毕，就可以使用 request.result 来获取 IndexedDB 对象。

**案例：示例 19-04：IndexedDB 示例演示程序**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="Canvas" />
        <meta content="IndexedDB示例演示程序" />
        <title>IndexedDB示例演示程序</title>
    </head>

    <body>

    </body>
    <script type="text/javascript">
        var obj = this;
        //连接/创建数据库
        var request = indexedDB.open('myDatabase', 1.0);
        //连接数据库成功
        request.onsuccess = function (event) {
            //使之可以通过全局变量引db引用
            var db = event.target.result;
            request.onupgradeneeded = function(event) {
                //创建对象存储
                var store = db.createObjectStore('course', {
                    keyPath: '_id',
                    autoIncrement: true
                })
            }
        };

        //连接数据库失败
        request.onerror = function (event) {
            alert('连接数据库失败！');
        }

    </script>
</html>
```

#### 2.1 创建对象存储

利用 IndexedDB 属性和 open() 方法将打开指定名称的数据库，如果数据库不存在，就用指定名称新建一个数据库。连接成功后获取数据库实例 db = e.target.result；用数据库实例的 createObjectStore 方法可以创建 object store。具体代码如下所示：

```js
/**
 * 创建/打开数据库，并创建对象存储
 * @param {type} name 数据库名称
 * @param {type} version 版本信息
 * @param {type} storeName
 * @returns {undefined}
 */
function openDB(name, version, arrStoreName) {
    var version = version || 1;
    var request = window.indexedDB.open(name, version);
    request.onerror = function(e) {
        console.log(e.currentTarget.error.message);
    };
    request.onsuccess = function(e) {
        db = e.target.result;
        console.log('DB version changed to ' + version);
    };
    request.onupgradeneeded = function(e) {
        db = e.target.result;
        for (var i = 0; i < arrStoreName.length; i++) {
            var storeName = arrStoreName[i];
            if (!db.objectStoreNames.contains(storeName)) {
                var store = db.createObjectStore(storeName, {keyPath: "id"});
                store.createIndex('nameIndex', 'name', {unique: false});
            }
        }
        console.log('DB version changed to ' + version);
    };
}

openDB('studentScore', 2, ['scoreList']);
```

#### 2.2 数据写入

调用数据库实例的 transaction 方法打开事务，通过事务获取对象存储实例，再调用对象存储实例的 add 方法添加数据。具体如下所示：

```js
/**
 * 添加数据
 * @param {type} db 数据库实例
 * @param {type} storeName 对象存储名称
 * @return {undefined}
 */
function addData(db, storeName, data) {
    var transaction = db.transaction(storeName, 'readwrite');
    // 读写方式打开事务
    var store = transaction.objectStore(storeName);
    // 获取对象存储
    for (var i = 0; i < data.length; i++) {
        var request = store.add(data[i]);
        // 调用 add 方法添加数据
        request.onsuccess = function(event) {
            console.log('addData success! key', event.target.result);
        }
    }
}

function closeDB() {
    db.close();
}

var score =[
    {id: 20150001, name: "张三", sex: "男", major: "计算机科学与技术", grades: {web: 80, os: 75, network: 78, database: 80}},
    {id: 20150002, name: "王静", sex: "女", major: "计算机科学与技术", grades: {web: 80, os: 75, network: 78, database: 80}}
];
openDB('studentScore', 2, ['scoreList']);
setTimeout(function() {
    addData(db, 'scoreList', score);
    closeDB(db);
}, 100);
```

#### 2.3 数据读取

调用数据库实例的 transaction 方法打开事务，通过事务获取对象存储实例，再调用对象存储实例的 openCursor 方法打开游标，cursor.continue() 会使游标下移，直到没有数据时返回 undefined。具体代码如下：

```js
/**
 * 游标遍历对象存储
 * @param {type} db 数据库实例
 * @param {type} storeName 对象存储名称
 * @return {undefined}
 */
function fetchStoreByCursor(db, storeName) {
    var transaction = db.transaction(storeName);
    var store = transaction.objectStore(storeName);
    var request = store.openCursor();
    request.onsuccess = function(e) {
        var cursor = e.target.result;
        if (cursor) {
            var currentStudent = cursor.value;
            console.log(currentStudent);
            cursor.continue();
        }
    };
}

openDB('studentScore', 2, ['scoreList']);
setTimeout(function() {
    fetchStoreByCursor(db, 'scoreList');
    closeDB(db);
}, 100);
```

#### 2.4 数据修改

调用数据库的 transaction 方法打开事务，通过事务获取对象存储实例，再调用对象存储实例的 get 方法读取数据，修改处理后，调用 put 方法返回对象存储。具体代码如下所示：

```js
/**
 * 数据修改
 * @param {type} db
 * @param {type} storeName
 * @param {type} value 键值
 * @param {undefind}
 */
function updateDataByKey(db, storeName, key, value) {
    var transaction = db.transaction(storeName, 'readwrite');
    var store = transaction.objectStore(storeName);
    var request = store.get(key);
    request.onsuccess = function(e) {
        var student = e.target.result;
        student = value;
        store.put(student);
    };
}

/**
 * 查找数据
 * @param {type} db 数据库实例
 * @param {type} storeName 对象存储名称
 * @param {type} value 键值
 * @return {undefined}
 */
function getDataByKey(db, storeName, value) {
    var transaction = db.transaction(storeName, 'readwrite');
    var store = transaction.objectStore(storeName);
    var request = store.get(value);
    request.onsuccess = function(e) {
        var student = e.target.result;
        console.log(student);
    };
}

openDB('studentScore', 2, ['scoreList']);
setTimeout(function() {
    updateDataByKey(db, 'scoreList', 20050001, {
        id: 20050001,
        name: "张三三",
        sex: "男",
        major: "计算机科学与技术",
        grades: {
            web: 80,
            os: 75,
            network: 78,
            database: 80
        }
    });
    getDataByKey(db, 'scoreList', 20050001);
}, 100);
```

#### 2.5 数据检索

调用数据实例的 transaction 方法打开事务，通过事务获取对象存储实例，再调用对象存储实例的 delete 方法根据 key 删除对象。具体代码如下所示：

```js
/**
 * 根据键值删除记录
 * @param {type} db
 * @param {type} storeName
 * @param {type} key 键值
 * @returns {undefined}
 */
function deleteDataByKey(db, storeName, key) {
    var transaction = db.transaction(storeName, 'readwrite');
    var store = transaction.objectStore(storeName);
    store.delete(key);
}

openDB('studentScore', 2, ['scoreList']);
setTimeout(function() {
    getDataByKey(db, 'scoreList', 20050001);
    deleteDataByKey(db, 'scoreList', 20050001);
    getDataByKey(db, 'scoreList', 20050001);
}, 100);
```

#### 2.6 数据检索

##### 2.6.1 通过键值检索对象

```js
/**
 * 查找数据
 * @param {type} db 数据库实例
 * @param {type} storeName 对象存储名称
 * @param {type} value 键值
 * @return {undefined}
 */
function getDataByKey(db, storeName, value) {
    var transaction = db.transaction(storeName, 'readwrite');
    var store = transaction.objectStore(storeName);
    var request = store.get(value);
    request.onsuccess = function(e) {
        var student = e.target.result;
        console.log(student);
    };
}

openDB('studentScore', 2, ['scoreList']);
setTimeout(function() {
    getDataByKey(db, 'scoreList', 20050001);
}, 100);
```

##### 2.6.2 通过索引检索对象

```js
/**
 * 按索引读取数据
 * @param {type} db 数据库实例
 * @param {type} storeName 对象存储名称
 * @param {type} indexName 键值
 * @return {undefined}
 */
 function getDataByIndex(db, storeName, indexName) {
    var transaction = db.transaction(storeName, 'readwrite');
    var store = transaction.objectStore(storeName);
    var index = store.index("nameIndex");
    index.get(indexName).onsuccess = function(e) {
        var student = e.target.result;
        console.log(student);
    };
}

openDB('studentScore', 2, ['scoreList']);
setTimeout(function() {
    getDataByIndex(db, 'scoreList', '王静');
    closeDB();
}, 100);
```

