"""
Sprawdzenie czy da się utworzyć daną liczbę z jakichkolwiek dwóch liczb z listy
"""
lista = [2, 45, 25, 34, 8, 5, 3, 4]
my_number = 8
is_true = False


def summary(list, number=my_number):
    times = 0
    ed = len(lista) - 1
    for el in list:
        for nel in range(1, ed):
            if el + lista[nel] == number:
                times += 1
    if times > 0:
        print(f'There is {times} possible way(s) of creating {number} by adding two numbers from given list')
    else:
        print(f'No matching sums to create {number}')


while is_true is False:
    try:
        inn = int(input("insert wanted sum: "))
        is_true = 0
    except ValueError:
        print('Please insert integers only')

summary(lista, inn)
