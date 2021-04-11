### 9.4　保存set-user-ID和保存set-group-ID

设计保存set-user-ID（saved set-user-ID）和保存set-group-ID (saved set-group-ID)，意在与set-user-ID和set-group-ID程序结合使用。当执行程序时，将会（依次）发生如下事件（在诸多事件之中）。

**1．** 若可执行文件的set-user-ID (set-group-ID)权限位已开启，则将进程的有效用户（组）ID置为可执行文件的属主。若未设置set-user-ID (set-group-ID)权限位，则进程的有效用户（组）ID将保持不变。

**2．** 保存set-user-ID和保存set-group-ID的值由对应的有效ID复制而来。无论正在执行的文件是否设置了set-user-ID或set-group-ID权限位，这一复制都将进行。

举例说明上述操作的效果，假设某进程的实际用户ID、有效用户ID和保存set-user-ID均为1000，当其执行了root用户（用户ID为0）拥有的set-user-ID程序后，进程的用户ID将发生如下变化：



![194.png](../images/194.png)
有不少系统调用，允许将set-user-ID程序的<sup class="my_markdown">②</sup>有效用户ID在实际用户ID和保存set-user-ID之间切换。针对set-group-ID程序对其进程有效组ID的修改，也有与之相类似的系统调用来支持。如此一来，对于与执行文件用户（组）ID相关的任何权限，程序能够随时 “收放自如”。（换言之，程序可以游走于两种状态之间：具备获取特权的潜力和以特权进行实际操作。）正如38.2节所述，只要set-user-ID程序和set-group-ID程序没有执行与特权级ID（亦即实际ID）相关的任何操作，就应将其置于非特权（即实际）ID的身份之下，这是一种安全的编程手法。

> 有时也将保存set-user-ID和保存set-group-ID称之为保存用户ID（saved user ID）和保存组ID（saved group ID）。
> 保存设置ID由System V首创，后为POSIX所采用。4.4之前的BSD版本不提供对此特性的支持。最初的POSIX.1标准将对这些ID的支持列为可选，但之后的版本（始于1988年诞生的FIPS 151-1 标准）则强制要求提供这一特性。

