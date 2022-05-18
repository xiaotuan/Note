1. 在项目源代码列表中的 `module-info.java` 文件中添加如下代码：

   ```java
   requires java.logging;
   ```

   例如：

   ```java
   module JavaTest {
   	requires java.desktop;
   	requires java.logging;
   }
   ```

2. 在使用 Logger  类的源代码中导入 Logger 包：

   ```java
   import java.util.logging.Logger;
   ```

   