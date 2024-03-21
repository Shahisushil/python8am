
# # 1. DELL (8000), MAC (50000), TOSHIBA (30000)

# # Enter option
# # Enter quantity

# # Delivery Option
# # 1. home (1000) 2. pickup (free)

# # Packing option
# # 1. plastic (500) 2. bag (1000) 3. gift bag (5000)

# # Location
# # 1. ktm (tax 13%) ltp (free) bkt (free)

# # Product
# # Quality
# # Tax amount
# # Grand total

print("==========================COMPUTER BAZAR=============================")
print("1. Dell (Rs. 80000) 2. Mac (Rs. 50000) 3.Toshiba (Rs. 30000)")
Dell_price=0
Mac_price=0
Toshiba_price=0
product_name=""
quantity=0
delivery_charge=0
plastic_price=0
bag_price=0
gift_box_price=0
tax_amount=0
total_price=0
grand_total=0
option=int(input("Enter your choice: "))
if option==1:
    quantity=int(input("Enter the quantity: "))
    Dell_price=80000*quantity
    product_name="Dell"
elif option==2:
    quantity=int(input("Enter your quantity: "))
    Mac_price=50000*quantity
    product_name="Mac"
elif option==3:
    quantity=int(input("Enter your quantity: "))
    Toshiba_price=30000*quantity
    product_name="Toshiba"
else:
    print("Invalid Choice")
    print("exit")

print("Delivery option 1. Home Delivery (Rs. 1000) 2. Pick up (Free)")
delivery_option=int(input("Enter your delivery option: "))
if delivery_option==1:
    delivery_charge=1000
    

print(" Packing : 1. Plastic bag ( Rs.500) 2. Bag (Rs.1000) 3. Gift Bag (Rs. 5000)")
packing_option=int(input("Enter your packing option: "))
if packing_option==1:
    plastic_price=500
elif packing_option==2:
    bag_price=1000
elif packing_option==3:
    gift_box_price=5000

total=Dell_price+Mac_price+Toshiba_price
print("Location: 1. Ktm (13%)  2. Bkt. (Free) 3. Ltp. (Free)")
location_option=int(input("Enter your location: "))
if option==1:
    tax_amount=total*0.13

grand_total=total+delivery_charge+plastic_price+bag_price+gift_box_price+tax_amount
print("============================INVOICE=========================")
print("Product Name: ",product_name)
print("Quantity: ", quantity)
print("Tax amount: ",tax_amount)
print("Delivery charge: ",delivery_charge)
print("Plastic price: ",plastic_price)
print("Bag price: ",bag_price)
print("Gift box price: ",gift_box_price)
print("Grand total: ",grand_total)









