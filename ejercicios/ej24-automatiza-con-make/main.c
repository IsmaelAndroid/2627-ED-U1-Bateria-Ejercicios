#include <stdio.h>
#include "operaciones.h"

int main(void) {
    int a = 12, b = 4;
    printf("%d + %d = %d\n", a, b, sumar(a, b));
    printf("%d - %d = %d\n", a, b, restar(a, b));
    printf("%d * %d = %d\n", a, b, multiplicar(a, b));
    printf("%d / %d = %d\n", a, b, dividir(a, b));
    return 0;
}
