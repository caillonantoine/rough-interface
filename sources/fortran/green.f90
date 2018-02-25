subroutine green(r,r0,k,y)
implicit none
!Fonction de Green 2D en fonction de r,r0 et du nombre d'onde k
!Typage des arguments en entrée
real, intent(in), dimension(2) :: r
real, intent(in), dimension(2) :: r0
real, intent(in) :: k
complex, intent(out) :: y

!Création des variables temporaires
real :: dist
real:: pi

pi=4*atan(real(1))

dist = norm2(r-r0)

y = cexp(complex(0,k*dist))/(2*pi*dist)

if (r(1) == r0(1) .and. r(2) == r0(1)) then
	y = complex(0,0)
end if

end subroutine green