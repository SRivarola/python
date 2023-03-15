from agenda.funciones_agenda import mostrar_diccionario, comprobar_opcion, contactos

# menu de opciones

menu = {
    1: 'Agregar contacto',
    2: 'Eliminar contacto',
    3: 'Editar contacto',
    4: 'Ver todos los contactos',
    5: 'Buscar contacto',
    6: 'Salir'
}

# Ciclo while
verificacion = True

while verificacion:
    mostrar_diccionario(menu)
    valor= int(input('\nElija una opcion: '))
    verificacion = comprobar_opcion(valor)


print(contactos)