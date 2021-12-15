def encontra_impares(lista):
    if not lista:
        return[]
    if lista[0]%2==1:
        return [lista[0]] +encontra_impares(lista[1:])
    return encontra_impares(lista[1:])




a=[1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17]
print(encontra_impares(a))