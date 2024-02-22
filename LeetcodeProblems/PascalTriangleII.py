def pascal(RowIndex):
     l=[]
    # These 2 conditions because no changes can be occured in any pascal triangle
    if RowIndex == 0:
        return [1]
    elif RowIndex == 1:
        return [1,1]
    else:
        # This for loop is used to assign the triangle with ones only
        for i in range(RowIndex+1):
            l.append([1]*(i+1))
        #Generally pascal Triangle calculations starts from row 2 and updated the values from the 2 index position
        for i in range(2,RowIndex+1):
            for j in range(1,len(l[i])-1):
                # Calculated approach to follow the count with not change first and last position ones
                l[i][j]=l[i-1][j-1]+l[i-1][j]
       
   
    
    
    return l[RowIndex]

print(pascal(3))

#output : [1,3,3,1]