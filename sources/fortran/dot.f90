function dot(x,y) result(z)
implicit none

complex, intent(in) :: x(2)
real, intent(in) :: y(2)
complex :: z

z = x(1)*y(1) + x(2)*y(2)

end function dot