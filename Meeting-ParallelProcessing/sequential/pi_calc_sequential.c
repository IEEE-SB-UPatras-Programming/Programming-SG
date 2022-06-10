#include <stdio.h>
// #include <math.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>
#define SEED time(NULL)
#define n 40000000000

int main() {

    srand( SEED );
    long long i, count;
    double x,y,z,pi;
    double begin,end;

    begin = omp_get_wtime();
    count = 0;

    for(i = 0; i < n; i++) {

        x = (double)rand() / RAND_MAX;

        y = (double)rand() / RAND_MAX;

        z = x * x + y * y;

        if( z <= 1 ) count++;
        if( i % 1000000000 == 0)
        {
            printf("we are at %d \n",(int) i);
        }
    }

    pi = (double) count / n * 4;
    end = omp_get_wtime();

    printf("Approximate PI = %g\n", pi);
    printf("Time taken: %lf\n",end - begin);

    return(0);
}