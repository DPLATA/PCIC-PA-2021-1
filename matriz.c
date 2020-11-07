#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#define TAM_M 500
#define TAM_N 500

// -----------COMENTARIOS ESCRITOS SIN ACENTOS ----------------------- //
// Funcion para obtener los segundos y microseconds trancurridos 
// desde epoch (https://es.wikipedia.org/wiki/Tiempo_Unix).
// 
// Utilizada para medir el tiempo que toma realizar la suma de los
// elementos de la matriz.
//
// get_seconds  fue tomada del archivo  mt_dgemm.c que se puede obtener 
// de http://portal.nersc.gov/project/m888/apex/mt-dgemm_160114.tgz 
//
// Referecias:
// https://www.oreilly.com/library/view/understanding-and-using/9781449344535/ch04.html
// ------------------------------------------------------------------- //
double get_seconds() {
	struct timeval now;
	gettimeofday(&now, NULL);

	const double seconds = (double) now.tv_sec;
	const double usec    = (double) now.tv_usec;

	return seconds + (usec * 1.0e-6);
}

// ------------------------------------------------------------------- //
// Funcion principal.
//
// Establecemos la semilla "seed" para la generacion de numeros aleatorios
// llamando a la funcion srand() haciendo casting al valor regresado 
// de la funcion get_seconds() 
// srand( (unsigned int) get_seconds() )
//
// Inicializa los elementos de la matriz con valores enteros aleatorios
// en el rango  [0 - 9] 
//
// Se realiza la suma de los elementos de la matriz, accediento a los 
// elementos por:
// La forma convencional mat[m][n]
// La forma *(mat[i] + j)
// La forma *(p + n*i + j)
// ------------------------------------------------------------------- //
int main(void) {
  int SUMA;
	int indice_m, indice_n;
  double start,end;
  int A[TAM_M][TAM_N];
//	double* A = (double*) malloc(sizeof(double) * TAM_M * TAM_N );
srand( (unsigned int) get_seconds() );
for(indice_m = 0; indice_m < TAM_M; indice_m++)
    for(indice_n = 0; indice_n < TAM_N; indice_n++)
			A[indice_m][indice_n] = rand() % 9;

//-------------------------  FORMA 1. mat[m][n]
SUMA=0;
start = get_seconds();
	for(indice_m = 0; indice_m < TAM_M; indice_m++)
    for(indice_n = 0; indice_n < TAM_N; indice_n++){
			SUMA += A[indice_m][indice_n];
//      printf("- %d -",A[indice_m][indice_n]);
    }
end = get_seconds();
    printf("Tiempo forma 1: %f. SUMA: %d \n",end - start,SUMA );

//-------------------------  FORMA 2. *(mat[i] + j)
SUMA=0;
start = get_seconds();
	for(indice_m = 0; indice_m < TAM_M; indice_m++)
    for(indice_n = 0; indice_n < TAM_N; indice_n++){
			SUMA +=  *(A[indice_m] + indice_n) ;
//      printf("- %d -",*(A[indice_m] + indice_n));
    }
end = get_seconds();
    printf("Tiempo forma 2: %f. SUMA: %d \n",end - start,SUMA );

//-------------------------  FORMA 3. *(p + n*i + j) 
SUMA=0;
start = get_seconds();
	for(indice_m = 0; indice_m < TAM_M; indice_m++)
    for(indice_n = 0; indice_n < TAM_N; indice_n++){
			SUMA += *(A[0] + (indice_m * TAM_N +  indice_n) ) ;
//      printf("- %d -",  *(A[0] +desplazamiento ) );
    }
end = get_seconds();
    printf("Tiempo forma 3: %f. SUMA: %d \n",end - start,SUMA );

//	free(A);
	return 0;
}

