#include <stdlib.h>
#include <stdio.h>
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