def ternary_search(arr, target,st,end):
    if st>=end:
        return -1

    mid1=st+(end-st)//3
    mid2=end-(end-st)//3

    if arr[mid1]==target:
        return mid1

    elif arr[mid2]==target:
        return mid2

    elif target<arr[mid1]:
       return ternary_search(arr,target,st,mid1-1)

    elif target>arr[mid2]:
       return ternary_search(arr,target,mid2+1,end)

    else:
        return ternary_search(arr,target,mid1+1,mid2-1)

arr=[10,40,300,540,666,720,750,1000]
print(ternary_search(arr,720,0,7))