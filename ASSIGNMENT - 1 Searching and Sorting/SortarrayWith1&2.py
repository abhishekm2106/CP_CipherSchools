def seperate(arr):
    start = 0
    end = len(arr)-1
    while(start<end):
        if arr[start]==1:
            start+=1
        elif arr[end]==2:
            end-=1
        else:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    
x=[2,2,2,1,2,1,2,2,1,1,1,1,2]
seperate(x)
print(x)