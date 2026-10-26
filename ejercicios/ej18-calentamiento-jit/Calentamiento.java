// Ej18 · El calentamiento del JIT
public class Calentamiento {

    // PASO 1: escribe un método que diga si un número es primo:
    //     static boolean esPrimo(int n) {
    //         if (n < 2) return false;
    //         for (int d = 2; d * d <= n; d++) {
    //             if (n % d == 0) return false;
    //         }
    //         return true;
    //     }


    // PASO 2: escribe un método que cuente cuántos primos hay entre 2 y "limite":
    //     static int contarPrimos(int limite) { ... usa esPrimo en un for ... }


    public static void main(String[] args) {
        // PASO 3: repite 10 rondas. En cada una:
        //   long inicio = System.nanoTime();
        //   int total = contarPrimos(20000);
        //   long ms = (System.nanoTime() - inicio) / 1_000_000;
        //   System.out.println("Ronda " + ronda + ": " + total + " primos en " + ms + " ms");

    }
}
