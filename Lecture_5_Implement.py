# TODO liner searching in array

def leniarsearching(arrayy,number):
    for i in range(len(arrayy)):
        if arrayy[i] == numberl:
            return 'present in index', i
    return "not present in array " 
arrayy=[232,34,35,3465,754,242,3,234,3454,6,56,5,65,6,5]
numberl = 65
resultl = leniarsearching(arrayy, numberl)
print("your number is ",resultl)

# TODO binary search without using  recursion
def Binarysearch(arrayy,numberb,leftb,rightb):
    while leftb<=rightb:
        mid = leftb + (rightb-leftb)//2
        if arrayy[mid] == numberb:
            return mid
        elif arrayy[mid] < numberb:
            leftb = mid+1
        else:
            rightb = mid-1
    return -1               
arrayy=[232,34,35,3465,754,242,3,234,3454,6,56,5,65,6,5]
numberb = 3454
leftb = 0
rightb = 14 
sort= arrayy.sort()
resultb = Binarysearch(arrayy,numberb,leftb,rightb) 
print(arrayy,"\n",resultb)

#  TODO binary search using recursion
def Binarysearchrec(arrayy,numberc,leftc,rightc):
    while leftc<=rightc:
        mid = leftc + (rightc-leftc)//2
        if arrayy[mid]==numberc:
            return mid
        elif arrayy[mid] < numberc:
           return Binarysearch(arrayy, numberc,mid+1, rightc)    
        else:
            return Binarysearch(arrayy, numberc,leftc,mid-1,)  
    return "not present"        
   

arrayy=[232,34,35,3465,754,242,3,234,3454,6,56,5,65,6,5]
numberc = 35
leftc = 0
rightc = len(arrayy)-1
sort=arrayy.sort()
resultc = Binarysearchrec(arrayy,numberc,leftc,rightc) 
print(arrayy,"\n",resultc)