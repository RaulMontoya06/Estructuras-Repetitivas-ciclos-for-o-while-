print("CONTADOR DE DIGITOS")
num = int(input("ingresa un numero : "))
cont = 0
n = abs(num)  
while n > 0:
    n //= 10
    cont += 1
print(f"El número {num} tiene {cont} dígitos")              
