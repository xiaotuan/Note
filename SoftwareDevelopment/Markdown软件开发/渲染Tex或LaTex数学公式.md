MathJax.js 的官网地址：<https://www.mathjax.org/>

可以使用 MathJax.js 库对 Tex 或 LaTex 数学公式进行渲染。使用方法如下：

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>MathJax example</title>
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async
          src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
</head>
<body>
<p>
  When \(a \ne 0\), there are two solutions to \(ax^2 + bx + c = 0\) and they are
  \[x = {-b \pm \sqrt{b^2-4ac} \over 2a}.\]
</p>
  <p>
    $$
    \mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} 
    \mathbf{i} & \mathbf{j} & \mathbf{k} \\
    \frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
    \frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
    \end{vmatrix}
    ${$tep1}{\style{visibility:hidden}{(x+1)(x+1)}}
    $$
  </p>
</body>
</html>
```

