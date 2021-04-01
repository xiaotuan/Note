### 14.1.11　 `pulsate` 特效

`pulsate` 特效会使元素闪动。元素闪动的次数是通过 `options.times` 选项来指定的（默认值为5次）。而此特效设定的持续时间对应的是每一次闪动的时间：

```css
<script src = jquery.js></script>
<script src = jqueryui/js/jquery-ui-1.8.16.custom.min.js></script>
<link rel=stylesheet type=text/css 
　　　 href=jqueryui/css/smoothness/jquery-ui-1.8.16.custom.css />
<img id=img1 src=images/rails.jpg height=100 /><br /> 
<img id=img2 src=images/html.jpg height=100 />
<script>
$("#img1").effect ("pulsate", { times : 2 }, 1000); 
$("#img2").effect ("pulsate", { times : 5 }, 1000); 
</script>
```

