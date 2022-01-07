在实际应用中，应该为整个应用程序创建一个 `HttpClient`，并将其用于所有 HTTP 通信。应该注意在通过同一个 `HttpClient` 同时发出多个请求时可能发生的多线程问题。可以使用 `ThreadSafeClientConnManager` 创建 `DefaultHttpClient` 来解决多线程问题。

