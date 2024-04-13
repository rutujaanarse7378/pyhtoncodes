
"""Monica needs to buy a present for her best friend.
   She can buy it online or she can travel 30 Kilometers to buy at the store.
   She is not sure which would be less expensive considering shipping and handling 
   costs to buy online and Fuel costs to travel to the store.
   The cost of present is the same in both places.
   Write a solution to tell Monica which would be the best way to buy the present.
   impetus"""
#ANSWER
travelkilometer=30
fuelcostperlitres=57
costoffuel=fuelcostperlitres/travelkilometer*100
presentcost=int(input("enter the cost of present:"))
shippingcost=int(input("enter the cost of shipping cost:"))
handlingcost=int(input("enter the cost of handling cost:"))
print("this is your cost of fuel:",+costoffuel,'\n')
totalpurchasecost=shippingcost+handlingcost
totalcostatstore=totalpurchasecost+presentcost
print("this is the cost of buy it online:",+totalcostatstore,'\n')
totalcostatonline=costoffuel+presentcost
print("this is the cost of buy at store:",+totalcostatonline,'\n')
if costoffuel>totalpurchasecost:
    print("you can buy it online:",+totalcostatstore,'\n')
else:
    totalcostatonline=costoffuel+presentcost
    print("you can buy store:",+totalcostatonline,'\n')