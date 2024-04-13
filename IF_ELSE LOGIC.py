basicsalary=float(input("enter the basic salary of employee:"))
#WE HAVE GIVEN THIS BONUSPERCENTAGE
bonuspercentage=10
possiblegrade=str(input("enter the grade of the employee(only add(A,B,C,D):"))
#THIS IS THE FORMUL FO THE BONUS 
bonus=basicsalary/bonuspercentage
#THIS IS THE FORMUL OF OUR TOTALSALARY
totalsalary=basicsalary+bonus
if(possiblegrade=="A"):
    print("this is your total salary amount:",basicsalary)
elif(possiblegrade =="B"):
    print("this is your total salary amount",totalsalary)
elif(possiblegrade=="C"):
    print("this is your total salary amount:", totalsalary)   
elif(possiblegrade=="D"):
    print("this is your total salary amount:", totalsalary) 
else:
    print("")  
