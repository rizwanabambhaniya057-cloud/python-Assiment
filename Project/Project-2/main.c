#include <stdio.h>//Ensure standard library is included

int main(){
    int score;
    char grade;

    //prompt user to enter their score
    printf("Enter your score:");
    scanf("%d",&score);

    
    //Step 1: Grade calculation using Ternary operator
    grade = (score>=90)?'A':
            (score>=80)?'B':
            (score>=70)?'C':
            (score>=60)?'D':'F';

            //Print the calucalated grade
            printf("your grade is %c. ",grade);
            
            //step 2: Additional Comments using Switch-Case Statement
            switch (grade) {
                case 'A':
                     printf("Excellent work!");
                     break;
                case 'B':
                     printf("Well done.");
                     break;
                case 'C':
                     printf("Good job.");
                     break;
                case 'D':
                     printf("You passed, but you coulad do better.");
                     break;
                case 'F':
                     printf("Sorry, you failed.");
                     break;
                default:
                     printf("Invalid grade.");
                     break;
            }
            // Step 3: Eligibility check using If-Else Statement
            if  (grade>='A' && grade <= 'D'){
                printf("You are eligible for the next level,\n");
            }  else {
                 printf("please try again next time.\n");
            }
            return 0;
            
    
}