min = int(input("Minutos utilizados: "))
if min < 200:
    preco = 0.20
else:
    if min <= 400:
            preco = 0.18
    else:
            precexito = 0.15
print("Conta telefonica: R$ %6.2f" % (min*preco))