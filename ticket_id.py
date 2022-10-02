import random
import ticket_type

ticket_type_id = ticket_type.ticket_type()

def get_ticket_id():
    """
    Get ticket id by ticket type
    """
    if ticket_type_id == "Gold":
        return random.randint(100, 1000)
    elif ticket_type_id == "Silver":
        return random.randint(1000, 2000)
    elif ticket_type_id == "Platinum":
        return random.randint(2000, 3000)
    else:
        return None
