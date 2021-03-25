### G.4　set和map的其他操作

关联容器（集合和映射是这种容器的模型）带有模板参数Key和Compare，这两个参数分别表示用来对内容进行排序的键类型和用于对键值进行比较的函数对象（被称为比较对象）。对于set和multiset容器，存储的键就是存储的值，因此键类型与值类型相同。对于map和multimap容器，存储的值（模板参数T）与键类型（模板参数Key）相关联，值类型为pair<const Key, T>。关联容器有其他成员来描述这些特性，如表G.9所示。

<center class="my_markdown"><b class="my_markdown">表G.9　为关联容器定义的类型</b></center>

| 类型 | 值 |
| :-----  | :-----  | :-----  | :-----  |
| X::key_type | Key，键类型 |
| X::key_compare | Compare，默认为less<key_type> |
| X::value_compare | 二元谓词类型，与set和multiset的key_compare相同，为map或multimap容器中的pair<const Key, T>值提供了排序功能 |
| X::mapped_type | T，关联数据类型（仅限于map和multimap） |

关联容器提供了表G.10列出的方法。通常，比较对象不要求键相同的值是相同的；等价键（equivalent key）意味着两个值（可能相同，也可能不同）的键相同。在该表中，X为容器类，a是类型为X的对象。如果X使用唯一键（即为set或map），则a_uniq将是类型为X的对象。如果x使用多个键（即为multiset或multimap），则a_eq将是类型为X的对象。和前面一样，i和j也是指向value_type元素的输入迭代器，[i, j]是一个有效的区间，p和q2是指向a的迭代器，q和q1是指向a的可解除引用的迭代器，[q1, q2]是有效区间，t是X::value_type值（可能是一对），k是X::key_type值，而il是initializer_list<value_type>对象。

<center class="my_markdown"><b class="my_markdown">表G.10　为set、multiset、map和multimap定义的操作</b></center>

| 操作 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| X(i, j, c) | 创建一个空容器，插入区间[i, j]中的元素，并将c用作比较对象 |
| X a(i, j, c) | 创建一个名为a的空容器，插入区间[i, j]中的元素，并将c用作比较对象 |
| X(i, j) | 创建一个空容器，插入区间[i, j]中的元素，并将Compare()用作比较对象 |
| X a(i, j) | 创建一个名为a的空容器，插入区间[i, j]中的元素，并将Compare()用作比较对象 |
| X(il); | 等价于X(il.begin(), il.end()) |
| a = il | 将区间[il.begin(), il.end()]的内容赋给a |
| a.key_comp() | 返回在构造a时使用的比较对象 |
| a.value_comp() | 返回一个value_compare对象 |
| a_uniq.insert(t) | 当且仅当a不包含具有相同键的值时，将t值插入到容器a中。该方法返回一个pair<iterator, bool>值。如果进行了插入，则bool的值为true，否则为false。iterator指向键与t相同的元素 |
| a_eq.insert(t) | 插入t并返回一个指向其位置的迭代器 |
| a.insert(p, t) | 将p作为insert()开始搜索的位置，将t插入。如果a是键唯一的容器，则当且仅当a不包含拥有相同键的元素时，才插入；否则，将进行插入。无论是否进行了插入，该方法都将返回一个迭代器，该迭代器指向拥有相同键的位置 |
| a.insert(i, j) | 将区间[i, j]中的元素插入到a中 |
| a.insert(il) | 将initializer_list il中的元素插入到a中 |
| a_uniq.emplace(args) | 类似于a_uniq.insert(t)，但使用参数列表与参数包args的内容匹配的构造函数 |
| a_eq.emplace(args) | 类似于a_eq.insert(t)，但使用参数列表与参数包args的内容匹配的构造函数 |
| a.emplace_hint(args) | 类似于a.insert(p, t)，但使用参数列表与参数包args的内容匹配的构造函数 |
| a.erase(k) | 删除a中键与k相同的所有元素，并返回删除的元素数目 |
| a.erase(q) | 删除q指向的元素 |
| a.erase(q1, q2) | 删除区间[q1, q2)中的元素 |
| a.clear() | 与erase(a.begin(), a.end())等效 |
| a.find(k) | 返回一个迭代器，该迭代器指向键与k相同的元素；如果没有找到这样的元素，则返回a.end() |
| a.count(k) | 返回键与k相同的元素的数量 |
| a.lower_bound(k) | 返回一个迭代器，该迭代器指向第一个键不小于k的元素 |
| a.upper_bound(k) | 返回一个迭代器，该迭代器指向第一个键大于k的元素 |
| a.equal_range(k) | 返回第一个成员为a.lower_bound(k)，第二个成员为a.upper_bound(k)的值对 |
| a.operator | 返回一个引用，该引用指向与键k关联的值（仅限于map容器） |

