with open("input.txt", "r") as f:
    #1
    array = [list(map(int, row.split())) for row in f.readlines()]
    s = 0
    k = 0
    m = len(array)
    n = len(array[0])
    for i in array:
        s += sum(i)
    s /= n*m
    for i in array:
        for j in i:
            if j % s == 0:
                k += 1
    #2
    for i in range(m):
        slices = 1
        for j in range(n):
            array[i][j] = sum(array[i][0:slices])
            slices += 1
with open("output.txt", "a") as f:
    f.write("=" * 250 + "\n")
    for i in array:
        f.write(str(i)+"\n")
    f.write(str(k)+"\n")
    for i in array:
        f.write(str(i)+"\n")
    f.write("="*250 + "\n")
