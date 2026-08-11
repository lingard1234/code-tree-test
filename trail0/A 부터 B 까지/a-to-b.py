A, B = map(int, input().split())

num = A

while num <= B:
    print(num, end= " ")

    if num % 2 == 0:
        num += 3
    else:
        num *= 2