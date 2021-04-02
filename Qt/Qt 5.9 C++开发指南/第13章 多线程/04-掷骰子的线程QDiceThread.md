### 13.1.2　掷骰子的线程QDiceThread

作为实例，定义一个掷骰子的线程类QDiceThread，类的声明部分如下：

```css
#include   <Qthread>
class QDiceThread : public Qthread
{
   Q_OBJECT
private:
   int    m_seq=0;          //掷骰子次数序号
   int    m_diceValue;      //骰子点数
   bool   m_Paused=true;    //暂停
   bool   m_stop=false;     //停止
protected:
   void   run() Q_DECL_OVERRIDE;  //线程任务
public:
   QDiceThread();
   void   diceBegin();      //掷一次骰子
   void   dicePause();      //暂停
   void   stopThread();     //结束线程
signals:
   void   newValue(int seq,int diceValue); //产生新点数的信号
};
```

重载虚函数run()，在此函数里完成线程的主要任务。

自定义diceBegin()、dicePause()、stopThread() 3个公共函数用于线程控制，这3个函数由主线程调用。

定义了一个信号newValue(int seq,int diceValue) 用于在掷一次骰子得到新的点数之后发射此信号，由主线程的槽函数响应以获取值。

QDiceThread类的实现代码如下：

```css
#include   " qdicethread.h"
#include   <QTime>
QDiceThread::QDiceThread()
{//构造函数
}
void QDiceThread::diceBegin()
{ //开始掷骰子
   m_Paused=false;
}
void QDiceThread::dicePause()
{//暂停掷骰子
   m_Paused=true;
}
void QDiceThread::stopThread()
{//停止线程
   m_stop=true;
}
void QDiceThread::run()
{//线程任务
   m_stop=false;//启动线程时令m_stop=false
   m_seq=0; //掷骰子次数
   qsrand(QTime::currentTime().msec());//随机数初始化，qsrand是线程安全的
   while(!m_stop)//循环主体
   {
      if (!m_Paused)
      {
         m_diceValue=qrand(); //获取随机数
         m_diceValue=(m_diceValue % 6)+1;
         m_seq++;
         emit newValue(m_seq,m_diceValue);  //发射信号
      }
      msleep(500); //线程休眠500ms
   }
   quit();//相当于exit(0),退出线程的事件循环
}
```

其中，run()是线程任务的实现部分，线程开始就执行run()函数。run()函数一般是事件循环过程，根据各种条件或事件处理各种任务。当run()函数退出时，线程的事件循环就结束了。

在run()函数里，初始化变量m_stop和m_seq，用qsrand()函数对随机数种子初始化。run()函数的主循环体是一个while循环，在主线程调用stopThread()函数使m_stop为true，才会退出while循环，调用quit()之后结束线程。

在while循环体内，又根据m_Paused判断当前是否需要掷骰子，如果需要掷骰子，则用随机函数生成一次骰子的点数m_diceValue，然后发射信号newValue()，将m_seq和m_diceValue作为信号参数传递出去。主线程可以设计槽函数与此信号关联，获取这两个值并进行显示。

