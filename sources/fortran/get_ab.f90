subroutine get_ab(points,elements,normal,source,omega,M,N,Am,Bm,centre)
implicit none
integer, intent(in) :: M,N
real, intent(in), dimension(M,2) :: points
integer, intent(in), dimension(N,2) :: elements
complex, intent(in), dimension(N,2) :: normal
real, intent(in), dimension(2) :: source
real, intent(in) :: omega
complex, dimension(N,N), intent(out) :: Am
complex, dimension(N), intent(out) :: Bm

real :: k

integer :: ii, jj
real, dimension(2) :: a,b
real, intent(out), dimension(N,2) :: centre
complex, dimension(2) :: gradient

k = omega / 340
!Remplissage des matrices
do ii=1,N
	a = points(elements(ii,1)+1,:) !Le plus 1 vient du fait que fortran compte a partir de 1
	b = points(elements(ii,2)+1,:)
	centre(ii,:) = (a+b)/2

	do jj=1,N
		if (ii == jj) then
			Am(ii,jj) = complex(0,0)
		else
			a = points(elements(jj,1)+1,:)
			b = points(elements(jj,2)+1,:)
			
			call gradgreen(centre(ii,:),(a+b)/2,k,gradient)
			Am(ii,jj) = norm2(a-b)*(dot_product(gradient,normal(jj,:)))	
		endif
	enddo
	call green(centre(ii,:),source,k,Bm(ii))
enddo

end subroutine get_ab