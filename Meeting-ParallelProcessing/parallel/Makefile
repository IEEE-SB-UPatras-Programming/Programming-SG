CC=gcc
CFLAGS=-Wall -O3 -fopenmp

#TODO: add the following implementations: multistart_hooke_omp multistart_hooke_omp_tasks multistart_hooke_mpi multistart_hooke_mpi_omp

all: pi_calc_parallel

hooke: pi_calc_parallel.c
	$(CC) $(CFLAGS) -o pi_calc_parallel pi_calc_parallel.c


clean:
	rm -f pi_calc_parallel
