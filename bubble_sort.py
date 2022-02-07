"""
wzór na ilość przejść w bąbelkowym:

|n(n-1)|
|------|
|   2  |

"""


lista = [23, 4, 5, 3, 78, 34, 15, 2, 5, 7, 8, 56, 53]

def bubble_sortowanie(l):
    n = len(l)
    f = 0
    while n > 1:
        for x in range(0, n-1):
            if l[x] > l[x+1]:
                l[x], l[x+1] = l[x+1], l[x]
            print(lista)
            f += 1
        n -= 1
    print(f)


bubble_sortowanie(lista)
