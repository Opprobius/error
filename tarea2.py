# print("""
#         1.- Leer archivo
#         2.- Listar libros
#         3.- Agregar libros
#         4.- Eliminar libros
#         5.- Buscar Libro por ISBN o titulo
#         6.- Ordenar libros por titulo
#         7.- Buscar libros por autor, editorial, y/o genero
#         8.- Buscar libros por numero de autores
#         9.- Editar Libro
#         10.- Guardar Libros
#         """)


import time
import os
import csv


class Libro:
    def __init__(self, id, titulo, genero, isbn, editorial,autores):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autores = autores

    def set_autores(self, autores):
        self.autores = autores

    def get_autores(self):
        return self.autores

    def get_genero(self):
        return self.genero

    def get_titulo(self):
        return self.titulo

    def get_isbn(self):
        return self.isbn

    def mostrar_info(self):
        return f"({self.id})|{self.titulo} | {self.genero} | {self.isbn} | {self.editorial} | {self.get_autores()}"

    def __repr__(self):
        return f"({self.id})|{self.titulo} | {self.genero} | {self.isbn} | {self.editorial} | {self.get_autores()}"


def delete_books(data, id):
    print(data[0])
    for indice, item in enumerate(data[1::], start=1):
        if int(id) == int(item.id):
            libro = data.pop(indice)
            print(libro)
            print('El libro ha sido eliminado correctamente!')
            time.sleep(2)
    return data

def crear_libro(data) -> list:
    id = int(data[-1].id) + 1
    titulo, genero, isbn, editorial, autores = '', '', '', '',  []
    preguntas = [
        "Ingrese un titulo", "ingrese un genero",
        "Digite el isbn", "ingrese una editorial",
        "Escriba los autores(si hay mas de uno use una ',')"
    ]
    respuestas = []
    for pregunta in preguntas:
        dato = input(pregunta)
        # while dato
        respuestas.append(dato)

    titulo, genero, isbn, editorial, autores =  respuestas
    autores = autores.split(',')

    libro_instancia  = Libro(id, titulo, genero, isbn, editorial, autores)
    data.append(libro_instancia)
    print(libro_instancia)
    print('Libro creado correctamente!')
    time.sleep(1)
    return data

def listar_libros(data):
    print(data[0])
    for libro_instancia in data[1::]:
        print(libro_instancia.mostrar_info())

def crear_nuevo_archivo():
    filename ='libros1.csv'
    file = open('nuevo_archivo_libros.csv','w')
    file.write('Id,Titulo,Genero,Isbn,Editorial,Autores'+os.linesep)
    file.close()
    data_libros = cargar_archivo(filename)
    return data_libros



def cargar_archivo(nombre_archivo):
    try:
        data_libros = []
        with open(nombre_archivo, encoding="utf-8") as archivo:
            data_archivo = csv.reader(archivo)
            for indice, data in enumerate(data_archivo):
                if indice != 0:
                    id, titulo, genero, isbn, editorial, autores = data
                    autores = autores[:-1].split('|')
                    libro_instancia = Libro(id, titulo, genero, isbn, editorial, autores)
                    data_libros.append(libro_instancia)
                else:
                    data_libros.append(data)
        print('Datos cargados correctamente!')
        time.sleep(2)
    except FileNotFoundError:
        print("El archivo no existe. Porfavor ingrese el nombre de un archivo existente.")
        time.sleep(3)
        return nombre_archivo, datos_libros
    return nombre_archivo, data_libros







def order_books_by_title(data):
    print(data[0])
    data[1::].sort(key=str.lower)
    return data

def search_book_by_autor_editorial_genero(data, autor, editorial, genero):
    pass

def search_book_by_numero_autores(self, numero_autores):
    pass

def buscar_libro(data: list, isbn: str, titulo: str)->list:
    print(data[0])
    for indice, item in enumerate(data[1::], start=1):
        if str(isbn) == str(item.isbn):
            libro = data.pop(indice)
            print(libro)
            print('El libro ha sido eliminado correctamente!')
    return data

def edit_book(data, id):
    pass


def parse_data_libro(instance_book):
    data = []
    data.append(instance_book.id)
    data.append(instance_book.titulo)
    data.append(instance_book.get_genero())
    data.append(instance_book.isbn)
    data.append(instance_book.editorial)
    autores = "|".join(instance_book.autores)
    data.append(autores)
    return data

def guardar(datos_libros, nombre_archivo):
    with open(str(nombre_archivo), 'w', newline='') as archivo:
        print('ingreso al open')
        writer = csv.writer(archivo, delimiter=',')
        for indice, data in enumerate(datos_libros):
            print(str(indice)+' iterando for')

            if indice != 0:
                print(parse_data_libro(data))
                writer.writerow(parse_data_libro(data))
            else:
                writer.writerow(data)
    print('Datos guardados exitosamente')
    return "Datos Guardados exitosamente."


#MENU

menu_options = {
    1: 'Cargar Archivo',
    2: 'Listar Libros',
    3: 'Agregar libro',
    4: 'Eliminar libro',
    5: 'Buscar Libro por ISBN o titulo',
    6: 'Ordenar libros por titulo',
    7: 'Buscar libros por autor, editorial, y/o genero',
    8: 'Buscar libros por numero de autores',
    9: 'Editar Libro',
    10: 'Guardar libros en un nuevo archivo',
    11: 'Salir'
}

def mostrar_menu(menu_options, bandera=True):
    for key in menu_options.keys():
        print(str(key)+'-'+menu_options[key])


def verificar_datos(data):
    if not data:
        print('No tiene datos, cargue o cree un nuevo archivo.')
        time.sleep(2)
        return False
    return True

if  __name__ == '__main__':
    datos_libros = []
    nombre_archivo = ''
    while True:
        print(' ======================')
        print('|   MENU PRINCIPAL     |')
        print(' ======================')
        mostrar_menu(menu_options)
        try:
            opcion = int(input('Que desea hacer?: '))
        except:
            print('Por favor ingrese una opcion valida.')
        if opcion == 1:
            nombre_archivo = input('Ingrese el nombre del archivo: ')
            while len(nombre_archivo) == 0:
                nombre_archiv1o = input('Ingrese el nombre del archivo por favor')
            nombre_archivo +='.csv'
            nombre_archivo, datos_libros = cargar_archivo(nombre_archivo)
        elif opcion == 2:
            if not verificar_datos(datos_libros):
                time.sleep(1)
            else:
                listar_libros(datos_libros)
                respuesta = input('escriba "q" para regresar al menu principal : ')
                while respuesta.lower() not in ['q']:
                    respuesta = input(
                        'Por favor esriba "q" para salir al menu principal: ')
                    respuesta = respuesta.lower()
                if respuesta == 'q':
                    time.sleep(1)


        elif opcion == 3:
            datos_libros = crear_libro(datos_libros)
        elif opcion == 4:
            id_libro = ''
            try:
                id_libro = int(input('Escriba el id del libro a eliminar'))
            except:
                print('Se necesita un id(numero)')
            if id_libro > 0:
                datos_libros = delete_books(datos_libros, id_libro)
                listar_libros(datos_libros)
        elif opcion == 5:
            mostrar_menu({
                1: 'Buscar por ISBN',
                2: 'Buscar por Titulo',
                3: 'Volver al menu principal'
            })
            isbn, titulo = '', ''
            opcion = int(input('Ingrese una opcion'))
            while opcion not in [1, 2,3]:
                opcion = int(input(
                    'Por favor ingrese una opcion correcta.'))
            if opcion == 1:
                print('Buscar por isbn')
            elif opcion == 2:
                print('Buscar por titulo')
            else:
                pass
        elif opcion == 6:
            order_books_by_title(datos_libros)

        elif opcion == 7:
            mostrar_menu({
                1: 'Buscar por autor',
                2: 'Buscar por editorial',
                3: 'Buscar por genero',
                4: 'Regresar al menu principal'
            })
        elif opcion == 8:
            print('Buscar por numero de autores')
        elif opcion == 9:
            print("editar libro, insetar un id")
        elif opcion == 10:
            respuesta = input('Escriba el nombre del nuevo archivo: ')
            respuesta +='.csv'
            if respuesta.lower() == nombre_archivo:
                opcion = int(input('Desea sobreescribir el archivo? escriba si / no'))
                if opcion == 'si':
                    guardar(datos_libros, nombre_archivo)
                else:
                    print('No se ha podido guardar el archivo. Intente nuevamente')
            else:
                print('what')
                guardar(datos_libros, respuesta)
        elif opcion==11:
            exit()
        else:
            print('Opcion invalida. Por favor elija un numero correcto.')
