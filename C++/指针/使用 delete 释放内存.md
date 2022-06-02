当需要内存时，可以使用 `new` 来请求；当不再使用 `new` 请求的内存时，需要使用 `delete` 运算符释放该内存。使用 `delete` 时，后面加上指向内存块的指针：

```cpp
int *ps = new int;	// allocate memory with new
...					// use the memory
delete ps;			// free memory with delete when done
```

> 警告：一定要配对地使用 `new` 和 `delete`；否则将发生内存泄漏。

不要尝试释放已经释放的内存块，C++ 标准指出，这样做的结果将是不确定的，这意味着什么情况都可能发生。另外，不能使用 `delete` 来释放声明变量所获得的内存：

```cpp
int *ps = new int;	// ok
delete ps;			// ok
delete ps;			// not ok now
int jugs = 5;		// ok
int *pi = &jugs;	// ok
delete pi;			// not allowed, memory not allocated by new
```

> 提示：只能用 `delete` 来释放使用 `new` 分配的内存。然而，对空指针使用 `delete` 是安全的。

> 注意：使用 `delete` 的关键在于，将它用于 `new` 分配的内存。这并不意味着要使用用于 `new` 的指针，而是用于 `new` 的地址：
>
> ```cpp
> int *ps = new int;	// allocate memory
> int *pq = ps;	// set second pointer to same block
> delete pq;	// delete with second pointer
> ```
>
> 一般来说，不要创建两个指向同一个内存块的指针，因为这将增加错误地删除同一个内存块两次的可能性。

