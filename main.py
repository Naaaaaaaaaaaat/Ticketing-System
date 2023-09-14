from tickets import Ticket
# Ticket list
ticket_list = []
class TicketStatus:
    OPEN = "Open"
    CLOSED = "Closed"

class Helpdesk:
    ticket_number = 2000
    open_tickets = 0
    closed_tickets = 0
    def __init__(self):
        self.tickets = []

#To create ticket
def tNew():
    staff_id = input("Enter Staff ID: ")
    creator_name = input("Enter Ticket Creator Name: ")
    contact_email = input("Enter Contact Email: ")
    description = input("Enter Description of the Issue: ")
    ticket = Ticket(staff_id, creator_name, contact_email, description, "Open", "Not Yet Provided")
    ticket.ticket_number = Helpdesk.ticket_number
    ticket_list.append(ticket)
    Helpdesk.ticket_number += 1
    Helpdesk.open_tickets += 1
    print("Ticket submitted successfully.")

    if "Password Change".lower() in description:
        new_password = f"{staff_id[:2]}{creator_name[:3]}"
        ticket.response = f"New Password: {new_password}"
        print(f"{ticket.response}")
        ticket.status = "Closed"


#To close ticket
def respondToTicket(ticketNumber, response):
    print("Ticket List Contents:")
    for ticket in ticket_list:
        print(f"Ticket {ticket.ticket_number} - Status: {ticket.status}")

    matching_tickets = [ticket for ticket in ticket_list if ticket.ticket_number == ticketNumber]

    if not matching_tickets:
        print(f"Ticket {ticketNumber} not found.")
        return

    ticket = matching_tickets[0]

    if ticket.status == "Open":
        ticket.response = response
        ticket.status = "Closed"
        Helpdesk.closed_tickets += 1
        Helpdesk.open_tickets -= 1
        print(f"Ticket {ticketNumber} has been closed.")
    else:
        print(f"Ticket {ticketNumber} is already closed.")

#Ticket lists
def list_tickets(status):
    print(f"List of {status} Tickets:\n")
    for index, ticket in enumerate(ticket_list, start=1):
        if ticket.status == status:
            print(f"Ticket {Helpdesk.ticket_number}")

            print(f"Staff ID: {ticket.staff_id}")
            print(f"Creator Name: {ticket.creator_name}")
            print(f"Creator Email: {ticket.contact_email}")
            print(f"Description: {ticket.description}")
            print(f"Status: {ticket.status}\n")

def main():
    while True:
        print("\n----->>>>> Welcome to the Ticketing System <<<<<-----")
        print("1. Submit New Ticket")
        print("2. List Open Tickets")
        print("3. Close Ticket")
        print("4. List Closed Tickets")
        print("0. EXIT")

        choice = input("\nEnter Number: ")

        if choice == "1":
            tNew()

        elif choice == "2":
            list_tickets(TicketStatus.OPEN)

        elif choice == "3":
            print("Option 3 (Close Ticket) selected.")
            ticket_number = input("Enter the ticket number to close: ")
            response = input("Enter the response for the ticket: ")
            print(f"Attempting to close ticket {ticket_number} with response: {response}")
            respondToTicket(int(ticket_number), response)

        elif choice == "4":
            list_tickets(TicketStatus.CLOSED)

        elif choice == "0":
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()