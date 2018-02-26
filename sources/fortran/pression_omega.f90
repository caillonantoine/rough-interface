subroutine pression_omega(x,O,r,ps,source,elements,points,normal,omega,M,N,y)
implicit none

integer, intent(in) :: M,N,O
complex, intent(in) :: ps(N)
integer, intent(in) :: elements(N,2)
real, intent(in) :: x(O,2), r(N,2), source(2), points(M,2), normal(N,2), omega

complex, intent(out) :: y(O)

complex :: gradient(2), dot
integer :: i,j
real :: k,aire,a(2),b(2)
k = omega / 340

do j=1,O
	call green(x(j,:),source,k,y(j))
	do i=1,N
		a = points(elements(i,1)+1,:)
		b = points(elements(i,2)+1,:)
		aire = norm2(b-a)
		call gradgreen(x(j,:),r(i,:),k,gradient)
		y(j) = y(j) - ps(i)*aire*dot(gradient,normal(i,:))
	enddo
enddo


end subroutine pression_omega