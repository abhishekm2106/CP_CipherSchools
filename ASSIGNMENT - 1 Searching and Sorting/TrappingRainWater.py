def trappingWater(arr):
    leftArr = [0]*len(arr)
    mx = 0
    for i in range(len(arr)):
        leftArr[i] = mx
        mx = max(mx,arr[i])

    rightArr = [0]*len(arr)
    mx = 0
    for j in range(len(arr)-1,-1,-1):
        rightArr[j] = mx
        mx = max(mx,arr[j])

    total = [0]*len(arr)
    for k in range(len(arr)):
        total[k] = min(leftArr[k],rightArr[k])
        total[k]= total[k]-arr[k] if total[k]>arr[k] else 0

    return sum(total)

arr=[1,2,6,3,4,8,5,6,3,8,4,6,2,1,7]
print(trappingWater(arr))