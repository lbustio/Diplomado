# Solicitar al usuario ingresar un número entero positivo
numero_str = input("Ingrese un numero entero positivo: ")

# Validar que la entrada sea un número entero positivo
while not numero_str.isdigit():
    print("Error: La entrada debe ser un numero entero positivo.")
    numero_str = input("Ingrese un numero entero positivo: ")

# Convertir la entrada a un número entero
numero = int(numero_str)

# Calcular la suma de los dígitos del número
suma_digitos = 0
for digito in str(numero):
    suma_digitos += int(digito)

# Mostrar el resultado
print("La suma de los digitos del numero ingresado es:", suma_digitos)