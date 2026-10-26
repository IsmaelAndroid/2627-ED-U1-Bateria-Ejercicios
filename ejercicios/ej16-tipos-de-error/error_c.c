// error_c.c · Debe mostrar "Total: 24.00" (precio 12 por 2 unidades)
#include <stdio.h>

int main(void) {
    int unidades = 2;
    double total = precio * unidades;
    printf("Total: %.2f\n", total);
    return 0;
}
