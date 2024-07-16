
import sys
from sys import stdin

MOD = 10**9 + 7

def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def nthTermOfGP(n, a, r):
    if n == 0:
        return a % MOD
    nth_term = (a * modular_exponentiation(r, n-1, MOD)) % MOD
    return nth_term



t = int(sys.stdin.readline().strip())

while(t > 0):
    
    n, a, r = map(int,input().split())
    print(nthTermOfGP(n,a,r))
    
    t = t - 1
    
    
    

