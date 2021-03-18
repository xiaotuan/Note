[toc]

### 3.4.4　Redis缓存实现

现在，我们已经准备好使用与之前 `DiskCache` 类相同的类接口构建Redis缓存了。

```python
import json
from datetime import timedelta
from redis import StrictRedis
class RedisCache:
    def __init__(self, client=None, expires=timedelta(days=30),
encoding='utf-8'):
        # if a client object is not passed then try
        # connecting to redis at the default localhost port
        self.client = StrictRedis(host='localhost', port=6379, db=0)
            if client is None else client
        self.expires = expires
        self.encoding = encoding
    def __getitem__(self, url):
        """Load value from Redis for the given URL"""
        record = self.client.get(url)
        if record:
            return json.loads(record.decode(self.encoding))
        else:
            raise KeyError(url + ' does not exist')
    def __setitem__(self, url, result):
        """Save value in Redis for the given URL"""
        data = bytes(json.dumps(result), self.encoding)
        self.client.setex(url, self.expires, data)
```

这里的 `__getitem__` 和 `__setitem__` 方法与前一节中关于如何在Redis中获取及设置键的讨论很相似，不过在这里我们使用了 `json` 模块控制序列化，并使用了 `setex` 方法，能够使我们在设置键值时附带过期时间。 `setex` 既可以接受 `datetime.timedelta` ，也可以接受以秒为单位的数值。这是一个非常方便的Redis功能，可以在指定秒数后自动删除记录。这就意味着我们不再需要像 `DiskCache` 类那样手工检查记录是否在我们的过期规则内。让我们使用20秒的时间差在IPython中进行尝试，观察缓存过期。

```python
In [1]: from chp3.rediscache import RedisCache
In [2]: from datetime import timedelta
In [3]: cache = RedisCache(expires=timedelta(seconds=20))
In [4]: cache['test'] = {'html': '...', 'code': 200}
In [5]: cache['test']
Out[5]: {'code': 200, 'html': '...'}
In [6]: import time; time.sleep(20)
In [7]: cache['test']
----------------------------------------------------------------------
KeyError Traceback (most recent call last)
...
KeyError: 'test does not exist'
```

结果显示我们的缓存可以按照预期工作，可以在JSON、字典和Redis键值对存储间进行序列化和反序列化操作，并且能够对结果进行过期处理。

