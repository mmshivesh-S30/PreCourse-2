# Python program for implementation of MergeSort
def mergeSort(arr):
    #write your code here
    if len(arr) > 1:

        m = len(arr)//2

        left_half = arr[:m]
        right_half = arr[m:]
        mergeSort(left_half)
        mergeSort(right_half)

        i,j,k = 0,0,0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k+=1
        while i < len(left_half):
            arr[k] = left_half[i]
            k+=1
            i+=1
        while j < len(right_half):
            arr[k] = right_half[j]
            k+=1
            j+=1
# Code to print the list 
def printList(arr): 
    #write your code here
    for i in arr:
        print(i, end=' ')
    print()

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
