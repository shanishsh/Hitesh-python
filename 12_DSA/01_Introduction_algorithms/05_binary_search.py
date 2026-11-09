def binary_search(arr, st, end, target):
    if st>=end:
        return -1
    
    mid = (st + end) // 2
    if arr[mid] == target:
        return mid
    
    elif target > arr[mid]:
        return binary_search(arr,mid+1,end,target)

    elif target < arr[mid]:
        return binary_search(arr,st,mid-1,target)
 
 
l1=[1,30,40,100,300,550,650,2200]
print(binary_search(l1,1,8,1000))
