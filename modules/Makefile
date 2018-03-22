CC = f2py --quiet
CC2 = gfortran
OPENMP = --f90flags='-fopenmp' -lgomp
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

bemf.so: $(SOURCES)
	$(CC) $(OPENMP) -c $^ -m bemf

%.o: %.f90
	$(CC2) -c $^ -o $@

clear:
	rm *.o *.so *.pyc

debug: $(SOURCES)
	$(CC2) $^ -o $@
