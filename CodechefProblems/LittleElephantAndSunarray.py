N=int(input())
A=list(map(int,input().split()))
Q=int(input())
dict={}
for i in range(N):
    mi=A[i]
    for j in range(i,N):
        mi=min(mi,A[j])
        if mi in dict:
            dict[mi]+=1
        else:
            dict[mi]=1
for k in range(Q):
    print(dict.get(int(input()),0))