def pascal(numRows):
    l=[]
    # This for loop is used to assign the triangle with ones only
    for i in range(numRows):
        l.append([1]*(i+1))
    #Generally pascal Triangle calculations starts from row 2 and updated the values from the 2 index position
    for i in range(2,numRows):
        for j in range(1,len(l[i])-1):
            # Calculated approach to follow the count with not change first and last position ones
            l[i][j]=l[i-1][j-1]+l[i-1][j]
    return l

print(pascal(5))