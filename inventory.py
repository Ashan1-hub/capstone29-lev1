
# The class shoes is defined with the attributes country, code, product, cost, and quantity
class shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self. code =code
        self.product = product
        self.cost = cost
        self.quantity = quantity

        #The function get_cost() returns the cost of the item
        #return: The cost of the item.
    def get_cost(self):
        return self.cost

#It returns the quantity of the item.
#return: The function get_quantity is being returned.
    def get_quantity(self):
        return self.get_quantity

#The function setQuantity() takes in a parameter called quantity and adds it to the quantity
#attribute of the object
#param quantity: The amount of the item to be added to the cart
    def setQuantity(self, quantity):
        self.quantity += quantity
#The __str__ function is a special function in Python that is called when you use the print()
#function
#:return: The country, code, product, cost, and quantity.
    def __str__(self):
        return f"country: {self.country} | code:{self.code} | product:{self.product} | cost:{self.cost} |quantity:{self.quantity}"

shoe_objects =[]
# This function reads the inventory.txt file and sorts the data by the first column.
def read_shoe_data():
    with open("inventory.txt", "r+") as inventory:
        inventory_sort = inventory.readlines()
# Reading the inventory.txt file, creating a list of lists, and then printing the list of lists using
# the tabulate function.

        for lines in inventory_sort[1:]:
            lines_split = lines.split(",")
            temp_shoes = shoes(lines_split[0], lines_split[1], lines_split[2], float(lines_split[3]), int(lines_split[4].strip("\n")))
            shoe_objects.append(temp_shoes)

read_shoe_data()
 #This function takes in user input and appends it to the list shoe_objects
def capture_shoe():
    country_ob = input(" enter country :\n")
    code_ob = input("enter shoe code: \n")
    product_ob = input(" enter the porduct :\n")
    quantity_ob =int(input("enter vcost of shoes:\n"))
    new_shoe_info = int(input("enter shoe quantiy :\n"))
    new_shoe_obj = shoes(country_ob, code_ob, product_ob, quantity_ob, new_shoe_info)
    shoe_objects.append(new_shoe_obj)

    #It reads the inventory.txt file, creates a list of lists, and then prints the list of lists using
    #the tabulate function
def view_all():
    with open("inventory.txt", "r") as inventory:
        invlist = inventory.readlines()
        newlist = [[item] for item in invlist]
        print(tabulate(newlist, headers="firstrow"))
        print("\n")
#It finds the minimum value of the quantity of the shoe objects.
def re_stock():
    minvalue = int(shoe_objects[0].quantity)
    shoe_pos = 0
    
    # Looping through the shoe objects and printing the number and the object. It is also
    # checking if the quantity of the shoe is less than the minimum value. If it is, it
    # sets the shoe position to the number.

    for number, x in enumerate(shoe_objects):
        print(number, x)
        if int(x.quantity) < minvalue:
            shoe_pos = number
        print(minvalue)
        print(shoe_pos)

   # Updating the quantity of the shoes.
    value_change = input("do you want to change the quantity of the shoes: \n").lower()
    if value_change == "yes":
            new_value = int(input(" enter the quantity: \n"))
            updte_value = minvalue+new_value
            shoe_objects[shoe_pos].quantity = updte_value

            for number, x in enumerate(shoe_objects):
                print(number, x)
#It takes a shoe code as input, and then prints the shoe object that has that code
def search_shoe():
    shoe_code = input(" enter shoe code:\n")
    for i in shoe_objects:
        if i.code == shoe_code:
            print(i)

def value_per_item():
        for i in shoe_objects:
            value_per_item = i.cost*i.quantity
            print(f"the {i.product} value is :R{value_per_item}")

   # A function that returns the highest quantity of shoes in the list.
def hightest_qty():
    maxvalue = int(shoe_objects[1].quantity)
    shoe_objects_val = 0

# Finding the shoe with the highest quantity and printing it out.
    for number2, x in enumerate(shoe_objects):
        if int(x.quantity) > maxvalue:
            maxvalue = int(x.quantity)
            shoe_position = number2
    print(f"this {shoe_objects[shoe_position].product} is for sale!!!")

# The below code is a menu that allows the user to choose what they want to do.
while True:
    user_menu = input("""RD - read shoe data :\nCS - capture shoes:\nVA - view all datain inventory:\nRS - restock the inentory:
    SS - search for a shoe:\nVPI - value of each item:\nS - check which item on sale:\nE- exite\n""").upper()
    if user_menu == "RD":
        read_shoe_data()
    elif user_menu == "CS":
        capture_shoe() 
    elif user_menu == "VA":
        view_all()
    elif user_menu == "RS":
        re_stock()
    elif user_menu == "SS":
        search_shoe()
    elif user_menu == "VPI":
        value_per_item()
    elif user_menu == "S" :
        hightest_qty()
    elif user_menu == "E":
        print("good bye")
        break
    else:
        print(" input is incorrect, please try AGAIN!!!")
