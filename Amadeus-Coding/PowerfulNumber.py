import math
def isStrong(self, N):
        d=str(N)
        sof = 0
        for di in d:
            sof+=math.factorial(int(di))
        if N==sof:
            return 1
        else:
            return 0