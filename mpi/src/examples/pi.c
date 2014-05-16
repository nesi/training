#include <stdio.h>
#include <time.h>
void Pi(int num_steps) {
  double start, end, pi, step, x, sum;
  int i;
  start = clock();
  step = 1.0/(double)num_steps;
  sum = 0;	
  for (i=0;i<num_steps;i++) {
    x = (i+0.5)*step;
    sum = sum + 4.0/(1.0+x*x);
  }
  pi = step * sum;
  end= clock();
  printf("Pi with %d steps is %.20f in %f secs\n", num_steps, pi,(float)(end-start)/CLOCKS_PER_SEC);
}

int main() {
  Pi(100000000);
  return 0;
}
