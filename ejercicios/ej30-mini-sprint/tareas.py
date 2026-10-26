# Ej30 · tareas.py · Lista de tareas (el producto del Sprint)
# Cada tarea es un diccionario:  {"texto": "Estudiar", "hecha": False}


def añadir(tareas, texto):
    # Historia #1: añade al final de la lista una tarea nueva sin marcar.
    pass


def ver(tareas):
    # Historia #2: muestra cada tarea numerada desde 1, con [x] si está hecha y [ ] si no:
    #   1. [x] Ejercicios del tema 1 de ED
    # Pista: for i, tarea in enumerate(tareas, start=1):
    pass


def marcar_hecha(tareas, numero):
    # Historia #3: marca como hecha la tarea con ese número (¡ojo! la 1 está en la posición 0).
    pass


def borrar(tareas, numero):
    # Historia #4: borra la tarea con ese número. Pista: tareas.pop(numero - 1)
    pass


def pendientes(tareas):
    # Historia #5: devuelve el texto  "Pendientes: 2 de 3"
    return ""


# Prueba del producto: NO hay que cambiar nada de aquí abajo.
if __name__ == "__main__":
    mis_tareas = []
    añadir(mis_tareas, "Ejercicios del tema 1 de ED")
    añadir(mis_tareas, "Ver una serie")
    añadir(mis_tareas, "Estudiar para el examen")
    añadir(mis_tareas, "Práctica de GitHub")
    marcar_hecha(mis_tareas, 1)
    borrar(mis_tareas, 2)
    ver(mis_tareas)
    print(pendientes(mis_tareas))
