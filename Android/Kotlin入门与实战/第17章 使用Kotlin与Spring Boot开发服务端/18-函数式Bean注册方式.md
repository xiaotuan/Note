### 17.9.1　函数式Bean注册方式

Spring Framework 5.0引入了一种全新的Bean注册方式，即用Lambda表达式来替代传统的XML注册或者使用@Configuration和@BeanJavaConfig注解方式来注册Bean。它使用Supplier Lambda表达式充当FactoryBean，从而简化Bean的注册。例如，在GenericApplicationContext中注册Bean实体类，使用Java编写的代码如下。

```python
GenericApplicationContext context = new GenericApplicationContext();
context.registerBean(Foo.class);
context.registerBean(Bar.class, () -> new 
    Bar(context.getBean(Foo.class))
);
```

如果采用Kotlin来编写，具体化的类型参数可以进行简化。代码如下。

```python
val context = GenericApplicationContext {
     registerBean<Foo>()
     registerBean { Bar(it.getBean<Foo>()) }
}
```

