#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = [None] * length
    flight_hash = {}

    for ticket in tickets:
        flight_hash[ticket.source] = ticket.destination
    next = flight_hash["NONE"]

    for i in range(0, length):
        route[i] = next
        next = flight_hash[next]

    return route
