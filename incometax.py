"""drow a flow chart to calculate the income tax payable.
   income tax is 30% of the annual income
   senior citizen are eligible for concession of 50% in 
   the total income tax that they are payable 
   a citizen with age greater than or equal to 60 years is a 'senior citizen'"""
#ANSWER   
incometaxpercentage=0.3
concessionrate=0.5
minimumage=60
annualincome=int(input("Enter the annual income of citizen:"))
citizenage=int(input("enter the age of citizen:"))
incometaxrupees=0.3*annualincome
concessionamount=0.5*incometaxrupees
if minimumage>=citizenage:
   totalIncome = incometaxrupees - concessionamount
   print(totalIncome)
else:
    print(incometaxrupees)

""""when the age is greater than or equal to 21,
the person can have alcoholic beverages.
when the age of the person is greater than 18, the person can vote,
at the age of 20 ,a person can vote but cannot be served alcoholic hevaeagea
print''enjoy your drink!''if the person can be served alcoholic beverages
print''you can vote!''if person is eligible to vote"""
#answer
ageofaperson=int(input("enter the age of the person:"))
if ageofaperson>=21:
   print("enjoy your drink!")
if ageofaperson>18:
   print("you can vote!")
   
   
""""find the amout5 ot  charge people of verying ages for concert ticket 
when the people is under 16, the charge is $7; 
when the person is 65 or over,the charge is $5;
all other are charged $10 
the condition are the following
 age<16,age>=16&age<65,age>=65 """
#answer
personage=int(input("enter the age of the person:"))
if personage<16:
   print("your charge is $7")
elif personage>=16&personage<65:
   print("your charge is $10")
elif personage>=65:
   print("your charge is $5")

   
