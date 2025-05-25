import sys
import os 
import zipfile
import rarfile

def extraerZip(archivo, carpeta):
    try:
        with zipfile.ZipFile(archivo, "r") as archivo:
                archivo.extractall(carpeta)
        print("Archivo descomprimido con Exito!!")
    except zipfile.BadZipFile:
        print("Error: no es un archivo zip valido")

def extraerRar(archivo, carpeta):
    try:
        with rarfile.RarFile(archivo, "r") as archivo:
            if archivo.needs_password():
                password = input("Ingresa la contraseña: ")
                archivo.extractall(carpeta, pwd=password)
        print("Archivo descomprimido con Exito!!")
    except rarfile.Error:
        print("Error: no es un archivo rar valido")



if len(sys.argv) < 2:
    print("Debes de ingresar por lo menos un archivo")
    exit()

nombreArchivo = sys.argv[1]
nombreBase, extencion = os.path.splitext(nombreArchivo)

directorioTemporal = os.path.dirname(os.path.abspath(__file__))
rutaCarpeta = os.path.join(directorioTemporal, nombreBase)

try: 
    os.makedirs(rutaCarpeta)

except FileExistsError:
    print("La carpeta ya existe")

if extencion == ".zip":
    extraerZip(nombreArchivo, rutaCarpeta)

elif extencion == ".rar":
    extraerRar(nombreArchivo, rutaCarpeta)
