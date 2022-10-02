# from ticket_type import *
# from ticket_price import *
# from ticket_id import *

choice = int(input("""Choose an event of your choice:
                Enter:  1 for Event1
                        2 for Event2
                        3 for Event3 


"""))


def select_event():
    if choice == 1:
        return "Event1"
    elif choice == 2:
        return "Event2"
    elif choice == 3:
        return "Event3"
    else:
        return None
        

# print(select_event())
# print(get_ticket_id())
# print(ticket_price())
