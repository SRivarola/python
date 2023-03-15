productos = {}

def mostrar_diccionario(diccionario: dict):
    for x,y in diccionario.items():
        print(f'{x}. {y}')

def agregar_producto(diccionario: dict):
    nombre = input('Ingrese el nombre del producto: ')
    if nombre in diccionario:
        print('Este producto ya existe intente con otro')
    else:
        cantidad = input('Ingerse la cantidad: ')
        precio = input('Ingrese el precio: ')

        diccionario[nombre] = {'Cantidad': cantidad, 'Precio': precio}

        print('\nProducto guardado')

def eliminar_producto(diccionario: dict):
    nombre = input('Ingrese el nombre del producto a eliminar: ')
    if nombre in diccionario:
        diccionario.pop(nombre)
    else:
        print('El nombre ingresado no esta en la lista de productos')

    print(f'Producto {nombre} eliminado')

def ver_productos(diccionario: dict):
    for clave, valor in diccionario.items():
        print(f'\n{clave}:')
        for a, b in valor.items():
            print(f'\t{a}: {b}')
    print('\n\n')

def finalizar_compra(diccionario: dict):
    total_precio = 0
    total_cantidad = 0
    for clave, valor in diccionario.items():
        lista_2 = []
        for a, b in valor.items():
            lista_2.append(b)
        total_precio = total_precio + (int(lista_2[0])*float(lista_2[1]))
        total_cantidad = total_cantidad + int(lista_2[0])
    print(f'\n{total_cantidad} productos: ${total_precio}\n')

def comprobar_opcion(opcion):
    if opcion >= 1 and opcion <= 4:
        if opcion == 1:
            agregar_producto(productos)
            return False
        elif opcion == 2:
            eliminar_producto(productos)
            return False
        elif opcion == 3:
            ver_productos(productos)
            return False  
        elif opcion == 4:
            finalizar_compra(productos)
            print('\n')
            return True
    else:
        print('\nOpcion incorrecta, por favor eliga del 1 al 4\n')
        return False