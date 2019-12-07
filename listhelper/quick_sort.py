l = [8,1,12,7,6,10,3,4,8,5,9,2,11,5,13]

quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])

print(quick_sort(l))