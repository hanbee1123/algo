def mergesort(a):
    if len(a)>1:
        # First step. Split the array in half
        mid = len(a) //2
        left = a[:mid]
        right = a[mid:]

        # Perform mergesort for left one
        mergesort(left)
        # Perform mergesort for the right on
        mergesort(right)

        # Create variables i, j, k to track
        i = j = k = 0
        while i<len(left) and j< len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            a[k]=left[i]
            i+=1
            k+=1
        
        while j<len(right):
            a[k] = right[j]
            j+=1
            k+=1
        
    return a




if __name__ == "__main__":
    a = [365,13,6,34,2,6,45,2,6,6,402,482,585,1,495,1945,1]
    print(mergesort(a))