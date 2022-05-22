
def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len(a):
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len(b):
        arr[k] = b[j]
        j+=1
        k+=1

def search(arrayList,target):
    left = 0
    right=len(arrayList) -1
    while left<=right:
        mid=int((left+right)/2)
        if int(arrayList[mid]) == target:
            return mid
        elif arrayList[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

if __name__ == '__main__':
    arr =[10, 3, 15, 7, 8, 23, 98, 29]
    sortedList=merge_sort(arr)
    target=int(input("Enter value you want to search"))
    searchResult = search(arr, target)
    if searchResult== -1:
        print(f"Element {target} is not found in the list of data stored")
        enterValue=int(input("Press 1 to stored to the list"))
        if enterValue == 1: 
            arr.append(target)
            merge_sort(arr)
            print("The sorted Array of the list is \n",arr)
    else:
        print(f"The search elements {target} is found in index number {searchResult+1}")




