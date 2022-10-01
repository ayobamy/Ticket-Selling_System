import random
import ticket_type

def get_ticket_id(ticket_type):
    """
    Get ticket id by ticket type
    """
    if ticket_type == "Gold":
        return random.randint(100, 1000)
    elif ticket_type == "Silver":
        return random.randint(1000, 2000)
    elif ticket_type == "Platinum":
        return random.randint(2000, 3000)

print(get_ticket_id("Silver"))
