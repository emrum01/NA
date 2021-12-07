public class Ex12 {

    static long r;
    static long a, b;
    static long m;

    public static void main(String[] args) {

	Ex12 e = new Ex12();

	System.out.println();
	System.out.println("Monte Carlo with MSRNG");
	System.out.println();

	System.out.println("type1: 1D");
	for (int i=1000; i<=1000000; i*=10) {
	    e.InitGenerator(1, 16807, 0, 0x7fffffff);
        e.MonteCarlo1D(i);
        
	}

	System.out.println();
	System.out.println("type2: 2D");
	for (int i=1000; i<=1000000; i*=10) {
	    e.InitGenerator(1, 16807, 0, 0x7fffffff);
	    e.MonteCarlo2D(i);
	}

	System.out.println();
	System.out.println("type2: 3D");
	for (int i=1000; i<=1000000; i*=10) {
	    e.InitGenerator(1, 16807, 0, 0x7fffffff);
	    e.MonteCarlo3D(i);
	}

    }

    static double f(double x) { return 1.0/(1.0 + x*x);  }
    static double exact() { return 0.25*Math.PI; }

    static double f2(double x, double y) { return 13.0*x*x + 34.0*x*y + 25.0*y*y - 1.0; }
    static double exact2() { return Math.PI/6.0; }

    static double f3(double x, double y, double z) { 
	    return (x-1.0)*(x-1.0) + (y-0.5)*(y-0.5) + z*z - 1.0; 
    }
    static double exact3() { return 4.0*Math.PI/3.0; }

    void InitGenerator(long seed, long c1, long c2, long mod) {
        r = seed;
        a = c1;
        b = c2;
        m = mod;
    }
    double Rand() {
        r = (a*r + b)%m;
        return (double)r/(double)m;
    }

    void MonteCarlo1D(int n) {
        int i;
        double d = 0.0;
        for(i = 0; i<n; i++){
            d += f(Rand());
        }
        d = d/n;

        System.out.println("Num: " + n + " Result = " + d + " Error = " + (d - exact()));
    }

    void MonteCarlo2D(int n) {
        int i;
        int m = 0;
        double x,y;
        for(i=0; i<n; i++){
            x = 2*Rand()-1;
            y = 2*Rand()-1;
            if(f2(x,y)<0){
                m += 1;
            }
        }
        double d = 4.0*(double)m/(double)n;
        
        System.out.println("Num: " + n + " Result = " + d + " Error = " + (d - exact2()));
    }

    void MonteCarlo3D(int n) {
        double x,y,z;
        int i,m = 0;

        for(i=0;i<n;i++){
            x = 2.0*Rand();
            y = 2.0*Rand() - 0.5;
            z = 2.0*Rand() - 1;
            if(f3(x,y,z)<0){
                m += 1;
            }
        }
        double d = 8.0*(double)m/(double)n;
        
        System.out.println("Num: " + n + " Result = " + d + " Error = " + (d - exact3()));
    }

}