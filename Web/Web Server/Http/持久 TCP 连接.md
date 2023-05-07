在 HTTP/1.1 请求头中，以下选项用来设定持久 TCP 连接的参数：

```
Connection: Keep-Alive
Keep-Alive: max=5, timout=120
```

HTTP/1.1 建立 TCP 连接后，默认情况下不会在处理完一个 HTTP 请求后立即断开，而是允许处理多个有序的 HTTP 请求。客户端如果想要关闭连接，可以在最后一个请求的请求头中，加上 "Connection: close" 选项来指定安全关闭这个连接，或者当连接闲置时间达到指定值时，也会自动断开连接。在以上范例代码中，max 参数指定一个 TCP 连接允许处理的最大 HTTP 请求数目，timeout 参数指定 TCP 连接的最长闲置时间。