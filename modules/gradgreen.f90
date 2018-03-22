function gradgreen(r,r0,k,n) result(y)
implicit none
!gradient de la fonction de Green 2D en fonction de r,r0 et du nombre d'onde k
!Typage des arguments en entrée
real, intent(in) :: r(2),r0(2),n(2),k
complex :: y,dot

!Création des variables temporaires
real :: dist
real, dimension(2) :: vecteur


vecteur = r-r0
dist = norm2(r-r0)
if (dist == 0) then
	y = complex(0,0)
else
	y = dot(k*vecteur/(4*dist)*complex(-1*bessel_yn(1,k*dist),bessel_jn(1,k*dist)),n)
end if

end function gradgreen