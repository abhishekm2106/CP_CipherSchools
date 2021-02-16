def merge(arr1,arr2):
    i1 =0
    i2 =0
    arr3 = [0]*(len(arr1)+len(arr2))
    i3=0
    while(i1<len(arr1) and i2<len(arr2)):
        if arr1[i1]<arr2[i2]:
            arr3[i3]=arr1[i1]
            i1+=1
        else:
            arr3[i3]= arr2[i2]
            i2+=1
        i3+=1

    while(i1<len(arr1)):
        arr3[i3]=arr1[i1]
        i1+=1
        i3+=1
    
    while(i2<len(arr2)):
        arr3[i3]=arr2[i2]
        i2+=1
        i3+=1
    
    return arr3



arr1 = [1,3,5,6,9,23,24,41,43]
arr2 = [2,4,7,20,45]

print(merge(arr1,arr2))

