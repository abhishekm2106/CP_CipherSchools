def maxSum(arr):
    cs=ms=0

    for i in arr:
        if i+cs>i:
            cs+=i
        else:
            cs = i
        
        ms = max(cs,ms)
    
    return ms

print(maxSum([1,2,4,5,-8,7]))