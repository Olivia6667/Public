input_nums = input("Введите несколько чисел через пробел:").split()
for i in input_nums:
    if not i.isdigit():
        input_nums = input("Ошибка ввода. Вводите только числа через пробел:").split()
    else:
        pass

input_num = input("Введите число:").split()
for j in input_num:
    if j.isdigit() is not True:
        input_num = input("Ошибка ввода. Введите только число:").split()
    else:
        pass

list1 = [input_nums]
list2 = [input_num]
list_sum = list1 + list2

new_list = []
for number in list_sum:
    new_list += number

final_list = [int(i) for i in new_list]


def insertion_sort(list):
    for num1 in range(1, len(list)):
        el = list[num1]
        num2 = num1 - 1
        while list[num2] > el and num2 >= 0:
            list[num2 + 1] = list[num2]
            num2 -= 1
        list[num2 + 1] = el
    return list


print("Отсортированный по возрастанию список:", insertion_sort(final_list))


def binary_search(array, element, left, right):
    if left > right:
        return False

    if element > array[right]:
        return right

    middle = (right + left) // 2

    if array[middle] == element:
        while array[middle] == element:
            middle = middle - 1
        return middle
    elif array[middle + 1] > element > array[middle]:
        return middle
    elif element > array[middle]:
        return binary_search(array, element, middle + 1, right)
    else:
        return binary_search(array, element, left, middle - 1)


mass = insertion_sort(final_list)
array = [int(i) for i in final_list]
element = int(input_num[0])

if element <= array[0]:
    print("Список не содержит элементов меньше заданного числа")
else:
    print("Номер позиции элемента, соответствующего условиям:", binary_search(array, element, 0, len(array) - 1))
