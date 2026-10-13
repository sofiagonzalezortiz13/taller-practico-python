datos = []

saldo = float(input("Ingrese el saldo de su cuenta: "))
retiro = float(input("Ingrese el valor que desea retirar: "))

datos.append(saldo)
datos.append(retiro)

for valor in datos:
    print("Dato ingresado:", valor)

if retiro <= 0:
    print("Error: el retiro debe ser mayor que cero.")
elif retiro > saldo:
    print("Error: no tiene suficiente saldo.")
else:
    saldo = saldo - retiro
    datos.append(saldo)

    print("Retiro exitoso.")

    for valor in datos:
        print("Saldo, retiro o resultado:", valor)

    print("Su saldo restante es:", saldo)
