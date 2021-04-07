### 9.2　与标准Python客户端建立数据库接口

有很多重要的数据库遵从Python数据库API规范2.0版本，包括MySQL、PostgreSQL、Oracle、Microsoft SQL Server和SQLite。它们的驱动一般都比较复杂且久经考验，如果为Twisted重新实现的话则是巨大的浪费。人们可以在Twisted应用中使用这些数据库客户端，比如在Scrapy使用 `twisted.enterprise.adbapi` 库。我们将使用MySQL作为示例演示其使用，不过对于任何其他兼容的数据库来说，也可以应用相同的原则。

