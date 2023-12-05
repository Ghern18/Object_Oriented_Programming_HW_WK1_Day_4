# Start Your Code here
# Our third partner ditched us! :(

class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parking_spaces = list(range(1, total_parking_spaces + 1))
        self.current_ticket = {}

    def takeTicket(self):
        if not self.tickets:
            print("Sorry, the parking lot is full.")
        else:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parking_spaces.pop(0)
            self.current_ticket[ticket_number] = {'paid': False, 'parking_space': parking_space}
            print(f"Ticket {ticket_number} issued. Park in space {parking_space}.")

    def payForParking(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.current_ticket and not self.current_ticket[ticket_number]['paid']:
            payment_amount = input("Enter the payment amount: ")
            if payment_amount:
                payment_amount = float(payment_amount)
                if payment_amount >= 15.0:
                    print("Ticket paid! You have 15 minutes to leave.")
                    self.current_ticket[ticket_number]['paid'] = True
                else:
                    print("Payment amount must be at least $15.00")
            else:
                print("Payment amount cannot be empty.")
        else:
            print("Invalid ticket number or ticket already paid.")

    def leaveGarage(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.current_ticket:
            if self.current_ticket[ticket_number]['paid']:
                print("Thank you! Have a nice day.")
            else:
                payment_amount = input("Please pay for parking: ")
                if payment_amount:
                    payment_amount = float(payment_amount)
                    if payment_amount >= 15.0:
                        print("Thank you! Have a nice day.")
                        self.current_ticket[ticket_number]['paid'] = True
                        self.parking_spaces.append(self.current_ticket[ticket_number]['parking_space'])
                        self.tickets.append(ticket_number)
                    else:
                        print("Payment amount must be at least $15.00")
                else:
                    print("Payment amount cannot be empty.")
        else:
            print("Invalid ticket number.")
            
garage = ParkingGarage(total_tickets=30, total_parking_spaces=30)
garage.takeTicket()
garage.payForParking()
garage.leaveGarage()

       # self.ticket [item] = {'quantity' : quantity}
        
   # def remove_parking (self, item):
       # if item in self.ticket [item]:

   # def display_payment(self):
        #for item
#def driver():
    #while True:?