#Pergguntar a velocidade do carro (inteiro). Caso ultrapasse 110km/h, exibibir 
# mensagem dizendo que o usuário foi multado.
# Exibir valor da multa cobrando R$ 5,00 por km acima de 110.

vel = int(input("Velocidade: "))
if vel > 110:
    print("Você foi multado")
    multa = (vel-110)*5
    print("Valor da multa: R$ %5.2f" %multa)  