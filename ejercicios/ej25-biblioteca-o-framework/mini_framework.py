# mini_framework.py · Un framework de juguete para chatbots. NO HAY QUE CAMBIARLO.
# El framework tiene el control: decide CUÁNDO se llama a cada método de tu aplicación.

MENSAJES_DE_PRUEBA = ["hola", "¿cuándo es el examen?", "adiós"]


def arrancar(app):
    print("[framework] Arrancando la aplicación...")
    app.al_iniciar()
    for mensaje in MENSAJES_DE_PRUEBA:
        print(f"Tú: {mensaje}")
        respuesta = app.al_recibir(mensaje)
        print(f"Bot: {respuesta}")
    app.al_terminar()
    print("[framework] Aplicación terminada.")
