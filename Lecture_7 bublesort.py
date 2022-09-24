def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                # swapping
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr           
arr = [67,45,343,432,2656,86,34,31,2,45,6,4,3,63,]
result = bubblesort(arr)
print(f'Bubble sort output : {result}')
