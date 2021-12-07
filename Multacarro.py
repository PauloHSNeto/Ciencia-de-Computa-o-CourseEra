vel = int(input("Qual é a velocidade do carro:"))
if vel > 80:
    multa = (vel - 80)*7
    print("O carro será multado um valor de ", multa, "R$.")
