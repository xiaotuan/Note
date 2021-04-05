**案例：示例 18-27：某网站用户访问来源**

**pie.html**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="Canvas" />
        <meta content="某网站用户访问来源" />
        <title>某网站用户访问来源</title>
    </head>

    <body>
        <div style="width:750px; height:440px;margin:0 auto;">
            <canvas id="demo" width="750" height="440" style="border:1px solid #CCCCCC;"></canvas>
        </div>
        <script src="pie.js" type="text/javascript"></script>
    </body>
</html>
```

**pie.js**

```js
var data = [
    { cname: "直接访问", value: "335", color: "#2EC7C9" },
    { cname: "搜索引擎", value: "1548", color: "#D87A80" },
    { cname: "邮件营销", value: "310", color: "#B6A2DE" },
    { cname: "联盟广告", value: "234", color: "#5AB1EF" },
    { cname: "视频广告", value: "135", color: "#FFB980" }
]
//实例化绘图对象
var newPie = new drawPie(data);
newPie.drawTitle();//绘制标题
newPie.drawLegent();//绘制图例
newPie.drawSection();//绘制扇区

//绘图对象
function drawPie(data) {
    //获取canvas元素对应的DOM对象
    var canvas = document.getElementById("demo");
    //获取在canvas上绘图的canvasRenderingContext2D对象
    var ctx = canvas.getContext("2d");    

    //绘制标题
    this.drawTitle = function () {
        var width = canvas.width;
        var height = canvas.height;
        ctx.fillStyle = "#008ACD";
        ctx.font = "20px 微软雅黑";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        ctx.fillText("某网站用户访问来源", width / 2, 15);
    }

    //绘制图例
    this.drawLegent = function () {
        ctx.font = "14px 微软雅黑";
        ctx.textAlign = "left";
        ctx.textBaseline = "top";
        for (var key in data) {
            var item = data[key];
            //矩形图例
            ctx.fillStyle = item.color;
            ctx.fillRect(15, 15 + 25 * key,20,12);
            //图例说明
            ctx.fillStyle = "#666";
            ctx.fillText(item.cname, 40, 15+25*key);
        }
    }

    //绘制饼状图扇区
    this.drawSection = function () {
        var obj = this;
        //圆心坐标
        var centerX = canvas.width / 2, centerY = canvas.height / 2;
        var r = 100;//半径
        var descR = 130;
        var total = this.valueSum();
        var sectionSum = 0;
        for (var key in data) {
            //单项弧度
            var section = 2 * Math.PI * data[key].value / total;
            sectionSum += section;
            ctx.fillStyle = data[key].color;
            //定义路径
            ctx.beginPath();
            ctx.arc(centerX, centerY, r, sectionSum - section, sectionSum, false);//扇区圆弧
            ctx.lineTo(centerX, centerY);//扇区
            ctx.closePath();            
            ctx.fill();
            //增加扇区描述
            obj.sectionDescribe(data[key], sectionSum, section, centerX, centerY, descR);

        }
        this.drawWrapCircle();
    }

    //扇区描述
    this.sectionDescribe = function (item, sectionSum, section, centerX, centerY, descR) {
        var middleX = centerX + descR * Math.cos(sectionSum - section / 2);
        var middleY = centerY + descR * Math.sin(sectionSum - section / 2);
        ctx.strokeStyle = item.color;
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(middleX, middleY);
        ctx.closePath();
        ctx.stroke();
        var valueX = 0;
        //var percent = (100 * item.value / total).toFixed(2);
        if (middleX > centerX) {
            ctx.textAlign = "left";
            valueX = middleX + 5;
        } else if (middleX == centerX) {
            ctx.textAlign = "center";
            valueX = middleX;
        } else {
            ctx.textAlign = "right";
            valueX = middleX - 5;
        }
        ctx.textBaseline = "middle";
        ctx.fillText(item.cname + ':' + item.value, valueX, middleY);
    }

    //绘制外环
    this.drawWrapCircle = function () {
        var R = 110;
        //圆心坐标
        var centerX = canvas.width / 2, centerY = canvas.height / 2;
        ctx.strokeStyle = "#D3D3D3";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.arc(centerX, centerY, R, 0, 2*Math.PI, false);
        ctx.closePath();
        ctx.stroke();
    }

    //各项数值求和
    this.valueSum = function () {
        var sum = 0;
        for (var key in data) {
            sum += Number(data[key].value);
        }
        return sum;
    }
}
```

