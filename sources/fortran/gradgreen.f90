subroutine gradgreen(r,r0,k,y)
implicit none
!gradient de la fonction de Green 2D en fonction de r,r0 et du nombre d'onde k
!Typage des arguments en entrée
real, intent(in), dimension(2) :: r,r0
real, intent(in) :: k
complex, intent(out), dimension(2) :: y

!Création des variables temporaires
real :: dist
real:: pi
real, dimension(2) :: vecteur

pi = 4*atan(real(1))

vecteur = r-r0
dist = norm2(r-r0)
y = 1/(2*pi) * vecteur * cexp(complex(0,k*dist))*(dist**2 -1)/(dist**3)

if (r(1) == r0(1) .and. r(2) == r0(1)) then
	y = complex(0,0)
end if
end subroutine gradgreen