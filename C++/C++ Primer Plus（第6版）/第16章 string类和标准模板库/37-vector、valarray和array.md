### 16.7.1　vector、valarray和array

您可能会问，C++为何提供三个数组模板：vector、valarray和array。这些类是由不同的小组开发的，用于不同的目的。vector模板类是一个容器类和算法系统的一部分，它支持面向容器的操作，如排序、插入、重新排列、搜索、将数据转移到其他容器中等。而valarray类模板是面向数值计算的，不是STL的一部分。例如，它没有push_back()和insert()方法，但为很多数学运算提供了一个简单、直观的接口。最后，array是为替代内置数组而设计的，它通过提供更好、更安全的接口，让数组更紧凑，效率更高。Array表示长度固定的数组，因此不支持push_back()和insert()，但提供了多个STL方法，包括begin()、end()、rbegin()和rend()，这使得很容易将STL算法用于array对象。

例如，假设有如下声明：

```css
vector<double> ved1(10), ved2(10), ved3(10);
array<double, 10> vod1, vod2, vod3;
valarray<double> vad1(10), vad2(10), vad3(10);
```

同时，假设ved1、ved2、vod1、vod2、vad1和vad2都有合适的值。要将两个数组中第一个元素的和赋给第三个数组的第一个元素，使用vector类时，可以这样做：

```css
transform(ved1.begin(), ved1.end(), ved2.begin(), ved3.begin(),
          plus<double>());
```

对于array类，也可以这样做：

```css
transform(vod1.begin(), vod1.end(), vod2.begin(), vod3.begin(),
          plus<double>());
```

然而，valarray类重载了所有算术运算符，使其能够用于valarray对象，因此您可以这样做：

```css
vad3 = vad1 + vad2; // + overloaded
```

同样，下面的语句将使vad3中每个元素都是vad1和vad2中相应元素的乘积：

```css
vad3 = vad1 * vad2; // * overloaded
```

要将数组中每个元素的值扩大2.5倍，STL方法如下：

```css
transform(ved3.begin(), ved3.end(), ved3.begin(),
          bind1st(multiplies<double>(), 2.5));
```

valarray类重载了将valarray对象乘以一个值的运算符，还重载了各种组合赋值运算符，因此可以采取下列两种方法之一：

```css
vad3 = 2.5 * vad3; // * overloaded
vad3 *= 2.5; // *= overloaded
```

假设您要计算数组中每个元素的自然对数，并将计算结果存储到另一个数组的相应元素中，STL方法如下：

```css
transform(ved1.begin(), ved1.end(), ved3.begin(),
          log);
```

valarray类重载了这种数学函数，使之接受一个valarray参数，并返回一个valarray对象，因此您可以这样做：

```css
vad3 = log(vad1); // log() overloaded
```

也可以使用apply()方法，该方法也适用于非重载函数：

```css
vad3 = vad1.apply(log);
```

方法apply()不修改调用对象，而是返回一个包含结果的新对象。

执行多步计算时，valarray接口的简单性将更为明显：

```css
vad3 = 10.0* ((vad1 + vad2) / 2.0 + vad1 * cos(vad2));
```

有关使用STL vector来完成上述计算的代码留给您去完成。

valarray类还提供了方法sum()（计算valarray对象中所有元素的和）、size()（返回元素数）、max()（返回最大的元素值）和min()（返回最小的元素值）。

正如您看到的，对于数学运算而言，valarray类提供了比vector更清晰的表示方式，但通用性更低。valarray类确实有一个resize()方法，但不能像使用vector的push_back时那样自动调整大小。没有支持插入、排序、搜索等操作的方法。总之，与vector类相比，valarray类关注的东西更少，但这使得它的接口更简单。

valarray的接口更简单是否意味着性能更高呢？在大多数情况下，答案是否定的。简单表示法通常是使用类似于您处理常规数组时使用的循环实现的。然而，有些硬件设计允许在执行矢量操作时，同时将一个数组中的值加载到一组寄存器中，然后并行地进行处理。从原则上说，valarray操作也可以实现成利用这样的设计。

可以将STL功能用于valarray对象吗？通过回答这个问题，可以快速地复习一些STL原理。假设有一个包含10个元素的valarray<double>对象：

```css
valarray<double> vad(10);
```

使用数字填充该数组后，能够将STL sort()函数用于该数组吗？valarray类没有begin()和end()方法，因此不能将它们用作指定区间的参数：

```css
sort(vad.begin(), vad.end()); // NO, no begin(), end()
```

另外，vad是一个对象，而不是指针，因此不能像处理常规数组那样，使用vad和vad + 10作为区间参数，即下面的代码不可行：

```css
sort(vad, vad + 10); // NO, vad an object, not an address
```

可以使用地址运算符：

```css
sort(&vad[0], &vad[10]); // maybe?
```

但valarray没有定义下标超过尾部一个元素的行为。这并不一定意味着使用&vad[10]不可行。事实上，使用6种编译器测试上述代码时，都是可行的；但这确实意味着可能不可行。为让上述代码不可行，需要一个不太可能出现的条件，如让数组与预留给堆的内存块相邻。然而，如果3.85亿的交易命悬于您的代码，您可能不想冒代码出现问题的风险。

为解决这种问题，C++11提供了接受valarray对象作为参数的模板函数begin()和end()。因此，您将使用begin(vad)而不是vad.begin。这些函数返回的值满足STL区间需求：

```css
sort(begin(vad), end(vad)); // C++11 fix!
```

程序清单16.20演示了vector和valarray类各自的优势。它使用vector的push_back()方法和自动调整大小的功能来收集数据，然后对数字进行排序后，将它们从vector对象复制到一个同样大小的valarray对象中，再执行一些数学运算。

程序清单16.20　valvect.cpp

```css
// valvect.cpp -- comparing vector and valarray
#include <iostream>
#include <valarray>
#include <vector>
#include <algorithm>
int main()
{
    using namespace std;
    vector<double> data;
    double temp;
    cout << "Enter numbers (<=0 to quit):\n";
    while (cin >> temp && temp > 0)
        data.push_back(temp);
    sort(data.begin(), data.end());
    int size = data.size();
    valarray<double> numbers(size);
    int i;
    for (i = 0; i < size; i++)
        numbers[i] = data[i];
    valarray<double> sq_rts(size);
    sq_rts = sqrt(numbers);
    valarray<double> results(size);
    results = numbers + 2.0 * sq_rts;
    cout.setf(ios_base::fixed);
    cout.precision(4);
    for (i = 0; i < size; i++)
    {
        cout.width(8);
        cout << numbers[i] << ": ";
        cout.width(8);
        cout << results[i] << endl;
    }
    cout << "done\n";
    return 0;
}
```

下面是程序清单16.20中程序的运行情况：

```css
3.3 1.8 5.2 10 14.4 21.6 26.9 0
  1.8000:  4.4833
  3.3000:  6.9332
  5.2000:  9.7607
 10.0000: 16.3246
 14.4000: 21.9895
 21.6000: 30.8952
 26.9000: 37.2730
done
```

除前面讨论的外，valarray类还有很多其他特性。例如，如果numbers是一个valarray<double>对象，则下面的语句将创建一个bool数组，其中vbool[i]被设置为numbers[i] > 9的值，即true或false：

```css
valarray<bool> vbool = numbers > 9;
```

还有扩展的下标指定版本，来看其中的一个——slice类。slice类对象可用作数组索引，在这种情况下，它表的不是一个值而是一组值。slice对象被初始化为三个整数值：起始索引、索引数和跨距。起始索引是第一个被选中的元素的索引，索引数指出要选择多少个元素，跨距表示元素之间的间隔。例如，slice(1, 4, 3)创建的对象表示选择4个元素，它们的索引分别是1、4、7和10。也就是说，从起始索引开始，加上跨距得到下一个元素的索引，依此类推，直到选择了4个元素。如果varint是一个valarray<int>对象，则下面的语句将把第1、4、7、10个元素都设置为10：

```css
varint[slice(1,4,3)] = 10; // set selected elements to 10
```

这种特殊的下标指定功能让您能够使用一个一维valarray对象来表示二维数据。例如，假设要表示一个4行3列的数组，可以将信息存储在一个包含12个元素的valarray对象中，然后使用一个slice(0, 3, 1)对象作为下标，来表示元素0、1和2，即第1行。同样，下标slice(0, 4, 3)表示元素0、3、6和9，即第一列。程序清单16.21演示了slice的一些特性。

程序清单16.21　vslice.cpp

```css
// vslice.cpp -- using valarray slices
#include <iostream>
#include <valarray>
#include <cstdlib>
const int SIZE = 12;
typedef std::valarray<int> vint; // simplify declarations
void show(const vint & v, int cols);
int main()
{
    using std::slice;   // from <valarray>
    using std::cout;
    vint valint(SIZE); // think of as 4 rows of 3
    int i;
    for (i = 0; i < SIZE; ++i)
        valint[i] = std::rand() % 10;
    cout << "Original array:\n";
    show(valint, 3);                     // show in 3 columns
    vint vcol(valint[slice(1,4,3)]); // extract 2nd column
    cout << "Second column:\n";
    show(vcol, 1);                       // show in 1 column
    vint vrow(valint[slice(3,3,1)]); // extract 2nd row
    cout << "Second row:\n";
    show(vrow, 3);
    valint[slice(2,4,3)] = 10;         // assign to 2nd column
    cout << "Set last column to 10:\n";
    show(valint, 3);
    cout << "Set first column to sum of next two:\n";
    // + not defined for slices, so convert to valarray<int>
    valint[slice(0,4,3)] = vint(valint[slice(1,4,3)])
                              + vint(valint[slice(2,4,3)]);
    show(valint, 3);
    return 0;
}
void show(const vint & v, int cols)
{
    using std::cout;
    using std::endl;
    int lim = v.size();
    for (int i = 0; i < lim; ++i)
    {
        cout.width(3);
        cout << v[i];
        if (i % cols == cols - 1)
            cout << endl;
        else
            cout << ' ';
    }
    if (lim % cols != 0)
        cout << endl;
}
```

对于valarray对象（如valint）和单个int元素（如valint[1]），定义了运算符+；但正如程序清单16.21指出的，对于使用slice下标指定的valarray单元，如valint[slice(1, 4, 3)，并没有定义运算符+。因此程序使用slice指定的元素创建一个完整的valint对象，以便能够执行加法运算：

```css
vint(valint[slice(1,4,3)]) // calls a slice-based constructor
```

valarray类提供了用于这种目的的构造函数。

下面是程序清单16.21中程序的运行情况：

```css
Original array:
  0   3   3
  2   9   0
  8   2   6
  6   9   1
Second column:
  3
  9
  2
  9
Second row:
  2   9   0
Set last column to 10:
  0   3  10
  2   9  10
  8   2  10
  6   9  10
Set first column to sum of next two:
 13   3  10
 19   9  10
 12   2  10
 19   9  10
```

由于元素值是使用rand()设置的，因此不同的rand()实现将设置不同的值。

另外，使用gslice类可以表示多维下标，但上述内容应足以让您对valarray有一定了解。

