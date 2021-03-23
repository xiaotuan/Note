#### B.5.6　浮点特性： `float.h` 

`float.h` 头文件中定义了一些表示各种限制和形参的宏。表B.5.9列出了这些宏，C11新增的宏以斜体并缩进标出。许多宏都涉及下面的浮点表示模型：



![104.gif](../images/104.gif)
如果第1个数f<sub class="my_markdown">1</sub>是非 `0` （且 `x` 是非 `0` ），该数字被称为标准化浮点数。附录B的参考资料VIII中将更详细地解释一些宏。

<center class="my_markdown"><b class="my_markdown">表B.5.9　 `float.h` 宏</b></center>

| 宏 | 含义 |
| :-----  | :-----  | :-----  | :-----  |
| `FLT_ROUNDS` | 默认舍入方案 |
| `FLT_EVAL_METHOD` | 浮点表达式求值的默认方案 |
| `FLT_HAS_SUBNORM` | 存在或缺少 `float` 类型的反常值 |
| `DBL_HAS_SUBNORM` | 存在或缺少 `double` 类型的反常值 |
| `LDBL_HAS_SUBNORM` | 存在或缺少 `long double` 类型的反常值 |
| `FLT_RADIX` <sup class="my_markdown">[1]</sup> | 指数表示法中使用的进制数 `(b)` ，最小值为 `2` |
| `FLT_MANT_DIG` | 以 `FLT_RADIX` 进制表示的 `float` 类型数的位数（模型中的 `p` ） |
| `DBL_MANT_DIG` | 以 `FLT_RADIX` 进制表示的 `double` 类型数的位数（模型中的 `p` ） |
| `LDBL_MANT_DIG` | 以 `FLT_RADIX` 进制表示的 `long double` 类型数的位数（模型中的 `p` ） |
| `FLT_DECIMAL_DIG` | 在 `b` 进制和十进制相互转换不损失精度的前提下， `float` 类型的十进制数的位数（最小值是 `6` ） |
| `DBL_DECIMAL_DIG` | 在 `b` 进制和十进制相互转换不损失精度的前提下， `double` 类型的十进制数的位数（最小值是 `10` ） |
| `LDBL_DECIMAL_DIG` | 在 `b` 进制和十进制相互转换不损失精度的前提下， `long double` 类型的十进制数的位数（最小值是 `10` ） |
| `DECIMAL_DIG` | 在 `b` 进制与十进制相互转换不损失精度的前提下，浮点类型十进制数的最大个数（最小值为 `10` ） |
| `FLT_DIG` | 在不损失精度的前提下， `float` 类型可表示的十进制数位数（最小值为 `6` ） |
| `DBL_DIG` | 在不损失精度的前提下， `double` 类型可表示的十进制数位数（最小值为 `10` ） |
| `LDBL_DIG` | 在不损失精度的前提下， `long double` 类型可表示的十进制数位数（最小值为 `10` ） |
| `FLT_MIN_EXP` | `float` 类型 `e` 表示法，指数的最小负正整数值 |
| `DBL_MIN_EXP` | `double` 类型 `e` 表示法，指数的最小负正整数值 |
| `LDBL_MIN_EXP` | `long double` 类型 `e` 表示法，指数的最小负正整数值 |
| `FLT_MIN_10_EXP` | 用 `10` 的 `x` 次幂表示规范化 `float` 类型数时， `x` 的最小负整数值（不超过 `-37` ） |
| `DBL_MIN_10_EXP` | 用 `10` 的 `x` 次幂表示规范化 `double` 类型数时， `x` 的最小负整数值（不超过 `-37` ） |
| `LDBL_MIN_10_EXP` | 用 `10` 的 `x` 次幂表示规范化 `long double` 类型数时， `x` 的最小负整数值（不超过 `-37` ） |
| `FLT_MAX_EXP` | `float` 类型 `e` 表示法，指数的最大正整数值 |
| `DBL_MAX_EXP` | `double` 类型 `e` 表示法，指数的最大正整数值 |
| `LDBL_MAX_EXP` | `long double` 类型 `e` 表示法，指数的最大正整数值 |
| `FLT_MAX_10_EXP` | 用 `10` 的 `x` 次幂表示规范化 `float` 类型数时， `x` 的最大正整数值（至少 `+37` ） |
| `DBL_MAX_10_EXP` | 用 `10` 的 `x` 次幂表示规范化 `double` 类型数时， `x` 的最大正整数值（至少 `+37` ） |
| `LDBL_MAX_10_EXP` | 用 `10` 的 `x` 次幂表示规范化 `long double` 类型数时， `x` 的最大正整数值（至少 `+37` ） |
| `FLT_MAX` | `float` 类型的最大有限值（至少 `1E+37` ） |
| `DBL_MAX` | `doble` 类型的最大有限值（至少 `1E+37` ） |
| `LDBL_MAX` | `long double` 类型的最大有限值（至少 `1E+37` ） |
| `FLT_EPSILON` | `float` 类型比 `1` 大的最小值与 `1` 的差值（不超过 `1E-9` ） |
| `DBL_EPSILON` | `double` 类型比 `1` 大的最小值与 `1` 的差值（不超过 `1E-9` ） |
| `LDBL_EPSILON` | `long double` 类型比 `1` 大的最小值与 `1` 的差值（不超过 `1E-9` ） |
| `FLT_MIN` | 标准化 `float` 类型的最小正值（不超过 `1E-37` ） |
| `DBL_MIN` | 标准化 `double` 类型的最小正值（不超过 `1E-37` ） |
| `LDBL_MIN` | 标准化 `long double` 类型的最小正值（不超过 `1E-37` ） |
| `FLT_TRUE_MIN` | `float` 类型的最小正值（不超过 `1E-37` ） |
| `DBL_TRUE_MIN` | `double` 类型的最小正值（不超过 `1E-37` ） |
| `LDBL_TRUE_MIN` | `long double` 类型的最小正值（不超过 `1E-37` ） |

