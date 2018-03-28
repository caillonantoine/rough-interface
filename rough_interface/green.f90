function green(r,r0,k) result(y)
implicit none
!Fonction de Green 2D en fonction de r,r0 et du nombre d'onde k
!Typage des arguments en entrée
real, intent(in), dimension(2) :: r
real, intent(in), dimension(2) :: r0
real, intent(in) :: k

complex ::y 

real :: dist

dist = norm2(r-r0)

y = 1/4. * cmplx(bessel_yn(0,k*dist),-1*bessel_jn(0,k*dist))

end function green
