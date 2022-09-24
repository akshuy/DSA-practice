def selectionsort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # swapping 
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr   


arr = [34,5,4,323,2,34,45,4,6,57,54,343,43,5,46,4,434,2,4]               
result = selectionsort(arr)
print(f'Selection sort output : {result}') 