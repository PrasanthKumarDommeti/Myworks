class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # the range limit upto the 1337 only
        return pow(a,int(''.join(map(str,b))),1337)