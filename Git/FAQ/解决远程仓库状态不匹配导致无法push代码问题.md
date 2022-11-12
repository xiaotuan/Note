当前仓库关联多个远程仓库，由于某个远程仓库的状态与当前仓库状态不一致导致无法 push 代码到该远程仓库中（即该远程仓库的代码比本地仓库的代码新）。可以使用如下命令先将该远程仓库代码同步到本地仓库中，然后再上传代码到远程分支即可：

```shell
$ git pull 远程仓库分支 当前仓库分支
```

例如:

```shell
$ git remote -v
Github	git@github.com:xiaotuan/Note.git (fetch)
Github	git@github.com:xiaotuan/Note.git (push)
Gitlab	git@gitlab.com:xiaotuangit/note.git (fetch)
Gitlab	git@gitlab.com:xiaotuangit/note.git (push)
origin	git@gitee.com:xiaotuan/Notes.git (fetch)
origin	git@gitee.com:xiaotuan/Notes.git (push)
$ git branch
* master
$ git pull Github master
hint: Pulling without specifying how to reconcile divergent branches is
hint: discouraged. You can squelch this message by running one of the following
hint: commands sometime before your next pull:
hint: 
hint:   git config pull.rebase false  # merge (the default strategy)
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint: 
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
From github.com:xiaotuan/Note
 * branch              master     -> FETCH_HEAD
Merge made by the 'recursive' strategy.
$ git push Github
```

