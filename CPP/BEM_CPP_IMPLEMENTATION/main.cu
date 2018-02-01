#include <iostream>
#include <math.h>
#include <thrust/complex.h>

using namespace std;

int main()
{
    thrust::complex<int> *x = new thrust::complex<int>[5];
    for (unsigned int i(0);i<6;i++)
    {
        x[i].imag(2*i);
        x[i].real(i%3);
        cout << x[i] << endl;
    }

    return 0;
}
