### 18.8　用Twilio发送短信

在本节中，你将学习如何注册免费的Twilio服务，并用它的Python模块发送短信。Twilio是一个“SMS网关服务”，这意味着它是一种服务——让你通过程序发送短信。虽然每月发送多少短信会有限制，并且文本前面会加上Sent from a Twilio trial account，但这项试用服务也许能满足你的个人程序。免费试用没有限期，不必升级到付费的套餐。

Twilio不是唯一的SMS网关服务。如果你不喜欢使用Twilio，可以在线搜索free sms gateway、python sms api，甚至twilio alternatives，寻找替代服务。

在注册Twilio账户之前，请在 Windows操作系统上用 `pip install--user-- upgrade twilio` 安装 `twilio` 模块（或在macOS和Linux操作系统上使用 `pip3` ）。附录A详细介绍了如何安装第三方模块。



**注意：**
本节特别针对美国。Twilio确实也在美国以外的国家提供手机短信服务。但 `twilio` 模块及其函数在美国以外的国家也能用。



