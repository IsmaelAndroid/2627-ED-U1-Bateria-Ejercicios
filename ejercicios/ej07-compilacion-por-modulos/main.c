// main.c · Programa principal: usa el módulo de operaciones
#include <stdio.h>
#include "operaciones.h"   // gracias a esto, main "conoce" las funciones del módulo

int main(void) {
    int a = 12, b = 4;

    // PASO 3: muestra el resultado de las cuatro operaciones con a y b:
    //     printf("%d + %d = %d\n", a, b, sumar(a, b));
    // y lo mismo con -, * y /.
    // Por último, muestra también 12 / 0 usando dividir(a, 0).

    return 0;
}
