# given an array find the average of the array 

def average(arr, arr_size):
    sum_of_array=0
    for i in range(0,arr_size):
        sum_of_array=sum_of_array+arr[i]
    return sum_of_array/arr_size
    
arr=[]
arr_size=int(input("enter the no. of elements"))
for i in range(0, arr_size):
    element=int(input())
    arr.append(element)

print(arr)
print(average(arr, arr_size))
   

    
