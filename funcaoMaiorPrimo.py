def maior_primo (x):
    maiorPrimo=1
    num = 1
    while num <= x:
        divisores = 0
        divisor = 2
        while divisor<num:
            if num%divisor==0:
                divisores=divisores+1
            divisor = divisor+1
        if (divisores==0):
            maior_primo=num
        num = num + 1

    return maior_primo
