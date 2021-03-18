### 17.9.2　使用Kotlin调用Spring Web的功能性API

Spring Framework 5.0提供了一种更加简单的路由调用方式，可以让开发者更简单优雅地使用Kotlin代码来调用Spring的函数式 API。

```python
 ("/blog" and accept(TEXT_HTML)).route {
           GET("/", this@BlogController::findAllView)
           GET("/{slug}", this@BlogController::findOneView)
    }
    ("/api/blog" and accept(APPLICATION_JSON)).route {
           GET("/", this@BlogController::findAll)
           GET("/{id}", this@BlogController::findOne)
}
```

