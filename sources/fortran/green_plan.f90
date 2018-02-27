subroutine green_plan(r,r0,k,teta,y)
implicit none
!Fonction de Green plane 2D en fonction de r,r0 et du nombre d'onde k, ainsi que de l'angle d'incidence k
!Typage des arguments en entrée
real, intent(in), dimension(2) :: r
real, intent(in), dimension(2) :: r0
real, intent(in) :: k,teta
real :: a,r2(2)
complex, intent(out) :: y

r2 = r-r0
a = k* abs(cos(teta)*r2(1) + sin(teta)*r2(2))

y = 1/4. * complex(bessel_yn(0,a),-1*bessel_jn(0,a))

end subroutine green_plan