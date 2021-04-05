### 第3步：加载JSON数据并输出天气

`response.text` 成员变量保存了一个JSON格式数据的大字符串。要将它转换为Python值，就调用 `json.loads()` 函数。JSON数据会像这样：

```javascript
{'city': {'coord': {'lat': 37.7771, 'lon': -122.42},
          'country': 'United States of America',
          'id': '5391959',
          'name': 'San Francisco',
          'population':  0},
 'cnt': 3,
 'cod': '200',
 'list': [{'clouds': 0,
           'deg': 233,
           'dt': 1402344000,
           'humidity': 58,
           'pressure': 1012.23,
           'speed': 1.96,
           'temp': {'day': 302.29,
                    'eve': 296.46,
                    'max': 302.29,
                    'min': 289.77,
                    'morn': 294.59,
                    'night': 289.77},
           'weather': [{'description': 'sky is clear',
                        'icon': '01d',
--snip--
```

可以将 `weatherData` 传入 `pprint.pprint()` 以查看这个数据。你可能要进入OpenWeather官网，找到关于这些字段含义的文档。例如，在线文档会告诉你， `'day'` 后面的 `302.29` 是白天的开尔文温度，而不是摄氏或华氏温度。

你想要的天气描述在 `'main'` 和 `'description'` 之后。为了输出整齐，在getOpenWeather.py中添加以下代码：

```javascript
   ! python3
   # getOpenWeather.py - Prints the weather for a location from the command line.
   --snip--
   # Load JSON data into a Python variable.
   weatherData = json.loads(response.text)
   # Print weather descriptions.
❶  w = weatherData['list']
   print('Current weather in %s:' % (location)) 
   print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description']) 
   print()
   print('Tomorrow:')
   print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description']) 
   print()
   print('Day after tomorrow:')
   print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
```

请注意，代码将 `weatherData['list']` 保存在变量 `w` 中，这将节省一些打字时间❶。可以用 `w[0]` 、 `w[1]` 和 `w[2]` 来取得今天、明天和后天天气的字典。这些字典都有 `'weather'` 键，其中包含一个列表值。你感兴趣的是第一个表项（一个嵌套的字典，包含几个键），其索引是0。这里，我们输出保存在 `'main'` 和 `'description'` 键中的值，用连字符隔开。

如果用命令行参数 `getOpenWeather.py San Francisco, CA` 运行这个程序，那么输出结果看起来是这样的：

```javascript
Current weather in San Francisco, CA: 
Clear - sky is clear
Tomorrow:
Clouds - few clouds
Day after tomorrow:
Clear - sky is clear
```

（天气是我喜欢住在旧金山的原因之一！）

