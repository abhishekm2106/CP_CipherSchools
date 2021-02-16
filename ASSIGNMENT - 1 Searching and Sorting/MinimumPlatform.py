def minimumPlatform(arr,dep):
    arr.sort()
    arr.sort()
    maxp=1
    p = 1
    di = 0
    ai = 1
    while(di<len(dep) and ai<len(arr)):
        if arr[ai]<=dep[di]:
            ai+=1
            p+=1
        elif dep[di]<arr[ai]:
            p-=1
            di+=1
        
        maxp = max(maxp,p)

    return maxp


arr = [ 900, 940, 950, 1100, 1500, 1800 ]
dep = [ 910, 1200, 1120, 1130, 1900, 2000 ]
print(minimumPlatform(arr,dep))