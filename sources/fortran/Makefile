CC = f2py --quiet
CC2 = gfortran
OPENMP = --f90flags='-fopenmp' -lgomp
LAPACK = -llapack
SOURCES =\
	get_ab.f90 \
	gradgreen.o \
	green.o \
	pression_omega.f90\
	dot.o

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
