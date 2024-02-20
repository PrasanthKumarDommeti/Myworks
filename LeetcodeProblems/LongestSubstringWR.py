def lswr(s):
    eset = set()
    l=0
    res =0 
    for r in range(len(s)):
        #Elemenating the duplicated characters in your empty set
        while s[r] in eset:
            eset.remove(s[l])
            l+=1
        #Unique element must be added
        eset.add(s[r])
        # Check the len of empty list every time
        res = max(res,r-l+1)
    return res

if __name__ == 'main':
    s = "abcabcbb"
    print(lswr(s))