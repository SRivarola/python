contactos = {}

def mostrar_diccionario(diccionario: dict):
    for x,y in diccionario.items():
        print(f'{x}. {y}')


def agregar_contacto():

    nombre = input('Ingrese el nombre del contacto: ')
    id = input('Ingrese el Id: ')
    direccion = input('Ingrese la direccion: ')
    celular = input('Ingrese el celular: ')
    
    contactos[nombre] = {'Id': id, 'Direccion': direccion, 'Celular': celular}
    
    print('Contacto Guardado.\n')

def eliminar_contacto():
    nombre = input('Ingrese el nombre del contacto a eliminar: ')
    if nombre in contactos:
        contactos.pop(nombre)
    else:
        print('El nombre ingresado no esta en la lista de contactos')

    print(f'Contacto {nombre} eliminado')

def editar_contacto():
    nombre = input('Ingrese el nombre del contacto que quiere editar: ')
    if nombre in contactos:
        contacto = contactos[nombre]
        direccion = input('Ingresar nueva direccion: ')
        celular = input('Ingresar nuevo celular')
        contacto.update({'Direccion': direccion, 'Celular': celular})
        print('\nEl contacto ha sido actualizado')
    else:
        print('\nEl contacto no existe.\n\n')

def ver_contactos():
    for clave, valor in contactos.items():
        print(f'\n{clave}:')
        for a, b in valor.items():
            print(f'\t{a}: {b}')
    print('\n\n')

def buscar_contacto():
    nombre: input('Ingrese el nombre del contacto: ')
    if nombre in contactos:
        print(f'\n{nombre.upper()}:\n')
        
        contacto = contactos[nombre] 

        for x, y in contacto.items():
            print(f'{x}: {y}')
    else:
        print('Contacto no encontrado')
    print('\n')

def comprobar_opcion(opcion):
    if opcion >=1 and opcion <= 6:
        if opcion == 1:
            agregar_contacto()
            return True
        elif opcion == 2:
            eliminar_contacto()
            return True
        elif opcion == 3:
            editar_contacto()
            return True  
        elif opcion == 4:
            ver_contactos()
            return True   
        elif opcion == 5:
            buscar_contacto()
            return True   
        elif opcion == 6:
            'editar_contacto'
            return False
    else:
        print('\nOpcion incorrecta, por favor eliga del 1 al 6\n')
        return True