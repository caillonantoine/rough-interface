function green_plan(r,r0,k,teta) result(y)
implicit none
!Fonction de Green plane 2D en fonction de r,r0 et du nombre d'onde k, ainsi que de l'angle d'incidence k
!Typage des arguments en entrée
real, intent(in), dimension(2) :: r
real, intent(in), dimension(2) :: r0
real, intent(in) :: k,teta
real :: a,r2(2)
complex :: y

r2 = r-r0
a = k* abs(cos(teta)*r2(1) + sin(teta)*r2(2))

y = cexp(complex(0,-1*k*(cos(teta)*r(1) - sin(teta)*r(2))))


end function green_plan