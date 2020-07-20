#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # first ticket will have a source of none
    # final ticket will have a destination of none
    ticket_dict = {}
    route = []

    # creates the hash table
    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination

    route.append(ticket_dict["NONE"])

    current = route[0]

    while current != "NONE":
        next_dest = ticket_dict[current]
        route.append(next_dest)
        current = next_dest

    return route
