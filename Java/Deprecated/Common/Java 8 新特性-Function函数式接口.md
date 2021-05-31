[toc]

### 说明

java.util.function包是Java 8增加的一个新技术点"函数式接口"，此包共有43个接口。这些接口是为了使Lamdba函数表达式使用的更加简便，当然你也可以自己自定义接口来应用于Lambda函数表达式。Lambda是Java 8 的最大特点，本文对此并没有进行详解。本文还应用了Java 8的另一个特点“引用方法”(引用方法是用的冒号“::”来进行方法的调用)，有兴趣的Friends可以去上网查一下。

### Consumer-消费者

| Consumer\<T\>          | 提供一个T类型的输入参数，不返回执行结果            |
| -------------------- | -------------------------------------------------- |
| BiConsumer\<T,U\>      | 提供两个自定义类型的输入参数，不返回执行结果       |
| DoubleConsumer       | 表示接受单个double值参数，但不返回结果的操作       |
| IntConsumer          | 表示接受单个int值参数，但不返回结果的操作          |
| LongConsumer         | 表示接受单个long值参数，但不返回结果的操作         |
| ObjDoubleConsumer\<T\> | 表示接受object值和double值，但是不返回任何操作结果 |
| ObjIntConsumer\<T\>    | 表示接受object值和int值，但是不返回任何操作结果    |
| ObjLongConsumer\<T\>   | 表示接受object值和long值，但是不返回任何操作结果   |

#### Consumer\<T\>

提供一个T类型的输入参数，不返回执行结果

| void accept(T t)                                       | 对给定的参数执行操作                            |
| ------------------------------------------------------ | ----------------------------------------------- |
| default Consumer\<T\> andThen(Consumer\<? super T\> after) | 返回一个组合函数，after将会在该函数执行之后应用 |

**accept(T t)**

```java
StringBuilder sb = new StringBuilder("Hello ");
Consumer<StringBuilder> consumer = (str) -> str.append("Jack!");
consumer.accept(sb);
System.out.println(sb.toString());	// Hello Jack!
```

**andThen(Consumer<? super T> after)**

```java
Consumer<StringBuilder> consumer1 = (str) -> str.append(" Bob!");
consumer.andThen(consumer1).accept(sb);
System.out.println(sb.toString());	// Hello Jack! Bob!
```

#### BiConsumer\<T,U\> 

提供两个自定义类型的输入参数，不返回执行结果

| void accept(T t, U u)                                        | 对给定的参数执行操作                            |
| ------------------------------------------------------------ | ----------------------------------------------- |
| default BiConsumer<T,U> andThen(BiConsumer<? super T,? super U> after) | 返回一个组合函数，after将会在该函数执行之后应用 |

**accept(T t, U u)**

```java
StringBuilder sb = new StringBuilder();
BiConsumer<String, String> biConsumer = (a, b) -> {
	sb.append(a);
	sb.append(b);
};
biConsumer.accept("Hello ", "Jack!");
System.out.println(sb.toString());	// Hello Jack!
```

**andThen(BiConsumer<? super T,? super U> after)**

```java
BiConsumer<String, String> biConsumer1 = (a, b) -> {
	System.out.println(a + b);
};
biConsumer.andThen(biConsumer1).accept("Hello", " Jack!"); // Hello Jack!
```

#### DoubleConsumer

表示接受单个double值参数，但不返回结果的操作

| void accept(double value)                            | 对给定的参数执行操作                        |
| ---------------------------------------------------- | ------------------------------------------- |
| default DoubleConsumer andThen(DoubleConsumer after) | 返回一个组合函数，after在该函数执行之后应用 |

**accept(double value)**

```java
DoubleConsumer doubleConsumer = System.out::println;
doubleConsumer.accept(1.3); // 1.3
```

**andThen(DoubleConsumer after)**

```java
DoubleConsumer doubleConsumer1 = System.out::println;
doubleConsumer.andThen(doubleConsumer1).accept(1.3); // 1.3  1.3
```

#### ObjDoubleConsumer\<T\> 

表示接受object值和double值，但是不返回任何操作结果

| void accept(T t, double value) | 对给定的参数执行操作 |
| ------------------------------ | -------------------- |
|                                |                      |
**accept(T t, double value)**

```java
ObjDoubleConsumer<String> doubleConsumer = (obj, doub)
	-> System.out.println(obj + doub);
doubleConsumer.accept("金额：", 222.66); // 金额：222.66
```

### Predicate-谓语

| Predicate\<T\>   | 对给定的输入参数执行操作，返回一个boolean类型的结果（布尔值函数） |
| ---------------- | ------------------------------------------------------------ |
| BiPredicate<T,U> | 对给定的两个输入参数执行操作，返回一个boolean类型的结果（布尔值函数） |
| DoublePredicate  | 对给定的double参数执行操作，返回一个boolean类型的结果（布尔值函数） |
| IntPredicate     | 对给定的int输入参数执行操作，返回一个boolean类型的结果（布尔值函数） |
| LongPredicate    | 对给定的long参数执行操作，返回一个boolean类型的结果（布尔值函数） |

#### Predicate\<T\>

对给定的输入参数执行操作，返回一个boolean类型的结果（布尔值函数）

| boolean test(T t)                              | 根据给定的参数进行判断                                      |
| ---------------------------------------------- | ----------------------------------------------------------- |
| Predicate\<T\> and(Predicate<? super T> other) | 返回一个组合判断，将other以短路并且的方式加入到函数的判断中 |
| Predicate\<T\> or(Predicate<? super T> other)  | 返回一个组合判断，将other以短路或的方式加入到函数的判断中   |
| Predicate\<T\> negate()                        | 将函数的判断取反                                            |

**test(T t)**

```java
Predicate<Integer> predicate = number -> number != 0;
System.out.println(predicate.test(10));    //true
```
**and(Predicate<? super T> other)**

```java
predicate = predicate.and(number -> number >= 10);
System.out.println(predicate.test(10));    //true
```

**or(Predicate<? super T> other)**

```html
predicate = predicate.or(number -> number != 10);
System.out.println(predicate.test(10));    //true
```

**negate()**

```java
predicate = predicate.negate();
System.out.println(predicate.test(10));    //false
```

#### BiPredicate<T,U>

对给定的两个输入参数执行操作，返回一个boolean类型的结果（布尔值函数）

| boolean test(T t, U u)                                       | 根据给定的两个输入参数进行判断                              |
| ------------------------------------------------------------ | ----------------------------------------------------------- |
| BiPredicate<T,U> and(BiPredicate<? super T,? super U> other) | 返回一个组合判断，将other以短路并且的方式加入到函数的判断中 |
| BiPredicate<T,U> or(BiPredicate<? super T,? super U> other)  | 返回一个组合判断，将other以短路或的方式加入到函数的判断中   |
| BiPredicate<T,U> negate()                                    | 将函数的判断取反                                            |

**test(T t, U u)**

```java
BiPredicate<Integer, Integer> biPredicate = (a, b) -> a != b;
System.out.println(biPredicate.test(1, 2)); // true
```

**and(BiPredicate<? super T,? super U> other)**

```java
biPredicate = biPredicate.and((a, b) -> a.equals(b));
System.out.println(biPredicate.test(1, 2)); // false
```

**or(BiPredicate<? super T,? super U> other)**

```java
biPredicate = biPredicate.or((a, b) -> a == b);
System.out.println(biPredicate.test(1, 1)); // true
```

**negate()**

```java
biPredicate = biPredicate.negate();
System.out.println(biPredicate.test(1, 2)); // false
```

#### DoublePredicate

对给定的double参数执行操作，返回一个boolean类型的结果（布尔值函数）

| boolean test(double value)                 | 根据给定的参数进行判断                                      |
| ------------------------------------------ | ----------------------------------------------------------- |
| DoublePredicate and(DoublePredicate other) | 返回一个组合判断，将other以短路并且的方式加入到函数的判断中 |
| DoublePredicate or(DoublePredicate other)  | 返回一个组合判断，将other以短路或的方式加入到函数的判断中   |
| default DoublePredicate negate()           | 将函数的判断取反                                            |

**test(double value)**

```java
DoublePredicate doublePredicate = doub -> doub != 0;
System.out.println(doublePredicate.test(10)); // true
```

**and(DoublePredicate other)**

```java
doublePredicate = doublePredicate.and(doub -> doub < 2);
System.out.println(doublePredicate.test(1.7)); // true
```

**or(DoublePredicate other)**

```java
doublePredicate = doublePredicate.or(doub -> doub > 2);
System.out.println(doublePredicate.test(1.7)); // true
```

**negate()**

```java
doublePredicate = doublePredicate.negate();
System.out.println(doublePredicate.test(1.7)); // false
```

### Function-功能

| Function<T,R>           | 接收一个参数并返回结果的函数                 |
| ----------------------- | -------------------------------------------- |
| BiFunction<T,U,R>       | 接受两个参数并返回结果的函数                 |
| DoubleFunction\<R\>     | 接收一个double类型的参数并返回结果的函数     |
| DoubleToIntFunction     | 接收一个double类型的参数并返回int结果的函数  |
| DoubleToLongFunction    | 接收一个double类型的参数并返回long结果的函数 |
| IntFunction\<R\>        | 接收一个int类型的参数并返回结果的函数        |
| IntToDoubleFunction     | 接收一个int类型的参数并返回double结果的函数  |
| IntToLongFunction       | 接收一个int类型的参数并返回long结果的函数    |
| LongFunction\<R\>       | 接收一个long类型的参数并返回结果的函数       |
| LongToDoubleFunction    | 接收一个long类型的参数并返回double结果的函数 |
| LongToIntFunction       | 接收一个long类型的参数并返回int结果的函数    |
| ToDoubleBiFunction<T,U> | 接收两个参数并返回double结果的函数           |
| ToDoubleFunction\<T\>   | 接收一个参数并返回double结果的函数           |
| ToIntBiFunction<T,U>    | 接收两个参数并返回int结果的函数              |
| ToIntFunction\<T\>      | 接收一个参数并返回int结果的函数              |
| ToLongBiFunction<T,U>   | 接收两个参数并返回long结果的函数             |
| ToLongFunction\<T\>     | 接收一个参数并返回long结果的函数             |

#### Function<T, R>

接收一个参数并返回结果的函数

| R apply(T t)                                                 | 将此参数应用到函数中                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Function<T, R> andThen(Function<? super R,? extends V> after) | 返回一个组合函数，该函数结果应用到after函数中                |
| Function<T, R> compose(Function<? super V,? extends T> before) | 返回一个组合函数，首先将入参应用到before函数，再将before函数结果应用到该函数中 |

**apply(T t)**

```java
Function<String, String> function = a -> a + " Jack!";
System.out.println(function.apply("Hello")); // Hello Jack!
```

**andThen(Function<? super R,? extends V> after)**

```java
Function<String, String> function = a -> a + " Jack!";
Function<String, String> function1 = a -> a + " Bob!";
String greet = function.andThen(function1).apply("Hello");
System.out.println(greet); // Hello Jack! Bob!
```

**compose(Function<? super V,? extends T> before)**

```java
Function<String, String> function = a -> a + " Jack!";
Function<String, String> function1 = a -> a + " Bob!";
String greet = function.compose(function1).apply("Hello");
System.out.println(greet); // Hello Bob! Jack!
```

#### BiFunction<T,U,R>

接受两个参数并返回结果的函数

| R apply(T t, U u)                                            | 将参数应用于函数执行                        |
| ------------------------------------------------------------ | ------------------------------------------- |
| BiFunction<T,U,V> andThen(Function<? super R,? extends V> after) | 返回一个组合函数，after函数应用于该函数之后 |

**apply(T t, U u)**

```java
BiFunction<String, String, String> biFunction = (a, b) -> a + b;
System.out.println(biFunction.apply("Hello ", "Jack!")); // Hello Jack!
```

**andThen(Function<? super R,? extends V> after)**

```java
Function<String, String> function = (a) -> a + "!!!";
System.out.println(biFunction.andThen(function).apply("Hello", " Jack")); // Hello Jack!!!
```

#### DoubleFunction\<R\>

接收一个double类型的参数并返回结果的函数

| R apply(double value) | 根据给定参数执行函数 |
| --------------------- | -------------------- |
|                       |                      |

**apply(double value)**

```java
DoubleFunction<String> doubleFunction = doub -> "结果：" + doub;
System.out.println(doubleFunction.apply(1.6)); // 结果：1.6
```

#### DoubleToIntFunction

接收一个double类型的参数并返回int结果的函数

| int applyAsInt(double value) | 根据给定的参数执行函数 |
| ---------------------------- | ---------------------- |
|                              |                        |

**applyAsInt(double value)**

```java
DoubleToIntFunction doubleToIntFunction = doub -> Double.valueOf(doub).intValue();
System.out.println(doubleToIntFunction.applyAsInt(1.2)); // 1
```

#### ToDoubleBiFunction<T,U>

接收两个参数并返回double结果的函数

| double applyAsDouble(T t, U u) | 根据给定的参数执行函数 |
| ------------------------------ | ---------------------- |
|                                |                        |

**applyAsDouble(T t, U u)**

```java
ToDoubleBiFunction<Long, Float> toDoubleBiFunction = (lon, floa) -> lon
	.doubleValue() + floa.doubleValue();
System.out.println(toDoubleBiFunction.applyAsDouble(11L, 235.5f)); // 246.5
```

#### ToDoubleFunction\<T\>

接收一个参数并返回double结果的函数

| double applyAsDouble(T value) | 根据给定参数执行函数 |
| ----------------------------- | -------------------- |
|                               |                      |

**applyAsDouble(T value)**

```java
ToDoubleFunction<Float> toDoubleFunction = floa -> floa.doubleValue();
System.out.println(toDoubleFunction.applyAsDouble(12315f)); // 12315.0
```

### Supplier-供应商

| Supplier\<T\>   | 不提供输入参数，但是返回结果的函数        |
| --------------- | ----------------------------------------- |
| BooleanSupplier | 不提供输入参数，但是返回boolean结果的函数 |
| DoubleSupplier  | 不提供输入参数，但是返回double结果的函数  |
| IntSupplier     | 不提供输入参数，但是返回int结果的函数     |
| LongSupplier    | 不提供输入参数，但是返回long结果的函数    |

#### Supplier\<T\>

无需提供输入参数，返回一个T类型的执行结果

| T get() | 获取结果值 |
| ------- | ---------- |
|         |            |

**get()**

```java
Supplier<String> supplier = () -> "Hello Jack!";
System.out.println(supplier.get()); // Hello Jack!
```

#### BooleanSupplier

不提供输入参数，但是返回boolean结果的函数

| boolean getAsBoolean() | 获取函数的执行结果 |
| ---------------------- | ------------------ |
|                        |                    |

**getAsBoolean()**

```java
BooleanSupplier booleanSupplier = () -> true;
System.out.println(booleanSupplier.getAsBoolean()); // true
```

#### DoubleSupplier

不提供输入参数，但是返回double结果的函数

| double getAsDouble() | 获取函数的执行结果 |
| -------------------- | ------------------ |
|                      |                    |

**getAsDouble()**

```java
DoubleSupplier doubleSupplier = () -> 2.7;
System.out.println(doubleSupplier.getAsDouble()); // 2.7
```

### Operator-操作员

| UnaryOperator\<T\>   | 提供单个参数，并且返回一个与输入参数类型一致的结果 |
| -------------------- | -------------------------------------------------- |
| BinaryOperator\<T\>  | 提供两个参数，并且返回结果与输入参数类型一致的结果 |
| DoubleBinaryOperator | 提供两个double参数并且返回double结果               |
| DoubleUnaryOperator  | 提供单个double参数并且返回double结果               |
| IntBinaryOperator    | 提供两个int参数并且返回int结果                     |
| IntUnaryOperator     | 提供单个int参数并且返回int结果                     |
| LongBinaryOperator   | 提供两个long参数并且返回long结果                   |
| LongUnaryOperator    | 提供单个long参数并且返回long结果                   |

#### UnaryOperator\<T\>

对输入参数执行操作，并且输入参数与返回参数类型相同

| T apply(T t)                                                 | 将给定参数应用到函数中                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Function<T, R> andThen(Function<? super R,? extends V> after) | 返回一个组合函数，该函数结果应用到after函数中                |
| Function<T, R> compose(Function<? super V,? extends T> before) | 返回一个组合函数，首先将入参应用到before函数，再将before函数结果应用到该函数中 |

**apply(T t)**

```java
UnaryOperator<String> unaryOperator = greet -> greet + " Bob!";
System.out.println(unaryOperator.apply("Hello")); // Hello Jack!
```

**andThen(Function<? super R,? extends V> after)**

```java
UnaryOperator<String> unaryOperator1 = greet -> greet + " Jack!";
String greet = unaryOperator.andThen(unaryOperator1).apply("Hello");
System.out.println(greet); // Hello Bob! Jack!
```

**compose(Function<? super V,? extends T> before)**

```java
String greet = unaryOperator.compose(unaryOperator1).apply("Hello");
System.out.println(greet); // Hello Jack! Bob!
```

#### BinaryOperator\<T\>

提供两个参数，并且返回结果与输入参数类型一致的结果

| R apply(T t, U u)                                            | 根据给定参数执行函数                    |
| ------------------------------------------------------------ | --------------------------------------- |
| BiFunction<T,U,V> andThen(Function<? super R,? extends V> after) | 返回一个组合函数，after应用于该函数之后 |

**apply(T t, U u)**

```java
BinaryOperator<String> binaryOperator = (flag, flag1) -> flag + flag1;
System.out.println(binaryOperator.apply("Hello ", "Jack!")); // Hello Jack!
```

**andThen(Function<? super R,? extends V> after)**

```java
Function<String, String> function = a -> a + "!!!";
System.out.println(binaryOperator.andThen(function).apply("Hello", " Jack")); // Hello Jack!!!
```

#### DoubleBinaryOperator

提供两个double参数并且返回double结果

| double applyAsDouble(double left, double right) | 根据给定的参数执行函数 |
| ----------------------------------------------- | ---------------------- |
|                                                 |                        |

**applyAsDouble(double left, double right)**

```java
DoubleBinaryOperator doubleBinaryOperator = (doub1, doub2) -> doub1
	+ doub2;
System.out.println(doubleBinaryOperator.applyAsDouble(1.1, 2.3)); // 3.4
```

#### DoubleUnaryOperator

提供单个double参数并且返回double结果

| double applyAsDouble(double operand)                    | 根据给定参数执行函数                     |
| ------------------------------------------------------- | ---------------------------------------- |
| DoubleUnaryOperator andThen(DoubleUnaryOperator after)  | 返回一个组合函数，after应用于该函数之后  |
| DoubleUnaryOperator compose(DoubleUnaryOperator before) | 返回一个组合函数，before应用于该函数之前 |

**applyAsDouble(double operand)**

```java
DoubleUnaryOperator doubleUnaryOperator = doub -> doub + 2.5;
System.out.println(doubleUnaryOperator.applyAsDouble(2.6)); // 5.1
```

**andThen(DoubleUnaryOperator after)**

```java
DoubleUnaryOperator doubleUnaryOperator1 = doub -> doub * 3;
double result = doubleUnaryOperator.andThen(doubleUnaryOperator1)
	.applyAsDouble(10); 
System.out.println(result); // (10 + 2.5) * 3 = 37.5
```

**compose(DoubleUnaryOperator before)**

```java
double result = doubleUnaryOperator.compose(doubleUnaryOperator1)
	.applyAsDouble(10);
System.out.println(result); // 10 * 3 + 2.5 = 32.5
```