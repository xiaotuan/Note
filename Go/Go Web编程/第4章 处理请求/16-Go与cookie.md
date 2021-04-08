### 4.4.1　Go与cookie

cookie在Go语言里面用 `Cookie` 结构表示，这个结构的定义如代码清单4-12所示。

代码清单4-12　 `Cookie` 结构的定义

```go
type Cookie struct {
　Name　　　 string
　Value　　　string
　Path　　　 string
　Domain　　 string
　Expires　　time.Time
　RawExpires string
　MaxAge　　 int
　Secure　　 bool
　HttpOnly　 bool
　Raw　　　　string
　Unparsed　 []string
}
```

没有设置 `Expires` 字段的cookie通常称为会话cookie或者临时cookie，这种cookie在浏览器关闭的时候就会自动被移除。相对而言，设置了 `Expires` 字段的cookie通常称为持久cookie，这种cookie会一直存在，直到指定的过期时间来临或者被手动删除为止。

`Expires` 字段和 `MaxAge` 字段都可以用于设置cookie的过期时间，其中 `Expires` 字段用于明确地指定cookie应该在什么时候过期，而 `MaxAge` 字段则指明了cookie在被浏览器创建出来之后能够存活多少秒。之所以会出现这两种截然不同的过期时间设置方式，是因为不同浏览器使用了各不相同的cookie实现机制，跟Go语言本身的设计无关。虽然HTTP 1.1中废弃了 `Expires` ，推荐使用 `MaxAge` 来代替 `Expires` ，但几乎所有浏览器都仍然支持 `Expires` ；而且，微软的IE 6、IE 7和IE 8都不支持 `MaxAge` 。为了让cookie在所有浏览器上都能够正常地运作，一个实际的方法是只使用 `Expires` ，或者同时使用 `Expires` 和 `MaxAge` 。

