subroutine solve_pression(A,B,C,N)
implicit none
integer, intent(in) :: N
complex, intent(in) :: A(N,N), B(N)
complex, intent(out) :: C(N)
integer :: ipiv(N), info

complex :: I(N,N)
integer :: ii

forall (ii=1:N) I(ii,ii) = complex(.5,0)

call cgesv(N,1,I+A,N,ipiv,B,N,info)

end subroutine solve_pression