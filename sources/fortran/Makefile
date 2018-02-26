CC = f2py
CC2 = gfortran
FLAG = 
SOURCES =\
	get_ab.f90 \
	gradgreen.o \
	green.o \
	pression_omega.f90\
	dot.o

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