
def getName():
    name = input("What Is Your Name? ").lower().strip()
    
    nameList = ["my name is","I am called", "me"]
    
    while True:
        found = False
        pos = 0
        for nameListText in nameList:
            if nameListText in name:
                pos = len(nameListText)
                found = True
                break
        if not found:
            name = input("Please try again with '"+"', '".join(str(x) for x in nameList)+"'")
        else:
            break
    name = (name[pos:])
    name = name.strip()
    return name

print("Welcome To IwantFoodbot.exe. My name is Geoff your virtual assistant. ")

name=getName()
            
      
answer = input ("Hello, "+ name.title()+". Would you like to see the menu? ")
class1 = 'food'
if answer=="yes"  :
    print("Ok here it is.")
    print("~~The Menu~~"+".")
else :
     print("Ok then, Order!!")
                            
menu = {
        "bbq meatlovers pizza" : 15.40,
        "pepperoni pizza" : 15.40,
        "cheese pizza" : 15.40,
         "all the pizza" : 25.40,
        "hawaiian pizza" : 15.40,
        "ham and cheese pizza" : 15.40,
        "peri peri chicken pizza" : 15.40,
        "woodfired pizza" : 15.40,
            "tacos" : 17.60,
                "pasta" : 13.00,
                 "fruit basket" : 12.40,
                    "half a leg of ham" : 20.40,
                     "apple of nothingness" : 36.00,
                    "nothing" : 00.00,
                    "6 nuggets" : 3.80,
                    "15 nuggets " : 6.30,
                    "24 nuggets" : 10.00,
                        "hamburger" : 5.20,
                         "cheeseburger" : 2.00,
                         "double cheeseburger" : 4.00,
                         "triple cheeseburger" : 8.00,
                        "small fries" : 2.10,
                        "medium fries" : 3.00,
                        "large fries" : 4.30,
                            "coles chicken" : 19.70,
                                "woolworths chicken" : 27.10,
                                "coca cola" : 3.50,
                                "coca cola classic" : 3.50,
                                "fanta" : 350,
                                "sprite" : 3.50,
                                "lift" : 3.50,
                                "mountain dew" : 3.50,
                                "coke no sugar" : 3.50,
                                "diet coke" : 3.50,
                                "vanilla coke" : 3.50,
                                "powerade blue" : 3.50,
                                "powerade red" : 3.50,
                                "frozen coke" : 1.00,
                                "frozen rasberry" : 1.00,
                                "frozen mountain dew" : 1.00,
                                "solo freeze" : 1.00,
                                
        }
print("menu")
count=1
for item in menu:
    price = menu[item]
    print(f"> {item} - ${price}0")
    count+=1
    
     
totalcost=0
while True:
    order = input("What would you like to order? or press enter to move on ").lower().strip()
    if order =="":
        print(f"your total is now ${totalcost}0, ")
        input("press enter to pay and exit")
        exit()
    if order in menu:
        cost = menu[order]
        totalcost += cost
        print(f"Thank you for ordering - {order}, that will cost ${cost}0, and your total is now ${totalcost}0, ")
    else:
        print(f"what") 
        print(f"{order} is not on the menu")
        if totalcost > 0:
            print(f"thanks...you now have a total cost of {totalcost}0, Thank you for ordering with IwantFoodbot.exe.")
           
            exit
                              