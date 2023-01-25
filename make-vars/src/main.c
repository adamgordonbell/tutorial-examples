#include <stdlib.h>
#include <stdio.h>
#include "coinflipper.c"

int main() {
   printf("Hello, World!\n\n");
   printf("Let's flip some coins!\n");
   flip_coins(10);

   printf("\nGoodbye, World!\n");
   return 0;
}