"""*Is it even or odd?*
   - Write a program that takes a number as input and checks if it's even or odd.
   - Use an if-else statement to determine evenness (number % 2 == 0) and print
   "Even" or "Odd" accordingly."""
#ANSWER
a=int(input("enter the number:"))
if a % 2 == 0 :
    print("even")
else:
    print("odd")
    
    
"""*Grading system:*
   - Create a program that takes a student's score as input.
   - Use if-else statements to assign
   letter grades based on score ranges (e.g., A: 90-100, B: 80-89, etc.) 
   and print the assigned grade."""
#ANSWER
score=int(input("enter the score of student's:")) 
if score>=90:
    print("A")
elif score>=80 :
    print("B")
else:
    print("C")


