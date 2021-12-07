#include <iostream>
#include <random>
using namespace std;

#define NUM 1000

int main(int argc, char const *argv[])
{
    random_device rnd;
    mt19937 mt(rnd());
    uniform_real_distribution<double> score(0.0,1.0);
    double x, y;
    int counter=0;
    for(int i=0;i<NUM;i++){
        x=score(mt);
        y += 1/(1+x*x);
    }
    printf("%f\n",y/NUM );
    return 0;
}