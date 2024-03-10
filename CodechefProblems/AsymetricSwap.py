for _ in range(int(input())):
      n=int(input())
      la=list(map(int,input().split()))
      lb=list(map(int,input().split()))
      main=la+lb
      main.sort()
      i=0
      a=1000000000
      while(i<=n):
        s=i;e=i+n-1
        a=min(a,main[e]-main[s])
        i+=1
      print(a)