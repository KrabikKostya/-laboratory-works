#1
def func(A:list, B:list, K:float, L:float):
    KL = K/L
    M=[None, None]
    M[0] = (A[0]+KL*B[0])/(1+KL)
    M[1] = (A[1]+KL*B[1])/(1+KL)
    return f"{M}"


print(func([5,3], [-3,-1], 1, 3))

#2
def f1(A:int, B:int):
    A_BITES = A*1024
    B_BITES = B*1024**2
    if A_BITES > B_BITES:
        print("В А кілобайтах пам'яті більше байт, ніж у В мегабайтах памяті")
    else:
        print("В В мегабайтах памяті більше байт, ніж у А кілобайтах пам'яті")


A = int(input("Введыть число А: "))
B = int(input("Введыть число B: "))
f1(A, B)


def f3(a1:str, a2:str, a3:str, a4:str, a5:str, b1:str, b2:str, b3:str):
    if int(a1+a2) < 24:
        if int(a3+a4) < 60:
            if int(b2+b3) == 2:
                if int(a5+b1) <= 28:
                    print("Формат часу введено правильно")
                else:
                    print("Формат часу введено неправильно")
            elif int(b2+b3) <= 12:
                if int(a5+b1) <= 30:
                    print("Формат часу введено правильно")
                else:
                    print("Формат часу введено неправильно")
            else:
                print("Формат часу введено неправильно")
        else:
            print("Формат часу введено неправильно")
    else:
        print("Формат часу введено неправильно")


a1 = input("Введыть число a1: ")
a2 = input("Введыть число a2: ")
a3 = input("Введыть число a3: ")
a4 = input("Введыть число a4: ")
a5 = input("Введыть число a5: ")
b1 = input("Введыть число b1: ")
b2 = input("Введыть число b2: ")
b3 = input("Введыть число b3: ")
b4 = input("Введыть число b4: ")
b5 = input("Введыть число b5: ")
f3(a1, a2, a3, a4, a5, b1, b2, b3)


def f2(x1:int, x2:int, x3:int, x4:int, x5:int):
    k = 0
    x = [x1, x2, x3, x4, x5]
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            k+=1
    print("Кількість пар однакових чисел =", k)


x1 = int(input("Введіть x1: "))  # Введення першої змінної
x2 = int(input("Введіть x2: "))  # Введення другої змінної
x3 = int(input("Введіть x3: "))  # Введення третьої змінної
x4 = int(input("Введіть x4: "))  # Введення четвертої змінної
x5 = int(input("Введіть x5: "))  # Введення п'ятої змінної
f2(x1, x2, x3, x4, x5)
