menu = {
        "pizza" : 3.40,
		"tacos" : 5.60,
		"curry chicken" : 13.00
print(menu)
for item in menu:
    price = menu[item]
     print(f"> {item} - ${price}")
	 count+=1
	 
totalcost=0
while True:
    order = input("What do you want to eat?").lower().strip()
	if order =="":
	break
	if order in menu:
	cost = menu[order]
	totalcost += cost
	print(f"Thank you for ordering - {order}, that will cost {cost}, and 
else:
print(f"what 
if totalcost > 0:
print(f"thanks...you now owe me 