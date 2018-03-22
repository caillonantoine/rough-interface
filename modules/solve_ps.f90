subroutine solve_ps(A,ps,angles,N)
implicit none
integer, intent(in) :: N
complex, intent(in) :: A(N,N)
real, intent(in) :: angles(N)
complex, intent(inout) :: ps(N)

integer :: ipiv(N), info,i
complex :: identite(N,N)

forall (i=1:N) identite(i,i) = complex(angles(i),0)

call cgesv(N,1,A + identite,N,ipiv,ps,N,info)
end subroutine solve_ps