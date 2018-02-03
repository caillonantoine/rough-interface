#include <iostream>
#include <math.h>
#include <fstream>
#include <thrust/complex.h>
#include <thrust/host_vector.h>
#include <string>

using namespace std;

template<typename T>
void save(string outputname,T *x,int N)
{
    ofstream output(outputname.c_str(),ios::out);
    if (output)
    {
        for (int i(0); i< N; i++)
        {
            output << x[i] << " ";
        }
        output.close();
    }
    else
    {
        cout << "Raté!" << endl;
    }
}

template<typename T>
thrust::complex<T> sym(thrust::complex<T> &s,thrust::complex<T> &a,thrust::complex<T> &b)
{
    T const dot = (s-a).real()*(b-a).real() + (s-a).imag()*(b-a).imag();
    thrust::complex<T> t(dot/pow(norm(b-a),2),0);
    thrust::complex<T> h = (b-a)*t + a;
    h *= thrust::complex<float>(2,0);
    return (h -s);
}

int main()
{
    //ON PREPARE LES DONNEES DU PROBLEME
    int const N = 4; //NOMBRE DE SEGMENTS -/\-
    //CREATION DES DEUX VECTEURS DE POINTS
    int *px = new int[N+1];
    int *py = new int[N+1];

    for (unsigned int i(0);i<N+1;i++)
    {
        px[i] = i;
    }

    py[0] = 0;
    py[1] = 0;
    py[2] = 1;
    py[3] = 0;
    py[4] = 0;

    //INITIALISATION DU VECTEUR SEGMENT (Contient les sommets de chaque segment)
    int *a = new int[N];
    int *b = new int[N];

    for (int i(0); i<N; i++)
    {
        a[i] = i%N;
        b[i] = (i+1)%N;
    }

    //NOMBRE DE PASSES DE REFLEXION
    int const P = 3;
    //NOMBRE TOTAL DE SOURCES
    int const NT = 1 + N*(1-pow(N-1,P))/(2-N);

    //CREATION DES COORDONNEES DES SOURCES IMAGES
    thrust::complex<float> *si = new thrust::complex<float>[NT];
    si[0].real(1);
    si[0].imag(2);
    int lastindex = 0;
    int currentindex = 0;
    for (unsigned int i(1); i< P; i++)
    {
        currentindex =  1 + N*(1-pow(N-1,i-1))/(2-N);
        for (int s(lastindex);s<currentindex;s++)
        {
            for (int p(0);p<N;p++)
            {
                thrust::complex<float> u(px[a[p]],py[a[p]]);
                thrust::complex<float> v(px[b[p]],py[b[p]]);
                thrust::complex<float> symetrique = sym(si[s],u,v);
                bool nouveau(true);
                for (int s2(lastindex); s2<currentindex;s2++)
                {
                    if (si[s2] == symetrique)
                    {
                        nouveau = false;
                    }
                }
                if (nouveau)
                {
                    si[currentindex] = symetrique;
                    currentindex ++;
                }

            }
        }
    }

    save("output/sym.txt",si,NT);
    /*
    for i in range(1,n): #Calcul des sources n-ième
        si[i] = []
        for source in si[i-1]:
            for plan in plans:
                symetrique = sym(source, points[plan[0]],points[plan[1]])
                if not (True in [(symetrique == elm).all() for elm in si[i-1]]):
                    si[i].append(symetrique)
    */
    delete [] px;
    delete [] py;
    delete [] a;
    delete [] b;
    delete [] si;
    return 0;
}
