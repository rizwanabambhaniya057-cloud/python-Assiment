#include <stdio.h>

void convertTemperature(){
    float celsius,fahrenheit;
    printf("\n___Temperature Converter---\n");
    printf("input the temperature in Celsius:");
    scanf("%f",&celsius);

    //Formula:F=(9/5*c)+32
    fahrenheit=(9.0/5.0*celsius)+32;

    printf("output: The temprature in Fahrenhei:%.1f\n",fahrenheit);
}

void calculateGrossSalary() { 
    float base_salary,hra_percent,da_parcent,ta_percent;
    float hra,da,ta,gross_salary;

    printf("\n---Gross Salary Calculator---\n");
    printf("input Base Salary:");
    scanf("%f",&base_salary);
    printf("Input HRA percentage (%%):");
    scanf("%f",&hra_percent);
    printf("Input DA percentage (%%):");
    scanf("%f",&da_parcent);
    printf("Input TA percentage(%%):");
    scanf("%f",&ta_percent);

    hra=base_salary * (hra_percent/100.0);
    da=base_salary * (da_parcent/100.0);
    ta=base_salary * (ta_percent/100.0);

    gross_salary = base_salary + hra + da + ta;
     printf("Output: Gross salary: Rs.%.0f\n",gross_salary);
}
void findTrinagleAngle(){
    float first_angle, second_angle,third_angle;

    printf("\n---Trinangle Angle Finder---\n");
    printf("Input First angle:");
    scanf("%f", &first_angle);
    printf("Input Second angle:");
    scanf("%f",&second_angle);

    third_angle=180.0-(first_angle+second_angle);

    printf("Output: Third angle:%.of\n",third_angle);
}
int main(){
    int choice;

    while(1){
        printf("\n===============================\n");
        printf("     MULTI-UTILITY PROGRAM      \n");
        printf("================================\n");
        printf("1. Convert Temperature \n");
        printf("2. Gross Salry Calculator\n");
        printf("3. Triangle Angle Finder\n");
        printf("4. Exit\n");
        printf("Enter your choice (1-4):");
        scanf("%d",&choice);

        switch (choice){
            case 1:
                 convertTemperature();
                 break;
            case 2:
                 calculateGrossSalary();
                 break;
            case 3:
                 findTrinangleAngle();
                 break;
            case 4:
                 printf("Exiting program. Thank you!\n");
                 return 0;
            default:
                printf("Invalid choice! please select between 1 and 4.\n"):
        }
        
        
        }
    }
