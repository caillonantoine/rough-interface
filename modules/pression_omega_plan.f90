subroutine pression_omega_plan(zz,O,ps,points,N,elements,normales,M,source,angle,omega,yy)
implicit none
integer, intent(in) :: M,N,O
real, intent(in) :: zz(O,2), points(N,2), normales(M,2), source(2), omega,angle
integer, intent(in) :: elements(M,2)
complex, intent(in) :: ps(N)

complex, intent(out) :: yy(O)

!Calcul de la pression sur de point dans zz
integer :: i,j,a,b
real :: taille,milieu(2),k
complex :: green_plan,gradgreen

k = omega/340.

!$OMP PARALLEL
!$OMP DO PRIVATE(j,a,b,taille,milieu)
do i=1,O
	yy(i) = green_plan(zz(i,:),source,k,angle)
	do j=1,M
		a = elements(j,1) + 1
		b = elements(j,2) + 1
		taille = norm2(points(a,:) - points(b,:))
		milieu = (points(a,:) + points(b,:))/2.

		yy(i) = yy(i) - taille*ps(a)*(1/6. * gradgreen(zz(i,:),points(a,:),k,normales(j,:)) + &
			1/3. * gradgreen(zz(i,:),milieu,k,normales(j,:)))
		yy(i) = yy(i) - taille*ps(b)*(1/6. * gradgreen(zz(i,:),points(b,:),k,normales(j,:)) + &
			1/3. * gradgreen(zz(i,:),milieu,k,normales(j,:)))
	enddo
enddo
!$OMP END DO
!$OMP END PARALLEL
end subroutine pression_omega_plan