#Basic variabless types(**int, float, string, boolean**)
age=25                     #int(integer)
height=6.2                 #float(decimal)
name  = "ABHIJEETH"          #(string)
is_student= True           #boolean
print(f"NAME: {name}\n AGE={age}\n HEIGHT={height}\n IS_STUDENT={is_student}\n")


#Dynamic typing(Python is dynamically typed, which means you can change the type of a variable by assigning a new value to it.)or(changing types)
box = 100             #box is an integer
print(type(box))     # Output : 'class int'
box = "A box of chocolates"  # Now box is a string
print(type(box))     # Output : 'class str'
box = 3.14            # Now box is a float
print(type(box))     # Output : 'class float'
box = False           # Now box is a boolean
print(type(box))     # Output : 'class bool'
box = [1,2,3]         # Now box is a list
print(type(box))     # Output : 'class list'

#multiple assignment
x, y, z = 10, 20, 30
x,y=y,x
print(f'x={x}, y={y}, z={z}')


# practice 
#create variables for a product(name,price,in-stock)and print a formatted message
product_name = "IPAD"
product_price = 190000
in_stock = 30
print(f'{product_name} $ {product_price} Available: {in_stock}')