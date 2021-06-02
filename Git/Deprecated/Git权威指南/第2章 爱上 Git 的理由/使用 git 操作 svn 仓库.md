使用 `Git` 来操作 `SVN` 版本控制服务器的一般工作流程为：

+ 访问 SVN 服务器，将 SVN 版本库克隆为一个本地的 Git 库，一个货真价实的 Git 库，不过其中包含针对 SVN 的扩展。

  ```shell
  $ git svn clone <svn_repos_url>
  ```

+ 使用 Git 命令操作本地克隆的版本库。

+ 当能够通过网络连接到 SVN 服务器，并想将本地提交同步到 SVN 服务器时，先获取 SVN 服务器上最新的提交，然后执行变基操作，最后再将本地提交推送给 SVN 服务器。

  ```shell
  $ git svn fetch
  $ git svn rebase
  $ git svn dcommit
  ```

  

