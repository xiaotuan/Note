[toc]

### 1. 示例程序

```java
package reflection;

import java.util.*;
import java.lang.reflect.*;

/**
 * This program uses reflection to print all features of a class.
 * @version 1.1 2004-02-21
 * @author Cay Horstmann
 */
public class ReflectionTest
{
   public static void main(String[] args)
   {
      // read class name from command line args or user input
      String name;
      if (args.length > 0) name = args[0];
      else
      {
         Scanner in = new Scanner(System.in);
         System.out.println("Enter class name (e.g. java.util.Date): ");
         name = in.next();
      }

      try
      {
         // print class name and superclass name (if != Object)
         Class cl = Class.forName(name);
         Class supercl = cl.getSuperclass();
         String modifiers = Modifier.toString(cl.getModifiers());
         if (modifiers.length() > 0) System.out.print(modifiers + " ");
         System.out.print("class " + name);
         if (supercl != null && supercl != Object.class) System.out.print(" extends "
               + supercl.getName());

         System.out.print("\n{\n");
         printConstructors(cl);
         System.out.println();
         printMethods(cl);
         System.out.println();
         printFields(cl);
         System.out.println("}");
      }
      catch (ClassNotFoundException e)
      {
         e.printStackTrace();
      }
      System.exit(0);
   }

   /**
    * Prints all constructors of a class
    * @param cl a class
    */
   public static void printConstructors(Class cl)
   {
      Constructor[] constructors = cl.getDeclaredConstructors();

      for (Constructor c : constructors)
      {
         String name = c.getName();
         System.out.print("   ");
         String modifiers = Modifier.toString(c.getModifiers());
         if (modifiers.length() > 0) System.out.print(modifiers + " ");         
         System.out.print(name + "(");

         // print parameter types
         Class[] paramTypes = c.getParameterTypes();
         for (int j = 0; j < paramTypes.length; j++)
         {
            if (j > 0) System.out.print(", ");
            System.out.print(paramTypes[j].getName());
         }
         System.out.println(");");
      }
   }

   /**
    * Prints all methods of a class
    * @param cl a class
    */
   public static void printMethods(Class cl)
   {
      Method[] methods = cl.getDeclaredMethods();

      for (Method m : methods)
      {
         Class retType = m.getReturnType();
         String name = m.getName();

         System.out.print("   ");
         // print modifiers, return type and method name
         String modifiers = Modifier.toString(m.getModifiers());
         if (modifiers.length() > 0) System.out.print(modifiers + " ");         
         System.out.print(retType.getName() + " " + name + "(");

         // print parameter types
         Class[] paramTypes = m.getParameterTypes();
         for (int j = 0; j < paramTypes.length; j++)
         {
            if (j > 0) System.out.print(", ");
            System.out.print(paramTypes[j].getName());
         }
         System.out.println(");");
      }
   }

   /**
    * Prints all fields of a class
    * @param cl a class
    */
   public static void printFields(Class cl)
   {
      Field[] fields = cl.getDeclaredFields();

      for (Field f : fields)
      {
         Class type = f.getType();
         String name = f.getName();
         System.out.print("   ");
         String modifiers = Modifier.toString(f.getModifiers());
         if (modifiers.length() > 0) System.out.print(modifiers + " ");         
         System.out.println(type.getName() + " " + name + ";");
      }
   }
}
```

### 2. API

#### 2.1 java.lang.Class 1.0

------

+ **Field[] getFields()	1.1**

+ **Field[] getDeclaredFields()	1.1**

  `getFields()` 方法将返回一个包含 `Field` 对象的数组，这些对象记录了这个类或其超类的公有域。`getDeclaredField()` 方法也将返回包含 `Field` 对象的数组，这些对象记录了这个类的全部域。如果类中没有域，或者 Class 对象描述的是基本类型或数组类型，这些方法将返回一个长度为 0 的数组。

+ **Method[] getMethods()	1.1**

+ **Method[] getDeclareMethods()	1.1**

  返回包含 Method 对象的数组： `getMethods()` 将返回所有的公有方法，包括从超类继承来的公有方法； `getDeclaredMethods()` 返回这个类或接口的全部方法，但不包括由超类继承了的方法。

+ **Constructor[] getConstructors()    1.1**

+ **Constructor[] getDeclaredConstructors()    1.1**

  返回包含 Constructor 对象的数组，其中包含了 Class 对象所描述的类的所有公有构造器（`getConstructors()`）或所有构造器（`getDeclaredConstructors()`）。

#### 2.2 java.lang.reflect.Field    1.1

#### 2.3 java.lang.reflect.Method    1.1

#### 2.4 java.lang.reflect.Constructor    1.1

+ **Class getDeclaringClass()**

  返回一个用于描述类中定义的构造器、方法或域的 Class 对象。

+ **Class[] getExceptionTypes()** (在 Constructor 和 Method 类中)

  返回一个用于描述方法抛出的异常类型的 Class 对象数组。

+ **int getModifiers()**

  返回一个用于描述构造器、方法或域的修饰符的整型数值。使用 Modifier 类中的这个方法可以分析这个返回值。

+ **String getName()**

  返回一个用于描述构造器、方法或域名的字符串。

+ **Class[] getParameterTypes()**  (在 Constructor 和 Method 类中)

  返回一个用于描述参数类型的 Class 对象数组。

+ **Class getReturnType()**   （在 Method 类中）

  返回一个用于描述返回类型的 Class 对象。

#### 2.5 java.lang.reflect.Modifier    1.1

+ **static String toString(int modifiers)**

  返回对应 modifiers 中位设置的修饰符的字符串表示。

+ **static boolean isAbstract(int modifiers)**

+ **static boolean isFinal(int modifiers)**

+ **static boolean isInterface(int modifiers)**

+ **statiic boolean isNative(int modifiers)**

+ **static boolean isPrivate(int modifiers)**

+ **static boolean isProtected(int modifiers)**

+ **static boolean isPublic(int modifiers)**

+ **static boolean isStatic(int modifiers)**

+ **static boolean isStrict(int modifiers)**

+ **static boolean isSynchronized(int modifiers)**

+ **static boolean isVolatile(int modifiers)**

  这些方法将检测方法名对应的修饰符在 modifiers 值中的位。

