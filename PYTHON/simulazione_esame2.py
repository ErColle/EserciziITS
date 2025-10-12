class Ticket:
    def __init__(self, ticket_id: str, movie: str, seat: str, is_booked:bool):
        self.ticket_id = ticket_id
        self.movie = movie 
        self.seat = seat
        self.is_booked = is_booked
        
    def book(self):
        if self.is_booked == False:
            self.is_booked = True
        else:
            print(f"Il biglietto per '{self.movie}' posto '{self.seat}' è già prenotato.")
        
    def cancel(self):
        if self.is_booked == True:
            self.is_booked = False
        else:
            print(f"Il biglietto per '{self.movie}' posto '{self.seat}' non risultaprenotato.")
    
class Viewer:
    def __init__(self, viewer_id: str, name: str):
        
        self.viewer_id = viewer_id
        self.name = name 
        self.booked_tickets = []

    def book_ticket(self, ticket: Ticket):
        if ticket.is_booked == False:
            self.booked_tickets.append(ticket)
        else:
            print( f"Il biglietto per '{ticket.movie}' non è disponibile.")
        
    def cancel_ticket(self, ticket: Ticket ):
        if ticket in self.booked_tickets:
            self.booked_tickets.pop(ticket)
            ticket.cancel()
    
        else:
            print( f"Il biglietto per '{ticket.movie}' non è stato prenotato da questo spettatore.")

class Cinema:
    def __init__(self):
        self.tickets = {}
        self.viewers = {}
        
    def add_ticket(self, ticket_id:str, movie: str, seat: str):
        if self.ticket_id in self.tickets:
            print( f"Il biglietto con ID '{ticket_id}' esiste già.")
        else:
            self.tickets[ticket_id] = Ticket(ticket_id, movie, seat, False )
        
    def register_viewer(self, viewer_id: str, name:str ):
        if viewer_id in self.viewers:
            print( f"Lo spettatore con ID '{viewer_id}' è già registrato.")
        else:
            self.viewers[viewer_id] = Viewer(viewer_id, name)
            
    def book_ticket(self, viewer_id:str, ticket_id:str ):
        if viewer_id in self.viewers and self.tickets:
            self.viewer.book_ticket(self.ticket)
        else: 
            print( "Spettatore o biglietto non trovato.")
        
    def cancel_ticket(self, viewer_id: str, ticket_id: str):
        if viewer_id in self.viewers and self.tickets:
            self.viewer.cancel_ticket(self.ticket)
        else: 
            print( "Spettatore o biglietto non trovato.")
            
    def list_avaible_tickets(self):
        
        for ticket in self.tickets:
            avaible_tickets = []
            if not ticket.is_booked:
                avaible_tickets.append(ticket)
        
        print(avaible_tickets)
        
    def list_viewer_bookings(self, viewer_id: str) -> list[str] | str:
        if viewer_id in self.viewers:
            viewer = self.viewers[viewer_id]
            booked_ids = [ticket.ticket_id for ticket in viewer.booked_tickets]
            return booked_ids
        else:
            return "Errore: spettatore non trovato."
        
    