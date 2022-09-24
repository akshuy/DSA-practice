# def trinarysearch(arr,i,j,num):
#     mid1 = i+(j-i)//3
#     mid2 = j-(j-i)//3
#     for i in range(len(arr)):
#         if arr[mid1] == num:
#             return mid1
#         if arr[mid2] == num:
#             return mid2
#         if arr[mid1] > num:
#             return trinarysearch(arr, i, mid1-1, num)
#         if arr[mid2] < num:
#             return trinarysearch(arr, mid2+1, j, num)
#         else:
#             return trinarysearch(arr,mid1+1,mid2-1, num)                          
#     return -1
# arr = [20,25,47,56,59,63,65,69,82]
# i = 0
# j = len(arr)-1
# num = int(input("enter the no of arr to know about index : "))

# searching = trinarysearch(arr,i,j,num)
# print(searching)

# TODO foursearch

def foursearch(arr,i,j,num):
    mid1 = i+(j-i)//4
    mid2 = j-(j-i)//4
    mid3 = mid1+(mid2-mid1)//4
    for i in range(len(arr)):
        if arr[mid1] == num:
            return mid1
        if arr[mid2] == num:
            return mid2
        if arr[mid3] == num:
            return mid3
        if arr[mid1] > num:
            return foursearch(arr, i, mid1-1, num)    
        if arr[mid2] > num and arr[mid1] < num:
            return foursearch(arr, mid1+1,mid2-1, num)    
        if arr[mid3] > num and arr[mid2] < num :
            return foursearch(arr,mid2+1, mid3-1, num)
        else:
            return foursearch(arr, mid3+1, j, num)     
    return -1           

arr = [20,25,47,56,59,63,65,69,82,89,104,555]
i = 0
j = len(arr)-1 
num = int(input("enter the no to search : "))

searching = foursearch(arr,i,j,num)
print(searching)