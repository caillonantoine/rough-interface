subroutine get_ab(points,M,elements,N,normal,source,omega,Am,Bm,centre)
implicit none
integer, intent(in) :: M,N
real, intent(in) :: points(M,2), normal(N,2), source(2), omega
integer, intent(in) :: elements(N,2)

complex, intent(out) :: Am(N,N), Bm(N)
real, intent(out) :: centre(N,2)

real :: k, a(2), b(2), rj(2)
integer :: i,j
complex :: gradient(2)
k = omega / 340.

do i=1,N
	a = points(elements(i,1)+1,:)
	b = points(elements(i,2)+1,:)
	centre(i,:) = (a+b)/2.
	do j=1,N
		if (i==j) then
			Am(i,j) = complex(0,0)
		else
			a = points(elements(j,1)+1,:)
			b = points(elements(j,2)+1,:)
			rj = (a+b)/2
			
			call gradgreen(centre(i,:),rj,k,gradient)
			Am(i,j) = norm2(b-a)*(dot_product(gradient,normal(j,:)))
		endif
	enddo
	call green(centre(i,:),source,k,Bm(i))
enddo

end subroutine get_ab