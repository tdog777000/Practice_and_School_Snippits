#include <stdio.h>
int main (void)
{
int a, x;
char y;

printf ("\n\t\t\t\t\t\t0 to 31 are commands that don't give obvious outputs.\n \t\t\t\t\t\t 32 is a space character. 127 is a delete character.\n");

a = 0;
while (x <= 127)
{
    for (x = 32, y = 32 ; x <=127 ; y++, x++) {
    printf ("%5d | %-5c" , x, y); 
    a++;
    if (a % 12 == 0)
        putchar ('\n'); }
}


return 0;
}
