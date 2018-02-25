subroutine pression_omega(x,N,ps,M,source,elements,points,O,normal,omega,y)
implicit none
complex, intent(in) :: ps(M)
integer, intent(in) :: elements(M,2)
integer, intent(in) :: M,N,O
real, intent(in) :: x(N,2), source(2), points(O,2), normal(M,2), omega

complex, intent(out) :: y(N)

complex :: gradient(2)
integer :: i,j
real :: k,a(2),b(2)

k = omega / 340.

do i=1,N
	call green(x(i,:),source,k,y(i))
	do j=1,M
		a = points(elements(j,1)+1,:)
		b = points(elements(j,2)+1,:)
		call gradgreen(x(i,:),(a+b)/2,k,gradient)
		y(i) = y(i) - ps(j) * norm2(b-a) * dot_product(gradient,normal(j,:))
	enddo
enddo

end subroutine pression_omega

!k = omega/c
!    x = np.asarray(x)
!    y = amplitude*bemf.green(x,source,k)
!    #y = 0
!    for i,o in enumerate(elements):
!        a,b = points[o]
!        aire = norm(b-a)
!        n = normal[i]
!        y -= ps[i] *aire*(np.dot(bemf.gradgreen(x,r[i],k),n)) #vectoriser
!    return y