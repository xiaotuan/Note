### 18.4.2　Retrofit封装

Retrofit是Square开发的一款用于网络请求的开源库，默认使用OKHttp作为底层HTTP Client。Retrofit专注于接口的封装，而OKHttp则专注于网络请求，二者分工协作。

在项目开发过程中，Retrofit通常需要与RxAndroid配合使用，而二者的完美结合也让Android的开发效率提高不少，同时代码也变得清晰易读。虽然Retrofit已经考虑了大部分的基础情况，但在实际项目开发过程中，还是需要结合实际情况进行二次封装，例如设置请求头、请求函数体等。下面是本视频项目二次封装的代码。

```python
object RetrofitManager {
    private var client: OkHttpClient? = null
    private var retrofit: Retrofit? = null
    val service: ApiService by lazy { getRetrofit()!!.create(ApiService::class. java) }
    private var token: String by PreferenceUtils("token", "")
    /**
     * 添加参数
     */
    private fun addQueryParameterInterceptor(): Interceptor {
        return Interceptor { chain ->
            val originalRequest = chain.request()
            val request: Request
            val modifiedUrl = originalRequest.url().newBuilder()
                    .addQueryParameter("phoneSystem", "")
                    .addQueryParameter("phoneModel", "")
                    .build()
            request = originalRequest.newBuilder().url(modifiedUrl).build()
            chain.proceed(request)
        }
    }
    /**
     * 设置请求头
     */
    private fun addHeaderInterceptor(): Interceptor {
        return Interceptor { chain ->
            val originalRequest = chain.request()
            val requestBuilder = originalRequest.newBuilder()
                    .header("token", token)
                    .method(originalRequest.method(), originalRequest.body())
            val request = requestBuilder.build()
            chain.proceed(request)
        }
    }
    /**
     * 获取Retrofit实例
     */
    private fun getRetrofit(): Retrofit? {
        if (retrofit == null) {
            synchronized(RetrofitManager::class.java) {
                if (retrofit == null) {
                 //获取Client实例
                 client = OkHttpClient.Builder()
                    .addInterceptor(addQueryParameterInterceptor())
                    .addInterceptor(addHeaderInterceptor())
                    .connectTimeout(60L, TimeUnit.SECONDS)
                    .readTimeout(60L, TimeUnit.SECONDS)
                    .writeTimeout(60L, TimeUnit.SECONDS)
                    .build()
                  // 获取Retrofit的实例
                  retrofit = Retrofit.Builder()
                     .baseUrl(ApiService.BASE_URL)
                     .client(client!!)
                     .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
                     .addConverterFactory(GsonConverterFactory.create())
                     .build()
                }
            }
        }
        return retrofit
    }
}
```

可以看到，RetrofitManager工具类使用代理模式来处理属性延迟加载，当需要发出网络请求的时候，只需要通过MVP模式的Model层具体函数发送具体的请求即可。例如，下面是HomeModel获取首页数据的函数定义。

```python
fun requestHomeData(num:Int):Observable<HomeBean>{
        return RetrofitManager.service.getFirstHomeData(num)
                .compose(IoMainScheduler())
    }
```

