from funciones_ticketera import mostrar_diccionario, comprobar_opcion

menu = {
    1: 'Agregar producto',
    2: 'Eliminar producto',
    3: 'Ver lista de productos',
    4: 'Finalizar compra'
}

menu_variable = False

while not menu_variable:
    mostrar_diccionario(menu)

    valor = int(input('\nElija una opcion: '))

    menu_variable = comprobar_opcion(valor)