Windows Azure SDK for Node 安装说明：<https://www.windowsazure.com/en-us/develop/nodejs/>。

以下是在 `Windows 7 webmatrix` 中集成并运行 `Node` 的步骤：

1. 安装 `WebMatrix`；
2. 使用最新的 `Windows` 安装包安装 `Node`；
3. 安装 `iisnode for IIS Express 7.x`，以便让 `Windows` 上的 IIS 支持 `Node` 应用程序；
4. 为 `WebMatrix` 安装 `Node` 模板，使用模板可以简化 `Node` 开发。

`WebMatrix` 的下载地址：<http://www.microsoft.com/Web/Webmatrix/>。

`iisnode` 的 `Github` 链接地址为： <https://github.com/tjanczuk/iisnode>。

如果需要安装 `iisnode` 的附带的示例代码，则需要以管理员权限打开命令窗口，进入到 `iisnode` 的安装目录中，然后运行名为 `setupsamples.bat` 的批处理文件。

最后还需要为 `WebMatrix` 下载并安装 `Node` 模板，这样就完成了 `webMatrix/Node` 的所有安装。`Node` 模板由 Steve Serson 创建，可以在地址 <https://github.com/SteveSanderson/Node.js-Site-Templates-for-WebMatrix> 下载。

你可以通过如下步骤来测试以上工作的正确性，首先运行 `WebMatrix`，在打开页面中选择 "Site from Template" 选项。然后你可以看到两个 Node 模板选项：一个是 ”Express“，另一个是 “abasic, empty site configured for Node"。选择后者，并使用 "First Node Site"为新建的站点命名。

使用 `WebMatrix` 生成的新站点。点击页面左上角的 `Run` 按钮，浏览器窗口会弹出并显示包含有 “Hello, world!” 信息的页面。

> 提示：
> 若需要在 `WebMatrix` 中查看 `iisnode` 的示例，则需要在 `WebMatrix` 中选择选项 “Site from Folder"，然后在弹出的对话框中输入如下内容：`%localappdata%\iisnode\www`。