load 1.txt  %��tic�����ļ�д��matlabĬ�ϵ�����X1��
[A,PS]=mapminmax(X1) %��Ĭ�ϵķ���������й�һ���������Ϊ1����СΪ-1��
csvwrite('A.txt',A) %��һ���������д�뵽�µ�TXT�ļ���

load 2.txt %��tic�����ļ�д��matlabĬ�ϵ�����X1��
[B,PS]=mapminmax(X2) %��Ĭ�ϵķ���������й�һ���������Ϊ1����СΪ-1��

figure %��ͼ
dtw(A,B) %����������
