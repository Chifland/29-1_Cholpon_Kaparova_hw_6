def bubble_sort(list_unsorted):
    list_len = len(list_unsorted)
    for i in list_unsorted:
        for j in range(list_len-1):
            if list_unsorted[j] > list_unsorted[j+1]:
                list_unsorted[j], list_unsorted[j+1] = list_unsorted[j+1], list_unsorted[j]
    return list_unsorted


def binary_search(a, val):
    n = len(a)
    first = 0
    last = n-1
    middle = n // 2
    pos = 0
    while first <= last:
        if val == a[middle]:
            pos = middle
            break
        elif val > a[middle]:
            first = middle + 1
        else:
            last = middle - 1
        middle = (first + last) // 2

    if first > last:
        print(f'Результат не найден. {val} нет в списке: {a}')
    else:
        print(f'Результат найден индекс {val} в списке {a} равен:{pos}')



list_sorted = bubble_sort([10,9,5,45,88,1,3,8])
print(list_sorted)

binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 5)
