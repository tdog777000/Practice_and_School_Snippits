// Solution - 1 start
#include <stdio.h>
int main (void)
{
int S = 0;
int Dot_Product (int a[], int b[], int S);
int i, j;

printf ("Enter the size of the arrays you will be multiplying: ");
scanf ("%d" , &S);

int a[S], b[S];

printf ("Enter the values of the elements in array a! \n");
for (i = 0 ; i < S ; i++)
    {
    printf ("Element a[%d] = ", i);
    scanf ("%d" , &a[i]);
    }
    
printf ("Enter the values of the elements in array b! \n");
for (j = 0 ; j < S ; j++)
    {
    printf ("Element b[%d] = ", j);
    scanf ("%d" , &b[j]);
    }
    
printf ("The Dot Product of the arrays = %d \n", Dot_Product (a, b, S));

return 0;
}

int Dot_Product (int a[], int b[], int S)
{
int Answer = 0, x;
for (x = 0; x < S ; x++)
    Answer += a[x] * b[x];
return Answer;
}
// Solution - 1 end
// Solution - 2 start
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main (void)
{
int a[4][4] = {0}, x = 0, y = 0, blocks;

srand (time(0));

for (blocks = 0; blocks < 3; blocks++)
{
if (blocks == 0)
    {
    for (x = 0; x < 4; x++)
        {
        putchar ('\n'); 
        for (y = 0; y < 4; y++)
            {
            if (x >= y)
                a[x][y] = 1 + rand () % 9;
            else
                a[x][y] = 0;
        printf ("%d" , a[x][y]);
            }
        }
    }
else if (blocks == 1)
    {
    for (x = 0; x < 4; x++)
        {
        putchar ('\n'); 
        for (y = 0; y < 4; y++)
            {
            if (x <= y)
                a[x][y] = 1 + rand () % 9;
            else
                a[x][y] = 0;
        printf ("%d" , a[x][y]);
            }
        }
    }
else 
    {
    for (x = 0; x < 4; x++)
        {
        putchar ('\n');
        for (y = 0; y < 4; y++)
            {
            if (x == y)
                a[x][y] = 1 + rand () % 9;
            else
                a[x][y] = 0;
        printf ("%d" , a[x][y]);
            }
         }
     }  
putchar ('\n');
}      

putchar ('\n');
return 0;
}
// Solution - 2 end
// Solution - 3 start
#include <stdio.h>
#define ROWS 2
#define COL 3

void modify_array (int c[][COL], int a[][COL], int b[][COL]) 
{
int x, y;
for (x = 0 ; x < ROWS ; x++) 
    for (y = 0 ; y < COL ; y++)
        c[x][y] = a[x][y] + b[x][y];
}

int main (void)
{
int a[ROWS][COL] = {{1,2,3}, {3,4,6}}; 
int b[ROWS][COL] = {{4,5,6}, {7,8,4}};
int c[ROWS][COL] = {{0,0,0}, {0,0,0}};
int x, y;

printf ("ROWS = %d, COL = %d\n", ROWS, COL);
printf ("The values of array a[ROWS][COL] are:");
for (x = 0 ; x < ROWS ; x++)
    {
    printf (" {");
    for (y = 0 ; y < COL ; y++)
        if (y == 2)
        printf ("%2d", a[x][y]);
        else
        printf ("%2d," , a[x][y]);
    printf ("} ");
    }

printf ("\nThe values of array b[ROWS][COL] are:");
for (x = 0 ; x < ROWS ; x++)
    {
    printf (" {");
    for (y = 0 ; y < COL ; y++)
        if (y == 2)
        printf ("%2d", b[x][y]);
        else
        printf ("%2d,", b[x][y]);
    printf ("} ");
    }

printf ("\n\n");

printf ("c[%d][%d] = ", ROWS, COL);
for (x = 0; x < ROWS; x++)
    {
    printf ("{");
    for (y = 0; y < COL; y++)
        printf (" %d+%d ", a[x][y], b[x][y]);   
    printf ("}  ");
    }
puts (" ");

modify_array (c, a, b);

printf ("\nThe values of array c[][] (a+b) are:");
for (x = 0 ; x < ROWS ; x++)
    {
    printf (" {");
    for (y = 0 ; y < COL ; y++)
        if (y == 2)
        printf ("%2d", c[x][y]);
        else 
        printf ("%2d,", c[x][y]);
    printf ("} ");
    }
putchar ('\n'); 

return 0;
}
// Solution - 3 end
// Solution - 4 start
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void MAXMIN_values (int a[][5])
{
int x, y, low = 10, high = 0;
for (x = 0; x < 2; x++)
    for (y = 0; y < 5; y++)
    {
        if (a[x][y] < low)
        low = a[x][y];
        else if (a[x][y] > high)
        high = a[x][y];
    }
printf ("The lowest valued number in the set is %d.\nThe highest valued number in the set is %d.\n\n", low, high);
}

int COUNT_values (int i, int a[][5])
{
int x, y, count = 0, values;

for (x = 0; x < 2; x++)
    for (y = 0; y < 5; y++)
        if (a[x][y] == i)
        count++;
        return count;  
}

int main (void)
{
int x, y, values;
int a[2][5] = {{0},{0}};
srand (time(0));

printf ("  -- Array a[2][5] -- \n");
for (x = 0; x < 2; x++)
    for (y = 0; y < 5; y++)
    {
    a[x][y] = 1 + rand() % 10;
    printf ("%4d", a[x][y]);
    if (y == 4)
    printf ("\n");
    }
puts("");
    
MAXMIN_values (a);

for (values = 0; values <= 10; values++)
    if (COUNT_values (values, a) == 1)
    printf ("The number %d appeared in the array %d time!\n", values, COUNT_values (values, a));
    else
    printf ("The number %d appeared in the array %d times!\n", values, COUNT_values (values, a));
return 0;
}
// Solution - 4 end
// Solution - 5 start
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int MULT (int a[][4], int b[][2], int i, int j)
{
int k, Answer = 0;
for (k = 0; k < 4; k++)
    Answer += a[i][k] * b[k][j];
    return Answer;   
}

int main (void)
{
int a[3][4] = {{0},{0}}, b[4][2] = {{1},{0}}, c[3][2] = {{0},{0}}, x, y;

srand (time(0));

printf ("----Array A----\n");
for (x = 0; x < 3; x++)
{
    for (y = 0; y < 4; y++)
    {
    a[x][y] = 1 + rand () % 10;
    printf ("%3d ", a[x][y]);
    }
printf ("\n");
}
puts (" ");

printf ("----Array B----\n");
for (x = 0; x < 4; x++)
{
    for (y = 0; y < 2; y++)
    {
    b[x][y] = 1 + rand () % 10;    
    printf ("%3d ", b[x][y]);
    }
printf ("\n");
}
puts (" ");    

printf ("----Array C----\n");
for (x = 0; x < 3; x++)
{
    for (y = 0; y < 2; y++)
    {   
    c[x][y] = MULT (a, b, x, y);
    printf ("%2d ", c[x][y]);
    }
puts (" ");
}

return 0;
}
// Solution - 5 end

