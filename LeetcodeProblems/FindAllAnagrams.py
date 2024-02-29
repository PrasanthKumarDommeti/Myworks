class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        c= Counter(p)
        # The counter is used to calculate the frequrncy of the element
        result =[]
        for i in range(len(s)-len(p) +1):
            temp = Counter(s[i:i+len(p)])
            if temp == c:
                result.append(i)
        return result        