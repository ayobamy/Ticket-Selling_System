# ticket selling system
import random

ticket = input("""What type of ticket do you want to buy? 
                Enter:  g for gold
                        s for silver
                        p for platinum
                .....
                """)

ticket = ticket.lower()

class System:

    def __init__(self, name):
        self.name = name

    def ticket_type(self):
        if ticket == "g":
            return "Gold"
        elif ticket == "s":
            return "Silver"
        elif ticket == "p":
            return "Platinum"
        else:
            return "Invalid ticket type"



person = System("Ahmed Olawale")

print(person.name)
print(person.ticket_type())

