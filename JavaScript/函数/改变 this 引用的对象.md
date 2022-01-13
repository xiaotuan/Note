[toc]

### 1. call() 方法

`call()` 方法的第一个参数指定了函数执行时 this  的值，其后的所有参数都是需要被传入函数的参数。

```js
function sayNameForAll(label) {
    console.log(label + " : " + this.name)
}

var person1 = {
    name: "Nicholas"
};

var person2 = {
    name: "Greg"
};

var name = "Michael";

sayNameForAll.call(this, "global"); // global : Michael
sayNameForAll.call(person1, "person 1");    // person 1 : Nicholas
sayNameForAll.call(person2, "person 2");    // person 2 : Greg
```

### 2. apply() 方法

`apply()` 的工作方式和 `call()` 完全一样，但它只接受两个参数：this 的值和一个数组或类似数组的对象，内含需要被传入函数的参数。

```js
function sayNameForAll(label) {
    console.log(label + " : " + this.name)
}

var person1 = {
    name: "Nicholas"
};

var person2 = {
    name: "Greg"
};

var name = "Michael";

sayNameForAll.apply(this, [ "global" ]); // global : Michael
sayNameForAll.apply(person1, [ "person 1" ]);    // person 1 : Nicholas
sayNameForAll.apply(person2, [ "person 2" ]);    // person 2 : Greg
```

### 3. bind() 方法

`bind()` 的第一个参数是要传给新函数的 this  的值。其他所有参数代表需要被永久设置在新函数中的命名参数。你可以在之后继续设置任何非永久参数。

```js
function sayNameForAll(label) {
    console.log(label + " : " + this.name)
}

var person1 = {
    name: "Nicholas"
};

var person2 = {
    name: "Greg"
};

var name = "Michael";

// create a function just for person1
var sayNameForPerson1 = sayNameForAll.bind(person1);
sayNameForPerson1("person 1");  // person 1 : Nicholas
// create a function just for person2
var sayNameForPerson2 = sayNameForAll.bind(person2, "person 2");
sayNameForPerson2();    // person 2 : Greg
// attaching a methond to an object doesn't change 'this'
person2.sayName = sayNameForPerson1;
person2.sayName("person 2");    // person 2 : Nicholas
```

