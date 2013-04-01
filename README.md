recoverable_pdb
===============

The project try to provide the pdb with recovery function.
Like time machine, you can recovery to the point you save without restarting whole program..
The code only test in windows python 2.7.
Maybe it can't work in other version.

Known issues:
  it can't work with pdb++


使用說明:
基本上這個版本的用法和原生的 PDB 差不多。只是多了三道指令。

===============

save snapshot_name

這道指令的作用是把現在的 local variable 值都存在 snapshot_name 裡。
The usage is the same as pdb. But I add three command for it.

  save point_name: save current runtime envir. So you can restore the runtime using restore command.
  restore point_name: recovery to the point you save.
  diff: compare current runtime envir from the runtime env you saved.

===============

restore snapshot_name

這道指令會把 local variable 和 lineno 還原到存在 snapshot_name 的狀態
lineno 是指下一個要執行的行號

=================

diff snapshot_name

比較現在的狀態與存在 snapshot_name 裡的狀態有何差異
這裡是指有哪些變數被新增、刪除、或是修改

=================

已知限制:

1.無法 restore 到 其他函數狀態。 因為這是 jump 的限制。
jump 無法跳到其他 pyframe 去。

註: 隨手寫的，沒有作嚴謹的測試。可能會有不少 bug。
