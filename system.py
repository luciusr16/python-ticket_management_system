class TicketSystem:
  def __init__(self):
    self.users = {}
    self.engineers = {}
    self.teams = {}
    self.tickets = {}
    self.next_ticket_id = 1