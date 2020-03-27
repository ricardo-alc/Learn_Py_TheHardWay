#Crear 1 lista vacía con dos index vacíos
datos = [] 
datos.append([])
datos.append([])

# Agregar elementos a nuestra lista
datos[0].append(1)
datos[0].append(2)
datos[1].append(3)
datos[1].append(4)


#print(datos[0][0])
print(datos)

# imprimir
for row in datos:
    for column in row:
        print(column, end="")
    print(end="\n")
