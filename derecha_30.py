
# 1. Crear una lista con ocho números
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# 2. Mostrar la lista original
print("Lista original:", numeros)

# 3. Guardar el último número de la lista
ultimo = numeros[-1]

# 4. Insertar el último número en la primera posición
numeros.insert(0, ultimo)

# 5. Eliminar el último elemento de la lista
numeros.pop()

# 6. Mostrar la lista rotada hacia la derecha
print("Lista rotada:", numeros)