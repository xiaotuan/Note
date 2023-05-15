脚本化的CSS最常见的用途之一是产生视觉动画效果。使用 `setTimeout()` 或 `setInterval()` 重复调用函数来修改元素的内联样式达到目的。  

**示例代码：CSS 动画**

```js
// 将e转化为相对定位的元素，使之左右"震动"
// 第一个参数可以是元素对象或者元素的id
// 如果第二个参数是函数，以e为参数，它将在动画结束时调用
// 第三个参数指定e震动的距离，默认是5像素
// 第四个参数指定震动多久，默认是500毫秒
function shake(e, oncomplete, distance, time) {
	// 句柄参数
	if (typeof e === "string") {
        e = document.getElementById(e);
    }
	if (!time) {
        time = 500;
    }
	if (!distance) {
        distance = 5;
    }
    var originalStyle = e.style.cssText; // 保存e的原始style
    e.style.position = "relative"; // 使e相对定位
    var start = (new Date()).getTime(); // 注意，动画的开始时间
    animate(); // 动画开始
    
    // 函数检查消耗的时间，并更新e的位置
    // 如果动画完成，它将e还原为原始状态
    // 否则，它更新e的位置，安排它自身重新运行
    function animate() {
        var now = (new Date()).getTime(); // 得到当前时间
        var elapsed = now-start; // 从开始以来消耗了多长时间？
        var fraction = elapsed/time; // 是总时间的几分之几？
        if (fraction < 1) { // 如果动画未完成
            // 作为动画完成比例的函数，计算e的x位置
                // 使用正弦函数将完成比例乘以4pi
            // 所以，它来回往复两次
            var x = distance * Math.sin(fraction*4*Math.PI);
            e.style.left = x + "px";
            // 在25毫秒后或在总时间的最后尝试再次运行函数
            // 目的是为了产生每秒40帧的动画
            setTimeout(animate, Math.min(25, time-elapsed));
    	} else { // 否则，动画完成
            e.style.cssText = originalStyle // 恢复原始样式
            if (oncomplete) {
                oncomplete(e); // 调用完成后的回调函数
            }
    	}
    }
}

// 以毫秒级的时间将e从完全不透明淡出到完全透明
// 在调用函数时假设e是完全不透明的
// oncomplete是一个可选的函数，以e为参数，它将在动画结束时调用
// 如果不指定time，默认为500毫秒
// 该函数在IE中不能正常工作，但也可以修改得能工作，
// 除了opacity，IE使用非标准的filter属性
function fadeOut(e, oncomplete, time) {
	if (typeof e === "string") {
        e = document.getElementById(e);
    }
	if (!time) {
        time = 500;
    }
    // 使用Math.sqrt作为一个简单的“缓动函数”来创建动画
    // 精巧的非线性：一开始淡出得比较快，然后缓慢了一些
    var ease = Math.sqrt;
    var start = (new Date()).getTime(); // 注意：动画开始的时间
    animate(); // 动画开始
    
    function animate() {
        var elapsed = (new Date()).getTime()-start; // 消耗的时间
        var fraction = elapsed/time; // 总时间的几分之几？
        if (fraction < 1) { // 如果动画未完成
            var opacity = 1 - ease(fraction); // 计算元素的不透明度
            e.style.opacity = String(opacity); // 设置在e上
            setTimeout(animate, // 调度下一帧
            Math.min(25, time-elapsed));
        } else { // 否则，动画完成
            e.style.opacity = "0"; // 使e完全透明
            if (oncomplete) {
                oncomplete(e); // 调用完成后的回调函数
            }
        }
	}
}
```

下面的 HTML 代码创建了一个按钮，当单击时，它左右震动并淡出：  

```html
<button onclick="shake(this, fadeOut);">Shake and Fade</button>
```

