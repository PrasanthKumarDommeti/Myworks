k, n = map(int,input().split())
l = []
for j in range(k):
    l.append(input())
for s in range(n):
    t = input()
    if len(t) >= 47:
        print('Good')
        continue
    for j in l:
        if j in t:
            print('Good')
            break
    else:
        print('Bad')