​        SWStbParamService_sd 应用主要功能是提供第三方调用 DevInfoManager 对象的 getValue() 方法的远程调用接口。

其核心代码如下所示：

```java
private final IStbParmService.Stub mBinder = new IStbParmService.Stub() {

    @Override
    public String getStbParameter(String parmName) throws RemoteException {
        String parmValue = null;
        Log.d(TAG, "======================parmName:"+parmName);
        parmValue = mDevInfoManager.getValue(parmName);
        Log.d(TAG, "============parmValue="+parmValue);
        return parmValue;
    }
};
```

