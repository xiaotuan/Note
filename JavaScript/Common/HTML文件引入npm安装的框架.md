直接使用相对路径或绝对路径进行引用。比如引入如下目录结构的框架：

```
.根目录
  |_node_modules
  |   |_vue
  |       |_dist
  |           |_vue.js
  |_HelloWorld.html
```

引入上面的 vue 框架的方法如下：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>HelloWorld</title>
  </head>
  <body>
    <div id='app'>
      <h1>{{message}}</h1>
    </div>
    <script type="text/javascript" src="node_modules/vue/dist/vue.min.js"></script>
    <script type="text/javascript">
      var vm = new Vue({
        el: '#app',
        data: {
          message: 'Hello world, I am Vue.js'
        }
      })
    </script>
  </body>
</html>
```