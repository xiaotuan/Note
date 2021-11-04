[toc]

### 应用场景

有时候，我们需要将自己对某个问题的修改分享给同事，这时如果能够提供修改前的代码和修改后的代码，将会帮助同事更好的理解或合入该问题的修改代码。

### 需求

将修改前的代码放置在 `before` 的文件夹中，将修改后的代码放置 `after` 的文件夹中，修改的文件按照文件原始的目录结构放置，并将 `before` 和 `after` 文件夹打包到 `diff.zip` 压缩包中。例如，有一条提交记录：

```shell
commit 820b9c9cc644ac3f126f62f5f6d0be1e88cd5979
Author: QinTuanye <qintuanye@weibu.com>
Date:   Mon Nov 1 19:15:57 2021 +0800

    [Message]: 解决锁卡解锁密码长度不足问题
    [Project]:m863ur200_64-YBT-MMI
    [Side Effects]:no
    [Self Test]:yes
    [Author]：QinTuanye

 weibu/m863u_bsp_64/m863ur200_64-YBT-MMI/vendor/mediatek/proprietary/packages/apps/SystemUI/src/com/mediatek/keyguard/Telephony/KeyguardSimPinPukMeView.java | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

现在需要创建 `diff` 目录，将 `KeyguardSimPinPukMeView.java` 文件修改前的内容保存在

`diff/before/weibu/m863u_bsp_64/m863ur200_64-YBT-MMI/vendor/mediatek/proprietary/packages/apps/SystemUI/src/com/mediatek/keyguard/Telephony/KeyguardSimPinPukMeView.java` 中，将修改后的文件内容保存在 `diff/after/weibu/m863u_bsp_64/m863ur200_64-YBT-MMI/vendor/mediatek/proprietary/packages/apps/SystemUI/src/com/mediatek/keyguard/Telephony/KeyguardSimPinPukMeView.java` 中。

