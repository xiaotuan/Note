执行 `git add -p` 命令可以对一个文件内的修改进行有选择性的添加到暂存区：

```shell
git add -p 
```

例如：

```shell
$ git add -p
diff --git a/Android/Android Project/编译/Android13代码介绍.md b/Android/Android Project/编译/Android13代码介绍.md
index 0be7d1c0..7705081d 100644
--- a/Android/Android Project/编译/Android13代码介绍.md
+++ b/Android/Android Project/编译/Android13代码介绍.md
@@ -10,6 +10,8 @@ $ git submodule foreach git checkout master

 整个代码有3个仓库：

+修改1
+
 + `mtk_sp_t0/.git`： 主仓库，只管理编译脚本等⽂件

 + `mtk_sp_t0/vnd/.git`： `vendor`⼦仓库，就是我们维护的仓库 对应地址
(1/3) Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]? n
@@ -19,7 +21,7 @@ $ git submodule foreach git checkout master
   `git@192.168.0.24:mtk/mtk_t_mssi.git`

 ### 2、更新代码
-+ `cd mtk_sp_t0; git pull --rebase`： 更新主仓库脚本类
++ `cd mtk_sp_t0; git pull --rebase`： 修改2更新主仓库脚本类

 + `cd mtk_sp_t0/vnd;git pull --rebase`： 更新vendor仓库

(2/3) Stage this hunk [y,n,q,a,d,K,j,J,g,/,e,?]? n
@@ -39,7 +41,7 @@ Split Build 1.0 ( MT8321 MT8765 MT8766 MT8768 MT8183 MT8788 适⽤)
 cd vnd ; source build/envsetup.sh && export OUT_DIR=out && lunch vnd_tb8766p1_64_bsp-userdebug M869YCR100_YM_546 && make krn_images vnd_images
 ```

-WB_PROJECT对应vnd/weibu/tb8766p1_64_bsp/M866YA_WB_420，如果不存在则报错
+WB_PROJECT对应vnd/weibu/tb8766p1_64_bsp/M866YA_WB_420，如果不存在则报错 修改3

 #### 3.2 编译 mssi

(3/3) Stage this hunk [y,n,q,a,d,K,g,/,e,?]? y

```

> 注意：该命令只对版本库中的文件有用，新增文件没有作用。