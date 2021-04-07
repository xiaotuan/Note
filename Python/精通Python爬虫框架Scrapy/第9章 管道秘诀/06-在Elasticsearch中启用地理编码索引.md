### 9.1.4　在Elasticsearch中启用地理编码索引

既然已经拥有了坐标位置，现在就可以做一些事情了，比如根据距离对结果进行排序。下面是一个HTTP POST请求（使用 `curl` 执行），返回标题中包含"Angel"的房产信息，并按照它们与点 `{51.54, -0.19}` 的距离进行排序。

```python
$ curl http://es:9200/properties/property/_search -d '{
　　"query" : {"term" : { "title" : "angel" } },
　　"sort": [{"_geo_distance": {
　　　　"location":　　　{"lat": 51.54, "lon": -0.19},
　　　　"order":　　　　 "asc",
　　　　"unit":　　　　　"km",
　　　　"distance_type": "plane"
}}]}'

```

唯一的问题是当尝试运行它时，会发现运行失败，并得到了一个错误信息：" `failed to find mapper for [location] for geo distance based sort` "。这说明位置字段并不是执行空间操作的适当格式。要想设置为合适的类型，则需要手动重写其默认类型。首先，将其自动检测的映射关系保存到文件中。

```python
$ curl 'http://es:9200/properties/_mapping/property' > property.txt

```

然后编辑 `property.txt` 的如下代码。

```python
"location":{"properties":{"lat":{"type":"double"},"lon":{"type":"d
ouble"}}}
```

将该行的代码修改为如下代码。

```python
"location": {"type": "geo_point"}
```

另外，我们还删除了文件尾部的 `{"properties":{"mappings": and two }}` 。对该文件的修改到此为止。现在可以按如下代码删除旧类型，使用指定的模式创建新类型。

```python
$ curl -XDELETE 'http://es:9200/properties'
$ curl -XPUT 'http://es:9200/properties'
$ curl -XPUT 'http://es:9200/properties/_mapping/property' --data
@property.txt

```

现在可以再次运行该爬虫，并且可以重新运行本节前面的 `curl` 命令，此时将会得到按照距离排序的结果。我们的搜索返回了房产信息的JSON，额外包含了一个 `sort` 字段，该字段的值是到搜索点的距离，单位为千米。

