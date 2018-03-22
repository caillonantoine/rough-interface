subroutine get_ab(points,M,elements,N,normales,source,omega,ksi,beta)
implicit none
integer, intent(in) :: M,N
complex, intent(out) :: ksi(N,N), beta(N)
integer, intent(in) :: elements(M,2)
real, intent(in) :: points(N,2), normales(M,2), source(2),omega

!Implémentation d'un schéma P1 de BEM
real :: k, taille
integer :: i,j,a,b
complex :: green,gradgreen

k = omega / 340.

do i=1,N
	do j=1,M
		a = elements(j,1) + 1
		b = elements(j,2) + 1
		taille = norm2(points(a,:) - points(b,:))
		ksi(i,a) = ksi(i,a) + taille*(1/6. * gradgreen(points(i,:),points(a,:),k,normales(j,:)) + &
			1/3. * gradgreen(points(i,:),(points(a,:)+points(b,:))/2.,k,normales(j,:)))
		ksi(i,b) = ksi(i,b) + taille*(1/6. * gradgreen(points(i,:),points(b,:),k,normales(j,:)) + &
			1/3. * gradgreen(points(i,:),(points(a,:)+points(b,:))/2.,k,normales(j,:)))
	enddo
	beta(i) = green(points(i,:),source,k)
enddo

end subroutine get_ab