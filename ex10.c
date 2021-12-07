#include <stdio.h>
#include <stdlib.h>
#include <math.h>
               /* number of grid points */

               //各ノードにフラグをつけて、全てのノードのフラグが0になったら繰り返しをやめる
void liebman(double h,double **u){
   double exunew,unew;
   int i, j, n, iter, flag4;

   //h=0.1の時の各ノードのflagの配列
   int flag2[11][11];

   //h=0.05の時の各ノードのflagの配列
   int flag3[21][21];

   if(h == 0.1)n = 11;
   else if(h == 0.050)n = 21;
   
   
   for(i = 0; i<n;i++){
      u[i] = malloc(n*sizeof(double));   
      for (j=0; j<n; j++){
         u[i][j] = 0;
         flag2[i][j] = 0;
         flag3[i][j] = 0;
      } 
   }

   for(iter=1;; iter++)               /* iterations */
   {
      for(i=1; i<n-1; i++)                 /* x-direction */
      {
        //dpmax=0.0;
        for(j=1; j<n-1; j++)               /* y-direction */
        {
            unew = 0.25*(u[i+1][j]+u[i-1][j]+u[i][j+1]+u[i][j-1]-h*h*(-2.0));
            
            if(fabs((unew-u[i][j])/unew) > 1.0e-10){
               if(h==0.1){
                  flag2[i][j] = 1;
               }
               else if (h==0.050){
                  flag3[i][j] = 1;
               }
            }
            else {
               if(h==0.1){
                  flag2[i][j] = 0;
               }
               else if (h==0.050){
                  flag3[i][j] = 0;
               }
            }
            u[i][j] = unew;
         }
      }

      
      flag4 = 0;
      //以下で全てのノードにおいて収束条件を満たしているかどうかの判定
      //h = 0.1の時
      if(h==0.1){
         for(i = 1; i<n-1;i++){
            for (j=1; j<n-1; j++){
               if(flag2[i][j]==1){
                  flag4 = 1;
                  break;
               }
            }
            
         }
      if(flag4 == 1) continue;
      else break; 
      }

      //h = 0.050の時
      else if (h==0.050){
         for(i = 1; i<n-1;i++){
            for (j=1; j<n-1; j++){
               if(flag3[i][j]==1){
                  flag4 = 1;
                  break;
               }
            }
         }
      }
      if(flag4 == 1) continue;
      else break; 
      
   }
   printf("Liebman method\n");
   printf("n = %d  h = %1.3lf\niter = %d\n",n-1,h,iter);
   double x = 0.0;
   if(h == 0.1) {
      for (j=0; j<n;j++){
         printf("x = %1.2lf  u = %5.5lf\n",x,u[5][j]);
         x += 0.1;
      }
      printf("\n");
   }
   else if(n == 21){
      for (j=0; j<n;j++){
         printf("x = %1.2lf  %5.5lf\n",x,u[10][j]);
         x += 0.050;
      }
      printf("\n");
   }
   
   for (int i = 0; i < n; i++) {
        free(u[i]); //各行のメモリを解放
   }
   free(u);
}

void sor(double h,double **u){
   double exunew,unew;
   int i, j, n, iter, flag4;

   //h=0.1の時の各ノードのflagの配列
   int flag2[11][11];
   //h=0.05の時の各ノードのflagの配列
   int flag3[21][21];
   if(h == 0.1)n = 11;
   else if(h == 0.050)n = 21;
   
   
   for(i = 0; i<n;i++){
      u[i] = malloc(n*sizeof(double));   
      for (j=0; j<n; j++){
         u[i][j] = 0;
         flag2[i][j] = 0;
         flag3[i][j] = 0;
      } 
   }

   for(iter=1;; iter++)               /* iterations */
   {
      for(i=1; i<n-1; i++)                 /* x-direction */
      {
        //dpmax=0.0;
        for(j=1; j<n-1; j++)               /* y-direction */
        {
            unew = u[i][j]+1.6*0.25*(u[i+1][j]+u[i-1][j]+u[i][j+1]+u[i][j-1]-4.0*u[i][j]-h*h*(-2.0));
            
            if(fabs((unew-u[i][j])/unew) > 1.0e-10){
               if(h==0.1){
                  flag2[i][j] = 1;
               }
               else if (h==0.050){
                  flag3[i][j] = 1;
               }
            }
            else {
               if(h==0.1){
                  flag2[i][j] = 0;
               }
               else if (h==0.050){
                  flag3[i][j] = 0;
               }
            }
            u[i][j] = unew;
         }
      }
      flag4 = 0;
      //以下で全てのノードにおいて収束条件を満たしているかどうかの判定
      //h = 0.1の時
      if(h==0.1){
         for(i = 1; i<n-1;i++){
            for (j=1; j<n-1; j++){
               if(flag2[i][j]==1){
                  flag4 = 1;
                  break;
               }
            }
            
         }
      if(flag4 == 1) continue;
      else break; 
      }

      //h = 0.05の時
      else if (h==0.050){
         for(i = 1; i<n-1;i++){
            for (j=1; j<n-1; j++){
               if(flag3[i][j]==1){
                  flag4 = 1;
                  break;
               }
            }
         }
      }
      if(flag4 == 1) continue;
      else break; 
      
   }

   printf("SOR method, overrelaxation factor = 1.6\n");
   printf("n = %d  h = %1.3lf\niter = %d\n",n-1,h,iter);
   double x = 0.0;
   if(h == 0.1) {
      for (j=0; j<n;j++){
         printf("x = %1.2lf  u = %5.5lf\n",x,u[5][j]);
         x += 0.1;
      }
      printf("\n");
   }
   else if(n == 21){
      for (j=0; j<n;j++){
         printf("x = %1.2lf  %5.5lf\n",x,u[10][j]);
         x += 0.050;
      }
      printf("\n");
   }
   
   for (int i = 0; i < n; i++) {
        free(u[i]); //各行のメモリを解放
   }
   free(u);
}

int main(){
   double exunew,unew;
   int i, j, iter, flag;
   
   double **u1 = malloc(11*sizeof(double *));	/* save data in laplace_dp.dat */
   double **u2 = malloc(11*sizeof(double *));
   double **u3 = malloc(21*sizeof(double *));
   double **u4 = malloc(21*sizeof(double *));

   liebman(0.1,u1);
   sor(0.1,u2);
   liebman(0.050,u3);
   sor(0.05,u4);
   /* write data gnuplot 3D format */
   return 0;
}