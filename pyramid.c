#include <stdio.h>
int main (void)
{
int a, b, c;
/*a = 1;
b = 2;
c = 1;

do  { 
    printf("%d", a);
    if (c == a){
        c += b;
        b++;
        putchar ('\n');}
    a++;
    }           
while (a <= 10);*///From 1 to 10, increments of 1

/*a = 4;
b = 2;
c = 4;

do  { 
    printf("%d", a);
    if (c == a){
        c += b;
        b++;
        putchar ('\n');}
    a++;
    } 
while (a <= 13);*///From 4 to 13, increments of 1

a = 2;
b = 4;
c = 2;

do  { 
    printf("%d", a);
    if (c == a){
        c += b;
        b += 2;
        putchar ('\n');}
    a += 2;
    } 
while (a <= 20); //From 4 to 20, increments of 2

return 0;
}
