假设你有一个 `C` 或者 `C++` 的程序，并且想要调用一些 `Java` 代码。调用 `API`（`invocation API`）使你能够把 `Java` 虚拟机嵌入到 `C` 或者 `C++` 程序中。下面是你初始化虚拟机所需的基本代码：

```c
JavaVMOption options[1];
JavaVMInitArgs vm_args;
JavaVM* jvm;
JNIEnv* env;

options[0].optionString = "-Djava.class.path=.";

memset(&vm_args, 0, sizeof(vm_args));
vm_args.version = JNI_VERSION_1_2;
vm_args.nOptions = 1;
vm_args.options = options;

JNI_CreateJavaVM(&jvm, (void**) &env, &vm_args);
```

可以给虚拟机提供任意数目的选项，这只需增加选项数组的大小和 `vm_args.nOptions` 的值。例如：

```c
options[i].optionString = "-Djava.compiler=NONE";
```

> 提示：当你陷入麻烦导致程序崩溃，从而不能初始化 `JVM` 或者不能装载你的类时，请打开 `JNI` 调试模式。设置一个选项如下：
>
> ```c
> options[i].optionString = "-verbose:jni";
> ```

一旦设置完虚拟机，只要按常规方法使用 `env` 指针即可。

只有在调用 `invocation API` 中的其他函数时，才需要 `jvm` 指针。目前，只有四个这样的函数。最重要的一个是终止虚拟机的函数：

```c
(*jvm)->DestroyJavaVM(jvm);
```

遗憾的是，在 `Windows` 下，动态链接到 `jre/bin/client/jvm.dll` 中的 `JNI_CreateJavaVM` 函数变得非常困难，因为 `Vista` 改变了链接规则，而 `Oracle` 的类库仍旧依赖于旧版本的 `C` 运行时类库。下面示例程序通过手工加载该类库解决了这个问题，这种方式与 `Java` 程序所使用的方式一样，请参阅 `JDK` 中的 `src.jar` 文件里的 `launcher/java_md.c` 文件。（在开始启用测试程序之前，需要将 `Welcome.java` 文件放置到与 `c` 文件同一个目录中，并编译好 `Welcome.jav` 文件）。

>注意：这个示例代码在 `Windows` 中并不能执行成功，如果开启 `_WINDOWS` 宏后，还需要修改代码，传递正确 `Windows API` 方法对应的参数类型才能获取到正确的值。

**示例程序：InvocationTest.c**

```c
/**
   @version 1.20 2007-10-26
   @author Cay Horstmann
*/

#include <jni.h>
#include <stdlib.h>

#ifdef _WINDOWS

#include <windows.h>
static HINSTANCE loadJVMLibrary(void);
typedef jint (JNICALL *CreateJavaVM_t)(JavaVM **, void **, JavaVMInitArgs *);

#endif

int main()
{  
   JavaVMOption options[2];
   JavaVMInitArgs vm_args;
   JavaVM *jvm;
   JNIEnv *env;
   long status;

   jclass class_Welcome;
   jclass class_String;
   jobjectArray args;
   jmethodID id_main;

#ifdef _WINDOWS
   HINSTANCE hjvmlib;
   CreateJavaVM_t createJavaVM;
#endif

   options[0].optionString = "-Djava.class.path=.";

   memset(&vm_args, 0, sizeof(vm_args));
   vm_args.version = JNI_VERSION_1_2;
   vm_args.nOptions = 1;
   vm_args.options = options;


#ifdef _WINDOWS   
   hjvmlib = loadJVMLibrary();
   createJavaVM = (CreateJavaVM_t) GetProcAddress(hjvmlib, "JNI_CreateJavaVM");
   status = (*createJavaVM)(&jvm, (void **) &env, &vm_args);
#else
   status = JNI_CreateJavaVM(&jvm, (void **) &env, &vm_args);
#endif

   if (status == JNI_ERR)
   {  
      fprintf(stderr, "Error creating VM\n");
      return 1;
   }

   class_Welcome = (*env)->FindClass(env, "Welcome");
   id_main = (*env)->GetStaticMethodID(env, class_Welcome, "main", "([Ljava/lang/String;)V");

   class_String = (*env)->FindClass(env, "java/lang/String");
   args = (*env)->NewObjectArray(env, 0, class_String, NULL);
   (*env)->CallStaticVoidMethod(env, class_Welcome, id_main, args);

   (*jvm)->DestroyJavaVM(jvm);

   return 0;
}

#ifdef _WINDOWS

static int GetStringFromRegistry(HKEY key, const char *name, char *buf, jint bufsize)
{
   DWORD type, size;

   return RegQueryValueEx(key, name, 0, &type, 0, &size) == 0
      && type == REG_SZ
      && size < (unsigned int) bufsize
      && RegQueryValueEx(key, name, 0, 0, buf, &size) == 0;
}

static void GetPublicJREHome(char *buf, jint bufsize)
{
   HKEY key, subkey;
   char version[MAX_PATH];

   /* Find the current version of the JRE */
   char *JRE_KEY = "Software\\JavaSoft\\Java Runtime Environment";
   if (RegOpenKeyEx(HKEY_LOCAL_MACHINE, JRE_KEY, 0, KEY_READ, &key) != 0) 
   {
      fprintf(stderr, "Error opening registry key '%s'\n", JRE_KEY);
      exit(1);
   }

   if (!GetStringFromRegistry(key, "CurrentVersion", version, sizeof(version))) 
   {
      fprintf(stderr, "Failed reading value of registry key:\n\t%s\\CurrentVersion\n", JRE_KEY);
      RegCloseKey(key);
      exit(1);
   }

   /* Find directory where the current version is installed. */
   if (RegOpenKeyEx(key, version, 0, KEY_READ, &subkey) != 0) 
   {
     fprintf(stderr, "Error opening registry key '%s\\%s'\n", JRE_KEY, version);
      RegCloseKey(key);
      exit(1);
   }

   if (!GetStringFromRegistry(subkey, "JavaHome", buf, bufsize)) 
   {
      fprintf(stderr, "Failed reading value of registry key:\n\t%s\\%s\\JavaHome\n", 
         JRE_KEY, version);
      RegCloseKey(key);
      RegCloseKey(subkey);
      exit(1);
   }

   RegCloseKey(key);
   RegCloseKey(subkey);
}

static HINSTANCE loadJVMLibrary(void)
{
   HINSTANCE h1, h2;
   char msvcdll[MAX_PATH];
   char javadll[MAX_PATH];
   GetPublicJREHome(msvcdll, MAX_PATH);   
   strcpy(javadll, msvcdll);
   strncat(msvcdll, "\\bin\\msvcr71.dll", MAX_PATH - strlen(msvcdll));
   msvcdll[MAX_PATH - 1] = '\0';
   strncat(javadll, "\\bin\\client\\jvm.dll", MAX_PATH - strlen(javadll));
   javadll[MAX_PATH - 1] = '\0';

   h1 = LoadLibrary(msvcdll);
   if (h1 == NULL)
   {
      fprintf(stderr, "Can't load library msvcr71.dll\n");
      exit(1);
   }

   h2 = LoadLibrary(javadll);
   if (h2 == NULL)
   {
      fprintf(stderr, "Can't load library jvm.dll\n");
      exit(1);
   }
   return h2;
}

#endif
```

**Welcome.java**

```java
/**
 * @version 1.20 2004-02-28
 * @author Cay Horstmann
 */
public class Welcome
{
   public static void main(String[] args)
   {
      String[] greeting = new String[3];
      greeting[0] = "Welcome to Core Java";
      greeting[1] = "by Cay Horstmann";
      greeting[2] = "and Gary Cornell";

      for (String g : greeting)
         System.out.println(g);
   }
}
```

要在 `Linux` 下编译该程序，请用：

```shell
gcc -I jdk/include -I jdk/include/linux -o InvocationTest -L jdk/jre/lib/i386/client -ljvm InvocationTest.c
```

在 `Solaris` 下，请用：

```shell
cc -I jdk/include -I jdk/include/solaris -o InvocationTest -L jdk/jre/lib/sparc -ljvm InvocationTest.c
```

在 `Windows` 下用微软的 `C` 编译器时，请用下面的命令行：

```shell
cl -D_WINDOWS -I jdk\include -I jdk\include\win32 InvocationTest.c jdk\lib\jvm.lib  advapi32.lib
```

需要确保 `INCLUDE` 和 `LIB` 环境变量包含了 `Windows API` 头文件和库文件的路径。

用 `Cygwin` 时，用下面的语句进行编译：

```shell
gcc -D_WINDOWS -mno-cygwin -I jdk\include -I jdk\include\win32 -D__int64="long long" -I c:\cygwin\usr\include\w32api -o InvocationTest
```

在 `Linux/UNIX` 下运行该程序之前，需要确保 `LD_LIBRARY_PATH` 包含了共享类库的目录。例如，如果使用 `Linux` 上的 `bash` 命令行，则需要执行下面的命令：

```shell
export LD_LIBRARY_PATH=jdk/jre/lib/i386/client:$LD_LIBRARY_PATH
```



