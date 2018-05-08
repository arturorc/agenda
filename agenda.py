agenda = {}


def agregar_contacto():
    """Función para agregar contacto"""
    nombre = input('Nombre del nuevo contacto: ')
    numero = input('Ingrese el número: ')
    agenda[nombre] = numero
    print('Contacto %s agregado' % nombre)


def remover_contacto():
    """Función para eliminar contacto"""
    nombre = input('Nombre del contacto: ')
    try:
        del (agenda[nombre])
    except KeyError:
        'Ese contacto no existe'
    else:
        print('Contacto %s eliminado' % nombre)


def actualizar_contacto():
    """Función para actualizar contacto"""


def ver_contacto():
    """Función para ver contacto"""


def ver_todos():
    """Función para ver todos los contactos"""


print('Bienvenido a la agenda')
while True:
    print('1 - Agregar contacto')
    print('2 - Remover contacto')
    print('3 - Actualizar contacto')
    print('4 - Ver un contacto')
    print('5 - Ver todos los contactos')
    print('6 - Salir')
    try:
        op = int(input('Seleccione operacion: '))
    except ValueError:
        print('Ingrese un numero')
    else:
        if op == 1:
            agregar_contacto()
        elif op == 2:
            remover_contacto()
        elif op == 3:
            actualizar_contacto()
        elif op == 4:
            ver_contacto()
        elif op == 5:
            ver_todos()
        else:
            break
