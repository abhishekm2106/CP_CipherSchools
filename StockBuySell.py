def stockBuySell(arr, n):
    start=end=0
    ret = []
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            end=i-1
            if start!=end and arr[start]!=arr[end]:
                while(arr[start]==arr[start+1]):
                    start+=1
                ret.append([start,end])
            start=i
        
    if start!=n-1:
        ret.append([start,n-1])
    return ret


arr = [1,12,34,22,22,1,45,67]
print(stockBuySell(arr,len(arr)))