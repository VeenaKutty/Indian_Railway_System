# Defining Variables for Indian Railway System

train_name = "Rajdhani Express"
train_number = 12301                  
ticket_price = 2450.50               
is_ac_available = True               
seat_numbers = [1, 2, 3, 4, 5]

# Showing the Details using print Function

# print("Train Name: ",train_name)
# print("Train Number: ",train_number)
# print("Ticket Price: ",ticket_price)
# print("AC Availability: ",is_ac_available)
# print("Seat Numbers: ",seat_numbers)

# Show The data types of the variables using type Function

# print("The data type of train_name: ",type(train_name))
# print("The data type of train_number: ",type(train_number))
# print("The data type of ticket_price: ",type(ticket_price))
# print("The data type of is_ac_available: ",type(is_ac_available))
# print("The data type of seat_numbers: ",type(seat_numbers))

# Getting passenger information
# print("=== Indian Railway Booking System ===")
# passenger_name = input("Enter passenger name: ")
# age = int(input("Enter age: "))
# destination = input("Enter destination: ")

# Display booking confirmation
# print("\n=== Booking Details ===")
# print(f"Passenger: {passenger_name}")
# print(f"Age: {age}")
# print(f"Destination: {destination}")
# print("Booking confirmed!")

#Arthimetic Operators

# base_price = 1500
# service_charge = 100
# total_price = base_price + service_charge

# print(f"Base Price: ₹{base_price}")
# print(f"Service Charge: ₹{service_charge}")
# print(f"Total Price: ₹{total_price}")

# Comparison operators
# passenger_age = 25
# senior_citizen_age = 60
# is_senior = passenger_age >= senior_citizen_age

# print(f"\nIs passenger senior citizen? {is_senior}")

# Logical operators

# has_ticket = True
# has_id_proof = True
# can_board = has_ticket and has_id_proof

# print(f"Can Board Train? {can_board}")

# Control Flow - If Statments

#Age based Pricings

# age = int(input("Enter passenger age: "))

# if age < 5:
#     price = 0
#     category = "Infant (Free)"
# elif age < 12:
#     price = 750
#     category = "Child (50% discount)"
# elif age >= 60:
#     price = 1200
#     category = "Senior Citizen (20% discount)"
# else:
#     price = 1500
#     category = "Adult"

# print(f"Category: {category}")
# print(f"Ticket Price: ₹{price}")

# For Loop - Display available trains

# trains = [
#     {"name": "Rajdhani Express",
#      "number":12301,
#      "destination":"New Delhi"},
#     {"name": "Shatabi Express",
#      "number":12001,
#      "destination":"Chennai"},
#     {"name": "Duronto Express",
#      "number":12291,
#      "destination":"Mumbai"}
# ]

# print("Available Trains: ")
# for train in trains:
#     print(f"{train['number']} - {train['name']} to {train['destination']}")

# While Loop - Booking System Menu

# print("\n=== Booking Menu ===")
# choice = 0

# while choice != 3:
#     print("1. Book Ticket")
#     print("2. Check Status")
#     print("3. Exit")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         print("Booking ticket ......")
#     elif choice == 2:
#         print("Checking Status")
#     elif choice == 3:
#         print("Thank you for using Indian Railways!")
#     else:
#         print("Invalid Choice!")

# Ticket Price Calculator

# def calculate_ticket_price(distance,class_type):
#     base_rate =0.5

#     if class_type == "Sleeper":
#         multiplier = 1.0
#     elif class_type == "AC 3 Tier":
#         multiplier = 1.5
#     elif class_type == "AC 2 Tier":
#         multiplier = 2.0
#     elif class_type == "AC 1st Class":
#         multiplier = 3.0
#     else:
#         multiplier = 1.0

#     price = distance * base_rate * multiplier

#     return round(price,2)

# distance = 500
# class_type = "AC 2 Tier"
# price = calculate_ticket_price(distance,class_type)

# print(f"Price for {distance}km in {class_type}:₹{price}")

# Ticket Booking

def book_ticket(passenger_name,age,destination,class_type = "Sleeper"):
    ticket = {
        "Passenger Name":passenger_name,
        "Age":age,
        "Destination":destination,
        "Booking ID":f"BK{hash(passenger_name)% 10000:04d}"
    }
    return ticket

def get_passenger_details(*args,**kwargs):
    print("Positional arguments: ", args)
    print("Keyword arguments: ",kwargs)


ticket1 = book_ticket("Rahul Kumar",28,"Mumbai")
ticket2 = book_ticket("Priya Singh", 32,"Delhi","AC 3 Tier")

print("\nTicket 1: ",ticket1)
print("Ticket 2: ",ticket2)

get_passenger_details("Rahul",28,"Mumbai",class_type = "Sleeper",meal_preference = "Veg")