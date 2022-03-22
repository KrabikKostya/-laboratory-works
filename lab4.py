from random import randint

m = 10
n = 10
#1
s = 0
k = 0
array = [[randint(-1000, 1001) for i in range(m)] for j in range(n)]
for i in array:
    s += sum(i)
s /= n*m
for i in array:
    for j in i:
        if j % s == 0:
            k += 1
print(array)
print(k)
#2
slices = 1
for i in array:
    for j in range(n):
        i[j] = sum(i[0:slices])
        slices += 1
print(array)
