segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos//(3600*24)
resto_de_dias = segundos%(3600*24)
horas = resto_de_dias//3600
resto_de_horas = resto_de_dias%3600
minutos = resto_de_horas//60
segundos = resto_de_horas%60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")

