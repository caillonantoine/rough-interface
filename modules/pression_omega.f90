subroutine pression_omega(zz,O,ps,points,N,elements,normales,M,source,omega,yy)
implicit none
integer, intent(in) :: M,N,O
real, intent(in) :: zz(O,2), points(N,2), normales(M,2), source(2), omega
integer, intent(in) :: elements(M,2)
complex, intent(in) :: ps(N)

complex, intent(out) :: yy(O)

!Calcul de la pression sur de point dans zz
integer :: i,j,a,b
real :: taille,milieu(2),k
complex :: green,gradgreen

k = omega/340.

!$OMP PARALLEL
!$OMP DO PRIVATE(j,a,b,taille,milieu)
do i=1,O
	yy(i) = green(zz(i,:),source,k)
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
end subroutine pression_omega


!def pression(zz,ps,points,elements,normales,source,omega):
!	zz = np.asarray(zz)
!	points = np.asarray(points)
!	elements = np.asarray(elements)
!	normales = np.asarray(normales)
!	ps = np.asarray(ps)
!	
!	yy = np.zeros(len(zz),dtype=complex)
!	k = omega/340.
!	
!	for i,o in enumerate(zz):
!		yy[i]  = green(o,source,k)
!		for j,elm in enumerate(elements):
!			a,b = elm
!			taille = np.linalg.norm(points[a] - points[b])
!			milieu = (points[a] + points[b])/2
!			yy[i] -= taille*(ps[a]*(1/6. *gradgreen(o,points[a],k,normales[j]) + \
!									 1/3. *gradgreen(o,milieu,k,normales[j])))
!
!			yy[i] -= taille*(ps[b]*(1/6. *gradgreen(o,points[b],k,normales[j]) + \
!									 1/3. *gradgreen(o,milieu,k,normales[j])))
!	return yy