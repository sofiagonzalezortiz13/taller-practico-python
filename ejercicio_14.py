numero = int(input("Hola ingresa un número entero no negativo y diferente de cero porfaaaa: "))

while numero < 0:
    numero = int(input("Ma G, error, Ingresa un número no negativo: "))

factorial = 1
contador = 1

while contador <= numero:
    factorial = factorial * contador
    contador = contador + 1

print("El factorial es:", factorial)
