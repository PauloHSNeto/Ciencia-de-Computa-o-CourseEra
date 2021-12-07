lista=list( input ("digite a lista:"))
novalista=[]
for x in lista:
    if int(x)%2==0:
        novalista+=x
        
print(novalista)
