/** Solution of the symmetric band equation system

 * by LDU method. The matrix is in column format. <br>

 * Column format: upper symmetric part of the matrix is

 * stored by columns. Coefficients in columns start from the

 * top and end by the diagonal. Zeros added to the top of 

 * first (h-1) columns in order to have constant column height h

 * (h is matrix bandwidth = column height).

 */

public class LUband {
/** UtDU decomposition for symmetric band matrix.
     * @param a matrix by columns of constant height
     * @param n number of equations
     * @param h bandwidth
     */

    public static void decompose (double[] a, int n, int h) {
	    int i,j,k,c,h1=h-1;
        double w;
        for(j=1; j<n; j++) {
            for(i=Math.max(j-h1,0); i<j; i++) {
                for(k=Math.max(j-h1,0); k<i; k++) {
                    a[i+h1*(j+1)] -= a[k+h1*(i+1)] * a[k+h1*(j+1)];
                }
            }   

            for(i=Math.max(j-h1,0); i<j; i++) {
                w = a[i+h1*(j+1)];
                a[i+h1*(j+1)] /= a[i+h1*(i+1)];
                a[j+h1*(j+1)] -= a[i+h1*(j+1)]*w;
            }
        }
        
    }

    /** Reduction and backsubstitution for RHS
     * @param a decomposed matrix by columns of constant height
     * @param n number of equations
     * @param h bandwidth
     * @param b right-hand side(in)/solution vector(out)
     */
    public static void solve (double[] a, int n, int h, double[] b) {
	    int i,j,c,h1=h-1 ;
        for(j=1; j<n; j++) {
            for(i=Math.max(j-h1,0); i<j; i++) b[j] -= a[i+h1*(j+1)]*b[i];
        }
        for(j=0; j<n; j++) {
            b[j] /= a[j+h1*(j+1)];
        }
        for(j=n-1; j>=0; j--) {
            for(i=Math.max(j-h1,0); i<j; i++) {
            b[i] -= a[i+h1*(j+1)] * b[j];
            }
        }
    }

    public static void main(String[] args) {
        int i,h = 5;
        double a[] = {0.0,0.0,3.0,-1.0,-1.0, 0.0,-1.0,2.0,0.0,-2.0, -1.0,0.0,3.0,-1.0,0.0, -2.0,-1.0,2.0,0.0,0.0, 0.0,0.0,1.0,-2.0,0.0, 0.0,-2.0,1.0,0.0,0.0, 0.0,0.0,0.0,0.0,0.0};
        double b[] = {-2.0,-5.0,4.0,1.0,-7.0,-4.0};
        double a2[] = {3.0,-1.0,-1.0,-1.0,2.0,0.0,-2.0,-1.0,0.0,3.0,-1.0,-2.0,-1.0,2.0,1.0,-2.0,-2.0,1.0};
        int n = 6;
        

        decompose(a,n,h);
        solve(a,n,h,b);

        for(i=0;i<35;i++){
            System.out.println(a[i]);
        }
        System.out.println();
        for(i=0;i<n;i++){
            System.out.println(b[i]);
        }
    }
}
