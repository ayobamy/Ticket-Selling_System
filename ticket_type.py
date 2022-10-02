# ticket selling system
ticket = input("""What type of ticket do you want to buy? 
                Enter:  g for gold
                        s for silver
                        p for platinum
                .....
                """)

ticket = ticket.lower()

def ticket_type():
    if ticket == "g":
        ticket_type = "Gold"
        return ticket_type
    elif ticket == "s":
        ticket_type = "Silver"
        return ticket_type
    elif ticket == "p":
        ticket_type = "Platinum"
        return ticket_type
    else:
        return "Invalid ticket type"



