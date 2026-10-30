# def greet():
#     print("Hello, World!")
 
# greet()     


# def check_weather():
#     temperature = 19
#     if temperature > 25:
#         print("It's a hot day")
#     else:
#         print("It's a cold day")
        
        
# check_weather()


# def greet(name):
#     print(f"Hello, {name}!")
    
# greet("Alice")


# def greet(first_name, last_name="Jilla"):
#     print(f"Hello, {first_name} {last_name}!")
    
# greet("Alice", "Smith")
# greet("Abhishek")


# def calculate_total(price, tax_rate, discount):
#     tax = price * tax_rate
#     final_price = price + tax - discount
#     print(f"Total: ${final_price}")

# # Order matters!
# calculate_total(price=100, tax_rate=0.08, discount=10)  # $98


# def add_print(a, b):
#     print(a + b)
    
# add_print(5, 10)


# def add_return(a, b):
#     return a + b

# two_number_sum = add_return(5, 10)

# print(two_number_sum)


def simple_function():
    numbers=[1, 2, 3, 4, 5, 6]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number


first, last = simple_function()
first, last