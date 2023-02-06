`all` 属性表示 CSS 的所有属性，但不包括 `unicode-bidi` 和 `direction` 这两个 CSS 属性。

```html
p.unset {
	all: unset;
}
```

如果在样式中声明的属性非常多，使用 `all` 会极为方便，可以避免逐个设置每个属性。