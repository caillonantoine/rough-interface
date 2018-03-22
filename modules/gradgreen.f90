subroutine gradgreen(r,r0,k,y)
implicit none
!gradient de la fonction de Green 2D en fonction de r,r0 et du nombre d'onde k
!Typage des arguments en entrée
real, intent(in), dimension(2) :: r,r0
real, intent(in) :: k
complex, intent(out), dimension(2) :: y

!Création des variables temporaires
real :: dist
real, dimension(2) :: vecteur


vecteur = r-r0
dist = norm2(r-r0)

y = k*vecteur/(4*dist)*complex(-1*bessel_yn(1,k*dist),bessel_jn(1,k*dist))
end subroutine gradgreen