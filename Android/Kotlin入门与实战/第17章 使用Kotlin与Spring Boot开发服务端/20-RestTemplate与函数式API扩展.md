### 17.9.3　RestTemplate与函数式API扩展

Kotlin具体化的类型参数为JVM泛型的类型擦除提供了一种有效的解决方法，因此Spring引入了这些扩展以便提供更好的API。例如，检索Foo对象中列表的Java代码如下。

```python
List<Foo> result = restTemplate.exchange(url, HttpMethod.GET, null, new 
ParameterizedTypeReference<List<Foo>>() { }).getBody();
```

如果采用Spring Framework 5扩展函数，则在Kotlin中可以简写为如下格式。

```python
val result: List<Foo> = restTemplate.getForObject(url)
```

