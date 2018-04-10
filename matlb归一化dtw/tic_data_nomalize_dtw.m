load 1.txt  %将tic数据文件写入matlab默认的数组X1中
[A,PS]=mapminmax(X1) %用默认的方法数组进行归一化处理（最大为1，最小为-1）
csvwrite('A.txt',A) %归一化后的数据写入到新的TXT文件中

load 2.txt %将tic数据文件写入matlab默认的数组X1中
[B,PS]=mapminmax(X2) %用默认的方法数组进行归一化处理（最大为1，最小为-1）

figure %作图
dtw(A,B) %两数组间距离
