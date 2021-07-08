1. 按 <kbd>Win</kbd>+<kbd>R</kbd> 打开运行窗口，输入 `cmd` 后确认打开命令提示符窗口。

2. 复制粘贴下面的内容到命令窗口后回车即可在代理模式下启动 `Chrome`，**使用命令前请确认 Chrome 已完成退出**。（在 `Chrome` 的快捷方式上右键，点击菜单中的属性。如果是 `Windows` 的任务栏图标，请按住 Shift 后再点击右键。在弹出的窗口中，找到目标一栏，即可复制对应的 `Chrome.exe` 的路径，然后替换引号内部的内容，引号需要保留）

   ```shell
   "这里替换为 Chrome.exe 的路径" --proxy-server="socks5://127.0.0.1:1080"
   ```

   例如：

   ```shell
   C:\Users\Xiaotuan>"C:\Program Files\Google\Chrome\Application\chrome.exe" --proxy-server="http://127.0.0.1:58591"
   ```
   
   `macOS` 用户（请注意客户端的 `socks5` 监听端口需要设置为 1080）：
   
   ```shell
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --proxy-server="socks5://127.0.0.1:1080"
   ```
   
3. 然后可以打开 <https://www.google.com/> 测试或是访问<https://ip.sb> 以及 <https://www.ipip.net/ip.html> 查看自己的 IP 状态。

