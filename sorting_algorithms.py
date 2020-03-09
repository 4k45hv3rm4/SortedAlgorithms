#******SELECTIONSORT******#
def selectionSort(seq):
    #iterates over the given sequence of elements
    for s in range(len(seq)):
        #taking s as minposition
        minpos = s
        #iterating over the sequence considering s as minposition and comparing with every element
        for i in range(s, len(seq)):
            #condition to check if element is smaller than our minimum element
            if(seq[i]<seq[minpos]):
                #if condition evalutaes to true minpos is changed to i
                minpos = i
        #than minimum elment is changed to element in position s
        seq[s], seq[minpos] = seq[minpos], seq[s]
    #returning sorted list
    return seq

#******INSERTTIONSORT******#
def insertionSort(nlist):
    #iterating over the given list
    for sliceEnd in range(len(nlist)):
        #position of an element
        pos = sliceEnd
        #checking that position is >0 and element at position is greater than any  element to the left
        while pos>0 and nlist[pos]<nlist[pos-1]:
            # if this condition evaluates to true than swap the 2 positions
            nlist[pos], nlist[pos-1] = nlist[pos-1],nlist[pos]
            #decrementing pos value by 1
            pos=pos-1
    #returning the obtained sorted List
    return nlist

#******QUICKSORT******#
def quickSort(array):
    #condition to check the length of passed array
    if len(array)<2:
        #if length of array is less than 2 return the same array
        return array
    else:
        #selecting first element in the array as pivot element
        pivot = arr[0]

        #storing elements smaller than pivot in smaller list
        smaller=[i for i in array[1:] if i < pivot]

        #storing elments greater than pivot in greater list
        greater=[j for j in array[1:] if j > pivot]

        #returning the sorted list as required
        return quickSort(smaller) + [pivot] + quickSort(greater)

#******BUBBLESORT******#
def bubbleSort(lyst):
    #iterating for times as there are elements in the list
    for i in range(len(lyst)):
        #we wannt the last pair to be lyst[j], lyst[j+1]
        for j in range(len(lyst)-1):

            if lyst[j]>lyst[j+1]:
                #swap
                lyst[j],lyst[j+1]=lyst[j+1],lyst[j]
    return lyst

#******HEAPSORT******#
def heapSort(arr):
   n = len(arr)
   # maxheap
   for i in range(n, -1, -1):
      heapify(arr, n, i)
   # element extraction
   for i in range(n-1, 0, -1):
      arr[i], arr[0] = arr[0], arr[i] # swap
      heapify(arr, i, 0)
