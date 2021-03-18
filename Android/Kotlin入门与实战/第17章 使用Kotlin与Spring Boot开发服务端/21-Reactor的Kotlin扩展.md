### 17.9.4　Reactor的Kotlin扩展

Reactor是Spring Framework 5.0附带的响应式框架。利用这一特性，在开发响应式Web应用程序时，可以很好地与Mono、Flux以及StepVerifier API等框架进行融合。

现在，通过reactor-kotlin扩展项目Reactor引入了Kotlin支持，它可以通过foo.toMono()方式来创建Mono实例的扩展，当然也有很多人倾向于通过Mono.just(foo)的方式。同时，它还支持通过stream.toFlux()方式从Java 8的Stream实例中创建Flux。

