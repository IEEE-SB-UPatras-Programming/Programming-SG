CC=gcc
CFLAGS=-Wall -O3 -fopenmp

#TODO: add the following implementations: multistart_hooke_omp multistart_hooke_omp_tasks multistart_hooke_mpi multistart_hooke_mpi_omp

all: pi_calc_sequential

hooke: pi_calc_sequential.c
	$(CC) $(CFLAGS) -o pi_calc_sequential pi_calc_sequential.c


clean:
	rm -f pi_calc_sequential
