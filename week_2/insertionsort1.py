# https://www.hackerrank.com/challenges/insertionsort1/problem



def insertionSort1(n, arr):
    
    k = arr[-1] # the last element to be sorted
    i = n-1 # the last index 
    
    while i > 0 and arr[i-1] > k:
        arr[i] = arr[i-1]
        print(*arr)
        i -= 1
    
    # ASA the while loop break assign "k" to its right position    
    arr[i] = k
    print(*arr)
