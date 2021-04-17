### 12.5.5　Timer控件

Timer控件是一个定时引发事件的组件。该组件每隔一个指定的周期产生一个Tick事件，接收到此事件就可以执行相应的动作。下表列出了Timer控件的主要成员以及说明。

| 成员名称 | 类别 | 说明 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| Enable | 属性 | 启用Elapsed事件生成 |
| Interval | 属性 | Elapsed事件的频率（以毫秒为单位） |
| Tick | 事件 | 每当经过指定的时间间隔时发生 |
| Start() | 方法 | 启动计时器 |
| Stop() | 方法 | 停止计时器 |

下面介绍几个比较常用的成员。

（1）Enable属性。此属性用于指定计时器是否运行，此属性设置为True则表示可以启动计时器。

（2）Interval属性。获取或设置引发Elapsed事件的间隔。属性值为引发Elapsed事件的间隔时间（以ms为单位），默认值为100ms。代码如下。

```c
01  this.timer1.Interval = 1000         //设置Elapsed事件的频率，间隔时间为100ms
02  this.timer1.Enabled = false;        //设置timer1不可用，无法启用Elapsed事件
```

（3）Tick事件。该事件在当指定的计时器间隔已过去而且计时器处于启用状态时发生。代码如下。

```c
01  private void timer1_Tick(object sender, EventArgs e)    //Tick事件
02  {
03          this.label2.Text = "现在时间为:" + DateTime.Now.ToString(); //在label2上显示现在时间
04  }
```

**【范例12-8】 显示操作进度。**

（1）启动Visual Studio 2013，新建一个C# Windows窗体应用程序，项目名称为“TimerSample”。

（2）向Windows窗体中添加一个Timer控件、一个ProgressBar控件和两个Lable控件。在属性窗口中将ProgressBar控件的最大值设为200，最小值设为0。

（3）双击【开始】按钮，切换到代码视图，在【开始】按钮的Click事件中编写如下代码（代码12-8-1.txt）。

```c
01  private void button1_Click(object sender, EventArgs e) //开始按钮的Click事件
02  {
03          if (timer1.Enabled == true)                    //判断timer1控件是否可用
04          {
05                  timer1.Enabled = false;                //将timer1控件设置为不可用
06                  button1.Text = "开始";                 //将按钮上的显示文本设置为开始
07          }
08          else                                          //如timer1不可用执行如下代码
09          {
10                  timer1.Enabled = true;               //启用timer1
11                  button1.Text = "停止";               //button1的Text属性设置为“停止”
12          }
13  }
```

（4）编写Timer控件的Tick事件，代码如下（代码12-8-2.txt）。

```c
01  private void timer1_Tick(object sender, EventArgs e)
02  {
03          if (this.progressBar1.Value == this.progressBar1.Maximum)           //判断进度条的当前值
04          {
05                  this.progressBar1.Value = this.progressBar1.Minimum; //重新设置进度条的值
06          }                                        //实现了进度的不断循环显示
07          else
08          {
09                  this.progressBar1.PerformStep(); //调用进度条的PerformStep方法
10          }
11          int intPercent;                          //定义变量，用来存储当前进度的百分比值
12          intPercent = 100 * (this.progressBar1.Value - this.progressBar1.Minimum)
13          / (this.progressBar1.Maximum - this.progressBar1.Minimum);
14          label2.Text = Convert.ToInt16(intPercent).ToString() + "%";
15  }
```

**【运行结果】**

单击工具栏中的【启用调试】按钮<img src="https://cdn.ptpress.cn/pubcloud/5B0A982E/ushu/N19937/online/FBOL6c69757cf0cda/Images/204.jpg" style="width:24px;  height: 22px; " class="my_markdown"/>
，在输出窗体界面单击【开始】按钮，进度条开始显示进度信息，Lable控件上显示具体的数字，按钮文本变为【停止】。

**【范例分析】**

本范例的重点是Timer的Tick事件。步骤（4）中的第12～14行实现了计算进度条进度的百分比数值，该数值与进度条的进度同步，并将结果显示在Lable控件上。代码Convert.ToInt16(intPercent).ToString()表示先将intPercent变量的值转换为16位有符号的整数，然后再转换为字符串类型，因为代码后面“+”连接符的后面是字符串类型。

**【拓展训练】**

将Timer控件的Interval属性的默认值100改为其他值，比如1000，那么进度条前进的速度就会变慢，即原来需要100ms的时间来完成进度条的显示，现在则需要1000ms。

