CC = f2py
CC2 = gfortran
FLAG = -llapack
SOURCES = \
	calcul_pression_omega.f90 \
	get_ab.o \
	gradgreen.o \
	green.o \
	resolution_pression_surface.f90

module: bemf
	mv bemf.so ../bemf.so

bemf: $(SOURCES)
	$(CC) $(FLAG) -c $^ -m $@

%.o: %.f90
	$(CC2) $(FLAG) -c $^ -o $@

clear:
	rm *.o *.so