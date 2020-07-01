**Class绑定**

1. 对象语法：`v-bind:class` 接受参数是一个对象，而且可以与普通的 class 属性共存。

```html
<div class="tab" v-bind:class="{'active': active, 'unactive': !active}"></div>

vm实例中需要包含
data: {
  active: true
}

// <div class="tab active"></div>
```

2. 数组语法：`v-bind:class` 也接受数组作为参数：

```html
<div v-bind:class="[classA, classB]"></div>

vm实例中需要包含
data: {
  classA: 'class-a',
  classB: 'class-b'
}

// <div class="class-a class-b"></div>
```

**内联样式绑定**

1. 对象语法：直接绑定符合样式格式的对象。

```html
<div v-bind:style="alertStyle"></div>

data: {
  alertStyle: {
    color: 'red',
    fontSize: '20px'
  }
}

