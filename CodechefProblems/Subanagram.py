t=int(input())#number of strings
s=input()#the first string 
d={}#initializing a dictionary or hashmap
min=''#the resultant string which we gonna print it at the end
alpha='abcdefghijklmnopqrstuvwxyz'
for j in alpha:
    d[j]=s.count(j)
    #keeping the count of all letters for the first string in the variable 'd'
for i in range(t-1):#for the remaining strings
    a=input()
    for k in alpha:
        if a.count(k)<d[k]:
            d[k]=a.count(k)
            #if the letter count is less then we update the dictionary, so that we can keep the lowest count of letters. so that its count of characters is least and is common to all of the strings
for h in d:
    min+=h*d[h]
    #'h' is the letter and 'd[h]' is the number of characters, if the least number of that letter count is 0, then that letter won't get concatenated to the 'min' string
if min=='':
    print('no such string')
else:
    print(min)