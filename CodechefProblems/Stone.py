# check the pattern
# after k turn there are only 2 possible repetitive outcomes
# one for odd turns, other for even and both contains 0 (i.e. max - max)

n,k=list(map(int, input().split()))
a=list(map(int, input().split()))
if k>0:
  k%=2 # odd turns = 1 turn
  if k==0:
    k=2 # even turns = 2 turns

for i in range(k): # turn begins
  m=max(a)
  for i in range(n):
    a[i]=m-a[i]
    
print(*a)