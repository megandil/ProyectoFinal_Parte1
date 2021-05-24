import json
from funciones import *
nombre=input("Introduce tu nombre de steam (por defecto Megadani1020): ")
id=nombre_id(nombre)
key=os.environ["key"]
print()
print('''1.Ver juegos que tienes.
2.Ver juegos recientemente jugados.
3.Información sobre tu usuario.
4.Salir.
''')
opcion=int(input("Introduce una opcion: "))
while opcion != 4:
    if opcion == 1:
        print()
        print("---JUEGOS---")
        for i in juegos_obtiene(key,id):
            print("-",i)
        print()
    if opcion == 2:
        print()
        print("---JUEGOS RECIENTES---")
        for i in juegos_recientes(key,id):
            print("-",i)
        print()
    if opcion == 3:
        print()
        print("---INFORMACIÓN USUARIO---")
        print("- SteamID: ",info_user(key,id)[0])
        print("- Nombre Real: ",info_user(key,id)[1])
        print("- País: ",info_user(key,id)[2])
        print()
    print('''1.Ver juegos que tienes.
2.Ver juegos recientemente jugados.
3.Información sobre tu usuario.
4.Salir.
''')
    opcion=int(input("Introduce una opcion: "))