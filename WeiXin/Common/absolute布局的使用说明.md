<center><font size="5"><b>absolute 布局的使用说明</b></font></center>

**使用方法**

```css
{
    position: absolute;
}
```

`absolute`：绝对位置，使用 `left` 、`right` 、 `top`，`bottom` 等属性进行绝对定位。而其层叠通过 `z-index` 属性定义，此时对象不具有边距，但仍有补白和边框。

注意事项：

1. 使用绝对定位后设置外边距（margin）属性无效
2. 使用绝对定位后，如果没有设置其他任何属性的话，元素默认定位在距离父容器的左上角。
3. 使用绝对定位后，如果设置 `left` 、`right` 、 `top`，`bottom` 其中的值，这些值是依据顶级容器进行定位的，而不是根据父级容器进行定位。也就是说该元素已经脱离父容器的约束。
4. 可以使用 `z-index` 设置元素层叠位置，值越大就越靠前显示。