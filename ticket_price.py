import ticket_type
import ticket_id

ticket_type_amount = ticket_type.ticket_type()

def ticket_price():
    if ticket_type_amount == "Gold":
        return "$100"
    elif ticket_type_amount == "Silver":
            return "$75"
    elif ticket_type_amount == "Platinum":
        return "$50"
    else:
        return None

