"""
1.zliczyć wyrazy
2.zliczyc litery
3.zbadać częstotliwość występowania liter
"""

struna = "Na wyścigach wyścigowych wyścigówka wyścigowa wyścignęła wyścigówkę wyścigowa numer 2"

def task1():
    spl = struna.split()
    print(f"ilość wyrazów: {len(spl)}")

def task2():
    jn = ''.join(struna.split())
    print(f"ilość liter i spacji: {len(struna)}")
    print(f"ilość liter: {len(jn)}")

def task3():
    jn = ''.join(struna.split())
    a = 0
    b = 0
    i = 0
    for lt in jn:
        if lt.lower() == 'a':
            a += 1
        elif lt.lower() == 'b':
            b += 1
        elif lt.lower() == 'ś':
            i += 1
    print(f"liter 'a' jest {a}, 'b' jest {b}, a 'i' jest {i}")


task1()
task2()
task3()
