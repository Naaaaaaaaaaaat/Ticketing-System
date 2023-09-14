class Ticket:

    def __init__(self, staff_id, creator_name, contact_email, description, status, response):
        self.ticket_number = None
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.status = status
        self.response = response

    def provide_response(self, response_text):
        self.response = response_text

    def __str__(self):
        return (f"Ticket Number: {self.Helpdesk.ticket_number}\n"
                f"Name of the ticket’s creator: {self.creator_name}\n"
                f"StaffID: {self.staff_id}\n"
                f"Email address: {self.contact_email}\n"
                f"Description of the issue: {self.description}\n"
                f"Response from the IT department: {self.response}\n"
                f"Ticket status: {self.status}")



