arr = list(input())

i = len(arr)

arr[1] = 'a'
arr[i-2] = 'a'

print(*arr, sep="")