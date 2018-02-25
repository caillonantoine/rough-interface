CC = f2py
CC2 = gfortran
FLAG = -llapack
SOURCES =\
	get_ab.f90 \
	gradgreen.f90 \
	green.f90 \
	pression_omega.f90\
	solve_pression.f90

module: bemf
	mv bemf.so ../bemf.so

bemf: $(SOURCES)
	$(CC) $(FLAG) -c $^ -m $@

%.o: %.f90
	$(CC2) $(FLAG) -c $^ -o $@

clear:
	rm *.o *.so

debug: $(SOURCES)
	$(CC2) $^ -o $@