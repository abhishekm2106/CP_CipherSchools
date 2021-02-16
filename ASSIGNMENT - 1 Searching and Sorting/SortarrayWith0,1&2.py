def seperate(arr):
    first = 0
    second = 0
    third = len(arr)-1
    while(second<=third):
        if arr[second]==0:
            arr[first],arr[second] = arr[second],arr[first]
            first+=1
            second+=1
        elif arr[second]==1:
            second+=1
        else:
            arr[third],arr[second] = arr[second],arr[third]
            third-=1
    
x=[0,0,0,1,1,1,1,2,2,2,2,0,0,1,1,1,0]
seperate(x)
print(x)
        
        