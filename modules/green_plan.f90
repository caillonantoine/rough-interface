function green_plan(r,r0,k,teta) result(y)
implicit none
!Fonction de Green plane 2D en fonction de r,r0 et du nombre d'onde k, ainsi que de l'angle d'incidence k
!Typage des arguments en entrée
real, intent(in), dimension(2) :: r
real, intent(in), dimension(2) :: r0
real, intent(in) :: k,teta
complex :: y

y = cexp(complex(0,-k*sin(-teta)*r(1) - k*cos(-teta)*r(2)))
end function green_plan