def valida_numeros(list):
    for num in list:
        try:
            int(num)
        except:
            print("ingresó valor no valido")
            return False
    return True

validador = "valid"
while validador == "no valid":
    numbers = input("ingrese numeros separados por espacio: ")
    numbers_list = numbers.split()
    
    numbers_impar=[]
    numbers_par=[]

    validador == valida_numeros(numbers_list)

for numbers in numbers_list:
    mod = numbers % 2
    if mod == 0:
        numbers_impar.append(numbers)
        numbers_par.append(numbers)

print(f"numeros pares", numbers_par)
print(f"numeros pares", numbers_impar)


