// Ej14 · Las cuatro etapas de gcc
#include <stdio.h>

// PASO 1a: define la constante PI con el preprocesador (sin punto y coma):
//     #define PI 3.14159


// PASO 1b: escribe dos funciones que reciban un double radio:
//   double area(double r)      -> devuelve PI * r * r
//   double perimetro(double r) -> devuelve 2 * PI * r


int main(void) {
    // PASO 1c: muestra el área y el perímetro para radio 2.0 y para radio 5.0:
    //   printf("Radio %.1f -> área %.2f y perímetro %.2f\n", r, area(r), perimetro(r));
    // Pista: puedes usar un array  double radios[] = {2.0, 5.0};  y un for.

    return 0;
}
