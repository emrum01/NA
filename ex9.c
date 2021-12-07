#include <stdio.h>
#include <math.h>

double f(double x, double y) {
	return x * y;
}
double y_true(double x) {
	return exp(x*x/2);
}
void runge_kutta(double x,double y, double h,int N){
	double y_t = y_true(1);
	
	for (double i = 0; i < N; i++) {
		double k1 = h * f(x, y);
		double k2 = h * f(x + h/2.0, y + k1/2.0);
		double k3 = h * f(x + h / 2.0, y + k2 / 2.0);
		double k4 = h * f(x + h, y + k3);
		y = y + (k1 + 2.0*k2 + 2.0*k3 + k4) / 6.0;
		x = x + h;
	}
	double err = y - y_t;
	printf("Runge-Kutta:       h = %5.3lf  x =%5.3lf   y = %5.8lf  Error = %le\n",h,x,y,err);
}

void euler(double x,double y,double h,int N){
	double y_t = y_true(1.0);
	for(double i=0; i<N; i++){
    	y = y + h*f(x,y);
    	x = x + h;
  	}
	double err = y - y_t;
    printf("Euler:       	   h = %5.3lf  x =%5.3lf   y = %5.8lf  Error = %le\n",h,x,y,err);
}

int main(void) {
	//初期値
	int N = 10;
	double x = 0.0;
	double y = 1.0;
	double h = (1.0 - 0.0) / (double)N; //刻み幅
	printf("dy/dx = xy, a = 0, b = 1, y(a) = 1\n");
	euler(x,y,h,N);
	runge_kutta(x,y,h,N);

	N = 100;
	h = (1.0 - 0.0) / (double)N; //刻み幅
	euler(x,y,h,N);
	runge_kutta(x,y,h,N);

	return 0;
}

