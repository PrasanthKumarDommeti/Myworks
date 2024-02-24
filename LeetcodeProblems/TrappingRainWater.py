def trap(self, h: List[int]) -> int:
    count,l,r,lmax,rmax = 0,0,len(h)-1,0,0
    if r<2:
        return count
    while l<r:
        if h[l]<h[r]:
            lmax = max(lmax,h[l])
            count+=lmax-h[l]
            l+=1
        else:
            rmax = max(rmax,h[r])
            count+=rmax-h[r]
            r-=1
    return  count
