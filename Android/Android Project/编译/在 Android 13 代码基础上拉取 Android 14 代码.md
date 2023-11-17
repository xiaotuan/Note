 拉取mtk_sp_t0仓库 根据需求拉取13或者14代码
git clone git@192.168.0.24:mtk/mtk_sp_t0.git
git submodule init
\### 只拉取S代码
git submodule update vnd
\### 只拉取T代码
git submodule update vnd sys
\### 只拉取U代码
git submodule update vnd u_sys
git submodule foreach git checkout master


\### 现有的mtk_sp_t0上单独拉取u_sys代码
cd mtk_sp_t0
git pull
git submodule init
git submodule update u_sys
cd u_sys
git checkout master