// roto2.c · Este programa tiene UN error. ¿Lo detecta el compilador o el enlazador?
#include <stdio.h>

// Aquí se DECLARA la función (se dice que existe)...
double con_iva(double precio);

int main(void) {
    printf("Precio con IVA: %.2f\n", con_iva(100.0));
    return 0;
}

// ...pero nadie ha escrito su código.
// Para arreglarlo, escribe aquí la función con_iva: devuelve precio * 1.21
