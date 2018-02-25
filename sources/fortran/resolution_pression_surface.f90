subroutine resolution_pression_surface(points,elements,normal,source,omega,M,N,C,centre)
implicit none
integer, intent(in) :: M,N
real, intent(in), dimension(M,2) :: points
integer, intent(in), dimension(N,2) :: elements
complex, intent(in), dimension(N,2) :: normal
real, intent(in), dimension(2) :: source
real, intent(in) :: omega
complex, intent(out), dimension(N) :: C

complex :: Am(N,N), Bm(N)
real :: I(N,N)
integer :: ipiv(N),info,ii
real, intent(out), dimension(N,2) :: centre

forall (ii=1:N) I(ii,ii) = .5

call get_AB(points,elements,normal,source,omega,M,N,Am,Bm,centre)

call cgesv(N,1,I + Am,N,ipiv,Bm,N,info)

C = Bm

end subroutine resolution_pression_surface