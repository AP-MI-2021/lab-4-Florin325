def citire_lista(n):
    list = []
    for i in range(0, n):
        list.append(int(input("Numar=")))
    return list



def is_superprime(n):
    while n != 0:
        if is_prime(n):
            n = n//10
        else:
           return False
    return True


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for d in range(2, n//2):
            if n % d == 0:
                return False
    return  True

def get_superprime(list):
    superprime = []
    for n in list:
        if is_superprime(n):
            superprime.append(n)
    return superprime

def invers(n):
    inv = 0
    while n != 0:
        inv = inv + n % 10
        n = n//10

def find_cmmdc(n, m):
    while n != m:
        if n > m:
            n = n - m
        else:
            m = m - n
    return n

def smallest_last_digit_k(n, k, list):
    min = 0
    for n in list:
        if n % 10 == k and n < min:
            min = n
    if min in list:
        return min
    else:
        return False

def afisarea_numere_negative(list):
    neg = []
    for n in list:
        if n < 0:
            neg.append(n)
    return neg


def modificare_lista(list):
    list_modificat = []
    cmmdc = 1
    for i in range(0, len(list)):
        if list[i] > 0:
            cmmdc = find_cmmdc(cmmdc, list[i])
        else:
            list[i] =  -int(invers(list[i]))
    for i in range(0, len(list)):
        if list[i] > 0:
            list[i] = cmmdc
    return list_modificat

def test_modificare_lista(list):
    assert modificare_lista([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]
    assert modificare_lista([-1, 34, -25, 42, 12]) ==  [-1, 2, -52, 2, 2]

def main():

    print("1. Citire lista")
    print("2. Afișarea tuturor numerelor negative nenule din listă")
    print("3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură")
    print("4. Afișarea tuturor numerelor din listă care sunt superprime")
    print("5. Afișarea listei modificate")
    print("6. Iesire program")

    while True:
        x = input("Comanda=")
        if x == 1:
            n = int(input("Numar de elemente din lista="))
            citire_lista(n)
        elif x == 2:
            print(afisarea_numere_negative(list))
        elif x == 3:
            k = int(input("Cifra="))
            print(smallest_last_digit_k(len(list), k, list))
        elif x == 4:
            print(get_superprime(list))
        elif x == 5:
            print(modificare_lista(list))
        elif x == 6:
            break
        else:
            print("Comanda invalida")







