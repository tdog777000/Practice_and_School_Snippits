#include <stdio.h>
int main (void)
{
int x;
unsigned int y;

x = 2147483647;
printf ("Signed(x) = %d +1\t", x);
y = 4294967295;
printf ("Unsigned(y) = %u +1\n", y);
y += 1;                           //creates overflow
x += 1;
printf ("Signed = %d +1 \t", x);   //These numbers have diff behaviors.
printf ("Unsigned = %u +1\n", y); 
y += 1; 
x += 1;
printf ("Signed = %d \t\t", x);   
printf ("Unsigned = %u \n\n", y);

x *= 3;
y *= 3;
printf ("---Undefined behavior---\t---Defined behavior--- \n");
printf ("Signed: x * 3 = %d \t" , x);
printf ("Unsigned: y * 3 = %u \n", y);


return 0;
}
