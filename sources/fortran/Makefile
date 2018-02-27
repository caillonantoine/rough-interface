CC = f2py --quiet
CC2 = gfortran
OPENMP = --f90flags='-fopenmp' -lgomp
LAPACK = 
SOURCES =\
	check_core.f90\
	dot.o \
	get_ab.f90 \
	get_ab_plan.f90\
	gradgreen.o \
	green.o \
	green_plan.o \
	pression_omega.f90\
	pression_omega_plan.f90 \

module: bemf
	mv bemf.so ../bemf.so

bemf: $(SOURCES)
	$(CC) $(OPENMP) -c $^ -m $@

%.o: %.f90
	$(CC2) $(LAPACK) -c $^ -o $@

clear:
	rm *.o *.so

debug: $(SOURCES)
	$(CC2) $^ -o $@
