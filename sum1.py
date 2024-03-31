def counting(arr, arr_size):
    even_count=0
    odd_count=0


    for i in range(arr_size):
        if(arr[i] & 1 == 1):
            odd_count= odd_count+1
        else:
            even_count=even_count+1
        
    print("number of even elements ",even_count)
    print("number of odd elements", odd_count)

arr=[] # creating an empty array
arr_size = int(input("please enter the number of elements : "))

#iterating till the range

for i in range(0 ,arr_size):
    element= int(input())
    arr.append(element)

print(arr)
counting(arr ,arr_size)    