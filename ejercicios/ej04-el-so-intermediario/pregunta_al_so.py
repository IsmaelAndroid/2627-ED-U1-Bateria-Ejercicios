# Ej04 · El sistema operativo como intermediario
# Cada línea de este programa le pide algo al sistema operativo.
import os
import platform

# PASO 1: muestra el nombre del sistema y la versión del núcleo.
# Pista: platform.system() y platform.release()
#   Sistema operativo: Linux 6.5.0-1025-azure


# PASO 2: muestra la arquitectura del procesador. Pista: platform.machine()


# PASO 3: muestra cuántos núcleos tiene la CPU. Pista: os.cpu_count()


# PASO 4: pide al SO que cree un fichero "saludo.txt" con el texto "Hola, disco".
# Tu programa no escribe en el disco: se lo pide al SO, que usa el driver del disco.


# PASO 5: muestra la carpeta actual (os.getcwd()) y la lista de ficheros que hay
# en ella, ordenada (sorted(os.listdir("."))) y separada por comas.


# PASO 6: muestra el número de proceso que el SO ha dado a este programa (os.getpid()).

