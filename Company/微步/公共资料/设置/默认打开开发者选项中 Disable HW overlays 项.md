[toc]

### 1. 展讯平台

#### 1.1 Android R

修改  `frameworks/native/services/surfaceflinger/SurfaceFlinger.h` 文件，将 `mDebugDisableHWC` 变量的值设置成 `true` 即可：

```c
// don't use a lock for these, we don't care
int mDebugRegion = 0;
bool mDebugDisableHWC = true;
bool mDebugDisableTransformHint = false;
```

> 注意：上面的修改只是默认为打开 `Disable HW overlay` 选项，当用户关闭后再次开机该选项会是关闭状态，如下需要每次开机都打开该选项可以参照如下方法：
>
> 1. 在 `init.rc` 中加入：
>
>    ```rc
>    #add by eliot shao for bootup shutdown     dis_hwoverlay
>    service hwoverlay /system/bin/dis_hwoverlay.sh
>        class main
>        user system
>        disabled
>        oneshot
>    on property:sys.boot_completed=1
>        start hwoverlay
>    ```
>
> 2. 打包：./mk hexing72_cwet_lca bootimage
>
> 3. 把 dis_hwoverlay.sh 脚本 push 到 /system/bin/ 下面，dis_hwoverlay.sh 内容：
>
>    ```shell
>    
>    #!/system/bin/sh
>     
>    (while :
>    do
>        sf=$(service list | grep -c "SurfaceFlinger")
>     
>        if [ $sf -eq 1 ]
>        then
>            service call SurfaceFlinger 1008 i32 1
>            break
>        else
>            sleep 2
>        fi
>    done
>    ```



