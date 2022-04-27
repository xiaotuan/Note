可以使用 `delete` 运算符在使用完内存后，将其归还给内存池。使用 `delete` 时，后面要加上指向内存块的指针（这些内存块最长是用 new 分配的）：

```cpp
int *ps = new int;	// allocate memory with new
...					// use the memory
delete ps;			// free memory with delete when done
```

> 注意：使用 `delete` 运算符释放指针指向的内存，但不会删除指针本身。

> 警告：
>
> 1. 一定要配对地使用 `new` 和 `delete`；否则将发生内存泄漏。
>
> 2. 不要尝试释放已经释放的内存块，C++ 标准指出，这样做的结果将是不确定的。
>
> 3. 不能使用 `delete` 来释放声明变量所获得的内存。
>
>    ```cpp
>    int *ps = new int;	// OK
>    delete ps;	// OK
>    delete ps;	// not ok now
>    int jugs = 5;	// ok
>    int *pi = &jugs;	// ok
>    delete pi;	// not allowed, memory not allocated by new
>    ```
>
> 4. 对空指针使用 `delete` 是安全的。
>
> 5. 一般来说，不要创建两个指向同一个内存块的指针，因为这将增加错误地删除同一个内存块两次的可能。
>
>    ```cpp
>    int *ps = new int;	// allocate memory
>    int *pq = ps;	// set second pointer to same block
>    delete pq;	// delete with second pointer
>    ```

