class TrainTicket:
    def __init__(self, passenger_name, train_number, origin, destination, travel_date, seat_class, ticket_price):
        self.passenger_name = passenger_name
        self.train_number = train_number
        self.origin = origin
        self.destination = destination
        self.travel_date = travel_date
        self.seat_class = seat_class
        self.ticket_price = ticket_price

    def display_ticket_details(self):
        print("\nTrain Ticket Details")
        print("----------------------")
        print(f"Passenger Name : {self.passenger_name}")
        print(f"Train Number   : {self.train_number}")
        print(f"From           : {self.origin}")
        print(f"To             : {self.destination}")
        print(f"Date of Travel : {self.travel_date}")
        print(f"Class          : {self.seat_class}")
        print(f"Ticket Price   : ₹{self.ticket_price}")


# Sample usage
if __name__ == "__main__":
    # Sample ticket
    ticket = TrainTicket(
        passenger_name="Nand Sharma",
        train_number="12345",
        origin="Delhi",
        destination="Mumbai",
        travel_date="2025-06-15",
        seat_class="Sleeper",
        ticket_price=750
    )

    ticket.display_ticket_details()
