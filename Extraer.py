#!/usr/bin/env python3

import sys  # Manejo de argumentos desde la línea de comandos
import os  # Operaciones con el sistema de archivos
import zipfile  # Para manejar archivos ZIP
import rarfile  # Para manejar archivos RAR
from tqdm import tqdm # Para la barra de tareas

# Función para extraer archivos ZIP
def extraerZip(archivo, carpeta):
    try: 
        with zipfile.ZipFile(archivo, "r") as archivo:
            print("Extrayendo {archivo}")
            for member in tqdm(archivo.infolist(), desc="Extracting "):
                    archivo.extract(member)
            print("Archivo descomprimido con exito!!")
    except:
        print("Erro al extraer el archivo")

# Función para extraer archivos RAR
def extraerRar(archivo, carpeta):
    try:
        with rarfile.RarFile(archivo, "r") as archivo:
            print(f"Extrayendo {archivo}")
            if archivo.needs_password():  # Comprueba si necesita contraseña
                password = input("Ingresa la contraseña: ")
                for member in tqdm(archivo.infolist(), desc="Extracting"):
                    archivo.extract(member, pwd=password)
            else:
                for member in tqdm(archivo.infolist(), desc="Extracting"):
                    archivo.extract(member)

        print("Archivo descomprimido con éxito!!")
    except rarfile.Error:
        print("Error: no es un archivo RAR válido")

# Verifica que se haya proporcionado al menos un archivo como argumento
if len(sys.argv) < 2:
    print("Debes de ingresar por lo menos un archivo")
    exit()

nombreArchivo = sys.argv[1]
nombreBase, extencion = os.path.splitext(nombreArchivo)  # Separa el nombre y la extensión

# Crea una carpeta para la extracción con el nombre del archivo (sin extensión)
directorioActual = os.getcwd()
rutaCarpeta = os.path.join(directorioActual, nombreBase)

try: 
    os.makedirs(rutaCarpeta)  # Crea la carpeta si no existe
except FileExistsError:
    print("La carpeta ya existe")

# Determina el tipo de archivo por su extensión y llama a la función correspondiente
if extencion == ".zip":
    extraerZip(nombreArchivo, rutaCarpeta)
elif extencion == ".rar":
    extraerRar(nombreArchivo, rutaCarpeta)
else:
    print("El archivo no es un formato extraíble")

