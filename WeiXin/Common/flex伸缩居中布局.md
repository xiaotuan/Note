<center><font size="5"><b>flex 伸缩居中布局</b></font></center>

```css
.head {
    display: flex;
    justify-content: center;
    align-items: center;
}
```

+ justify-content：主轴居中布局
+ align-items：其他轴居中布局

> 布局的方向即为主轴，例如 `flex-direction: row;` 表示水平方向为主轴；`flex-direction: column;` 表示垂直方向为主轴。