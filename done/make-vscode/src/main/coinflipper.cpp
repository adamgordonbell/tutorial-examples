#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <assert.h>
#include <time.h>  

int flip_coins(int iters) {
  srand (time(NULL));
  int tails = 0;
  int heads = 0;

  for(int i=0;i < iters;i++){
      int coin = rand() % 2;
      if(coin == 1) {
          printf("heads\n");
          heads++;
      } else {
          printf("tails\n");
          tails++;
      }
  }
  printf("%d Heads, %d Tails\n",heads, tails);
  return abs(tails-heads);
}

int main(int argc,char* argv[]) { 
    int iters =100;
    int diff = flip_coins(iters);
    if(100 < iters) {
        printf("With enough trials Heads should be close to Tails\n");
    }
}