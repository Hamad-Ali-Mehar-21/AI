# WRITE THE CODE OF BINARY SEARCH 

def binary_search(arr,tar):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid = (low+high) // 2
        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            low=mid+1
        else:
            high=mid-1
        
    return -1    


arr = [6,16,23,38,45,77,84,90]

target= 38


b=binary_search(arr,target)

if b!=-1:
    print(f"Element is found at index: {b}")
else:
    print("Element is not found in array")

