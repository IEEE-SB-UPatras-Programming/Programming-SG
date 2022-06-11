#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

#define n 1000000000

double get_wtime(void);

int main() {

    double begin, end;
    int i, count;
    double pi;

    begin = omp_get_wtime();

    count = 0;

    #pragma omp parallel reduction( + : count )
    {
        double x,y,z;
        unsigned short randbuffer[] = {0,0,omp_get_thread_num() + begin};


        #pragma omp for
        for(i = 0; i < n; i++) {

            x = (double)erand48(randbuffer);

            y = (double)erand48(randbuffer);

            z = x * x + y * y;

            
            if( z <= 1 ) count++;
        }
    }

    pi = (double) count / n * 4;
    end = omp_get_wtime();

    printf("Approximate PI = %g\n", pi);
    printf("Time taken: %lf\n",end-begin);

    return(0);
}