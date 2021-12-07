
#include <stdio.h>
#include <math.h>

int main(void){

double a = 1.0;
double b = -8000.0;
double c = 1.0;

double x1 = (-b+sqrt(b*b-4*a*c))/2*a;
double x2 = (-b-sqrt(b*b-4*a*c))/2*a;
printf("%f\n",x1);
printf("%f\n",x2);

a = (float)a;
b = (float)b;
c = (float)c;

float xF1 = (-b+sqrt(b*b-4*a*c))/2*a;
float xF2 = (-b-sqrt(b*b-4*a*c))/2*a;
printf("%f\n",xF1);
printf("%f\n",xF2);

return 0;
}


