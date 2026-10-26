# Ej25 · Parte B · Usar un framework: el FRAMEWORK llama a tu código
from mini_framework import arrancar


class MiBot:
    # PASO 2a: en __init__, crea un contador self.respondidos = 0


    def al_iniciar(self):
        # PASO 2b: muestra  Bot: ¡Hola! Soy el bot de ED.
        pass

    def al_recibir(self, mensaje):
        # PASO 2c: suma 1 a self.respondidos y DEVUELVE (return) la respuesta:
        #   si el mensaje contiene "examen"  -> "El examen del tema 1 es el viernes."
        #   si contiene "hola"               -> "¡Hola! ¿Qué tal?"
        #   en otro caso                     -> 'No te entiendo, prueba con "examen" o "hola".'
        # Pista:  if "examen" in mensaje:
        return ""

    def al_terminar(self):
        # PASO 2d: muestra  Bot: Hasta luego. He respondido 3 mensajes.
        pass


# Fíjate: tú NO llamas a al_iniciar, al_recibir ni al_terminar. Se lo das al framework:
arrancar(MiBot())
