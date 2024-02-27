# It can be solved using Set Operation 
for _ in range(int(input())):
    x=list(map(int,input().split()))
    s=str(input())
    k='abcdefghijklmnopqrstuvwxyz'
    # Set opearation is used to return the not existing/missing elements in the given string
    m = set(k)-set(s)
    count=0
    for i in m:
        count+=x[k.index(i)]
    print(count)
    
    
# It can be solved by using dictionary also
    dic = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    count=0
    for i in dic.keys():
        if i in s:
            continue
        else:
            # It can be used the value of a key
            count+=dic.get(i)
            
    print(count)