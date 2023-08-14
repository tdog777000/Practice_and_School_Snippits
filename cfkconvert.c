#include <stdio.h>
int main(void)
{
  float C, K, F;
    printf("Enter the degrees in Fahrenheit to convert to Celcius and Kelvin.\n");
    scanf("%f", &F);
    
    C = (F - 32) * 5/9;
    K = C + 273.150000;
    
    printf("In celcius, that's %.2f degrees\n", C);
    printf("In Kelvin, that's %.2f degrees\n", K);

return 0;
}
