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

    ticket_type = ["gold", "silver", "platinum"]

    def __init__(self, name, ticket_id):
        self.name = name
        self.ticket_id = ticket_id

    def ticket_id(self):
        if ticket_type == "gold":
            return random.randint(100, 1000)
        elif ticket_type == "silver":
            return random.randint(1000, 2000)
        elif ticket_type == "platinum":
            return random.randint(2000, 3000)
        else:
            return random.randint(3000, 5000)

    def ticket_type(self):
        if self.ticket_type == "gold":
            return "gold"
        elif self.ticket_type == "silver":
            return "silver"
        elif self.ticket_type == "platinum":
            return "platinum"



# person = System("Ahmed Olawale", 2, "Gold")

# print(person.name)
# print(person.ticket_id)
# print(person.ticket_type)
