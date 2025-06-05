import json
import os

def limpiarconsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def ENTERContinuar(mensaje: str = "Presione ENTER para continuar: \n -> "):
    input(mensaje)

#DIC = {"ID": 1, "Nombre": "Adrian Bayona", "Telefono": "+57 3224732154", "Email": "adrianbayona325@gmail.com"}

def escribirArchivoJSON(path: str, mode= 'w'):
    try:
        ent = int(input("Ingrese la cantidad de usuarios a registrar: \n -> "))
        usuarios = []
        for i in range(ent):
            print("")
            Id = input(f"Ingrese el ID del usuario {i + 1}: ")
            Nombre = input(f"Ingrese el Nombre del usuario {i + 1}: ")
            Telefono = input(f"Ingrese el Telefono del usuario {i + 1}: ")
            Email = input(f"Ingrese el Email del usuario {i + 1}: ")
            usuarios.append({"ID": Id, "Nombre": Nombre, "Telefono": Telefono, "Email": Email})

        with open(path, mode) as file:
            campos = ["ID", "Nombre", "Telefono", "Email"]
            json.dump(usuarios, file, indent=4)

    except FileNotFoundError:
        print("Lo sentimos, el archivo no existe")

''' def agregarUsuario(path: str, mode= 'w'):
        try:
            with open(path, mode) as file:
                json.dump(DIC, file, indent=4)
        except FileNotFoundError:
            print("Lo sentimos, el archivo no existe")'''

def leerArchivoJSON(path: str, mode = 'r') -> list:
    try:
        with open(path, mode) as file:
            datos = json.load(file)
            print("\n=== TODOS LOS USUARIOS ===")
            for usuario in datos:
                print(f"ID: {usuario['ID']}, Nombre: {usuario['Nombre']}, Telefono: {usuario['Telefono']}, Email: {usuario['Email']}")
            return datos
    except FileNotFoundError:
        print("Lo sentimos, el archivo no existe")

def editarArchivoJSON(path: str, IDBusqueda: str, NewTelefono: str, NewEmail: str):
    try:
        with open(path, mode='r') as file:
            reader = json.load(file)
            datos = list(reader)
            print("\n=== TODOS LOS USUARIOS ===")
            for usuario in datos:
                print(f"ID: {usuario['ID']}, Nombre: {usuario['Nombre']}, Telefono: {usuario['Telefono']}, Email: {usuario['Email']}")
            return datos
        
        modificado = False
        for usuario in datos:
            if usuario['ID'] == IDBusqueda:
                usuario['Telefono'] = NewTelefono
                usuario['Email'] = NewEmail
                modificado = True
                break
        
        if not modificado:
            print(f'No se ha encontrado un usuario con ID: {IDBusqueda}')
            return False
        
        with open(path, mode='w') as file:
            json.dump(usuarios, file, indent=4)

        print(f"Los datos del usuario con ID: {IDBusqueda} han sido actualizados")
        return True
    
    except FileNotFoundError:
        print("Lo sentimos, el archivo no existe")

menu = """

██████████████████████████████
█▄─▀█▀─▄█▄─▄▄─█▄─▀█▄─▄█▄─██─▄█
██─█▄█─███─▄█▀██─█▄▀─███─██─██
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀

    1. Escribir datos
    2. Leer datos
    3. Editar datos
    4. Eliminar datos
    5. Salir
"""

while True:
    limpiarconsola()
    print(menu)
    opcion = input("Seleccionem una opcion del Menu:\n -> ")
    if opcion == "1":
        escribirArchivoJSON('contacts.json')
        #agregarUsuario('contacts.json')
        ENTERContinuar()
    elif opcion == "2":
        leerArchivoJSON('contacts.json')
        ENTERContinuar()
    elif opcion == "3":
        IDBusqueda = input("Ingrese el ID del usuario que desea buscar: \n -> ")
        NewTelefono = input("Ingrese el nuevo Número de telefono del usuario: \n -> ")
        NewEmail = input("Ingrese el nuevo Email de telefono del usuario: \n -> ")
        editarArchivoJSON('contacts.json', IDBusqueda, NewTelefono, NewEmail)
        ENTERContinuar()
    elif opcion == "4":
        ENTERContinuar()
    elif opcion == "5":
        print("Saliendo del programa....")
        print("Has salido del programa.")
        break
    else:
        ENTERContinuar()