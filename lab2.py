lst = input("Введіть список (кожен елемент через пробіл): ").split()

try:
    for i in range(len(lst)):
        lst[i] = int(lst[i])
except ValueError:
    print("Список має бути складеній ліше з чисел")
else:
    for i in range(1):
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                continue
            else:
                break
        else:
            print("Список впорядковно за збільшенням")
            break
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                continue
            else:
                break
        else:
            print("Список впорядковно за зменшенням")
            break
    else:
        print("Список невпорядковно")

    def quickSort(array):
        if len(array)> 1:
            pivot=array.pop()
            grtr_lst, equal_lst, smlr_lst = [], [pivot], []
            for item in array:
                if abs(item) == pivot:
                    equal_lst.append(abs(item))
                elif abs(item) > pivot:
                    grtr_lst.append(abs(item))
                else:
                    smlr_lst.append(abs(item))
            return (quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst))
        else:
            return array

    print(f"Відсортований масив: {quickSort(lst)}")
