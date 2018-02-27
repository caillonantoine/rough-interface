subroutine check_core(n)
implicit none
integer, intent(out) :: n

n = 0

!$OMP PARALLEL
!$OMP CRITICAL
n = n+1
!$OMP END CRITICAL
!$OMP END PARALLEL

end subroutine check_core