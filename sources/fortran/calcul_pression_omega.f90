subroutine calcul_pression_omega(x,r,ps,source,elements,points,normal,omega,M,N,O,y)
implicit none
integer, intent(in) :: M,N,O
real, intent(in), dimension(M,2) :: points
integer, intent(in), dimension(N,2) :: elements
real, intent(in), dimension(N,2) :: r
complex, intent(in), dimension(N,2) :: normal
real, intent(in), dimension(2) :: source
real, intent(in) :: omega
real, intent(in), dimension(O,2) :: x
complex, intent(in), dimension(N) :: ps
complex, intent(out), dimension(O) :: y
complex, dimension(2) :: gradient

real :: k,aire
real, dimension(2) :: a,b
integer :: ii,jj

k = omega / 340

do ii=1,O
	!call green(x(ii,:),source,k,y(ii))
	do jj=1,N
		
		a = points(elements(jj,1)+1,:)
		b = points(elements(jj,2)+1,:)
		call gradgreen(x(ii,:),r(jj,:),k,gradient)
		y(ii) = y(ii) + ps(jj) * norm2(b-a) * dot_product(gradient,normal(jj,:))		
	enddo
enddo


end subroutine calcul_pression_omega