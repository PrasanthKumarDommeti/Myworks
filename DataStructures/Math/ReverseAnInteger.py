class Solution:
    def reverse(self, x: int) -> int:
        st = str(x)
        m=""
        if st[0] == "+" or st[0] =="-":
            m+=st[0]
            st1 = st[1:]
            m+=st1[::-1]
        else:
            m+=st[::-1]
        if int(m) > 2 ** 31 - 1 or int(m) < -2 ** 31:
            return 0
        return int(m)
            
            