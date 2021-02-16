def binarySearch():
    pass


def searchPivot(arr,start,end):
    mid = start + (end-start)//2

    if arr[mid]>arr[mid+1]:
        return mid
    elif arr[mid]<arr[mid-1]:
        return mid-1
    
    if arr[mid]>=arr[end]:
        return searchPivot(arr,mid+1,end)
    else:
        return searchPivot(arr,start,mid)

        


def searchInSortedRotated(arr,x):
    pivot = searchPivot(arr,0,len(arr)-1)
    arr1 = binarySearch(arr,0,pivot,x)
    arr2 = binarySearch(arr,pivot+1,len(arr)-1,x)
    
    print(arr1,arr2)







arr = [5,7,11,15,21,24,34,78,98,99,2,3,4]
x = 11
searchInSortedRotated(arr,x)
