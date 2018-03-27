CC = f2py --quiet
CC2 = gfortran
F2PY = --fcompiler=intelem --f90flags='-fpp -qopenmp' --opt='-fast' -DF2PY_REPORT_ON_ARRAY_COPY=1 
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
	$(CC) --f90flags='-fopenmp' -lgomp -c $^ -m bemf

%.o: %.f90
	$(CC2) -fPIC -c $^ -o $@

clear:
	rm *.o *.so *.pyc

debug: $(SOURCES)
	$(CC2) $^ -o $@
