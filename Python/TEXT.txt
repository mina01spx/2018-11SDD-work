import json

orders = {}  ##Empty dictionary

## Input some data
def inputData(orders):
    while True:
        name = input("Name?)
        if name=="":
            break
        choice=input("Menu Choice?")
        order[name]=choice 
    return orders
## Store in in a file
def storeData(orders):
    with open("data.txt", 'w') as f:
        json.dump(orders, f)
    
## Get it from file
def getData():
    with open("data.txt", 'r') as f:
       orders = json.load(f) 
      return orders
## Display contents
def displayData():
    print(orders)
          
storeData(inputData(orders))
displayData(getData())
  
