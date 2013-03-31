recoverable_pdb
===============

The project try to provide the pdb with recovery function.
The code only test in windows python 2.7.
Maybe it can't work in other version.


使用說明:
基本上這個版本的用法和原生的 PDB 差不多。只是多了三道指令。

===============

save snapshot_name

這道指令的作用是把現在的 local variable 值都存在 snapshot_name 裡。

===============

restore snapshot_name

這道指令會把 local variable 和 lineno 還原到存在 snapshot_name 的狀態
lineno 是指下一個要執行的行號

=================

diff snapshot_name

比較現在的狀態與存在 snapshot_name 裡的狀態有何差異
這裡是指有哪些變數被新增、刪除、或是修改
