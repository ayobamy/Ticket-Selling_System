from ticket_type import *
from ticket_price import *
from ticket_id import *

choice = int(input("""Choose an event of your choice:
                Enter:  1 for Event1
                        2 for Event2
                        3 for Event3 


"""))


def select_event():
    if choice == 1:
        return "Event1"
        ticket_type()
        get_ticket_id()
        ticket_price()
    elif choice == 2:
        return "Event2"
        ticket_type()
        get_ticket_id()
        ticket_price()
    elif choice == 3:
        return "Event3"
        ticket_type()
        get_ticket_id()
        ticket_price()
    else:
        return None
        

print(select_event())
print(get_ticket_id())
print(ticket_price())
