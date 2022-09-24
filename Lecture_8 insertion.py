def insertionsearch(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while arr[j] >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
            print(arr)
        arr[j+1] = key
    return arr     


arr = [75,90,95,100,80,85]
result = insertionsearch(arr)
print(f"\n{result}")
# i = 1               j = 0            key = 90
# arr = [75,90,95,100,80,85]

# i = 2               j = 1            key = 95
# arr = [75,90,95,100,80,85]

# i = 3               j = 2            key = 100
# arr = [75,90,95,100,80,85]

# i = 4               j = 3            key = 80         100 > 80
# arr = [75,90,95,100,80,85]
#  when j = 3 then  arr = [75,90,95,100,100,85]
#  when j = 2 then  arr = [75,90,95,100,100,85]         95 > 80
#  when j = 1 then  arr = [75,90,95,95,100,85]          90 > 80
#  when j = 0 then  arr = [75,90,90,95,100,85]          75 > 80
#  when j = 0 then  arr = [75,80,90,95,100,85]          

# i = 5               j = 4          key = 85         80 > 85
# # arr = [75,80,90,95,100,85]
# when j = 4 then  arr = [75,80,90,95,100,100]      
# when j = 3 then  arr = [75,80,90,95,100,100]        95 > 85          
# when j = 2 then  arr = [75,80,90,95,95,100]        95 > 85          
# when j = 1 then  arr = [75,80,90,90,95,100]        90 > 85          
# when j = 1 then  arr = [75,80,90,90,95,100]        80 > 85       # conditon false   
# when j = 1 then  arr = [75,80,85,90,95,100]     


# sorted arr =  [75,80,85,90,95,100]     
