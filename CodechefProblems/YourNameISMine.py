def issub(s1,s2): 
    m=len(s1)  #shorter string
    n=len(s2) 
    i=0
    j=0
    while(i<m and j<n):
        if(s1[i]==s2[j]):
            i+=1 
            j+=1 
        else:
            j+=1 
    if(i==m):
        return "YES" 
    else:
        return "NO"
for i in range(int(input())):
    m,w=map(str,input().split()) 
    if(len(m)>len(w)):
        m,w=w,m 
    print(issub(m,w)) 