def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

liczby = [7, 10]

for liczba in liczby:
    if czy_pierwsza(liczba):
        print("True")
    else:
        print("False")
