# User Details
print("<---------------------------------------------------------------->")
name = input("Enter the Name: ")
number_of_tickets = int(input("Enter the Number of Tickets: "))
ticket_type = int(input("Enter the Ticket Type (0=Normal, 1=Premium): "))
number_days_before_show = int(input("Enter Number of days before show: "))
#Calculations
normal_price = 150
premium_price = 250

ticket_price = (ticket_type == 0) * normal_price + (ticket_type == 1) * premium_price

total_price = ticket_price * number_of_tickets

discount = (number_days_before_show >= 3) * (20 * number_of_tickets)

conv_fee = (number_of_tickets > 3) * 30 + (number_of_tickets <= 3) * 10

final_price = total_price - discount + conv_fee

# Output
print("\n----- Booking Details -----")
print("Name:", name)
print("Tickets:", number_of_tickets)
print("Ticket Type:", ticket_type)
print("Days Before Show:", number_days_before_show)
print("Total Price:", final_price)
print("<---------------------------------------------------------------->")
