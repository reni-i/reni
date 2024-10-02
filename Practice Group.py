print(" !!!!!WELCOME!!!!! ")
print(" Do you want to buy pizza? please select the menu^^ ")

# Define pizza size
small_pizza = 50000
medium_pizza = 75000
large_pizza = 10000

# Define crust prices
thin_crust = 20000
thick_crust = 25000

# Define extra cheese price
extra_cheese_price = 13000 # Mengubah nama variabel untuk menghindari bentrok

# Ask user for pizza size
pizza_size = input("What size of pizza do you want? (small, medium, large): ")

# Calculate pizza price based on size
if pizza_size.lower() == "small":
    pizza_price = small_pizza
elif pizza_size.lower() == "medium":
    pizza_price = medium_pizza
elif pizza_size.lower() == "large":
    pizza_price = large_pizza
else:
    print("Invalid pizza size. Please choose small, medium, or large.")
    pizza_price = 0

# Ask user for crust type
crust_type = input("What type of crust do you want? (thin, thick): ")

# Calculate crust price
if crust_type.lower() == "thin":
    crust_price = thin_crust
elif crust_type.lower() == "thick":
    crust_price = thick_crust
else:
    print("Invalid crust type. Please choose thin or thick.")
    crust_price = 0

# Ask user for extra cheese
extra_cheese = input("Do you want extra cheese? (yes, no): ")

# Calculate extra cheese price
if extra_cheese.lower() == "yes":
    extra_cheese_cost = extra_cheese_price  # Menggunakan harga keju tambahan
else:
    extra_cheese_cost = 0  # Jika tidak ingin keju tambahan, biayanya 0

# Ask user for toppings
toppings = input("What toppings do you want? (onions, pepperoni, mushrooms, black olives, all): ")

# Calculate topping price
if toppings.lower() == "onions":
    topping_price = 20000
elif toppings.lower() == "pepperoni":
    topping_price = 30000
elif toppings.lower() == "mushrooms":
    topping_price = 40000
elif toppings.lower() == "black olives":
    topping_price = 45000
elif toppings.lower() == "all":
    topping_price = 100000
else:
    print("Invalid topping. Please choose onions, pepperoni, mushrooms, black olives, or all.")
    topping_price = 0

print(" !!! Thank you for your order in 2024I's Pizza !!! ")
# Calculate total price
total_price = pizza_price + crust_price + extra_cheese_cost + topping_price

def format_rupiah(value):
    return " Your Final Price is: Rp {:,}".format(value).replace(",", ".")

nilai = total_price
print(format_rupiah(nilai))