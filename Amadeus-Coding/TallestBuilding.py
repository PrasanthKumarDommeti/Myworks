def solve(n, restrictions):
   if not restrictions:
      return n-1
   resi = sorted(restrictions, key = lambda x:x[0])

   k = 0
   idx = 1
   for re in resi:
      re[1] = min(re[1], k+re[0]-idx)
      k = re[1]
      idx = re[0]
   k = resi[-1][1]
   idx = resi[-1][0]
   resi.reverse()
   for re in resi[1:]:
      re[1] = min(re[1], k-re[0]+idx)
      k = re[1]
      idx = re[0]
   resi.reverse()

   f = 0
   idx = 1
   res = 0
   for re in resi:
      ff = min(f+re[0]-idx, re[1])
      res = max(res, (re[0] - idx + f + ff) // 2)
      idx = re[0]
      f = ff
   return max(f+n-idx,res)

n = 5
restrictions = [[2,1],[4,3]]
print(solve(n, restrictions))