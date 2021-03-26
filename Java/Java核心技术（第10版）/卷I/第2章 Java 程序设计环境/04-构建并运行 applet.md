### 2.5 构建并运行 applet

首先，打开终端窗口并转到 CoreJava/v1ch02/RoadApplet，然后，输入下面的命令：

```shell
javac RoadApplet.java
jar cvfm RoadApplet.jar RoadApplet.mf *.class
appletviewer RoadApplet.html
```

**程序清单2-3 RoadApplet/RoadApplet.html**

```html
<html xmlns="http://www.w3.org/1999/xhtml">
   <head><title>A Traffic Simulator Applet</title></head>
   <body>    
      <h1>Traffic Simulator Applet</h1>
      
      <p>I wrote this traffic simulation, following the article &quot;Und nun die
      Stauvorhersage&quot; of the German Magazine <i>Die Zeit</i>, June 7,
      1996. The article describes the work of Professor Michael Schreckenberger
      of the University of Duisburg and unnamed collaborators at the University
      of Cologne and Los Alamos National Laboratory. These researchers model
      traffic flow according to simple rules, such as the following: </p>
      <ul>
         <li>A freeway is modeled as a sequence of grid points. </li>
         <li>Every car occupies one grid point. Each grid point occupies at most
         one car. </li>
         <li>A car can have a speed of 0 - 5 grid points per time interval. </li>
         <li>A car with speed of less than 5 increases its speed by one unit in
         each time interval, until it reaches the maximum speed. </li>
         <li>If a car's distance to the car in front is <i>d</i> grid points, its
         speed is reduced to <i>d</i>-1 if necessary to avoid crashing into it.
         </li>
         <li>With a certain probability, in each time interval some cars slow down
         one unit for no good reason whatsoever. </li>
      </ul>
      
      <p>This applet models these rules. Each line shows an image of the same
      stretch of road. Each square denotes one car. The first scrollbar lets you
      adjust the probability that some cars slow down. If the slider is all the
      way to the left, no car slows down. If it is all the way to the right,
      every car slows down one unit. A typical setting is that 10% - 20% of the
      cars slow down. The second slider controls the arrival rate of the cars.
      When it is all the way to the left, no new cars enter the freeway. If it
      is all the way to the right, a new car enters the freeway every time
      interval, provided the freeway entrance is not blocked. </p>
      
      <p>Try out the following experiments. Decrease the probability of slowdown
      to 0. Crank up the arrival rate to 1. That means, every time unit, a new
      car enters the road. Note how the road can carry this load. </p>
      
      <p>Now increase the probability that some cars slow down. Note how traffic
      jams occur almost immediately. </p>
      
      <p>The moral is: If it wasn't for the rubberneckers, the cellular phone
      users, and the makeup-appliers who can't keep up a constant speed, we'd all
      get to work more quickly. </p>
      
      <p>Notice how the traffic jam is stationary or even moves backwards, even
      though the individual cars are still moving. In fact, the first car
      causing the jam has long left the scene by the time the jam gets bad. 
      (To make it easier to track cars, every tenth vehicle is colored red.) </p>
      
      <p><applet code="RoadApplet.class" archive="RoadApplet.jar" 
                 width="400" height="400" alt="Traffic jam visualization">
      </applet></p>
      
      <p>For more information about applets, graphics programming and
      multithreading in Java, see
      <a href="http://horstmann.com/corejava">Core Java</a>. </p>
   </body>
</html>

```

**程序清单2-4 RoadApplet/RoadApplet.java**

```java
import java.awt.*;
import java.applet.*;
import javax.swing.*;

public class RoadApplet extends JApplet
{  
   private RoadComponent roadComponent;
   private JSlider slowdown;
   private JSlider arrival;

   public void init()
   {
      EventQueue.invokeLater(() ->
         {
            roadComponent = new RoadComponent();
            slowdown = new JSlider(0, 100, 10);    
            arrival = new JSlider(0, 100, 50);
        
            JPanel p = new JPanel();
            p.setLayout(new GridLayout(1, 6));
            p.add(new JLabel("Slowdown"));
            p.add(slowdown);
            p.add(new JLabel(""));
            p.add(new JLabel("Arrival"));
            p.add(arrival);
            p.add(new JLabel("")); 
            setLayout(new BorderLayout());
            add(p, BorderLayout.NORTH);
            add(roadComponent, BorderLayout.CENTER);
         });
   }
   
   public void start()
   {
      new Thread(() -> 
         {
            for (;;) 
            {
               roadComponent.update(
                  0.01 * slowdown.getValue(),
                  0.01 * arrival.getValue());
               try { Thread.sleep(50); } catch(InterruptedException e) {}
            }
         }).start();
   }
}
```

