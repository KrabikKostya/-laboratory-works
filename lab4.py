from random import randint

#1
m = 10
n = 10
s = 0
slice = 1
array = [[randint(-1000, 1001) for i in range(m)] for j in range(n)]
print(array)
for i in array:
    s += sum(i)
s /= n*m
k = 0
for i in array:
    for j in i:
        if j % s == 0:
            k += 1
print(k)
#2
for i in array:
    for j in range(n):
        i[j] = sum(i[0:slice])
        slice += 1
print(array)
