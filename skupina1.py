x = input('zadejte čislo x: ')
y = input('zadejte čislo y: ')

x = int(x)
y = int(y)


print('Pro sčítání zadejte +')
print('Pro odčítání zadejte -')
print('Pro násobení zadejte *')
print('Pro dělení zadejte /')
print('Pro mocnění zadejte **')
print('Pro odmocnění zadejte /*')

znamenko = input('zvolte si operátor')

if znamenko == '+':
    vysledek = x + y
    vysledek = str(vysledek)
    print('vysledek je:' + vysledek)

elif znamenko == '-':
    vysledek = x - y
    vysledek = str(vysledek)
    print('vysledek je:' + vysledek)

elif znamenko == '*':
    vysledek = x * y
    vysledek = str(vysledek)
    print('vysledek je:' + vysledek)

elif znamenko == '/':
    if y != 0:
        vysledek = x / y
        vysledek = str(vysledek)
        print('vysledek je:' + vysledek)
    else:
        print('nemůžeš dělit nulou')


elif znamenko == '**':
    vysledek = x ** y
    vysledek = str(vysledek)
    print('vysledek je:' + vysledek)

elif znamenko == '/*':
    vysledek = x * 1/y
    vysledek = str(vysledek)
    print('vysledek je:' + vysledek)
